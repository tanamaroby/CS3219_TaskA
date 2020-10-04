from flask import Flask, render_template
import random

app = Flask(__name__)

firstwords = [
    "Hello", "Hi", "Wassup", "How is it going?", "Heyaa", "Nice to meet you", "Yoooo"
]

secondwords = [
    "My name is", "You can call me", "People usually call me", "I'm usually called", "I am"
]

thirdwords = [
    "Roby", "Robz", "Tanz", "Robz kebopz", "Robototo", "RobynTan", "Roooby"
]

@app.route('/')
def index():
    randomfirst = random.choice(firstwords)
    randomsecond = random.choice(secondwords)
    randomthird = random.choice(thirdwords)
    sentence = randomfirst +  " " + randomsecond + " " + randomthird + "."
    return render_template('index.html', word=sentence)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")