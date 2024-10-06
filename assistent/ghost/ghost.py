from g4f.client import Client
import telebot


def query_to_llm(query):
    client = Client()
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}])
    llm_answer = response.choices[0].message.content
    return llm_answer


TOKEN = "8006374875:AAGBAg1mzpTj8XKMdjZB4TSsE2IGJ9pEWV8"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['llm'])
def handle_llm(message):
    try:
        message_text = message.text.split(maxsplit=1)[1]
        llm_answer = query_to_llm(query=message_text)
        bot.reply_to(message, llm_answer)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")


def run_bot():
    bot.polling()

