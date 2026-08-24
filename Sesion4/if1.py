#Leer la nota de un estudiante y decir aprobado o reprobado
from colorama import Fore, Style
grade = int(input("Ingrese la nota: "))
if grade >= 70:
    print(Fore.GREEN + "Usted está aprobado.")
else:
    print(Fore.RED + "Usted está reprobado.")
print(Style.RESET_ALL)