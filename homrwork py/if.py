# a = int(input())
#
# if a >= 18:
#     print("Заходи товарищ ")
# elif a >= 100:
#     print("заходи ")
# else:
#     print("Вход нема")

#
#     def Func_Crc = 23
#      return Func_Crc

# a = int(input())
# b = (input())
# if  a == b :
#     print(" пиши число")

language = input("What is your language? ")
timeZone = input("What is the time (morning/evening(utro/vecher)? ")

if language == "english":
    if timeZone == "morning":
        print("Good morning!")
    elif timeZone == "evening":
        print("Good evening!")
    else:
        print("Sorry, time not recognized.")
elif language == "russian":
    if timeZone == "utro":
        print("Доброе утро!")
    elif timeZone == "vecher":
        print("Добрый вечер!")
    else:
        print("Sorry, time not recognized.")
else:
    print("Sorry, language not recognized.")

