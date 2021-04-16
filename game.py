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





menub = """
███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░

1.Консоль
2.Сообщения
3.Настройки
"""



errorb = """
####### ######  ######  ####### ######  
#       #     # #     # #     # #     # 
#       #     # #     # #     # #     # 
#####   ######  ######  #     # ######  
#       #   #   #   #   #     # #   #   
#       #    #  #    #  #     # #    #  
####### #     # #     # ####### #     #      
"""











load1 = 'Loading .'
load2 = 'Loading ..'
load3 = 'Loading ...'



asdd123wd = 0
def loading():
    while asdd123wd < 2:
        os.system(clear)
        print(load1)
        time.sleep(0.5)
        os.system(clear)
        print(load1)
        time.sleep(0.5)
        os.system(clear)
        print(load1)
        asdd123wd = asdd123wd + 1 

virus = "console: "














def menu():
    print(menu)
    ter12 = input('terminal: ')
    dasddsa23 = 0
    while dasddsa23 == 0:
        if ter12 == '1':
            dasddsada123 = 1
            console()

        elif ter12 == '2':

            


            dasddsada123 = 1
        else:
            ter12 = input('terminal: ')


def txt(x):
    txt = x
    for i in txt:  # этот цикл будет брать по 1 буковке из тхт
        time.sleep(0.05)
        print(i, end='', flush=True)













def errorfunc ():
    asdlds = 0
    
    while asdlds < 3:

            print(Fore.RED)
            print(errorb)
            print(Fore.GREEN)
            print(load1)
            time.sleep(0.5)
            os.system("clear")
            
            print(Fore.GREEN)
            print(errorb)
            print(Fore.GREEN)
            print(load2)
            time.sleep(0.5)
            os.system("clear")
            
            print(Fore.RED)
            print(errorb)
            print(Fore.GREEN)
            print(load3)
            time.sleep(0.5)
            os.system("clear")
            
            asdlds = asdlds + 1












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
txt = 'Так сейчас заходи в консоль\n'
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    time.sleep(0.05)
    print(i, end='', flush=True)


neotvet = input('\n'+'Чтобы выйти введите "exit": ')
qweqwewe123 = 0
while qweqwewe123 == 0:
    if neotvet == 'exit':
        os.system("clear")
        print(menub)
        qweqwewe123 = 1
    else:
        neotvet = input('terminal: ')
t = 'terminal: '

ter12 = 0

dasddsada123 = 0
while dasddsada123 == 0:
    if ter12 == '1':
        txt = '\nВ папке "files" обнаружины вирусы!\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
        txt = '\n(для перехода в папку напишите "cd название папки")\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
        
        dasddsada123 = 1
    else:
        ter12 = input('\nterminal: ')



asdadqw1 = 0
sdad = input(virus)

while asdadqw1 == 0:
    

    if sdad == 'cd files':
        txt = '\n(для списка файлов напишите "ls")\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
    
        asdadqw1 = 1
    else:
        sdad = input(virus)

cvirus = "\nconsole/files: "

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
        
asda = 0        




while asda == 0:
	
	
	
	
    txt = "\n(Для удаления файла напишите del имя файла.расширение!)"
    for i in txt:  # этот цикл будет брать по 1 буковке из тхт
                time.sleep(0.05)
                print(i, end='', flush=True)
    
    asdqwe1 = input(cvirus)
    
    
    
    
    if asdqwe1 == "del virus.exe":
        
        os.system('clear')
        txt = "Файл успешно удалён!"
        
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
        time.sleep(1)
        os.system("clear")
        
        print(cvirus)
        
        print("""
        data
        q123shadhiuq.txt
        1asdfijafiohij.txt
        jksdijasd.fdf
        asdlasdlw.png
        """)
        asda = 1  
	
        
        
        
        
        
      
      
      
    else:
        
        asdlds = 0
        os.system("clear")
        
        while asdlds < 3:

            print(Fore.RED)
            print(errorb)
            print(Fore.GREEN)
            print(load1)
            time.sleep(0.5)
            os.system("clear")
            
            print(Fore.GREEN)
            print(errorb)
            print(Fore.GREEN)
            print(load2)
            time.sleep(0.5)
            os.system("clear")
            
            print(Fore.RED)
            print(errorb)
            print(Fore.GREEN)
            print(load3)
            time.sleep(0.5)
            os.system("clear")
            
            asdlds = asdlds + 1
            
        
        os.system("clear")  
        print("""
        virus.exe
        data
        q123shadhiuq.txt
        1asdfijafiohij.txt
        jksdijasd.fdf
        asdlasdlw.png
        """)


