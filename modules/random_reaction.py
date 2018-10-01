from random import randint


def random_reaction(bot, update):
    message_id = update.message.message_id
    chat_id = update.message.chat_id
    if randint(1, 200) == 1:
        bot.sendMessage(chat_id=chat_id, reply_to_message_id=message_id,
                        text='Ты пидор.')
    if randint(1, 400) == 1:
        bot.sendMessage(chat_id=chat_id, reply_to_message_id=message_id,
                        text='Ты няша 😘')
    if randint(1, 200) == 1:
        bot.sendMessage(chat_id=chat_id, reply_to_message_id=message_id,
                        text='Верните ДИМУ!!!')
     if randint(1, 300) == 1:
        bot.sendMessage(chat_id=chat_id, reply_to_message_id=message_id,
                        text='ПАК ПО ДОЛЛАРУ!')
