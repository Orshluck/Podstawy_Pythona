import csv
import smtplib
from email.mime.text import MIMEText

from Student import Student
from Task_1 import MyLinkedList
from Task_1 import Element

students = {} # słownik studentów
students = MyLinkedList()


with open('ocenystudenci', newline='') as file:
    text_file = csv.reader(file, delimiter=',') # Zakładam że po przecinku
    for student_string in text_file:
        email, first_name, last_name = student_string[:3] # first 4 info
        all_grade = student_string[3:17]
        if(len(student_string) > 18):
            status = student_string[-1]
        else:
            status = None;

        student = Student(email,first_name,last_name,all_grade,status)
        print(f"student data = {student}")
        students.append(Element(student),lambda x, y: x.email >= y.email)

def write_changes():
    with open('students.txt', mode='w', newline="\n") as file:
        # a lot of problems here so i will just use simple method
        # ok i will do something ugly i am sorry


        while student_element:
            string = f"{student_element.data.email},{student_element.data.name},{student_element.data.surname},{student_element.data.all_grade},{student_element.data.status}\n"
            file.write(string)
            student_element = student_element.nextE

def get_grade(student):
    return 5 # todo later
    # I do not understand points in file and how they correspond to the grade, which are lists, projects etc

def get_students():
    student_element = students.get()
    while student_element:
        print(f"student {student_element.data}")
        student_element = student_element.nextE


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

remove_student("test2@gmail.com")
#mail_students()


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