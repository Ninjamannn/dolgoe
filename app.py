from flask import Flask, render_template, request

from database.models.users import User


app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/dolgoe/', methods=['GET'])
def hello():
    return render_template("Hello.html")


@app.route('/dolgoe/user/new', methods=['GET', 'POST'])
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


@app.route('/dolgoe/point/save', methods=['GET', 'POST'])
def save_points():
    user = User.get(request.values.get('user'))
    user.point += int(request.values.get('points'))
    User.save(user)
    return 'ok'


@app.route('/dolgoe/point/all')
def show_user_points():
    users = User.get_all(ordering=User.point.desc())
    print(users)
    return render_template('users_points.html', users=users)


@app.route('/dolgoe/user')
@app.route('/dolgoe/point')
def wrong_way():
    return 'Я, бл***, в своём познании настолько преисполнился, что я как будто бы уже 100 триллионов миллиардов лет,' \
           ' бл***, проживаю на триллионах и триллионах таких же планет, понимаешь? Как эта Земля. Мне уже этот мир' \
           ' абсолютно понятен, и я здесь ищу только одного: покоя, умиротворения и вот этой гармонии от слияния' \
           ' с бесконечно вечным.'


def create_app():
    app.run()


if __name__ == '__main__':
    create_app()
