from flask import Flask, render_template, request, jsonify

app = Flask(_name_)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    msg = request.form['message']
    messages.append(msg)
    return jsonify({'messages': messages})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