neotvet = input('\n'+'Чтобы выйти введите "exit": ')
qweqwewe123 = 0
while qweqwewe123 == 0:
    if neotvet == 'exit':
        os.system("clear")
        qweqwewe123 = 1
    elif neotvet == "ls":
        print("""
        data
        q123shadhiuq.txt
        1asdfijafiohij.txt
        jksdijasd.fdf
        asdlasdlw.png
        """)
    else:
        neotvet = input("\nconsole/files: " )


print(menub)
        
txt = '\nУ вас 1 новое сообщение!\n'    
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    time.sleep(0.05)
    print(i, end='', flush=True)




asdadqw1 = 0




while asdadqw1 == 0:
    asdadqw1 = 0
    print(Fore.GREEN)
    
    
    if sdad == '2':
        os.system("clear")
        
        print(anonim)
        txt = '\nАнонимус: Что это было?\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)

        txt = 'Анонимус: Чёрт, ты же работаешь на BlueBerryCompany?\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)

        txt = 'Анонимус: Это CorpEvil закинули тебе троян!\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)

        txt = 'Анонимус: Их хакеры некудышные\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)

        txt = 'Анонимус: Они хотели украсть твои данные!\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)

        txt = 'Анонимус: Напиши об этом боссу!\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)


        asdadqw1 = 1



    elif sdad == '1':
        os.system("clear")
        errorfunc ()
        print(menub)

    elif sdad == '3':
        os.system("clear")
        errorfunc ()
        print(menub)
    else:
        sdad = input(t)


dasddsada123 = 0
ter12 = input('\n'+'Чтобы выйти введите "exit": ')

while dasddsada123 == 0:
    if ter12 == 'exit':
        os.system("clear")
        print('\n'+ Fore.BLACK + Back.GREEN + dial)
        print(Fore.GREEN + Back.BLACK)
        print("""
        1. anomimus
        2. boss
        """)
        
        dasddsada123 = 1
    else:
        ter12 = input('terminal: ')

ter12 = input(t)

dasddsada123 = 0
while dasddsada123 == 0:
    if ter12 == '2':
        os.system("clear")

        
        print('\n'+ Fore.BLACK + Back.GREEN + dial)
        print(Fore.GREEN + Back.BLACK)

        
        txt = 'Boss: ЧТО СЛУЧИЛОСЬ?!\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
        
        txt = e +'Компания CorpEvil меня взломала!\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)
            
        txt = 'Boss: Ну так чего ждать, наноси ответный удар!\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)

        txt = 'Boss: Чёртовы хакеры...\n'
        for i in txt:  # этот цикл будет брать по 1 буковке из тхт
            time.sleep(0.05)
            print(i, end='', flush=True)


        dasddsada123 = 1
    else:
        ter12 = input('terminal: ')


ter12 = input('\n'+'Чтобы выйти введите "exit": ')
dasddsada123 = 0
while dasddsada123 == 0:
    if ter12 == 'exit':
        dasddsada123 = 1
    else:
        ter12 = input('terminal: ')

dasddsada123 = 0
ter12 = '123'


while dasddsada123 == 0:

    print('\n'+ Fore.BLACK + Back.GREEN + dial)
    print(Fore.GREEN + Back.BLACK)
    print("""
    1. anomimus
    2. boss
    """)

    if ter12 == '1':
        os.system("clear")
        print('Нет новых сообщений!')
        time.sleep(1)

    if ter12 == '2':
        os.system("clear")
        print('Нет новых сообщений!')
        time.sleep(1)

    elif ter12 == 'exit':
        os.system('clear')
        dasddsada123 = 1
    else:
        ter12 = input('terminal: ')

print(menub)

txt = e + 'Для начала надо закинуть вирус работникам EvilCorp'
for i in txt:  # этот цикл будет брать по 1 буковке из тхт
    time.sleep(0.05)
    print(i, end='', flush=True)

asdadqw1 = input('terminal: ')
asdadqw1 = 0


while asdadqw1 == 0:
    asdadqw1 = 0
    print(Fore.GREEN)
    
    
    if sdad == '1':
        os.system("clear")
        asdadqw1 = 0
        errorfunc ()
        print(menub)
        



    elif sdad == '2':
        os.system("clear")
        asdadqw1 = 1



    elif sdad == '3':
        asdadqw1 = 0
        os.system("clear")
        errorfunc ()
        print(menub)
    else:
        sdad = input(t)



print('console: ')

asdadqw1 = 0
while asdadqw1 == 0:
    asdadqw1 = 0
    print(Fore.GREEN)
    
    
    if sdad == '1':
        os.system("clear")
        asdadqw1 = 1



    elif sdad == '2':
        os.system("clear")
        errorfunc ()
        print(menub)

    elif sdad == '3':
        os.system("clear")
        errorfunc ()
        print(menub)
    else:
        sdad = input(t)

