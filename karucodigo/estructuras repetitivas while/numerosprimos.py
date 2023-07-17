n = int(input("Numero: "))

while n >= 0:
    #PROCESO Si n es primo
    if n > 1:
        primo = True
        divisor = 0
        # for i in range(2, n):
        #     if n % i == 0:
        #         primo = False
        #         divisor = i

        i = 2
        # while i < n:
        #     if n % i == 0:
        #         primo = False
        #         divisor = i
        #     i += 1  # i = i + 1
            
        while i < n and n % i !=0:
            i += 1
            
        if i < n:
            print("El numero NO ES primo.  Lo divide", i)
        else:
            print("El numero ES primo.")
                            
        # if primo:
        #     print("El numero ES primo")
        # else:
        #     print("El numero NO ES primo. lo divide", divisor)
        
        
    else:
        print("NO ES primo")
    
    n = int(input("\nNumero: "))