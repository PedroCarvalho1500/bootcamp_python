# Advanced Python Decorator Functions

def is_authenticate_decorator(function):
    def wrapper(*args):
        #print(args)
        #print(args[0].name)
        if args[0].is_logged_in == False:
            print(f"USER {args[0].name} IS NOT LOGGED IN!")
        
        else: function(args[0])
    
    return wrapper



class User:
    def __init__(self,name) -> None:
        self.name = name
        self.is_logged_in = False

    def log_in_with_user(self):
        self.is_logged_in = True


@is_authenticate_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")



if __name__ == "__main__":
    new_user = User("Angela")
    new_user.log_in_with_user()
    create_blog_post(new_user)