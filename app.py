from flask import Flask, render_template, request
from flask_jsglue import JSGlue
from werkzeug.wrappers import response

from database.models.users import User


app = Flask(__name__)
jsglue = JSGlue(app)


@app.route('/', methods=['GET'])
def hello():
    return render_template("Hello.html")


# @app.route('/')
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


@app.route('/point/save', methods=['GET', 'POST'])
def save_points():
    user = User.get(request.args.get('user'))
    user.point += int(request.args.get('points'))
    User.save(user)
    return 'ok'


@app.route('/point/all')
def show_user_points():
    users = User.get_all()
    print(users)
    return render_template("users_points.html", users=users)


def create_app():
    app.run()


# if __name__ == '__main__':
#     create_app()
