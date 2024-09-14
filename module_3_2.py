def send_email(message, recipient, *, sender="university.help@gmail.com"):
    list_ = ('.ru', '.com', '.net')
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0
    for i in range(0, len(list_)):
        if recipient.find(list_[i]) == -1:
            sum_1 += 1
        if sum_1 == 3:
            print("Невозможно отправить письмо с адреса:", sender, "на адрес:", recipient)
            break
        if sender.find(list_[i]) == -1:
            sum_2 += 1
        if sum_2 == 3:
            print("Невозможно отправить письмо с адреса:", sender, "на адрес:", recipient)
            break
        if recipient.find('@') == -1 or sender.find('@') == -1:
            print("Невозможно отправить письмо с адреса:", sender, "на адрес:", recipient)
            break
        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            break
        if sender == "university.help@gmail.com" and recipient.find(list_[i]) != -1:
            sum_4 += 1
            if sum_4 > 0:
                print("Письмо успешно отправлено с адреса:", sender, "на адрес:", recipient)
            break
        if sender != "university.help@gmail.com" and sender.find(list_[i]) != -1:
                sum_3 += 1
                if sum_3 > 0:
                    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса:", sender, "на адрес:", recipient)
                break
    return
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')