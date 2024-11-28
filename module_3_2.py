def send_email(message,recipient,*sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not (recipient.endswith(".com") or (recipient.endswith(".ru") or (recipient.endswith(".net)) or not (sender.endswith(".com") or (sender.endswith(".ru") or (sender.endswith(".net"")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        send_email(resipient,sender)