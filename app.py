from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get('http://universities.hipolabs.com/search').json()


@app.route('/')
def main():
    return render_template('index.html', info=response)


@app.route('/search')
def search():
    return render_template('details.html', info=response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
