from PIL import Image, ImageDraw, ImageFont
from random import randint
from colorama import init, Fore, Back
from os import path

#iniciar colorama 
init(autoreset=True)

#inputs de nome e ano de nascimento
name = input("Nome: ")
try:
    BirthDate = int(input("\nAno de nascimento: "))
except:
    print(Fore.RED+"Use apenas números")

#Calculo de idade
if BirthDate <= 2021:
    try:
        age = 2021 - BirthDate
    except:
        print(Fore.RED+"Use apenas números")
elif BirthDate >= 2021:
    try:
        age = BirthDate - 2021
    except:
        print(Fore.RED+"Use apenas números")


    

PersonalId = randint(1000110,9999999)
SecurityCode = randint(1011,9999)
SecurityCodeInput = int(input(f"\nCodigo de segurança [{SecurityCode}]:> "))
myFont = ImageFont.truetype(f"{path.dirname(__file__)}\main\Font.ttf", 13)

#funcao pra desenhar os informacoes na imagem do ticket
def drawText():
    TicketImg = Image.open(f"{path.dirname(__file__)}\main\EmptyTicket.jpg")
    TicketImgDrawn = ImageDraw.Draw(TicketImg)
    TicketImgDrawn.text((50,17), name, font=myFont, fill=(255,255,255))
    ##
    TicketImgDrawn.text((169,17), str(age), font=myFont, fill=(255,255,255))
    TicketImgDrawn.text((214,17), str(PersonalId), font=myFont, fill=(255,255,255))
    TicketImgDrawn.text((150,56), str(SecurityCode), font=myFont, fill=(255,255,255))
    TicketImg.show()
    TicketImg.save(f'{path.abspath(__file__)}TicketImg.jpg',quality=1000)

#verificar codigo de seguranca e escrever o texto
if SecurityCodeInput == SecurityCode:
    print(Fore.GREEN + "Codigo Correto")
    drawText()
else:
    print(Fore.RED + "Codigo Incorreto")
    exit()

