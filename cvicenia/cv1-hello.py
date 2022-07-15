#!/usr/bin/env python3

class Hello:
    def __init__(self, paMeno):
        self.aMeno = paMeno
        self.aPozdravSK = 'Ahoj'
        self.aPozdravEN = "Hello"
        
    def pozdravMna(self, paJazyk):
        if paJazyk == "EN":
            return self.aPozdravEN + " " + self.aMeno
        if paJazyk == "SK":
            return self.aPozdravSK + " " + self.aMeno
            
jazyk = input("Choose language/Vyberte jazyk (SK/EN):")
meno = input("Enter name/Zadajte meno:")

instancia = Hello(meno)
vystup = instancia.pozdravMna(jazyk)
print(vystup)