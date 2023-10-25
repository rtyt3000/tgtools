import time
from pyrogram import Client

# Читаем данные из файлов
with open('api_data.txt', 'r') as api_file, \
        open('user_data.txt', 'r') as user_file, \
        open('message.txt', 'r', encoding='utf-8') as message_file, \
        open('chats.txt', 'r') as chats_file:
    api_id, api_hash = api_file.read().splitlines()
    phone_number, password = user_file.read().splitlines()
    message = message_file.read()
    chat_ids = chats_file.read().splitlines()

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

# Запускаем синхронную функцию
if __name__ == '__main__':
    send_messages()
