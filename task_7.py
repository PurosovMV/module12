print('Задача 7. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.
import random

def rock_paper_scissors():    
    #Здесь будет игра "Камень, ножницы, бумага"
    arr_action = ["камень", "ножницы", "бумага"]
    computer_running = random.choice(arr_action)
    print(computer_running)
    input_action = input("\nВыберите действие:\n1) Камень\n2) Ножницы\n3) Бумага\n")
    if (input_action == "1" and computer_running == "ножницы") or (input_action == "2"  and computer_running == "бумага") or (input_action == "3"  and computer_running == "камень"):
        print("\nВы выиграли")
    elif (input_action == "1" and computer_running == "камень") or (input_action == "2"  and computer_running == "ножницы") or (input_action == "3"  and computer_running == "бумага"):
        print("\nНичья")
    elif (input_action == "1" and computer_running == "бумага") or (input_action == "2"  and computer_running == "камень") or (input_action == "3"  and computer_running == "ножницы"):
        print("\nВы проиграли")
    else:
        print("\nПопробуйте ещё раз")
        rock_paper_scissors()
    rock_paper_scissors()
    


def guess_the_number():
    #Здесь будет игра "Угадай число"
    rnd_num = random.randint(1, 10 + 1)
    print(rnd_num)
    while True:
        input_num = int(input("\nВведи число: \n"))
        if rnd_num == input_num:
            print("\nВы угадали число!\n")
            main_menu()
            break
        else:
            print("\nВы не угадали число! Попробуйте снова!\n")
        
   
    
    
    return None

def main_menu():
    #Здесь главное меню игры
    choice_game = input("Выберите игру:\n1) «Камень, ножницы, бумага»;\n2) “Угадай число”\n")
    if choice_game == "1":
        rock_paper_scissors()
    elif choice_game == "2":
        guess_the_number()
    else:
        print("Не правильный ввод. Попробуйте снова\n")
        main_menu()
        
    

main_menu()