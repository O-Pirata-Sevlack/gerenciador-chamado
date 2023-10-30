import django
import colorama
from colorama import Fore, Style


nome_do_arquivo = "registro.txt"
colorama.init()
print(Fore.RED + "SISTEMA: " + Style.RESET_ALL, end='')
print(Fore.GREEN + "Olá, bem vindo ao Gerenciador de Chamados da TI!" + Fore.RESET)

print("")
print(Fore.BLACK + "#"*80 + Fore.RESET)
print("")

while True:
  
  with open(nome_do_arquivo, "a") as arquivo:
           
    print(Fore.RED + "PERGUNTA: " + Style.RESET_ALL, end='')
    print ((Fore.GREEN +'Nome de quem ligou: ---> ') + Style.RESET_ALL, end="")
    P1 = input()
    arquivo.write((' Nome de quem ligou: ' + P1 + "\n"))
    

    print()
    
    print(Fore.RED + "PERGUNTA: " + Style.RESET_ALL, end='')
    print ((Fore.GREEN + "Ramal: ---> ")+ Style.RESET_ALL, end="")
    P2 = input()
    arquivo.write((" Ramal: " + P2 + "\n"))

    print()
       
       
    print(Fore.RED + "PERGUNTA: " + Style.RESET_ALL, end='')
    print ((Fore.GREEN + "Setor? ---> ")+Style.RESET_ALL, end="")
    P4 = input()
    arquivo.write((" Setor: " + P4 + "\n"))

    print()
    
    print(Fore.RED + "PERGUNTA: " + Style.RESET_ALL, end='')
    print ((Fore.GREEN + "Foi realizado a abertura do chamado no GLPI? (Responda: S / N) ---> ") + Style.RESET_ALL, end="")
    P5 = str(input())
    if P5 == "S" or P5 == "s":
       P5 = "SIM"
       arquivo.write((" Foi realizado a abertura do chamado no GLPI: " + P5 + "\n"))
       print(Fore.RED + "PERGUNTA: " + Style.RESET_ALL, end='')
       print ((Fore.GREEN + "Qual o número do chamado no GLPI? ---> ") + Style.RESET_ALL, end="")
       P6 = input()
       arquivo.write((" O número do chamado GLPI é: " + P6 + "\n"))
    else:
       P5 = "NÃO"
       arquivo.write((" Foi realizado a abertura do chamado no GLPI: " + P5 + "\n"))
    print()
    print(Fore.RED + "PERGUNTA: " + Style.RESET_ALL, end='')
    print ((Fore.GREEN +"Qual a solicitação? ---> ") + Style.RESET_ALL, end="")
    P3 = input()
    arquivo.write((" Qual a solicitação: " + P3 + "\n"))

    print()
    
    arquivo.write("\n")
    arquivo.write("\n")
    
    print("")
    print(Fore.BLACK + "#"*80 + Fore.RESET)
    print("")
    print(Fore.RED + "SISTEMA: " + Style.RESET_ALL, end='')
    STOP = input(Fore.BLUE + "Deseja registrar outro chamado? (Responda: S / N) " + Fore.RESET)
    print("")
    print(Fore.BLACK + "#"*80 + Fore.RESET)
    print("")
    
    arquivo.close()
    
    if STOP == "N" or STOP == 'n':
      break
    else:
     continue
    