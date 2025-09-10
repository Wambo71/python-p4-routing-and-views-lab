from flask import Flask

app = Flask(__name__)

# 1. Index route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# 2. Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # prints in console
    return parameter  # displays in browser

# 3. Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "\n".join(str(i) for i in range(parameter ))
    return numbers +"\n"

# 4. Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        result = "Invalid operation"
    return str(result)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
