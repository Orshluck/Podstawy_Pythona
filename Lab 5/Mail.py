import csv
import smtplib
from email.mime.text import MIMEText

students = {} # słownik studentów


with open('students.txt', newline='') as file:
    text_file = csv.reader(file, delimiter=',') # Zakładam że po przecinku
    for student in text_file:
        email, first_name, last_name, points = student[:4] # first 4 info
        grade, status = student[4:] if len(student) > 4 else ('', '') #"Mogą znajdować się" jeśli nie to krotka
        student_data = {
            'first_name': first_name,
            'last_name': last_name,
            'points': points,
            'grade' : grade,
            'status': status
        }
        students[email] = student_data # "zagnieżdzanie" bo to jest słownik stringa i słownika

def write_changes():
    with open('students.txt', mode='w', newline="\n") as file:
        # a lot of problems here so i will just use simple method
        # ok i will do something ugly i am sorry
        for email in students:
            student = students.get(email)
            first_name = student.get("first_name")
            last_name = student.get("last_name")
            points = student.get("points")
            grade = student.get("grade")
            status = student.get("status")
            string = f"{email},{first_name},{last_name},{points},{grade},{status}\n"
            file.write(string)


def get_grade(points):
    points = int(points)
    if points <= 50:
        return 2
    if points >= 51 and points <= 60:
        return 3
    if points >= 61 and points <= 70:
        return 3.5
    if points >= 71 and points <= 80:
        return 4
    if points >= 81 and points <= 90:
        return 4.5
    if points >= 91 and points <= 100:
        return 5

def get_students():
    for student in students:
        print(f"studend {student} with values {students.get(student)}")

def grade_students():
    for student in students:
        if students.get(student).get('status') not in ("GRADED", "MAILED"):
            grade = get_grade(students.get(student).get("points"))
            students.get(student)['status'] = "GRADED"
            students.get(student)['grade'] = grade
            print("Changed value")

def add_student(email, first_name, last_name, points, grade, status):
    if students.get(email) != None:
        print("There is already student with this email")
        return
    else:
        student_data = {
            'first_name': first_name,
            'last_name': last_name,
            'points': points,
            'grade': grade,
            'status': status
        }
        students[email] = student_data # "zagnieżdzanie" bo to jest słownik stringa i słownika
    write_changes()

def remove_student(email):
    if students.get(email) == None:
        print("There is no  student with this email")
        return
    else:
        students.pop(email)
        print("Removed")
    write_changes()

def mail(email, grade):
    pass
    #TODO: Mail function

def send_email(grade, mail):
    sender = "Teacher@gmail.com"
    password = "This should not be in the text file but outside"
    msg = MIMEText(f"Your final grade is {grade}")
    msg['Subject'] = "Final grade"
    msg['From'] = sender
    msg['To'] = mail  # Yea i will send mail individually, because idk if it is Cc or Bcc
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #smtp_server.login(sender, password)  #comented because obv
    #smtp_server.sendmail(sender,mail,msg) #comented because obv
    smtp_server.quit()

def mail_students():
    for student in students:
        if students.get(student)['status'] != 'MAILED':
            grade =  students.get('grade')
            send_email(student,grade) # send mail
            students.get(student)['status'] = "MAILED" #change status
    write_changes()

## HERE are tests
get_students()
add_student("s24185@pjstk.edu.pl","Franciszek","Orszulak", 78,5,"GRADED")
remove_student("test2@gmail.com")
mail_students()


choice = -1
while choice != 1:
    choice = int(input("To quit press 1\n"
                      "To add student press 2\n"
                      "To remove student press 3\n"
                      "To mail students press 4\n"
                      "This does not take other inputs, it will work though\n"
                      ":\t"))
    if input == 2:
        add_student("s24185@pjstk.edu.pl","Franciszek","Orszulak", 78,5,"GRADED")
    if input == 3:
        remove_student("test2@gmail.com")
    if input == 4:
        mail_students()