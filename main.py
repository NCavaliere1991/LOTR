from flask import Flask, render_template, request
from RequestLord import RequestLord

app = Flask(__name__)


lord = RequestLord()


@app.route('/')
def home():
    lord.get_characters()
    return render_template("index.html", characters=lord.characters)


@app.route('/quotes')
def quotes():
    id = request.args.get('id')
    name = request.args.get('name')
    lord.get_quotes(id)
    return render_template("quotes.html", quotes=lord.quote_list, name=name)


if __name__ == "__main__":
    app.run(debug=True)
