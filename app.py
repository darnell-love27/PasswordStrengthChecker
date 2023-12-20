from flask import Flask,request,render_template,jsonify
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

special = "!@#$%^&*()"

def check_length(password):
    #Checks length of the password.
    if len(password) >= 11:
        return len(password)
    return "Password Length Is Too Short"

def has_uppercase(password):
    #Check if there is an uppercase
    for char in password:
        if char.isupper():
            return True
    return "Need an Uppercase Letter"

def has_lowercase(password):
    #Check if there is an uppercase
    for char in password:
        if char.islower():
            return True
    return "Need a Lowercase Letter"

def has_special_character(password):
    #Check if there are any special characters
    for char in password:
        if char in special:
            return True
    return "Need At Least One Special Character"

def evaluate_strength(password):
    """
    Evaluate strength of password
    """
    strength = 0

    if check_length(password):
        strength += 1
    if has_uppercase(password):
        strength += 1
    if has_lowercase(password):
        strength += 1
    if has_special_character(password):
        strength += 1

    if strength < 4:
        return jsonify({'status': 'Success'})
    else:
        return jsonify({'status': 'Login attempt unsuccessful'})

@app.route('/evaluate_passowrd', methods=['POST'])
def evaluate_password():
    data = request.get_json()
    password = data.get('password')

    # Performs a passowrd strength evaluation
    strength = evaluate_strength(password)
    return jsonify({'strength': strength})


"""
Project Name: Password Strength Checker
Owner: Darnell Love
Description: This project will have a user interface that takes the user's
password and username, checks to see if the password fulfills the requirements,
then outputs "Success" if the user can log in and "Retry" otherwise.
"""




#Github Token
#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
