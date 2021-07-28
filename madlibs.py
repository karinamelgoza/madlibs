"""A madlib game that compliments its users."""

from logging import debug
import random

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

colors = ['blue', 'red', 'periwinkle', 'salmon', 'yellow', 'magenta']


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template("hello.html")


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = random.sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    player_choice = request.args.get('yesorno')
    choices = random.sample(AWESOMENESS, 6)
    if player_choice == 'no':
        return render_template('goodbye.html')
    return render_template('game.html', choices=choices, colors=colors)


@app.route('/madlib', methods=['GET', 'POST'])
def show_madlib():
    if request.method == 'POST':
        person = request.form['person']
        color = request.form['color']
        noun = request.form['noun']
        adjective = request.form['adjective']

        return render_template('madlib.html', person=person, color=color, noun=noun, adjective=adjective)

    return render_template('game.html')


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
