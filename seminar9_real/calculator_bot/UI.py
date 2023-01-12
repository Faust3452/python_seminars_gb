from telebot import TeleBot, types
import methods_rational as mthd_rat
import methods_complex as mthd_com
import app_logger


def user_interface():
    token = '5760936256:AAGawYwmXYa8IuF5SwxIuovdxg2cPG4Sox0'
    bot = TeleBot(token)

    @bot.message_handler(commands=['start', 'help'])
    def answer(msg: types.Message):
        txt = """Добро пожаловать в калькулятор-бот!
        Он умеет работать с комплексными и рациональными числами.
        Список доступных операций:
        1) Сложение
        2) Вычитание
        3) Умножение
        4) Деление
        Доступные команды:
        /ratio - работа с рациональными числами
        /complex - работа с комплексными числами
        /log - показать лог работы
        """
        bot.send_message(chat_id=msg.from_user.id, text=txt)
        app_logger.msg_write(msg)
        app_logger.reply_for_message(msg, 'Welcome text of /start command')

    @bot.message_handler(commands=['log'])
    def answer(msg: types.Message):
        bot.register_next_step_handler(msg, start_log)
        bot.send_message(chat_id=msg.from_user.id, text='Лог будет выводиться по одной записи за раз, начиная с поледней записи\nДля начала напишите start, чтобы не просматривать - что-либо другое')
        txt = 'LOG showed'
        app_logger.msg_write(msg)
        app_logger.reply_for_message(msg, txt)

    def start_log(msg: types.Message):
        global f
        f = open('LOG.txt', encoding='UTF-8').readlines()
        if msg.text == 'start':
            txt = f.pop()
            bot.register_next_step_handler(msg, next_log)
            bot.send_message(chat_id=msg.from_user.id, text=txt + '\n Для просмотра следующей записи напишите next, чтобы закончить просмотр - что-либо другое')
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        else:
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, 'User decided not to look at LOG')
            return 0

    def next_log(msg: types.Message):
        if msg.text == 'next':
            txt = f.pop()
            bot.register_next_step_handler(msg, next_log)
            bot.send_message(chat_id=msg.from_user.id, text=txt + '\n Для просмотра следующей записи напишите next, чтобы закончить просмотр - что-либо другое')
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        else:
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, "LOG's show ended!")
            return 0

# ---------------------------------------------------------Ratio----------------------------------------------------------------------------

    @bot.message_handler(commands=['ratio'])
    def answer(msg: types.Message):
        txt = """Введите номер операции (1-5), которую будем совершать над рациональными числами
        1. сложение
        2. деление
        3. умножение
        4. деление
        5. Возведение в степень
        """
        bot.register_next_step_handler(msg, operation)
        bot.send_message(chat_id=msg.from_user.id, text=txt)
        app_logger.msg_write(msg)
        app_logger.reply_for_message(msg, txt)

    def input_one(msg: types.Message):
        try:
            global one
            one = float(msg.text)
            bot.register_next_step_handler(msg, input_two)
            txt = 'Первое число принято, введите второе число.'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, input_one)
            txt = 'Вы ввели неверное число, пожалуйста, повторите ввод!'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def input_two(msg: types.Message):
        try:
            global two
            two = float(msg.text)
            bot.register_next_step_handler(msg, making_operation)
            txt = 'Второе число принято. Отправьте что-либо, чтобы увидеть результат'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, input_two)
            txt = 'Вы ввели не число, пожалуйста, повторите ввод!'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def operation(msg: types.Message):
        try:
            global operation_num
            operation_num = int(msg.text)
            if operation_num in range(1, 5):
                bot.register_next_step_handler(msg, input_one)
                txt = 'Введите первое число'
                bot.send_message(chat_id=msg.from_user.id, text=txt)
                app_logger.msg_write(msg)
                app_logger.reply_for_message(msg, txt)
            elif operation_num == 5:
                bot.register_next_step_handler(msg, num_for_degree)
                txt = 'Введите число для возведения в степень'
                bot.send_message(chat_id=msg.from_user.id, text=txt)
                app_logger.msg_write(msg)
                app_logger.reply_for_message(msg, txt)
            else:
                raise Exception
        except Exception as e:
            bot.register_next_step_handler(msg, operation)
            txt = """Вы ввели неверный номер операции, введите номер операции (1-5), которую будем совершать над рациональными числами
                                        1. сложение
                                        2. деление
                                        3. умножение
                                        4. деление
                                        5. Возведение в степень
                                        """
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def num_for_degree(msg: types.Message):
        try:
            global one
            one = float(msg.text)
            bot.register_next_step_handler(msg, degree)
            txt = 'Число для возведения в степень принято. Теперь введите степень, в которую будем возводить число.'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, num_for_degree)
            txt = 'Вы неверно ввели число, повторите ввод.'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def degree(msg: types.Message):
        try:
            global two
            two = float(msg.text)
            bot.register_next_step_handler(msg, making_operation)
            txt = 'Степень, в которую будем возводить, принята. Отправьте что-либо, чтобы увидеть результат'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, degree)
            txt = 'Вы неверно ввели степень для возведения, повторите ввод.'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def making_operation(msg: types.Message):
        global operation_num
        global one
        global two
        if operation_num == 1:
            operation_num = ' + '
            result = mthd_rat.sum(one, two)
        elif operation_num == 2:
            operation_num = ' - '
            result = mthd_rat.substraction(one, two)
        elif operation_num == 3:
            operation_num = ' * '
            result = mthd_rat.multiplication(one, two)
        elif operation_num == 4:
            operation_num = ' / '
            result = mthd_rat.division(one, two)
        elif operation_num == 5:
            operation_num = ' ^ '
            result = mthd_rat.power(one, two)
        txt = f'Итог:\n{one}{operation_num}{two}' + ' = ' + f'{result}'
        bot.send_message(chat_id=msg.from_user.id, text=txt)
        app_logger.msg_write(msg)
        app_logger.reply_for_message(msg, txt)

