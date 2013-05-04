def calcASegundos(horas,minutos,segundos):

    return 3600*int(horas) + 60*int(minutos) + int(segundos)

def main():
    for i in range(3):
        hs = raw_input("Cuantas horas: ")
        mins = raw_input("Cuantos minutos: ")
        seg = raw_input("Cuantos segundos: ")
        print(calcASegundos(hs,mins,seg))

if __name__ == "__main__":
    main()
