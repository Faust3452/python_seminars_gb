import methods
from telebot import TeleBot, types
import os

def ui():
    global numbers
    numbers = methods.make_numbers_list()
    token = '5884155558:AAH-Tykh-J09sp_xHuUkNV2w1tw2lgO3Q1A'
    bot = TeleBot(token)
    @bot.message_handler(commands=['help', 'start'])
    def answer(msg: types.Message):
        txt = """Добро пожаловать в телефонный справочник! Для выбора какого-либо пункта меню введите команду:
                            1. Просмотр телефонного справочника - /show
                            2. Добавление записи - /add
                            3. Импорт записей - /import
                            4. Экспорт записей - /export
                            -------------------------------------------
                            Дополнительно:
                            5. Поиск записи в справочнике - /search
                            6. Удаление записи в справочнике - /delete
                            -------------------------------------------
                            Введите цифру
        """
        bot.send_message(chat_id=msg.from_user.id, text=txt)
        pass

    @bot.message_handler(commands=['test'])
    def answer(msg: types.Message):
        bot.send_document(chat_id=msg.from_user.id, document=types.InputFile('data.csv'))

    @bot.message_handler(commands=['show'])
    def answer(msg: types.Message):
        i = 1
        bot.send_message(chat_id=msg.from_user.id, text='-------Телефонный--справочник-------')
        for l in range(len(numbers)):
            txt = methods.show_numbers(numbers[l], i)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            i += 1


    @bot.message_handler(commands=['add'])
    def answer(msg: types.Message):
        global new_member
        new_member = []
        txt = 'Введите фамилию нового абонента'
        bot.register_next_step_handler(msg, add_surname)
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    def add_surname(msg: types.Message):
        global new_member
        new_member.append(msg.text)
        txt = 'Принято! Введите имя нового абонента'
        bot.register_next_step_handler(msg, add_name)
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    def add_name(msg: types.Message):
        global new_member
        new_member.append(msg.text)
        txt = 'Принято! Введите номер нового абонента'
        bot.register_next_step_handler(msg, add_number)
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    def add_number(msg: types.Message):
        global new_member
        new_member.append(msg.text)
        txt = 'Принято! Введите примечание для нового абонента'
        bot.register_next_step_handler(msg, add_note)
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    def add_note(msg: types.Message):
        global new_member
        global numbers
        new_member.append(msg.text)
        methods.add_record(surname=new_member[0], name=new_member[1], num=new_member[2], info=new_member[3])
        member = methods.show_numbers(l=new_member)
        numbers = methods.make_numbers_list()
        txt = f'Следующий абонент добавлен в телефонный справочник!\n{member}'
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    @bot.message_handler(commands=['import'])
    def answer(msg: types.Message):
        txt = 'Прикрепите файл для импорта'
        bot.register_next_step_handler(msg, import_format)
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    def import_format(msg: types.Message):
        global numbers
        if msg.content_type == 'document':
            if msg.document.file_name.split('.')[1] == 'txt':
                fmt = 1
                file = bot.get_file(file_id=msg.document.file_id)
                wr = bot.download_file(file.file_path)
            elif msg.document.file_name.split('.')[1] == 'csv':
                fmt = 2
                file = bot.get_file(file_id=msg.document.file_id)
                wr = bot.download_file(file.file_path)
            elif msg.document.file_name.split('.')[1] == 'json':
                fmt = 3
                file = bot.get_file(file_id=msg.document.file_id)
                wr = bot.download_file(file.file_path)
            elif msg.document.file_name.split('.')[1] == 'xml':
                fmt = 4
                file = bot.get_file(file_id=msg.document.file_id)
                wr = bot.download_file(file.file_path)
            else:
                txt = 'Вы отправили файл не того формата, отправьте повторно!'
                bot.register_next_step_handler(msg, import_format)
                bot.send_message(chat_id=msg.from_user.id, text=txt)
                return 0
            try:
                with open(msg.document.file_name, mode='wb') as f:
                    f.write(wr)
                txt = 'Сделано!'
                methods.import_record(fmt, msg.document.file_name)
                numbers = methods.make_numbers_list()
                bot.send_message(chat_id=msg.from_user.id, text=txt)
                os.remove(msg.document.file_name)
            except Exception as e:
                os.remove(msg.document.file_name)
                txt = 'Содержание файла не соответствует формату! Отправьте файл повторно'
                bot.register_next_step_handler(msg, import_format)
                bot.send_message(chat_id=msg.from_user.id, text=txt)
        else:
            txt = 'Вы не отправили файл! Отправьте повторно!'
            bot.register_next_step_handler(msg, import_format)
            bot.send_message(chat_id=msg.from_user.id, text=txt)

    @bot.message_handler(commands=['export'])
    def answer(msg: types.Message):
        txt = """Необходимо выбрать формат для созадаваемого файла, выберите и введите цифру, соответствующую сделанному выбору:
                        1. Исходный формат, в котором хранится справочник (исходный)
                        2. csv-формат
                        3. json-формат
                        4. xml-формат
            """
        bot.register_next_step_handler(msg, export_format)
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    def export_format(msg: types.Message):
        try:
            if int(msg.text) in range(1, 5):
                if int(msg.text) == 1:
                    name = methods.export_record(1)
                elif int(msg.text) == 2:
                    name = methods.export_record(2)
                elif int(msg.text) == 3:
                    name = methods.export_record(3)
                elif int(msg.text) == 4:
                    name = methods.export_record(4)
                bot.send_document(chat_id=msg.from_user.id, document=types.InputFile(name))
            else:
                raise Exception
        except Exception as e:
            txt = """Вы неверно указали цифру формата для экспорта, пожалуйства, повторите ввод!
                        1. Исходный формат, в котором хранится справочник (исходный)
                        2. csv-формат
                        3. json-формат
                        4. xml-формат
            """
            bot.register_next_step_handler(msg, export_format)
            bot.send_message(chat_id=msg.from_user.id, text=txt)

    @bot.message_handler(commands=['search'])
    def answer(msg: types.Message):
        txt = 'Введите через пробел значения, по которым будет произведен поиск. Внимание: будут отражены все записи в телефонной книге, где встречается хотя бы одно из указанных значений целиком хотя бы в одном из полей!'
        bot.register_next_step_handler(msg, search_res)
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    def search_res(msg: types.Message):
        search_list = msg.text.split()
        res = methods.search(numbers, search_list)
        if len(res) == 0:
            bot.send_message(chat_id=msg.from_user.id, text='По вашему запросу ничего не найдено')
        else:
            i = 1
            bot.send_message(chat_id=msg.from_user.id, text='Результаты поиска по вашему запросу:')
            for k in res:
                txt = methods.show_numbers(k, i)
                bot.send_message(chat_id=msg.from_user.id, text=txt)
                i += 1

    @bot.message_handler(commands=['delete'])
    def answer(msg: types.Message):
        i = 1
        bot.send_message(chat_id=msg.from_user.id, text='-------Телефонный--справочник-------')
        for l in range(len(numbers)):
            txt = methods.show_numbers(numbers[l], i)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            i += 1
        bot.send_message(chat_id=msg.from_user.id, text='Введите порядковый номер абонента для удаления!')
        bot.register_next_step_handler(msg, delete)

    def delete(msg: types.Message):
        global numbers
        num_to_delete = []
        try:
            num = int(msg.text)
            if num in range(1, len(numbers)+1):
                num_to_delete.append(numbers[num - 1])
                bot.send_message(chat_id=msg.from_user.id, text='Запись успешно удалена!')
                methods.delete_records(num_to_delete, numbers)
                numbers = methods.make_numbers_list()
            else:
                bot.send_message(chat_id=msg.from_user.id, text='Вы ввели порядковый номер абонента, которого нет в телефонном справочнике!')
                bot.register_next_step_handler(msg, delete)
        except Exception as e:
            bot.send_message(chat_id=msg.from_user.id, text='Вы ввели не число, повторите ввод!')
            bot.register_next_step_handler(msg, delete)


    @bot.message_handler()
    def answer(msg: types.Message):
        txt = 'Вы ввели что-то, что бот не в силах понять! Для помощи введите /start или /help'
        bot.send_message(chat_id=msg.from_user.id, text=txt)

    bot.polling()

if __name__ == "__main__":
    ui()