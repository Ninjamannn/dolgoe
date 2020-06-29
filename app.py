from flask import Flask, render_template, request

from database.models.users import User

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template("Hello.html")


@app.route('/game')
def game():
    user = {'nickname': 'Dolgoe 2020'}
    return render_template('game.html')


@app.route('/')
@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        exist_user = User.get_first(name=request.form['name'])
        if exist_user:
            return render_template('game.html')
        if not exist_user:
            new_user = User(name=request.form['name'])
            User.save(new_user)
            return render_template('game.html')
    else:
        return render_template("newUser.html")


def create_app():
    app.run()


if __name__ == '__main__':
    create_app()
