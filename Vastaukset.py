# T1
# print("Henriikka Raappana")
#
# T2
# Pycharm värit
# symboli ja nimet: vaalea harmaa/valkoinen
# tulostus: violetti/sininen
# Virheet: punainen alleviivaus
# avainsanat: oranssi
# teksti lainausmerkeissä: vihreä
#
# T3
# import string
# print(string.ascii_lowercase)
# print(string.ascii_lowercase[::-1])
#
# T3,5
# print("pelihahmoni on")
#     print("kissa")
# Vastaus: print("kissa") IndentationError: unexpected indent
#
# T4
# print("#        #   ########    #")
# print("#        #   #           #")
# print("##########   ########    #")
# print("#        #   #           #")
# print("#        #   ########    #")
#
# T5
# henkilo = input("Mikäs sun nimi on? ")
# print("Morjesta sulle!", henkilo)
#
# sukunimi = input("Entäpäs sukunimi? ")
# print("Kiitos kiitos", sukunimi + " " + henkilo)
#
# postinumero = input("postinumero?? ")
# print("mmm yeeesss, okok eli ", postinumero)
#
# postitoimipaikka = input("vai että semmosta, mikäs postitoimipaikka? ")
# print("kiitosta tästä,", postitoimipaikka)
# print(" on rekisteröity")
#
# sahkoposti = input("Entäpä vielä sähköposti? O.o ")
# print("HEHE HÖLÖMÖ!", sahkoposti)
# print("on nyt tallessa!")
#
# print("Minullapa on nyt kaikki sun tiedot!", henkilo + " "  + sukunimi + " "  + postinumero + " "  + postitoimipaikka + " "  + sahkoposti)
#
# T6
# nimi = "Lasse"
# print("Syrjäisessä laaksossa asui nuorukainen", nimi + ",")
# print("joka oli ammatiltaan lammaspaimen.")
# print(nimi + " oli vasta herännyt,")
# print("kun pihaan ratsasti tumma-asuinen ritari.")
# print("Pian " + nimi + " saisi kuulla, että hänet oli valittu tärkeään tehtävään...")
#
#  T7
# luku1 = 5
# luku2 = 4
# summa = luku1 + luku2
# print(luku1, "+", luku2, "=", summa)
#
# luku3 = 22
# luku4 = 8
# erotus = luku3 - luku4
# print(luku3, "-", luku4, "=", erotus)
#
# luku5 = 2
# luku6 = 8
# kerto = luku5 * luku6
# print(luku5, "*", luku6, "=", kerto)
#
# luku7 = 22
# luku8 = 8
# jako = luku7 / luku8
# print(luku7, "/", luku8, "=", jako)
#
#  T8
# luku1 = float(input("Anna luku: "))
# luku2 =float(input("Anna toinen luku: "))
# print("summa", luku1 + luku2)
#
# luku1 = float(input("Anna luku: "))
# luku2 =float(input("Anna toinen luku: "))
# print("summa", luku1 - luku2)
#
# luku1 = float(input("Anna luku: "))
# luku2 =float(input("Anna toinen luku: "))
# print("summa", luku1 * luku2)
#
# luku1 = float(input("Anna luku: "))
# luku2 =float(input("Anna toinen luku: "))
# print("summa", luku1 / luku2)
#
#  T9
# nimi = "Hyvä asiakas"
# tervehdys = "Tervetuloa sairaalaan, "
# viesti = tervehdys + nimi
# print(viesti)
# print(len(viesti))
#
#  T9,5
# nimi = "Teija Testaaja"
# ika = "17"
# taito1 = "Python (aloittelija)"
# taito2 = "Web-ohjelmointi (veteraani)"
# taito3 = "Ohjelmointi (puoliammattilainen)"
# luku = "2000 - 3000"
# print("Nimeni on " + nimi + ", olen " + ika + " vuotias")
# print("Taitoihini kuuluvat " + taito1 + " ja " + taito2 + " sekä " + taito3)
# print("Ja haen työtä, josta maksetaan palkaa " + luku + " euroa kuukaudessa.")
#
#  T10
# x = int(input("Anna ensimmäinen luku: "))
# y = int(input("Anna toinen luku: "))
# summa = x + y
# print(summa)
#
#  T11
# kirjain = input("Anna kirjain: ")
# print("Syötit kirjaimen:", kirjain)
#
#  T12
# nimi1 = input("Kerro nimesi: ")
# ika1 = int(input("Kerro ikäsi: "))
#
# nimi2 = input("Kerro nimesi: ")
# ika2 = int(input("Kerro ikäsi: "))
#
# yhteensa = ika1 + ika2
#
# print(nimi1, "ja", nimi2, "ovat yhteensä", yhteensa, "vuotta vanhoja")
#
#  T13
# viesti = "Olen "
# luku = 25
# print(viesti + str(luku) + " vuotta vanha")
#
#  T13,5
# henkilo = input("Nimesi?: ")
# kenka = input("Kengän kokosi?: ")
# print("Nimesi on " + henkilo + " ja kengän kokosi on " + kenka)
#
#  T1 - 13 Oma koodi
# print("Tervetuloa metsään.. mihin olet eksynyt.")
#
# hp = 25
#
# nimi = input("Jos muistat, mikä on nimesi? ")
# print("\nHei " + nimi + "! Olet tosijaa iha eksyny tänne mettää.")
#
# valinta1 = input("Valitte suunta (vasen/oikea): ")
#
# if valinta1 == "vasen":
#     print("\nMeet sitte vasemmalle. Vasemmalta löytyi mettää.")
#
# elif valinta1 == "oikea":
#     print("\nOikealta löytyi lisää metsää")
#
# valinta2 = input("Valitte suunta (kiipeä puuhun/eteenpäin): ")
#
# if valinta2 == "kiipeä puuhun":
#     print("Ei kukaan enää aikuisiässä minnekkää puuhun jaksa kiivetä. Tipuit ja vahingoituit, -15hp.")
#     hp -= 15
#     print("hp: " + str(hp) + "hp")
#
# elif valinta2 == "eteenpäin":
#     print("Edestä löytyy lisä mettää... mutta.. ")
#
# valinta3 = input("Näyvillä on luola, kylä sekä kukka aukio, menetkö johonkin näistä? (joo/en): ")
#
# if valinta3 == "joo":
#     print("No minne?")
#
# elif valinta3 == "en":
#     print("Womp womp kuolit nälkään.")
#     print("Menetät " + str(hp) + "hp")
#     hp -= 25
#     print("hp", hp)
#
#     if hp <= 0:
#         print("Peli menetetty.")
#     exit()
#
# valinta4 = input("Valitte (luola/kylä/kukka aukio): ")
#
# if valinta4 == "luola":
#     print("Menet luolaan.")
#     print("Luolassa on yksi tuoli.")
#     print("tuoli katsoo sinua..")
#     print("Et tiedä miten tuoli sua kattoo, mutta niin se tekkee.")
#     print("Tilanne muuttuu eritysen kiusaliseksi.")
#     print("Menetät " + str(hp) + "hp")
#     print("Kuolit kiusalliseen tunnelmaan.")
#     hp -= 25
#     print("hp", hp)
#
#     if hp <= 0:
#         exit()
#
# elif valinta4 == "kylä":
#     print("Saavuit kylään.")
#     print("Kyläläiset tuijottavat sinua hiljaa.")
#     print("Yksi heistä sanoo: 'Oisit voinut tulla eilen.'")
#     print("Kaikki nyökkäävät pettyneinä.")
#     print("Häpeä vahingoittaa sinua.")
#     print("Sinulla on nyt " + str(hp) + " hp.")
#     print("Kuolit sosiaaliseen ahistukseen.")
#
#     if hp <= 0:
#         exit()
#
# elif valinta4 == "kukka aukio":
#     print("Saavuit kukka aukiolle.")
#     print("Yksi kukka alkaa puhua.")
#     print("'Vihdoinkin', kukka sanoo passiivis aggressiivisesti.")
#     print("'Missä olet ollut koko elämäni?'")
#     print("Tilanne menee liian syvälliseksi.")
#     print("Sinulla on nyt " + str(hp) + " hp.")
#     print("Kuolit eksistentiaaliseen kriisiin.")
#
#     if hp <= 0:
#         exit()

 # T14
# ika = "5"
# print("Muuttujassa ika on arvo " + ika)

 # T15
# omena = 3
# banaani = 2
# print((omena == 3) and (banaani == 2))
#
# omena1 = 3
# banaani1 = 2
# print((omena == 3) or (banaani == 2))
#
# omena2 = 5
# banaani2 = 2
# print((omena == 5) and (banaani == 2))
#
# omena3 = 3
# banaani3 = 2
# print((omena == 2) and (banaani == 5))

  # T16
