import self


class Kissa:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä

    def tiedot(self):
        return f"{self.nimi} on {self.ikä} vuotta vanha."

kissa1 = Kissa("Kissa", 8)
kissa2 = Kissa("Kala", 6)

print(kissa1.tiedot())
print(kissa2.tiedot())