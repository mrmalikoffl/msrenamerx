#Thank you Mr Malik for helping me in this journey !
#Must Subscribe On YouTube @voiceofmalikoffl 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@MrMalik'


if __name__ == "__main__":
    app.run()
