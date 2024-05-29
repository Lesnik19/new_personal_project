import win10toast
import schedule
ran = True


def prank():
    global ran
    toast = win10toast.ToastNotifier()
    toast.show_toast(title='Тест', msg='Это просто проверка связи', duration=5)
    toast.show_toast(title='Связь', msg='Так, вроде бы ты меня слышишь, привет!', duration=10)
    toast.show_toast(title='Требую внимания', msg='Эй, я знаю что ты меня слышишь!', duration=10)
    toast.show_toast(title='Предупреждение', msg='Если ты не обратишь на меня внимание, я выключу компьютер!',
                     duration=10)
    toast.show_toast(title='Отчёт времени', msg='Считаю до трёх', duration=10)
    toast.show_toast(title='Время', msg='Раз', duration=3)
    toast.show_toast(title='Время', msg='Два', duration=3)
    toast.show_toast(title='Время', msg='Три', duration=3)
    toast.show_toast(title='Обида', msg='Всё, я обиделся, я ухожу отсюда!', duration=10)
    ran = False


schedule.every(3).do(prank)

while True:
    if ran:
        schedule.run_pending()
    else:
        break
