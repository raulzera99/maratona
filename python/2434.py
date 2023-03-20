def main():
    array = [int(x) for x in input().split()]
    dias = array[0]
    saldo_inicial = array[1]
    saldo = saldo_inicial
    menor = saldo
    for i in range(dias):
        t = int(input())
        saldo = saldo + t
        if (saldo < menor):
            menor = saldo
             
    print(menor)
    
if(__name__ == '__main__'):
    main()