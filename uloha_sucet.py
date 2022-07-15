def ciselny_sucet(paCislo):
    cifSucet = 0

    while paCislo > 0:
        cifSucet += paCislo % 10
        paCislo = paCislo // 10


    return cifSucet

print(ciselny_sucet(159753))