# ---------------------------------------------------------Complex----------------------------------------------------------------------------

    @bot.message_handler(commands=['complex'])
    def answer(msg: types.Message):
        txt = """Введите номер операции (1-5), которую будем совершать над комплексными числами
        1. сложение
        2. деление
        3. умножение
        4. деление
        5. Возведение в степень
        """
        bot.register_next_step_handler(msg, operation_com)
        bot.send_message(chat_id=msg.from_user.id, text=txt)
        app_logger.msg_write(msg)
        app_logger.reply_for_message(msg, txt)

    def input_one_re(msg: types.Message):
        try:
            global one
            one = []
            inp = float(msg.text)
            one.append(inp)
            bot.register_next_step_handler(msg, input_one_im)
            txt = 'Действительная часть первого числа принята, введите комлпексную часть первого числа.'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, input_one_re)
            txt = 'Вы ввели неверно действительную часть первого числа, пожалуйста, повторите ввод!'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def input_one_im(msg: types.Message):
        try:
            global one
            inp = float(msg.text)
            one.append(inp)
            txt = 'Комплексная часть первого числа принята, введите действительную часть второго числа.'
            bot.register_next_step_handler(msg, input_two_re)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, input_one_im)
            txt = 'Вы ввели неверно комплексную часть первого число, пожалуйста, повторите ввод!'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)


    def input_two_re(msg: types.Message):
        try:
            global two
            two = []
            inp = float(msg.text)
            two.append(inp)
            txt = 'Действительная часть второго числа принята. Введите комлпексную часть второго числа'
            bot.register_next_step_handler(msg, input_two_im)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            txt = 'Вы ввели неверно действительную часть второго числа, пожалуйста, повторите ввод!'
            bot.register_next_step_handler(msg, input_two_re)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def input_two_im(msg: types.Message):
        try:
            global two
            inp = float(msg.text)
            two.append(inp)
            txt = 'Комплексная часть второго число принята. Отправьте что-либо, чтобы увидеть результат'
            bot.register_next_step_handler(msg, making_operation_complex)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            txt = 'Вы ввели неверно комплексную часть второго числа, пожалуйста, повторите ввод!'
            bot.register_next_step_handler(msg, input_two_im)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def operation_com(msg: types.Message):
        try:
            global operation_num
            operation_num = int(msg.text)
            if operation_num in range(1, 5):
                txt = 'Введите действительную часть первого число'
                bot.register_next_step_handler(msg, input_one_re)
                bot.send_message(chat_id=msg.from_user.id, text=txt)
                app_logger.msg_write(msg)
                app_logger.reply_for_message(msg, txt)
            elif operation_num == 5:
                txt = 'Введите действительную часть числа для возведения в степень'
                bot.register_next_step_handler(msg, num_for_degree_re)
                bot.send_message(chat_id=msg.from_user.id, text=txt)
                app_logger.msg_write(msg)
                app_logger.reply_for_message(msg, txt)
            else:
                raise Exception
        except Exception as e:
            txt = """Вы ввели неверный номер операции, введите номер операции (1-5), которую будем совершать над рациональными числами
                                        1. сложение
                                        2. деление
                                        3. умножение
                                        4. деление
                                        5. Возведение в степень
                                        """
            bot.register_next_step_handler(msg, operation_com)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def num_for_degree_re(msg: types.Message):
        try:
            global one
            one = []
            inp = float(msg.text)
            one.append(inp)
            txt = 'Действительная часть числа для возведения в степень принята. Теперь введите комплексную часть числа.'
            bot.register_next_step_handler(msg, num_for_degree_im)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, num_for_degree_re)
            txt = 'Вы неверно ввели действительную часть числа, повторите ввод.'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def num_for_degree_im(msg: types.Message):
        try:
            global one
            inp = float(msg.text)
            one.append(inp)
            txt = 'Комплексная часть числа для возведения в степень принята. Теперь введите степень, в которую будем возводить число.'
            bot.register_next_step_handler(msg, degree_complex)
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, num_for_degree_im)
            txt = 'Вы неверно ввели комплексную часть числа, повторите ввод.'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def degree_complex(msg: types.Message):
        try:
            global dgr
            dgr = float(msg.text)
            bot.register_next_step_handler(msg, making_operation_complex)
            txt = 'Степень, в которую будем возводить, принята. Отправьте что-либо, чтобы увидеть результат'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
        except Exception as e:
            bot.register_next_step_handler(msg, degree_complex)
            txt = 'Вы неверно ввели степень для возведения, повторите ввод.'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)

    def making_operation_complex(msg: types.Message):
        global operation_num
        global one
        global two
        global dgr
        if operation_num == 1:
            operation_num = ' + '
            result = mthd_com.sum(one, two)
        elif operation_num == 2:
            operation_num = ' - '
            result = mthd_com.substraction(one, two)
        elif operation_num == 3:
            operation_num = ' * '
            result = mthd_com.multiplication(one, two)
        elif operation_num == 4:
            operation_num = ' / '
            result = mthd_com.division(one, two)
        elif operation_num == 5:
            operation_num = ' ^ '
            result = mthd_com.power(one, dgr)
            if one[1] >= 0:
                one[1] = f'+{str(one[1])}'
            if result[1] >= 0:
                result[1] = f'+{str(result[1])}'
            txt = f'Итог:\n({one[0]} {one[1]}i){operation_num}{dgr}' + ' = ' + f'{result[0]} {result[1]}i'
            bot.send_message(chat_id=msg.from_user.id, text=txt)
            app_logger.msg_write(msg)
            app_logger.reply_for_message(msg, txt)
            return 0
        if one[1] >= 0:
            one[1] = f'+{str(one[1])}'
        if two[1] >= 0:
            two[1] = f'+{str(one[1])}'
        if result[1] >= 0:
            result[1] = f'+{str(result[1])}'
        txt = f'Итог:\n({one[0]} {one[1]}i){operation_num}({two[0]} {two[1]}i)' + ' = ' + f'{result[0]} {result[1]}i'
        bot.send_message(chat_id=msg.from_user.id, text=txt)
        app_logger.msg_write(msg)
        app_logger.reply_for_message(msg, txt)

    @bot.message_handler()
    def answer(msg: types.Message):
        txt = 'Вы ввели что-то, что бот не в силах понять! Для помощи введите /start или /help'
        bot.send_message(chat_id=msg.from_user.id, text=txt)
        app_logger.msg_write(msg)
        app_logger.reply_for_message(msg, txt)

    bot.polling()
