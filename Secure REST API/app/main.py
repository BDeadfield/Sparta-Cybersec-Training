from flask import Flask, make_response, request, render_template, redirect, jsonify
from random import randrange
import jwt
import datetime
import calc_functions

SECRET_KEY = "53EB4E333DF73D56824F796D6EEBD"

flask_app = Flask(__name__)

def verify_token(token):
    if token:
        decoded_token = jwt.decode(token, SECRET_KEY, "HS256")
        print(decoded_token)

        # check whether informaiton in decoded token is correct or not
        return True # if information is correct, otherwise return false
    else:
        return False

@flask_app.route('/')
def index():
    print(request.cookies)

    if 'token' in request.cookies:
        isUserLoggedIn = verify_token(request.cookies['token'])

    if 'user_id' in request.cookies:
        return "Welcome back to the website"
    else:
        user_id = randrange(1,10)
        print(f"The user ID is: {user_id}")
        resp = make_response("This is the index page of a Secure REST API server.")
        resp.set_cookie('user_id', str(user_id))
        return resp

@flask_app.route('/help')
def help():
    return "This is the help page."

@flask_app.route('/login')
def login():
    return render_template('login.html')

@flask_app.route('/test')
def test():
    return render_template('test.html')

def create_token(username, password):
    validity = datetime.datetime.utcnow() + datetime.timedelta(days=15)
    token = jwt.encode({'user_id': 123154, 'username': 'user', 'expiry': str(validity)}, SECRET_KEY, "HS256")
    return token

@flask_app.route('/authenticate', methods = ['POST'])
def authenticate():
    data = request.form
    username = data['username']
    password = data['password']

    #check whether the username and password are correct
    user_token = create_token(username, password)

    resp = make_response("You have successfully logged in!")
    #resp.set_cookie("loggedIn", "True")
    resp.set_cookie('token', user_token)
    return resp

@flask_app.route('/calculator', methods = ['GET'])
def calculator_get():
    if 'token' in request.cookies:
        isUserLoggedIn = verify_token(request.cookies['token'])

    if 'user_id' in request.cookies:
        return render_template('calculator.html')
    else:
        resp = make_response(redirect('/login'))
        resp.set_cookie('user_id', str(user_id))

@flask_app.route('/calculate', methods = ['POST'])
def calculate_post():
    number_1 = request.form.get('number_1', type = int)
    number_2 = request.form.get('number_2', type = int)
    operation = request.form.get('operation')

    result = calc_functions.process(number_1, number_2, operation)

    return str(result)

@flask_app.route('/calculate2', methods = ['POST'])
def calculate_post2():
    number_1 = request.form.get('number_1', type = int)
    number_2 = request.form.get('number_2', type = int)
    operation = request.form.get('operation')

    result = calc_functions.process(number_1, number_2, operation)

    response_data = {
        'data': result
    }

    return make_response(jsonify(response_data))

if __name__ == '__main__':
    print("This is a Secure REST API Server:")
    flask_app.run(debug = True, ssl_context=('cert/cert.pem', 'cert/key.pem'))
