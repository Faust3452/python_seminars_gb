from telebot import TeleBot, types
msg_demo = {'content_type': 'text',
            'id': 4,
            'message_id': 4,
            'from_user': {'id': 376018529, 'is_bot': False, 'first_name': 'Alexandr',
                          'username': 'Faust7296', 'last_name': 'Pel', 'language_code': 'ru',
                          'can_join_groups': None, 'can_read_all_group_messages': None,
                          'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None},
            'date': 1671826401,
            'chat': {'id': 376018529, 'type': 'private', 'title': None,
                     'username': 'Faust7296', 'first_name': 'Alexandr',
                     'last_name': 'Pel', 'is_forum': None, 'photo': None, 'bio': None,
                     'join_to_send_messages': None, 'join_by_request': None,
                     'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None,
                     'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None,
                     'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None,
                     'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None,
                     'active_usernames': None, 'emoji_status_custom_emoji_id': None},
            'sender_chat': None,
            'forward_from': None,
            'forward_from_chat': None,
            'forward_from_message_id': None,
            'forward_signature': None,
            'forward_sender_name': None,
            'forward_date': None, 'is_automatic_forward': None,
            'reply_to_message': None, 'via_bot': None, 'edit_date': None,
            'has_protected_content': None,
            'media_group_id': None,
            'author_signature': None,
            'text': 'bello',
            'entities': None,
            'caption_entities': None,
            'audio': None,
            'document': None,
            'photo': None,
            'sticker': None,
            'video': None,
            'video_note': None,
            'voice': None,
            'caption': None,
            'contact': None,
            'location': None,
            'venue': None,
            'animation': None,
            'dice': None,
            'new_chat_member': None,
            'new_chat_members': None,
            'left_chat_member': None,
            'new_chat_title': None,
            'new_chat_photo': None,
            'delete_chat_photo': None,
            'group_chat_created': None,
            'supergroup_chat_created': None,
            'channel_chat_created': None,
            'migrate_to_chat_id': None,
            'migrate_from_chat_id': None,
            'pinned_message': None,
            'invoice': None,
            'successful_payment': None,
            'connected_website': None,
            'reply_markup': None,
            'message_thread_id': None,
            'is_topic_message': None,
            'forum_topic_created': None,
            'forum_topic_closed': None,
            'forum_topic_reopened': None,
            'json': {'message_id': 4,
                     'from': {'id': 376018529, 'is_bot': False,
                              'first_name': 'Alexandr', 'last_name': 'Pel',
                              'username': 'Faust7296', 'language_code': 'ru'},
                     'chat': {'id': 376018529, 'first_name': 'Alexandr',
                              'last_name': 'Pel', 'username': 'Faust7296',
                              'type': 'private'},
                     'date': 1671826401, 'text': 'bello'}}

msg_doc = {'content_type': 'document',
           'id': 42, 'message_id': 42,
           'from_user': {'id': 376018529, 'is_bot': False, 'first_name': 'Alexandr',
                         'username': 'Faust7296', 'last_name': 'Pel', 'language_code': 'ru',
                         'can_join_groups': None, 'can_read_all_group_messages': None,
                         'supports_inline_queries': None, 'is_premium': None,
                         'added_to_attachment_menu': None},
           'date': 1671912768,
           'chat': {'id': 376018529, 'type': 'private', 'title': None, 'username': 'Faust7296',
                    'first_name': 'Alexandr', 'last_name': 'Pel',
                    'is_forum': None, 'photo': None, 'bio': None, 'join_to_send_messages': None,
                    'join_by_request': None, 'has_private_forwards': None,
                    'has_restricted_voice_and_video_messages': None, 'description': None,
                    'invite_link': None, 'pinned_message': None, 'permissions': None,
                    'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None,
                    'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None,
                    'active_usernames': None, 'emoji_status_custom_emoji_id': None},
           'sender_chat': None,
           'forward_from': None,
           'forward_from_chat': None,
           'forward_from_message_id': None,
           'forward_signature': None,
           'forward_sender_name': None,
           'forward_date': None,
           'is_automatic_forward': None,
           'reply_to_message': None,
           'via_bot': None,
           'edit_date': None,
           'has_protected_content': None,
           'media_group_id': None,
           'author_signature': None,
           'text': None,
           'entities': None,
           'caption_entities': None,
           'audio': None,
           'document': {'file_id': 'BQACAgIAAxkBAAMqY6ddQKbf3r_bIXJg1ay0QMLDDBsAAuMeAAKW6kBJKuokv9Rsq3EsBA',
                        'file_unique_id': 'AgAD4x4AApbqQEk', 'thumb': None,
                        'file_name': 'data.json',
                        'mime_type': 'application/json',
                        'file_size': 627},
           'photo': None,
           'sticker': None,
           'video': None,
           'video_note': None,
           'voice': None,
           'caption': None,
           'contact': None,
           'location': None,
           'venue': None,
           'animation': None,
           'dice': None,
           'new_chat_member': None,
           'new_chat_members': None,
           'left_chat_member': None,
           'new_chat_title': None,
           'new_chat_photo': None,
           'delete_chat_photo': None,
           'group_chat_created': None,
           'supergroup_chat_created': None,
           'channel_chat_created': None,
           'migrate_to_chat_id': None,
           'migrate_from_chat_id': None,
           'pinned_message': None,
           'invoice': None,
           'successful_payment': None,
           'connected_website': None,
           'reply_markup': None,
           'message_thread_id': None,
           'is_topic_message': None,
           'forum_topic_created': None,
           'forum_topic_closed': None,
           'forum_topic_reopened': None,
           'json': {'message_id': 42,
                    'from': {'id': 376018529,
                             'is_bot': False, 'first_name': 'Alexandr',
                             'last_name': 'Pel', 'username': 'Faust7296',
                             'language_code': 'ru'},
                    'chat': {'id': 376018529,
                             'first_name': 'Alexandr',
                             'last_name': 'Pel',
                             'username': 'Faust7296',
                             'type': 'private'},
                    'date': 1671912768,
                    'document': {'file_name': 'data.json',
                                 'mime_type': 'application/json',
                                 'file_id': 'BQACAgIAAxkBAAMqY6ddQKbf3r_bIXJg1ay0QMLDDBsAAuMeAAKW6kBJKuokv9Rsq3EsBA',
                                 'file_unique_id': 'AgAD4x4AApbqQEk', 'file_size': 627}}
           }

TOKEN = '5884155558:AAH-Tykh-J09sp_xHuUkNV2w1tw2lgO3Q1A'

bot = TeleBot(TOKEN)

@bot.message_handler(content_types=['log'])
def answer(msg: types.Message):
    pass

@bot.message_handler(commands=['log'])
def answer(msg: types.Message):
    # bot.send_message(chat_id=msg.from_user.id, text='ЛООООООООООг')
    with open('test.txt', 'rb') as f:
        bot.send_document(chat_id=msg.from_user.id, document=types.InputFile(f))


@bot.message_handler(content_types=['document'])
def answer(msg: types.Message):
    print('DOC received')
    try:
        file = bot.get_file(file_id=msg.document.file_id)
        print(f'file is {file}')
        wr = bot.download_file(file.file_path)
        print(f'wr is {wr}')
        with open(msg.document.file_name, mode='wb') as f:
            f.write(wr)
    except Exception as e:
        bot.send_message(chat_id=msg.from_user.id, text=e)

    print('done')

@bot.message_handler()
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='ЧТООООООООООООООООо')

# @bot.message_handler()
# def answer(msg: types.Message):
#         bot.register_next_step_handler(msg, answer1) # это ответ на следующее сообщение для бота
#         bot.register_next_step_handler(msg, answer2)
#     # bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: '+msg.text)
#
#
# def answer1(msg):
#     bot.send_message(chat_id=msg.from_user.id, text='Вы ввели четное число')
#
# def answer2(msg):
#     bot.send_message(chat_id=msg.from_user.id, text='Вы ввели нечетное число')

bot.polling()