import time
from pyrogram import Client
from tkinter import *
from tkinter import ttk
from data import api_id, api_hash, chat_ids, message

wind = Tk()  # создаем корневой объект - окно
wind.title("Telegram Spamer by rtyt")  # устанавливаем заголовок окна
wind.geometry("400x400")  # устанавливаем размеры окна
wind.iconbitmap(default="ico.ico")
wind.attributes("-alpha", 0.8)


# Синхронная функция для отправки сообщений с задержкой
def send_messages():
    with Client('my_session', api_id=api_id, api_hash=api_hash) as client:
        # Присоединяемся к каждому чату или каналу и отправляем сообщение
        for chat_id in chat_ids:
            try:
                # Присоединяемся к чату или каналу
                chat = client.get_chat(int(chat_id))
                print(f"Подписан на чат или канал с ID {chat_id}")

                # Ждем 2 секунды перед отправкой сообщения
                time.sleep(2)

                # Отправляем сообщение в чат или канал
                client.send_message(chat_id, message)
                print(f"Сообщение отправлено в чат или канал с ID {chat_id}")

                # Ждем 2 секунды перед следующей подпиской или отправкой
                time.sleep(2)

            except Exception as e:
                print(f"Ошибка в чате или канале с ID {chat_id}: {e}")

        # Закрываем подключение
        client.stop()


label = Label(text="Hello user")  # создаем текстовую метку
label.pack()  # размещаем метку в окне

btn = ttk.Button(text="Start", command=send_messages)  # создаем кнопку из пакета ttk
btn.pack()  # размещаем кнопку в окне

wind.mainloop()
