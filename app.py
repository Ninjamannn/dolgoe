from flask import Flask, render_template

from database.models.users import User

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     user = {'nickname': 'Dolgoe 2020'}
#     return render_template('index.html', title='Home', user=user)

@app.route('/')
def game():
    user = {'nickname': 'Dolgoe 2020'}
    return render_template('index.html')


@app.route('/')
@app.route('/users')
def get_users():
    books = User.get_all()
    print(books)
    # return render_template("books.html", books=books)


def create_app():
    app.run()


if __name__ == '__main__':
    create_app()
