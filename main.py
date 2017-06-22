#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# June 2017
# Flask User Sign-up re: LaunchCode
# Rubric: http://education.launchcode.org/web-fundamentals/assignments/user-signup/


from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', 'GET'])
def sign_up():

    username = ''
    email = ''
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    title = 'Sign up'

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']

        if (username == '') or (len(username) < 3) or (len(username) > 20) or (' ' in username):
            username_error = "That's not a valid username"
            username = ''

        if (password == '') or (len(password) < 3) or (len(password) > 20) or (password.find(' ') != -1):
            password_error = "That's not a valid password"

        if (verify_password == '') or (verify_password != password):
            verify_password_error = "Password don't match"

        if (email != '') and (not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
            email_error = "Please include an @ and a . in your email. {email} is not valid.".format(email=email)
            email = ''

        if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
            return redirect('/welcome?username={}'.format(username))

    return render_template('signup.html', title=title, username=username, email=email, username_error=username_error,
                           password_error=password_error, verify_password_error=verify_password_error,
                           email_error=email_error)


@app.route('/welcome')
def valid_username():
    username = request.args.get('username')
    title = "Welcome!"
    return render_template('welcome.html', title=title, username=username)


if __name__ == '__main__':
    app.run()

