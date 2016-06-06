from flask import Flask , render_template, request

app = Flask (__name__)



@app.route('/')
def home():
    return "hello world"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
           if valid_login(request.form ['username'],
                          request.form ['password']):
              return log_the_user_in(request.form['username'])

           else:
            error = 'Invalid username/password'
    return render_template('login.html', error = error)

if __name__ == '__main__':
	app.run(debug = True)

