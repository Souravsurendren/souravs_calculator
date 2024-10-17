from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        try:
            expression = request.form.get('expression')
            result = sp.sympify(expression)  # Safe evaluation using sympy
        except Exception:
            result = "Error"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
