#!/usr/bin/python
#########################################################
#	Wyszukiwanie dominanty w dowolnym zbiorze	#
#	Autor: Dominik Kesselring			#
#	Przedmiot: Laboratoria - algorytmy 		#
#########################################################
import random
import operator
start = 0
stop = 0
step = 1
zakres = 0
tablica_danych=[]
tablica_liczb=[]
tablica_wystapien=[]

def pobierz_dane():
	print("Podaj zakres liczb")
	start = input("Podaj początek zbioru liczb: ")
	stop = input("Podaj koniec zbioru liczb: ")
	zakres = input("Podaj ile liczb ma być wygenerowanych: ")	
	#generuje tablice danych
	for i in range (int(zakres)):
    		tablica_danych.append(random.randrange(int(start),int(stop)))

def generowanie_tablic_pomocniczych(tablica_danych):
	for i in range(0, len(tablica_danych)):
	#przepisuje dane wejsciowe do nowej tablicy tylko jesli wczesniej ich tam nie wpisalem i 	zaznaczam ich wystapienie w trzeciej tablicy
		if tablica_danych[i] not in tablica_liczb:
			tablica_liczb.append(tablica_danych[i])
			tablica_wystapien.append(1)
	#jesli liczba wystąpiła już raz w tablicy liczb to zwiększam wartość o jeden pod tym samym 	indeksem w tablicy wystąpień
		else:
			index = tablica_liczb.index(tablica_danych[i])
			tablica_wystapien[index]+=1

pobierz_dane()
generowanie_tablic_pomocniczych(tablica_danych)
#wyświetlamy dane
print("Twój zakres danych to: ")
print(tablica_danych)
print()
#wyszukuje liczbę najczęściej występującą
m=max(tablica_wystapien)
#licznik pozwoli rozwiązać problem wielości dominant
licznik_dominant = 0
#szukam ile razy wystąpiła dominanta i na jakiej pozycji się znajduje co w efekcie daje porządany wynik
for i, j in enumerate(tablica_wystapien):
	if j == m:
		print("Dominanta: " +str(tablica_liczb[i])+" "+"wystąpiła: " +str(m))
		licznik_dominant += 1
#rozwiązanie problemu przy więcej niż 1 dominancie
if licznik_dominant > 1:
	print("Wystąpił błąd matrixa :-)")
	print("Rozkład wielomodalny")
