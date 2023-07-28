import functools
from flask import Flask
import flask
import random


#decorator to make the text bold
def make_bold(function):
    def wrapper(*args, **kwargs):
        #print(args)
        #print(args[0])
        #print(function())
        #print(function)
        #print(function())
        #turn_bold = "<b>"+function()+"</b>"
        #print('Vou pegar a cotação')
        #print(function())
        return "<b>"+function()+"</b>"
    
    return wrapper



def make_bold_with_args(function):
    def wrapper33(*args, **kwargs):
        print("KWARGS HERE"+str(kwargs))
        return "<b>"+function(kwargs.get("name"),kwargs.get("number"))+"</b>"
    
    return wrapper33


app = Flask(__name__)


@app.route('/')
def guess_number():
    return '<h1> Guess a number between 0 and 9 </h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"> </img>'

@app.route('/URL/<int:number>')
def url_number(number):
    if number < number_random_generated: return '<h1 style="color:blue;"> Number is too low </h1>'
    elif number > number_random_generated: return '<h1 style="color:red;"> Number is too high </h1>'
    else: return '<h1 style="color:green"> Correct Number! </h1>'


# @app.route('/username/<name>/<int:number>')
# @make_bold_with_args
# def greet(name,number):
#     #return 'Hello %s" You are %d years old.' %name %number 
#     return f"Hello {name}! You are {number} years old."


if __name__ == "__main__":
    number_random_generated = random.randint(0,9)
    #print(number_random_generated)
    app.run(debug=True)