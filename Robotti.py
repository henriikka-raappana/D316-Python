import turtle as t

t.bgcolor("beige")
t.hideturtle()
t.speed(0)

def rectangle(horizontal, vertical, color):
    t.pendown() #Kynä lasketaan
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for counter in range(1, 3): #range(1, 3), tarkoittaa, että silmukka suoritetaan 2x
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

# Jalkaterät
t.goto(-100, -150)
rectangle(50, 20, "blue")
t.goto(-30, -150)
rectangle(50, 20, "blue")

# Jalat
t.goto(-25, -50)
rectangle(15, 100, "grey")
t.goto(-55, -50)
rectangle(-15, 100, "grey")

# Vartalo
t.goto(-90, 100)
rectangle(100, 150, "red")

# Oikea käsivarsi
t.goto(-150, 70) # Oikea olkavarsi
rectangle(60, 15, "grey")
t.goto(-150, 70) # Oikea kyynärvarsi
rectangle(15, 40, "grey")

# Vasen käsivarsi
t.goto(10, 70) # Vasen olkavarsi
rectangle(60, 15, "grey")
t.goto(55, 110) # Vasen kyynärvarsi
rectangle(15, 40, "grey")

# Kaula
t.goto(-50, 120)
rectangle(15, 20, "grey")

# Pää
t.goto(-85, 170)
rectangle(80, 50, "red")

# Silmät
t.goto(-60, 160)
rectangle(30, 10, "white") # Valkuainen
t.goto(-55, 155)
rectangle(5, 5, "black") # Oikea pupilli
t.goto(-40, 155)
rectangle(5, 5, "black") # Vasen pupilli

# Suu
t.goto(-65, 135)
rectangle(40, 5, "black")

t.done() #Tämä pitää turtle ikkunan auki, ilman tätä ikkuna sulkeutuu piirtämisen jälkeen

# Paranneltua robottia ei saa toimimaan. Siis "Tee käsivarsi kerralla", silmät ja suu kyllä toimii.