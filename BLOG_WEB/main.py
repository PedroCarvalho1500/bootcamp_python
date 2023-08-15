from datetime import date
import datetime
import sqlite3
from flask import Flask, abort, render_template, redirect, request, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user, admin_only
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import werkzeug
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CommentForm, LoginForm, NewPostForm, RegisterForm
import urllib, hashlib


#email = "someone@somewhere.com"
#default = "https://www.example.com/default.jpg"
#size = 40

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)

# TODO: Configure Flask-Login
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)



@login_manager.user_loader
def load_user(user_id):
   db_obj.connect_db()
   lu = db_obj.get_or_404(user_id)
   print("LU -> "+str(lu))
   if lu is None:
      return None
   else:
      return User(int(lu[0]), lu[1], lu[2], lu[3])



class User(UserMixin):
    def __init__(self, id, email, password,name):
         self.id = id
         self.email = email
         self.password = password
         self.name = name
         #self.posts = []
         self.authenticated = False
    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
         return self.id




class DB_Actions():
    def __init__(self,title=""):
        self.title = title

    def connect_db(self):
        self.conn = sqlite3.connect("instance/posts.db")
        self.cursor = self.conn.cursor()

            
    def disconnect_db(self):
        print("DATABASE DISCONNECTED!!!")
        self.conn.close()

    def mountTables(self):
        self.connect_db()
        print("Conectando ao Banco de Dados!")
            
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS blog_posts (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(2000) UNIQUE NOT NULL,
                date VARCHAR(50) NOT NULL,
                body TEXT NOT NULL,
                author VARCHAR(100) NOT NULL,
                img_url VARCHAR(2000),
                subtitle VARCHAR(500) NOT NULL,
                author_id INT,
                FOREIGN KEY (author_id) REFERENCES user(id)
                )""")
                
        self.conn.commit()

        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS user (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(2000) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                name VARCHAR(1000) NOT NULL
                )""")
                
        self.conn.commit()

        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS comments (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                body_comment TEXT NOT NULL,
                author_id INT,
                author_name VARCHAR(100),
                blog_id INT,
                FOREIGN KEY (author_id) REFERENCES user(id),
                FOREIGN KEY (blog_id) REFERENCES blog_posts(id)
                )""")
                
        self.conn.commit()


        print("DATABASE CREATED!!!")
        self.disconnect_db()


    def get_all_posts(self):
        self.connect_db()

        all_posts = self.cursor.execute(""" SELECT * FROM blog_posts """).fetchall()
        self.conn.commit()

        #input(all_posts)
        self.disconnect_db()

        return all_posts

    def get_all_comments(self,id_blog):
        self.connect_db()

        all_comments_from_blog_post = self.cursor.execute(""" SELECT * FROM comments WHERE blog_id=?""", [id_blog]).fetchall()
        self.conn.commit()

        #input(all_comments_from_blog_post)
        self.disconnect_db()

        return all_comments_from_blog_post



    
    def get_post_by_id(self,id):
        self.connect_db()

        post_by_id = self.cursor.execute(""" SELECT * FROM blog_posts WHERE id=?""", [id]).fetchall()
        self.conn.commit()
        #input(all_post_by_location)

        self.disconnect_db()

        return post_by_id

    def get_author_from_author_id(self,author_id):
        self.connect_db()

        user_author = self.cursor.execute(""" SELECT * FROM user WHERE id=?""", [author_id]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        #input("USER AUTHOR "+str(user_author[0]))

        return user_author[0]  

    def get_author_name_from_author_id(self,author_id):
        self.connect_db()

        user_author = self.cursor.execute(""" SELECT name FROM user WHERE id=?""", [author_id]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        #input("USER AUTHOR "+str(user_author[0][0]))

        return user_author[0][0]


    def insert_new_post(self,title,date,body,img_url,subtitle):
        author_id = current_user.id
        author_name = self.get_author_from_author_id(author_id)[3]
        self.connect_db()
        self.cursor.execute(""" INSERT INTO blog_posts (title,date,body,author,img_url,subtitle,author_id) VALUES(?,?,?,?,?,?,?)""", (title,date,body,author_name,img_url,subtitle,author_id))
        self.conn.commit()

        self.disconnect_db()

    def insert_new_comment(self,body_comment,blog_id):
        author_id = current_user.id
        author_name = self.get_author_from_author_id(author_id)[3]
        self.connect_db()
        self.cursor.execute(""" INSERT INTO comments (body_comment,author_id,author_name,blog_id) VALUES(?,?,?,?)""", (body_comment,author_id,author_name,blog_id))
        self.conn.commit()

        self.disconnect_db()



    def update_post(self,title,body,author,img_url,subtitle,id):
        self.connect_db()

        self.cursor.execute(""" UPDATE blog_posts SET title=?, body=?, author=?, img_url=?, subtitle=? WHERE id=?""", (title,body,author,img_url,subtitle,id))
        self.conn.commit()
        print("UPDATED...")
        self.disconnect_db()

    # def update_price(self,id,new_price):
    #     self.connect_db()

    #     self.cursor.execute(""" UPDATE cafe SET coffee_price=? WHERE id=?""", (new_price,id))
    #     self.conn.commit()

    #     self.disconnect_db()

    def delete_post_by_id(self,id):
        self.connect_db()

        self.cursor.execute(""" DELETE FROM blog_posts WHERE id=?""", [id])
        self.conn.commit()

        self.disconnect_db()

    def insert_new_register(self, name, email, password):
        self.connect_db()
        print("ENTERED HERE...")
        self.cursor.execute(""" INSERT INTO user (email, password, name) VALUES(?,?,?)""", [email, password, name])
        self.conn.commit()

        self.disconnect_db()

    def get_user_name_by_email(self,email):
        self.connect_db()

        name_searched = self.cursor.execute(""" SELECT name FROM user WHERE email=?""", [email]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        return name_searched[0]

    def get_user_id_by_email(self,email):
        self.connect_db()

        id = self.cursor.execute(""" SELECT id FROM user WHERE email=?""", [email]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        return id[0]


    def get_or_404(self,id):

        try:
            self.connect_db()

            user = self.cursor.execute(""" SELECT * FROM user WHERE id=(?)""", [id]).fetchall()
            self.conn.commit()

            #input("USER -> "+str(user))

            self.disconnect_db()

            return user[0]
        
        except:
            return None


    def get_hash_user_by_email(self,email):
        self.connect_db()

        user_hash = self.cursor.execute(""" SELECT password FROM user WHERE email=?""", [email]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        return user_hash[0]

      
    def get_user_name_by_id(self,id):
        self.connect_db()

        user_name = self.cursor.execute(""" SELECT name FROM user WHERE id=?""", [id]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        return user_name[0]



db_obj = DB_Actions()




# TODO: Create a User table for all your registered users. 




# with app.app_context():
#     db.create_all()


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["POST","GET"])
def register():
    register_form = RegisterForm()
    login_form = LoginForm()
    if(register_form.validate_on_submit()):
        name = register_form.name.data
        email = register_form.email.data
        print("HERE")

        try:
            print("TRY")
            email_already_exists = db_obj.get_user_id_by_email(email)
            flash("You've already signed up with that email, log in instead!")
            #input("HERE...")
            return redirect('/login')

        except:
            print("EXCEPT")
            password = werkzeug.security.generate_password_hash(register_form.password.data, method='sha256', salt_length=8)
            db_obj.insert_new_register(name,email,password)
            new_user = User(db_obj.get_user_id_by_email(email)[0],email,password,name)
            logout_user()
            Us = load_user(db_obj.get_user_id_by_email(email)[0])
            login_user(Us)

            return redirect('/')
    return render_template("register.html",form=register_form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login/', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    error = None


    email = login_form.email.data
    if(login_form.validate_on_submit()):
        try:
            try:
                password_hash = db_obj.get_hash_user_by_email(email)[0]
            except:
                flash('This email does not exist. Please try again.')
                return redirect('/login')
            password = login_form.password.data
            was_logged_successfully = werkzeug.security.check_password_hash(pwhash=password_hash, password=password)
        except:
            
            was_logged_successfully = False
        #input("USER HASH: "+str(password_hash))
        #input("PASSWORD INSERTED..."+str(werkzeug.security.generate_password_hash(request.form['password'], method='sha256', salt_length=8)))

        if(was_logged_successfully):
            print("LOGGED")
            Us = load_user(db_obj.get_user_id_by_email(email)[0])
            login_user(Us)
            flash('You were successfully logged in')
            
            return redirect('/')

        else:
            print("NOT LOGGED...")
            flash('Password incorrect: Please Try Again!') 
            return render_template('login.html', form=login_form)
        
    return render_template('login.html', error=error, form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You were successfully logged out!') 
    return redirect(url_for('get_all_posts'))


@app.route('/',methods=["GET"])
def get_all_posts():
    
    is_logged=bool(current_user.is_authenticated)
    #input(is_logged)
    db_obj.mountTables()
    all_posts = db_obj.get_all_posts()

    final_json = []
    #input("ALL POSTS "+str(all_posts))
    for post in all_posts:
            #input("CURRENT POST "+str(post))
            post={
                "id":post[0],
                "title":post[1],
                "date":post[2],
                "body":post[3],
                "author":db_obj.get_author_name_from_author_id(post[7]),
                "img_url":post[5],
                "subtitle": post[6]
                }
        
            final_json.append(post)
    #input(final_json)


    # return jsonify(final_json)
    return render_template("index.html", all_posts=final_json, is_logged=is_logged)


@app.route('/show_post', methods=["GET","POST"])
@login_required
def show_post():
    comment_form = CommentForm()
    post_id = request.args.get("post_id")
    requested_post = db_obj.get_post_by_id(post_id)[0]
    comments = db_obj.get_all_comments(post_id)

    #input("COMMENTS..."+str(comments))
    #input("NAME OF THE AUTHOR..."+str(db_obj.get_author_name_from_author_id(comments[0][2])))

    post={
        "id":requested_post[0],
        "title":requested_post[1],
        "date":requested_post[2],
        "body":requested_post[3],
        "author":requested_post[4],
        "img_url":requested_post[5],
        "subtitle": requested_post[6]
        }
    
    if(comment_form.validate_on_submit()): 
        db_obj.insert_new_comment(comment_form.body_content.data,post_id)
        comments = db_obj.get_all_comments(post_id)
        return render_template("post.html", post=post, form=comment_form, comments=comments)

    #input("COMMENTS: "+str(comments))
    return render_template("post.html", post=post, form=comment_form, comments=comments)


# TODO: add_new_post() to create a new blog post
@app.route('/new_post', methods=["POST", "GET"])
@login_required
def add_post():
    new_post_form = NewPostForm()

    if(new_post_form.validate_on_submit()):
        x = datetime.datetime.now()
        date = (x.strftime("%B")+ " "+ x.strftime("%d")+", "+x.strftime("%Y"))
        #input(date)
        title = new_post_form.blog_post_title.data
        subtitle = new_post_form.blog_subtitle.data
        #author = new_post_form.author_name.data
        img_url = new_post_form.img_url.data
        body_content = new_post_form.body_content.data
        db_obj.insert_new_post(title,date,body_content,img_url,subtitle)
        return redirect('/')
    return render_template("make-post.html", form=new_post_form, action="NEW_POST")



# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=["POST","GET"])
@login_required
@admin_only
def edit_post(post_id):
    new_post_form = NewPostForm()
    id = post_id
    post_to_update = db_obj.get_post_by_id(id)
    #input("POST TO BE UPDATED: "+str(post_to_update))


    if(new_post_form.validate_on_submit()):
        #input(date)
        title = new_post_form.blog_post_title.data
        subtitle = new_post_form.blog_subtitle.data
        author = new_post_form.author_name.data
        img_url = new_post_form.img_url.data
        body_content = new_post_form.body_content.data
        #input("IT WILL BE UPDATED..."+str(title)+str(subtitle)+str(author)+str(img_url)+str(body_content))
        db_obj.update_post(title,body_content,author,img_url,subtitle, id)
        return redirect('/')
    
    else:
        new_post_form.blog_post_title.data = post_to_update[0][1]
        new_post_form.blog_subtitle.data = post_to_update[0][6]
        new_post_form.author_name.data = post_to_update[0][4]
        new_post_form.img_url.data = post_to_update[0][5]
        new_post_form.body_content.data = post_to_update[0][3]
    return render_template("make-post.html", form=new_post_form, action="EDIT_POST") 


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>', methods=["POST","GET", "DELETE"])
@login_required
@admin_only
def delete_post(post_id):
    id = post_id
    #input("POST TO BE UPDATED: "+str(post_to_update))
    db_obj.delete_post_by_id(id)
    return redirect('/')

#04 NOVEMBRO
# 14 DE OUTUBRO
# 11 de Novembro

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    is_logged=bool(current_user.is_authenticated)
    return render_template("about.html",is_logged=is_logged)


@app.route("/contact")
def contact():
    is_logged=bool(current_user.is_authenticated)
    return render_template("contact.html",is_logged=is_logged)




if __name__ == "__main__":
    db_obj.mountTables()
    app.run(debug=True, port=5002)
