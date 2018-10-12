from flask import Flask, render_template, request
from forms import signupForm

app = Flask(__name__)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
 
  form = signupForm() 
  
  if request.method == 'POST':
      if form.validate == False:
        return render_template("user-signup.html", form=form)
      else:
                
        return 'Welcome, ' + request.form['user_name']    
  elif request.method == 'GET':   
    return render_template("user-signup.html", form=form)


if __name__ == "__main__":
  app.run(debug=True)
