

from flask import Flask, request, render_template

app = Flask(__name__) #dunder methods are a set of predefined methods you can use to enrich your classes

# @app.route('/potato') #declerator = if you visit our website at the base directory the function below will run

# def welcome():
#     return 'This is my first Flask app! YAY'


@app.route('/', methods=['GET', 'POST']) #home page

def root():
    name = ''
    food = ''
    if request.method == "POST" and 'username' in request.form:
        name = request.form.get('username')
        food = request.form.get('userfood')
    return render_template("index.html",
                            name=name,
                            food=food)


# @app.route('/bob') #different route

# def bobpage():
#     return 'This is my BOBBBBB Page'


# @app.route('/method',methods=['GET', 'POST', 'DELETE']) #creating a route that accepts get and post method
# def method():
#     if request.method == 'POST': #using the request from line 3. if the method is a post return
#         return "Youve used a POST request"
#     elif request.method == 'DELETE':
#         return "Youve used the delete method"
#     else:
#         return "I reckon youre probably using a GET request"




#when running server go to localhost:5000


app.run() #needed to make app run