#Contar los números del 0 al 9
from colorama import Fore, Style
for numero in range(10):
    if numero % 2 == 0:
        print(Fore.GREEN + f"Número: {numero}" + Style.RESET_ALL)
        for num in range(numero):
            print(f"Antecesor: {num}")
            for n in range(num):
                if n % 2 != 0:
                    print (f"{n}")
    else:
        print(Fore.RED + f"Número: {numero}" + Style.RESET_ALL)
