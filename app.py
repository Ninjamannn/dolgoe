from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     user = {'nickname': 'Dolgoe 2020'}
#     return render_template('index.html', title='Home', user=user)

@app.route('/')
def game():
    user = {'nickname': 'Dolgoe 2020'}
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
