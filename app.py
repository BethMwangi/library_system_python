from flask import Flask , render_template, request, redirect, url_for, session, flash

from functools import wraps
app = Flask (__name__)


#login required decorator

app.secret_key = "avocado"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash ('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    return render_template('index.html')


#@app.route('/')
#def home():
#    return "hello world"

@app.route('/welcome')
def welcome():
   return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form ['username'] != 'admin' or request.form ['password'] != 'admin':
            error = 'Invalid username/password. Please try again'
        else:
           return redirect(url_for('welcome'))
    return render_template('login.html', error = error)



if __name__ == '__main__':
	app.run(debug = True)

#
## The welcome page
#@app.route('/welcome')
#def welcome():
#    return render_template('welcome.html') #render a template
