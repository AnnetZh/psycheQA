def send_email(message,recipient,*sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender:
       print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif not (recipient.endswith(".com") or (recipient.endswith(".ru") or (recipient.endswith(".net"):
       print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"))
    elif not (sender.endswith(".com") or (sender.endswith(".ru") or (sender.endswith(".net")):
       print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender==recipient:
        print(f"Нельзя отправить письмо самому себе!")

    elif sender!="university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient})

    else:
        send_email(resipient,sender) and print("Письмо успешно отправлено с адреса {sender} на адрес {recipient}")