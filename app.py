from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Будь ласка, оберіть хоча б один тип символів."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_upper = bool(request.form.get('upper'))
        use_lower = bool(request.form.get('lower'))
        use_digits = bool(request.form.get('digits'))
        use_symbols = bool(request.form.get('symbols'))

        passwords = [generate_password(length, use_upper, use_lower, use_digits, use_symbols) for _ in range(20)]
        return render_template('index.html', passwords=passwords)

    return render_template('index.html', passwords=None)

if __name__ == '__main__':
    app.run(debug=True)

