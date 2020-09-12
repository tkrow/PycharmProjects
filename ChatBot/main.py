from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Assistant')  # create the bot
trainer = ChatterBotCorpusTrainer(bot)  # Teacher
# bot.train(conv) # teacher train the bot

trainer.train('base')

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']

    bot_response = bot.get_response(user_input)
    bot_response = str(bot_response)
    print("Assistant: " + bot_response)
    return render_template('index.html', user_input=user_input, bot_response=bot_response)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
