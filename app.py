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
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form['length'])
        use_upper = 'upper' in request.form
        use_lower = 'lower' in request.form
        use_digits = 'digits' in request.form
        use_symbols = 'symbols' in request.form

        passwords = [generate_password(length, use_upper, use_lower, use_digits, use_symbols) for _ in range(20)]
        return jsonify(passwords)  # Повертаємо JSON-відповідь
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
