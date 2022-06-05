from math import pi

lst = []
figura = []
ilosc_figur = int(float(input().strip()))

for i in range(ilosc_figur):
    lst.append(input().split())

def obliczanie_kola(a):
        return pi * a * a
def obliczanie_prostokata(a,b):
        return a * b
def obliczanie_trojkata(a,b,c):
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

pole = 0

for figura in lst:
    if len(figura) == 1:
        a = float(figura[0])
        pole += obliczanie_kola(a)
    elif len(figura) == 2:
        a = float(figura[0])
        b = float(figura[1])
        pole += obliczanie_prostokata(a,b)
    elif len(figura) == 3:
        a = float(figura[0])
        b = float(figura[1])
        c = float(figura[2])
        s = ((a + b + c)/2)
        pole += obliczanie_trojkata(a,b,c)
    else:
        print("Błąd: można podać maksymalnie 3 liczby")
        break

print(round(pole,2))

if __name__ == '__main__':
    main()