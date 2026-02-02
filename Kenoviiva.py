#print("eka\ntoka\nkolmas")
#print("c:\\python\\testi.py")

#ika=25
#print(ika)

# Muuttujat ja tietotyypit
#nimi = ("Henriikka")
#kokonaisluku = 25
#liukuluku = 3.14
#onkoTotta = True
#print ("Nimesi on " +(nimi))
#print ("Kokonaislukumuuttujan arvo on " +str(kokonaisluku))
#print ("Liukulukumuttujan arvo on " +str(liukuluku))
#print ("Totuusarvonmuuttujan arvo on " +str(onkoTotta))

# Kokonaisluvut ja liukuluvut
#x=5
#y=x*9
#print(y)

#x=5
#y=x*10
#print(y)

# Luvun kysyminen käyttäjältä ja sen tallentaminen muuttujaan
#x = int(input("Anna ensimmäinen luku: "))
#y = int(input("Anna toinen luku: "))
#summa = x + y
#print(summa)
# Tää laskee

#x = input("Anna ensimmäinen luku: ")
#y = input("Anna toinen luku: ")
#summa = x + y
#print(summa)
# Tää vaa yhistää numerot

# Merkkkijonojen käsittely
#nimi = (Lassi Lisko)
#print(name)
#Lassi Lisko
# No eihän tämä näin voi toimia hä?

#nimi = "Lassi Lisko"
#tervehdys = "Tervetuloa Liskolandiaan, "
#viesti = tervehdys + nimi
#print(viesti)
#print(len(viesti))

# Komento str()
#print("route"+66)
#print("route "+str(66))

#kokonaisluku = 123
#print("Kokonailukumuuttujan arvo on " +str(kokonaisluku))

#kokonaisluku = 42
#print("Kokonaislukumuuttujan arvo on " +str(kokonaisluku))

# Luettelot
#tyrannosaurus_pelaajat = ["Maija", "Miina", "Minda", "Milla", "Maiju"]
#lentolisko_pelaajat = ["Mikko", "Mauno", "Matias", "Miika"]
#print(tyrannosaurus_pelaajat[2])
#print(lentolisko_pelaajat[0])

# Totuusarvo, loogiset operaattorit
#karkkia = 3
#limsaa = 2
#karkkia > limsaa
#True
#karkkia == limsaa
#False
#(karkkia == 3) or (limsaa == 2)
#True
#(karkkia == 4) and (limsaa == 2)
#True
# ei toimi?????

# Ehdot
#Onko_aurinkoista = input("Onko ulkona aurinkoista? (k/e)")
#If Onko_aurinkoista =="k":
#    print("Ihanaa! Heti ulos")
# En saanut tätä toimimaan, Onko_aurinkoista on kuulemma väärin

#Onko_aurinkoista = input("Onko ulkonaurinkoista? (k/e)")
#if Onko_aurinkoista =="k":
#    print("Ihanaa! Heti ulos")
#else:
#    print("Blääh! Taas pilvistä tai sateista")

#saa = input("Mitä sääennuste lupaa?" (vettä/lunta/aurinkoista))
#if saa =="vettä":
#    print("ota satikka mukaan")
#elif saa =="lunta":
#    print("muista talvivaatteet")
#else:
#    print("muista aurinkolasit")
# NameError: name 'vettä' is not defined

# Silmukat
# For koodi
#For laskuri in range(1,6):
#    print("No jo on kivaa!")

# Range
#range(1, 6)
# Sanoo, että laskuri on invalid syntax, range ei tuo mitään tulosta

# While-silmukka
#while True:
#    print("tämä on loppumaton silmukka")

#while True:
#    vastaus = input("tympiikö? (k/ei)")
#if vastaus =="k":
#        print("nyt jo?!")
#        break
#    if vastaus =="ei":
#        print("hyvä, ei muutako takas töihin")
#        break

#for hooray_laskuri in range(1, 4):
#    for holiday_laskuri in range(1, 3):
#        print("hooray hooray")
#        print("its a holi holiday")

# Funktiot
#def tervehdi():
#    print("Terveisiä funktiosta "tervehdit"")
# tervehdit on invalid syntax

#def main():
#    print("Kokeillaan onnituuko funktion kutsuminen:")
#    tervehdi()
# Tän kun juoksee yksinään, ei tapahdu mitään

#print("Ei näytä siltä, kokeillaan vielä":)
# Ei toimi nii ei toimi

#def tulosta_sekunnit_paivassa(paivat):
#    tunnit = 24
#    minuutit = tunnit * 60
#    sekunnit = minuutit * 60
#    print(sekunnit)
#tulosta_sekunnit_paivassa(1)

#def tulosta_sekunnit_paivassa(paivat):
#    tunnit = 24
#    minuutit = tunnit * 60
#    sekunnit = minuutit * 60
#    print(sekunnit)
#tulosta_sekunnit_paivassa(7)
# Kumpiki antaa samat tulokset, ulman että ylempään laittaa (paivat), tulee syntax error

# def muunna_päivät_sekunniksi(paivat):
#     tunnit = paivat * 24
#     minuutit = tunnit * 60
#     sekunnit = minuutit * 60
#     print(sekunnit)
#     return sekunnit
# Mitään ei tapahdu, kun tämän yksinään juoksee

# Kaikki_sekunnit_yhteensa = muunna_päivät_sekunniksi(7)
# millisekuntit = Kaikki_sekunnit_yhteensa * 1000
# print(millisekuntit)

#  Vakio esim.
# kilohinta = 5.4
# pakkauskulut = 3.2
#
# paino = float(input("Anna paino kilogrammoina:\n"))
# print("Tuote maksaa ", paino * kilohinta, pakkauskulut, "euroa.")
#  Täähän on ihan vitun kätevä

#  Moduulit
# import webbrowser
# webbrowser.open("https://docs.python.org/3/library")

# from random import choice
# suunta = choice(["P", "E", "I", "L"])
# print(suunta)

# from time import time as time_now
# now = time_now()
# print(now)

