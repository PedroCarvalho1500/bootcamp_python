# Advanced Python Decorator Functions

def name_function_printed(function):
    def wrapper(*args, **kwargs):
        print(f"FUNCTION NAME IS: {function.__name__}")
        function(args[0])
    return wrapper



@name_function_printed
def create_blog_post(user):
    print(f"This is {user}'s new blog post.")



if __name__ == "__main__":
    user = "Angela"
    create_blog_post(user)