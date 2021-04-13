import time
import math
import colorama
from colorama import Fore, Back, Style, init
import os
colorama.init()

#game v1
 







anonim = """
MMMMMMMMMWNNNklllllllllldKNNNWMMMMMMMMMM
MMMMMMMN0occcloooddoooodolcclxXMMMMMMMMM
MMMMMW0ocd000XNNNNNNNNNNNK00OocxXWMMMMMM
MMMMWd;dK0kkkKWWNNNNNNNNNOxxkKOc:0MMMMMM
MMMMWc;KKd:::clo0NNNNXxlcc::lkNd,kMMMMMM
MMMMWc;KNXXNXOc,:kNXOd,,dKNXXXNd,kMMMMMM
MMMMWc,OXKxlclldx0NXKkdoclloOXXl'kMMMMMM
MMMMWc.dOo,...,cdKNXKko;....:kO:'kMMMMMM
MMMMWc,OXKOO00KKO0NXKO0X000O0XXl'kMMMMMM
MMMMWc;0OddxKWNK0KNNX00XWN0xdxKd,kMMMMMM
MMMMWc,k0kk0XNKO0NNNXXO0NNKOkO0l'kMMMMMM
MMMMWc'd0l:xk00d;;ol:;ckKOko:xO:'kMMMMMM
MMMMWl;k0x:..,,..,oc;. .,..'lO0l,OMMMMMM
MMWWWXo:kXOxdkkddOK0OxdxkkdkKKo:ONMMMMMM
MMMMMMKockX000000xcodk00000KKdlkNMMMMMMM
MMMMMMMXl:d0KKXX0; .,dKXKK0kl;kMMMMMMMMM
MMMMMMMMWOlcxKNXO, .,lKNX0ocdKWMMMMMMMMM
MMMMMMMMMMNkolldk: .;dkolldKWMMMMMMMMMMM
MMMMMMMMMMMMWOol:'...,lodKMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNOxxxxxKMMMMMMMMMMMMMMMMM 

"""





menu = """
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░

1.Консоль
2.Настройки
3.Сообщения
"""





















load1 = 'Loading .'
load2 = 'Loading ..'
load3 = 'Loading ...'

asdlds = 0













e = " Elliot: "


os.system("clear")

while asdlds < 3:

    print(Fore.RED)
    print(anonim)
    print(Fore.GREEN)
    print(load1)
    time.sleep(0.5)
    os.system("clear")

    print(Fore.GREEN)
    print(anonim)
    print(Fore.GREEN)
    print(load2)
    time.sleep(0.5)
    os.system("clear")

    print(Fore.RED)
    print(anonim)
    print(Fore.GREEN)
    print(load3)
    time.sleep(0.5)
    os.system("clear")

    asdlds = asdlds + 1



a = 'Анонимус: '
print(anonim)
print(Fore.GREEN)

dial = 'Сообщения!'

txt = 'У вас новое сообщение!\n'
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    time.sleep(0.1)
    print(i, end='', flush=True)

sadasdasd = 0
while sadasdasd == 0:

    otvet123123 = input('1 - Открыть: ')
    if otvet123123 == '1':
        sadasdasd = 1
    else:
        os.system("clear")
        print(anonim)
        print('У вас новое сообщение!')
 
print('\n'+ Fore.BLACK + Back.GREEN + dial)
print(Fore.GREEN + Back.BLACK)
print('\n'+ Fore.GREEN + Back.BLACK + a)
txt = 'Эй ты тут?\n'
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    time.sleep(0.2)
    print(i, end='', flush=True)

otvetda = input('\n'+' Elliot: ')


print('\n'+ a)
txt = 'ТЫ ХОТЬ В КУРСЕ, ЧТО ТЕБЯ ЛОМАНУЛИ?!\n'
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    time.sleep(0.05)
    print(i, end='', flush=True)

txt = 'КАКОГО ЧЁРТА ТЫ СПИШЬ?!\n'
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    time.sleep(0.05)
    print(i, end='', flush=True)


otvetoqweow = input('\n' + e)

print('\n'+ a)
txt = 'Так сейчас заходи в консоль командой "cons"\n'
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    time.sleep(0.05)
    print(i, end='', flush=True)


neotvet = input('\n'+'Чтобы выйти введите "exit": ')
qweqwewe123 = 0
while qweqwewe123 == 0:
    if neotvet == 'exit':
        os.system("clear")
        print(menu)
        qweqwewe123 = 1
    else:
        neotvet = input('terminal: ')
t = 'terminal: '

ter12 = input('terminal: ')

dasddsada123 = 0
while dasddsada123 == 0:
    if ter12 == '1':
        txt = '\nВ папке "files" обнаружины вирусы!\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
        txt = '(для перехода в папку напишите "cd название папки")\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
        
        dasddsada123 = 1
    else:
        ter12 = input('terminal: ')



asdadqw1 = 0
sdad = input(virus)
while asdadqw1 == 0:
    virus = "console: "

    if sdad == 'cd files':
        txt = '(для списка файлов напишите "ls")\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
    
        asdadqw1 = 1
    else:
        sdad = input(virus)

cvirus = "console/files: "

asdqwe1 = input(cvirus)
asda = 0
while asda == 0:
    if asdqwe1 == "ls":
        print("""
        virus.exe
        data
        q123shadhiuq.txt
        1asdfijafiohij.txt
        jksdijasd.fdf
        asdlasdlw.png
        """)




        asda = 1   
    else:
        asdqwe1 = input(cvirus)
            


            





