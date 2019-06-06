from flask import Flask
from flask_assistant import Assistant, ask, tell


app = Flask(__name__)
assist = Assistant(app, project_id='voicechat-rxcihi')

@assist.action('basecall')
def greet_and_start():
    speech = "i know how to use english"
    return ask(speech)


@assist.action("give-gender")
def ask_for_color(gender):
    if gender == 'male':
        gender_msg = 'Sup bro!'
    else:
        gender_msg = 'Haay gurl!'

    speech = gender_msg + ' What is your favorite color?'
    return ask(speech)







if __name__ == '__main__':
    app.run(debug=True)