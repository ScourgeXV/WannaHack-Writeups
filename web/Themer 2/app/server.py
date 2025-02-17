from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route('/')
def index():
    safe_theme = request.args.get("theme", "themes/theme1.css")
    if safe_theme[0] == "/":
        safe_theme = safe_theme[1:-1]
    safe_theme = safe_theme.replace("../", "")
    f = open(safe_theme, "r")
    theme = f.read()
    f.close()
    return render_template('index.html', css=theme)

@app.route('/', methods=['POST'])
def calculate_binary():
    safe_theme = request.args.get("theme", "themes/theme1.css")
    if safe_theme[0] == "/":
        safe_theme = safe_theme[1:-1]
    safe_theme = safe_theme.replace("../", "")
    f = open(safe_theme, "r")
    theme = f.read()
    f.close()
    try:
        num = int(request.form['number'])
        result = format(num, '08b')
        return render_template('index.html', result=result, css=theme)
    except ValueError:
        error = "Invalid input"
        return render_template('index.html', error=error, css=theme)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=21338)
