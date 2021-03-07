# #Zad1
# sport = ["pilka nozna", "siatkowka", "koszykowka"]
#
# sport.reverse()
# print(sport)
#
# sport.append("golf")
# sport.append("tenis")
# print(sport)
# przerwa = "--------------------------------------"
# print(przerwa)

# #Zad2
# slownik = {"itp": "i tym podobne", "itd": "i tak dalej"}
#
# print(slownik)
# print(przerwa)

# #Zad3
# gry = {1: "Borderlands 3", 2: "Battlefield 3", 3: "Borderlands 2"}
# print(gry)
# print(przerwa)

# #Zad4
# napis = input("Napisz zdanie: ")
# #
# # print(napis.count("a"))
# print(przerwa)

# #Zad5
# import sys as system
#
# system.stdout.write("Podaj trzy liczby calkowite: ")
# liczba1 = int(system.stdin.readline())
# liczba2 = int(system.stdin.readline())
# liczba3 = int(system.stdin.readline())
# print((pow(liczba1, liczba2) + liczba3))
# print(przerwa)

# #Zad6
# liczba1 = input("Podaj pierwsza liczbe: ")
# liczba2 = input("Podaj druga liczbe: ")
# liczba3 = input("Podaj trzecia liczbe: ")
#
# if liczba1 > liczba2:
#     if liczba1 > liczba3:
#         najwieksza = liczba1
#         print(najwieksza)
#     else:
#         najwieksza = liczba3
#         print(najwieksza)
# elif liczba2 > liczba3:
#     najwieksza = liczba2
#     print(najwieksza)
# else:
#     najwieksza = liczba3
#     print(najwieksza)
# print(przerwa)

# #Zad7
# lista_liczb = [1,2.5,5,4,5]
#
# for x in lista_liczb:
#     print(x**2)
# print(przerwa)

# #Zad8
# lista_zadanie8 = []
#
# i = 1
#
# while i < 11:
#     zadanie8 = int(input('Podaj liczbe: '))
#     i+=1
#     if zadanie8%2==0:
#         lista_zadanie8.append(zadanie8)
# print(lista_zadanie8)
# print(przerwa)

# #Zad9
# lista = [1, 2, 3, 4, 5]
# cos = len(lista)
# for i in range(0,cos):
#     if (lista[i]%2 > 0):
#         lista[i] = 'EEEEEE'
#     elif (lista[i]%2 == 0):
#         lista[i] = 'E'
#     print(lista[i])
# print(przerwa)

# #Zad10
# from math import *
# a = input("podaj liczbe: ")
# try:
#  wynik = sqrt(int(a))
#  print(wynik)
# except:
#  print("zle")


