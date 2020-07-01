from flask import Flask, render_template, request
from flask_jsglue import JSGlue

from database.models.users import User


app = Flask(__name__)
jsglue = JSGlue(app)


@app.route('/', methods=['GET'])
def hello():
    return render_template("Hello.html")


@app.route('/')
@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        exist_user = User.get_first(name=request.form['name'])
        if exist_user:
            return render_template('game.html', user=request.form['name'], secret_by_user=exist_user.secret)

        if not exist_user:
            new_user_ = User(name=request.form['name'])
            User.save(new_user_)
            return render_template('game.html', user=request.form['name'], secret_by_user=new_user_.secret)

    else:
        return render_template("newUser.html")


# @app.route('/game')
# def game():
#     user = {'nickname': 'Dolgoe 2020'}
#     return render_template('game.html')
#
#
# @app.route('/secret', methods=['POST', 'GET'])
# def secret():
#     print(request.args.get('user'))
#     print(request.host)
#     return render_template('show_secret.html', secret='secret!')


def create_app():
    app.run()


if __name__ == '__main__':
    create_app()
