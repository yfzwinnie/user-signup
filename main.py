from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verifypassword_error = ''
    email_error = ''

    if username == '' or len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = "That's not a valid username"
        username = ''
    if password == '' or len(password) < 3 or len(password) > 20 or password.find(' ') != -1:
        password_error = "That's not a valid password"
    if verifypassword == '' or verifypassword != password:
        verifypassword_error = "Password don't match"
    if email != '':
        if len(email) < 3 or len(email) > 20 or "@." not in email or " " in email:
            email_error = "Please include an @ and a . in your email. {email} is not valid.".format(email=email)
    if not username_error and not password_error and not verifypassword_error and not email_error:
        return redirect('/welcome?username={}'.format(username))
    else:
        return render_template('signup.html',
            username_error = username_error,
            password_error = password_error,
            verifypassword_error = verifypassword_error,
            email_error = email_error,
            username = username,
            password = password,
            verifypassword = verifypassword,
            email = email)

@app.route('/welcome')
def valid_username():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

app.run()
