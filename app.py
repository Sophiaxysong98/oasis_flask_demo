import os
from flask import Flask, render_template, request, jsonify
import openai
from openai.error import RateLimitError

app = Flask(__name__)
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt4', methods=['GET', 'POST'])
def gpt4():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    messages = [{"role": "user", "content": user_input}]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response.choices[0].message["content"]
    except RateLimitError:
        content = "The server is experiencing a high volume of requests. Please try again later."

    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True)
