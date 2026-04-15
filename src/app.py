from flask import Flask, render_template, request, redirect, url_for
import random, json, time
from datetime import datetime

app = Flask(__name__, template_folder='../html', static_url_path='', static_folder='../static')

messages = [
    # { 'message': 'test message'}
]

def save_to_file(messages):
    with open("data/messagebank.json", "w") as f:
        f.write(json.dumps(messages))
        

def load_from_file():
    with open("data/messagebank.json", "r") as f:
        json_string = f.read()
        return json.loads(json_string)


messages = load_from_file()
print('messages', messages)


@app.route('/')
def index():
    return render_template('index.html', content='boo')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('submit.html')


@app.route('/add', methods=['POST'])
def add():
    content = request.form.get('message')

    if content:
        messages.append({
            "message": content,
            "created_at": int(time.time())
        })
        save_to_file(messages)

    return redirect(url_for('receive'))

@app.route('/receive')
def receive():
    if messages:
        message = random.choice(messages)
    else:
        message = {"text": "No messages yet. Be the first to send one!"}

    return render_template('receive.html', message=message)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(debug=True)