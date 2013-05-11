def hacerCombinaciones(comb):
    cont = 0
    result = ""
    for i in comb:
        for j in (comb[:cont] + comb[cont+1:]):
            result = result + "(\"%s , %s\") , " %(i,j)
        cont += 1
    return result

def main():
    comb = "abcd"
    print hacerCombinaciones(comb)

if __name__ == "__main__":
    main()
