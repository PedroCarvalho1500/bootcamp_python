import functools
from flask import Flask
import flask


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



#decorator to make the text bold
def make_emphasis(function):
    def wrapper1(*args,**kwargs):
        #print(function())
        #print(function)
        #print(function())
        #turn_bold = "<b>"+function()+"</b>"
        #print('Vou pegar a cotação')
        #print(function())
        return "<em>"+function(args[0], args[1])+"</em>"
    
    return wrapper1



#decorator to make the text bold
def make_underlined(function):
    def wrapper2(*args, **kwargs):
        #print(function())
        #print(function)
        #print(function())
        #turn_bold = "<b>"+function()+"</b>"
        #print('Vou pegar a cotação')
        #print(function())
        return "<ul>"+function(args)+"</ul>"
    
    return wrapper2


def decorator_to_print_attributes(function):
    def wrapper3(*args, **kwargs):
        print(args)
        print(kwargs)
        #for i in args:
        #    print(f"ARG: {i}\n")
        #print(f"NAME: {name}")
        #print(f"NUMBER: {number}")
        #print(function)
        #print(function())
        #turn_bold = "<b>"+function()+"</b>"
        #print('Vou pegar a cotação')
        #print(function())
        #return ""
        return function(args,kwargs)

    return wrapper3



def make_bold_with_args(function):
    def wrapper33(*args, **kwargs):
        #print("ARGS HERE"+str(args))
        print("KWARGS HERE"+str(kwargs))
        #print(args[0])
        #print(function())
        #print(function)
        #print(function())
        #turn_bold = "<b>"+function()+"</b>"
        #print('Vou pegar a cotação')
        #print(function())
        return "<b>"+function(kwargs.get("name"),kwargs.get("number"))+"</b>"
    
    return wrapper33


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World </h1>' \
    '<p> This is a paragraph. </p>' \
    '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmEzM2YxOTk4MzYwZDYzY2Q3MTEyOTEyODIyMzVlOWUyNWQyZjg0ZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/A3haYYuP6nu3AEppVk/giphy.gif">'


@app.route("/bye")
@make_bold
#@make_emphasis
#@make_underlined
def say_bye():
    return "Bye"





#@make_emphasis
@app.route('/username/<name>/<int:number>')
#@decorator_to_print_attributes
#@make_emphasis
@make_bold_with_args
def greet(name,number):
    #return 'Hello %s" You are %d years old.' %name %number 
    return f"Hello {name}! You are {number} years old."

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


if __name__ == "__main__":
    app.run(debug=True)