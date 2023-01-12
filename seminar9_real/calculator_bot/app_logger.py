import telebot
import time


def bot_start():
    f = open('LOG.txt', mode='a', encoding='UTF-8')
    f.write(time.strftime("%d-%m-%Y %H:%M:%S -> ") + 'bot started!' + '\n')
    f.close()


def msg_write(msg: telebot.types.Message):
    f = open('LOG.txt', mode='a', encoding='UTF-8')
    f.write(time.strftime("%d-%m-%Y %H:%M:%S -> ") + f'message from: UID: {msg.from_user.id}, username: {msg.from_user.username}, message ID: {msg.id}, text: {msg.text}' + '\n')
    f.close()

def reply_for_message(msg: telebot.types.Message, txt):
    f = open('LOG.txt', mode='a', encoding='UTF-8')
    f.write(time.strftime("%d-%m-%Y %H:%M:%S -> ") + f'reply for: UID: {msg.from_user.id}, username: {msg.from_user.username}, message ID: {msg.id}, reply: {txt}' + '\n')
    f.close()

def emergency_exit():
    f = open('LOG.txt', mode='a', encoding='UTF-8')
    f.write(time.strftime("%d-%m-%Y %H:%M:%S -> ") + 'Бот аварийно закончил свою работу!')
    f.close()

if __name__ == "__main__":
    bot_start()
