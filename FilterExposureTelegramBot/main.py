import telebot
from telebot.types import Message

Token = "Your bot token"
bot = telebot.TeleBot(Token)

exposure_list = [
    'بیشعور',
    'دیگر ناسزاها'
]


class FilterExposure(telebot.custom_filters.AdvancedCustomFilter):
    key = 'exposures'

    @staticmethod
    def check(message, text):
        for i in str(message.text).split():
            if i in text:
                return True
        return False


@bot.message_handler(commands=['start'])
def start(message: Message):
    confirm_message = f"""
    hello mr/mrs {message.from_user.first_name}
    welcome to this but
    """
    bot.reply_to(message, confirm_message)


@bot.message_handler(exposures=exposure_list)
def say(message):
    bot.reply_to(message, 'ناسزا گویی ممنوع است در صورت مشاهده تکرار مجدد آن از شما، از ربات بن خواهید شد!')


bot.add_custom_filter(FilterExposure())
