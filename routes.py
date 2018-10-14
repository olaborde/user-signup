from flask import Flask, render_template, request,flash, redirect, url_for
from forms import signupForm

app = Flask(__name__)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
  error = None
  # password = request.form.get['password']
  # vpassword = request.form.get['vpassword']
 
  form = signupForm() 
  
  if request.method == 'POST':
      if form.validate == False:
        return render_template("user-signup.html", form=form)
      else:
            if request.form['password'] != request.form['vpassword']:
                  # error = 'Password must match'
                  flash('Password must match!')
                  return redirect(url_for('signup'))
            else:    
              return 'Welcome, ' + request.form['user_name']    
  elif request.method == 'GET':   
    return render_template("user-signup.html", form=form, error=error)


if __name__ == "__main__":
  app.run(debug=True)
