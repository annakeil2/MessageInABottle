from flask import Flask, render_template, request, redirect, url_for
import random
from datetime import datetime

app = Flask(__name__, template_folder='../html', static_url_path='', static_folder='../static')

messages = []

@app.route('/')
def index():
    return render_template('index.html', content='boo')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        content = request.form.get('message')

        if content:
            messages.append({
                "text": content,
                "time": datetime.now()
            })

        return redirect(url_for('receive'))

    return render_template('submit.html')


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


@app.route('/hello')
def hello():
    return render_template('index.html', content='test')


if __name__ == '__main__':
    app.run(debug=True)