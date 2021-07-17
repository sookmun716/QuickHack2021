from flask import Flask, redirect, url_for, render_template, request, session
import requests
import json

app = Flask(__name__)
BASE_URL = "http://localhost:4000/"
app.secret_key = '12312fdfjkqnewfuajndf'

@app.route("/", methods=['GET', 'POST'])
def home():

    # hardcode user login info
    session['username'] = 'qiyuna'
    session['id'] = '60f283e7798ceb3b49b97c0c'
    session['password'] = 'password'


    return render_template("main_page.html")


@app.route("/instruction", methods=['GET', 'POST'])
def instruction():
    return render_template("instruction.html")


@app.route("/diary", methods=['GET', 'POST'])
def diary():
    return render_template("diary_display.html")


@app.route("/upload", methods=['POST'])
def upload():

    isPublic = False
    if request.form['submitBtn'] == 'Private':
        isPublic = False
    else:
        isPublic = True

    data = {
        'title':  request.form['title'],
        'content': request.form['text'],
        'owner': session['id'],
        'isPublic': isPublic,
        'dateCreated': request.form['date'].replace('-', '')
    }
    headers = {u'content-type': u'application/json'}

    response = requests.post(BASE_URL + 'diary/newDiary', data=json.dumps(data), headers=headers)

    if response.status_code == '200':
        return True
    else: 
        return response.json()


@app.route("/diary_entry", methods=['GET', 'POST'])
def diary_entry():
    return render_template("diary_entry.html")


if __name__ == "__main__":
    app.run(debug=True)
