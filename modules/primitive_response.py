import re
from random import choice, randint

from telegram.ext import CommandHandler, Filters, MessageHandler

from filters import reply_to_bot_filter
from utils import get_username_or_name


class PrimitiveResponse:
    def __init__(self, chat_id):
        self._chat_id = chat_id

    def add_handlers(self, add_handler):
        add_handler(MessageHandler(Filters.text, self.text_responses))
        add_handler(
            MessageHandler(Filters.text & reply_to_bot_filter,
                           self.reply_responses))
        add_handler(CommandHandler('me', self._me, pass_args=True))

    def text_responses(self, bot, update):
        def text_response(patterns, answer, chance=100):
            if any(re.search(pattern, text) for pattern in patterns):
                if answer.endswith('.txt'):
                    answer = self._choice_variant_from_file(answer)

                if randint(1, 100) <= chance:
                    bot.sendMessage(chat_id=chat_id, text=answer,
                                    reply_to_message_id=message_id,
                                    markdown_support=True)

        message = update.message
        chat_id = message.chat_id
        text = message.text.lower()
        message_id = message.message_id

        
        text_response([r'иди на ?хуй', r'на ?хуй пошел', r'на ?хуй иди',
                       r'пошел на ?хуй'], 'nahui.txt')
        
        text_response(['русня', 'русне' , 'русак', 'pycне', 'pycня'], 'rus.txt')
        
        text_response(['хохол', 'хохлы' , 'хохла', 'хохлов'], 'ukr.txt')
        
        text_response(['$pac', 'pac' , 'пак', 'паки'], 'pac.txt')
        
        text_response(['на Украiне', 'на Украине'], 'В Украине.')
        
        text_response(['есус', 'Иисус'], 'А наш Есус на самокате катается. И кот у него няшный.')
        
        text_response(['КАК ЖЕ ХОЧЕТСЯ'], 'Тянучку?.')
        
        text_response(['Тянучку'], 'Может с парнями попробуешь?.')
        
        text_response(['спать', 'посплю'], 'snov.txt')
        
        text_response(['бот пидор', 'бот идиот', 'бот мудак'], 'И?')

        text_response(['бот няша'], 'Спасибо, ты тоже <3')

        text_response(['утра', 'доброе утро', 'утречка'], 'utro.txt')

        text_response([r'\bнет$'], 'пидора ответ', 10)

    def reply_responses(self, bot, update):
        def reply_response(patterns, answer, chance=100):
            if any(re.search(pattern, text) for pattern in patterns):
                if answer.endswith('.txt'):
                    answer = self._choice_variant_from_file(answer)

                if randint(1, 100) <= chance:
                    bot.sendMessage(chat_id=chat_id, text=answer,
                                    reply_to_message_id=message_id,
                                    markdown_support=True)

        message = update.message
        chat_id = message.chat_id
        text = message.text.lower()
        message_id = message.message_id

        reply_response(['.*'], "Чё сказал?", 33)

    def _me(self, bot, update, args):
        message = update.message

        text = "{0} {1}".format(get_username_or_name(message.from_user), ' '.join(args))
        bot.sendMessage(chat_id=self._chat_id, text=text)

    @staticmethod
    def _choice_variant_from_file(file_name):
        with open('modules/responses/%s' % file_name) as file:
            variant = choice(file.read().splitlines())
        return variant
