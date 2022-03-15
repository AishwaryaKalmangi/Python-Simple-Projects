from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def index():
   if request.method == "POST":
      fname = request.form.get("fname")
      lname = request.form.get("lname")
      return "Welcome to web app " + fname + " " + lname
   return render_template("index.jinja2")

@app.route('/new/')
def new():
   return render_template("new.jinja2")

@app.route('/index/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
   return 'This is about page'

@app.route('/adds/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

@app.route('/chocs/<int:choc_id>')
def choc_user(choc_id):
   chocs = ['Lindt', 'Hersheys', 'Gems']
   try:
      return '{}'.format(chocs[choc_id])
   except IndexError:
      abort(404)

if __name__=='__main__':
   app.run(debug=True)