# Игра "Выбор имеет значение"
# Версия 0.1

choice = 0
check = 0
check2 = 0
check3 = 0

def hello():
    print("Приветствую вас в игре ,,Выбор имеет значение''")
    return int(input('Хотите начать игру? (1 - да, 2 - нет): '))


def check_exit():
    global check
    if start_project == 2:
        print('Хорошо, ждём вас снова')
    elif start_project == 1:
        check = 1
    else:
        print('Ошибка, ведён неправильный ответ, пожалуйста, повторите попытку')


def start_game():
    print('Вас зовёт король. Возможные действия: ')
    print("1 - Прийти")
    print("2 - Крикнуть ,,Мне лень''")
    print("3 - Крикнуть ,,Сам ко мне иди''")
    return int(input('Ваше действие: '))


def check_choice():
    global choice2
    if choice2 == 1:
        print('')
    elif choice2 == 2:
        print('')
    elif choice2 == 3:
        print('')
    else:
        print('Ошибка, ведён неправильный ответ, пожалуйста, повторите попытку')
        check_choice()


def talk_go_for_me():
    print('Король хотел казнить вас за такую дерзость,')
    print('но из - за свое скорой свадьбы король приказал')
    print('посадить вас в темницу, но вы остались живы!')
    print('Вы проиграли (нажмите 1 чтобы начать заново, 2 чтобы')


def check_choice2():
    global choice
    if start_project == 2:
        print('')
    elif start_project == 1:
        choice = start_game()  # выбор
    else:
        print('Ошибка, ведён неправильный ответ, пожалуйста, повторите попытку')


def work_function():
    t = 0
    print('')
    if t == 2:
        print('')
    elif t == 1:
        t = start_game()
    else:
        print('Ошибка, ведён неправильный ответ, пожалуйста, повторите попытку')
        print(t)
    return int(input('Ваше действие: '))


start_project = hello()
check_exit()
while check == 1:
    choice2 = start_game()
    break
check_choice()
