#Lista1
import random
import collections
'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''

#1. Ile unikatowych elementów znajduje się w liście:
#1 pkt
lista_1 = [0,7,8,3,3,0,7,0,3]
def count_unique(list):

    unique_elements = set(list)
    return str(len(unique_elements))

w_1 = count_unique(lista_1)
print(w_1)

#2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
#na '0':
def change_random_char(string):
    index = random.randint(0,len(string)-1)
    string = string[:index] +'0' + string[index + 1:]
    return string
#2 pkt

w_2 = change_random_char(s_2)
print(w_2)


#3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [ [{1: 'java', 0: ('python', 'R')},'c++'],['word', 'excel'] ]
lista_3[0][0][0] = ('python', 'JS')
w_3 = lista_3[0][0][0][1]
print(w_3)


    #4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
#boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
#1 pkt

w_4 = "list set"
print(w_4)

#5. Dla stringa wypisz
#ile razy pojawił się dany znak, w kolejności alfabetycznej.
#Użyj słownika - wynik również ma być słownikiem
#2 pkt

s_5 = "ala ma kota imie ma macko"
dict = {}
for char in s_5:
    dict[char] = dict.get(char, 0) + 1
od = collections.OrderedDict(sorted(dict.items()))
w_5 = od
print(w_5)

#6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
#jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
#Nie jeżeli nie wystąpił.
#1 pkt
def is_char_n_times_in_string(string, howmanytimes):
    for char in string:

        if string.count(char) == howmanytimes:
            return "Tak"
    return "No"

w_6= is_char_n_times_in_string(s_5,3)
print(w_6)

#7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
#i zwróci True lub False ( jest/ nie jest)
# pomiń znaki nie będące literami.
#3pkt

def palindrom(s):

    temp_s = ''.join(filter(str.isalpha, s)) #from internet removes all non letters
    s = ''.join(filter(str.isalpha, s))
    temp_s.lower() #to lower
    temp_s = temp_s[::-1]
    s.lower()
    return s == temp_s[::-1]

s_7_1 ="Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))

#8. Napisz funkcję, która wyświetli
#wszystkie liczby od 1 do n, jednak jeżeli liczba jest podzielna przez:
#trzy – wypisze „Fizz”,
#pięć – wypisze „Buzz”,
#trzy i pięć wypisz „FizzBuzz”.
#wszystkie liczby/słowa mają zostać wyświetlone w jednej linii, oraz być rozdzielone przecinkiem
#BEZ spacji
#2 pkt

def fizzbuzz(n):
    string = ""
    for i in range(1,n+1):
        if(i % 3 == 0):
            string += "Fizz"
        if(i % 5 == 0):
            string += "Buzz"
        if( i % 5 != 0 ) and (i % 3 !=0 ):
            string += str(i)
        if(i != n):
            string += ','
    return string

n_8 = 16
print(fizzbuzz(n_8))

#9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
#bez rekurencji:
#3 pkt

n_9 = 6
def fibonacci(n):
    if n <= 1:
        return n  #if it is lower than 1st just return it, or i can return an error
    else:
        a = 0
        b = 1
        for i in range(1, n):
            temp_a = a
            a = b
            b = temp_a+b

        return b
print(fibonacci(n_9))

#10. Napisz funkcję, która dla podanej posortowanej listy
#zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
#lub zwróci None gdy nie ma elementu w liscie:
#3 pkt


def binary_search(lista, e):
    min = 0
    max = len(lista)-1

    while (min <= max):
        guess = int((min+max)/2)
        if(lista[guess] == e):
            return guess
        if lista[guess] > e:
            max = guess - 1
        else:
            min = guess + 1
    return None

# def create_ordered_list(lenght):
#     temp = [0]
#     for i in range(1,lenght):
#         temp.append(temp[i-1] + random.randint(1,100))
#     return temp
# for i in range (1,1000):
#     temp_list = create_ordered_list(i)
#     random_element = random.choice(temp_list)
#     if temp_list.index(random_element) != binary_search(temp_list,random_element):
#         print(temp_list)
#         print(random_element)
#         print(binary_search(temp_list,random_element))

l_10 = [0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
print(binary_search(l_10, 2))


