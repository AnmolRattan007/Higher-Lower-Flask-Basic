from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a Number between 0 to 9 </h1>" \
           "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:number>')
def number_guessed(number):
    random_number = random.randint(0, 9)
    print(random_number)
    if random_number > number:
        return "<h1 style = 'color:red'>Too low</h1>" \
               "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif random_number < number:
        return "<h1 style='color:blue'>Too high</h1>" \
               "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color:green'>Found ME!</h1>" \
               "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
