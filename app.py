from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/static/images/logo.png')
# def logo():
#     return render_template('logo.png')

    if __name__ == "__main__":
        app.run(debug=True)
