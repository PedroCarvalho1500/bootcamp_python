import sqlite3
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
import flask
import werkzeug
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
import datetime
from wtforms import StringField, SubmitField, Label, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length
import logging



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6a'
app.config['UPLOAD_FOLDER'] = 'static/files'
login_manager = LoginManager()
login_manager.init_app(app)
# CONNECT TO DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#db = SQLAlchemy()
#db.init_app(app)






#werkzeug.security.generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

class User(UserMixin):
    def __init__(self, id, email, password,name):
         self.id = id
         self.email = email
         self.password = password
         self.name = name
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


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=1, max=1000)])
    email = StringField(label='Email', validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=1, max=12)])
    submit = SubmitField('Sign Me Up')



class DB_Actions():
    def __init__(self,title=""):
        self.title = title

    def connect_db(self):
        self.conn = sqlite3.connect("instance/users.db")
        self.cursor = self.conn.cursor()

            
    def disconnect_db(self):
        print("DATABASE DISCONNECTED!!!")
        self.conn.close()

    def mountTables(self):
        self.connect_db()
        print("Conectando ao Banco de Dados!")
            
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS cafe (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(2000) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL,
                name VARCHAR(1000) NOT NULL
                )""")
                
        self.conn.commit()
        print("DATABASE CREATED!!!")
        self.disconnect_db()

    def insert_new_register(self, name, email, password):
        self.connect_db()
        print("ENTERED HERE...")
        self.cursor.execute(""" INSERT INTO user (email, password, name) VALUES(?,?,?)""", [email, password, name])
        self.conn.commit()

        self.disconnect_db()

    def get_hash_user_by_email(self,email):
        self.connect_db()

        user_hash = self.cursor.execute(""" SELECT password FROM user WHERE email=?""", [email]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        return user_hash[0]
    
    def get_user_id_by_email(self,email):
        self.connect_db()

        id = self.cursor.execute(""" SELECT id FROM user WHERE email=?""", [email]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        return id[0]
    
    def get_user_name_by_email(self,email):
        self.connect_db()

        name_searched = self.cursor.execute(""" SELECT name FROM user WHERE email=?""", [email]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        return name_searched[0]
    
    def get_password_by_email(self,email):
        self.connect_db()

        password_searched = self.cursor.execute(""" SELECT password FROM user WHERE email=?""", [email]).fetchall()
        self.conn.commit()

        self.disconnect_db()

        return password_searched[0]

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




db_obj = DB_Actions()
#new_user = User("","","","")
#user = User()

# CREATE TABLE IN DB
#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(100), unique=True)
#    password = db.Column(db.String(100))
#    name = db.Column(db.String(1000))
 


 
#with app.app_context():
#    db.create_all()
@login_manager.user_loader
def load_user(user_id):
   db_obj.connect_db()
   lu = db_obj.get_or_404(user_id)
   print("LU -> "+str(lu))
   if lu is None:
      return None
   else:
      return User(int(lu[0]), lu[1], lu[2], lu[3])
   


@app.route('/')
def home():
    db_obj.mountTables()
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
@login_required
def register():
    #new_register_form = RegisterForm()

    return render_template("register.html")


@app.route('/registered', methods=["POST","GET"])
def registered():
    name = request.form['name']
    email = request.form['email']
    password = werkzeug.security.generate_password_hash(request.form['password'], method='sha256', salt_length=8)

    
    db_obj.insert_new_register(name,email,password)

    #input("HERE...")
    new_user = User(db_obj.get_user_id_by_email(email)[0],email,password,name)
    #input(db_obj.get_user_id_by_email(email)[0])
    logout_user()
    Us = load_user(db_obj.get_user_id_by_email(email)[0])
    login_user(Us)

    return redirect('/secrets/'+str(email))


@app.route('/login', methods=["POST", "GET"])
def login():

    return render_template("login.html")


@app.route('/logged', methods=["GET", "POST"])
def logged():
    error = None
    email = request.form['email']

    try:
        password_hash = db_obj.get_hash_user_by_email(email)[0]
        password = request.form['password']
        was_logged_successfully = werkzeug.security.check_password_hash(pwhash=password_hash, password=password)
    except:
        error = 'Password incorrect: Please Try Again!'
        was_logged_successfully = False
    #input("USER HASH: "+str(password_hash))
    #input("PASSWORD INSERTED..."+str(werkzeug.security.generate_password_hash(request.form['password'], method='sha256', salt_length=8)))

    if(was_logged_successfully):
        print("LOGGED")
        Us = load_user(db_obj.get_user_id_by_email(email)[0])
        login_user(Us)
        flash('You were successfully logged in')
        #input("LOGGED...")
        return redirect('/secrets/'+str(email))

    else:
        print("NOT LOGGED...")
    
    return render_template('login.html', error=error)




@app.route('/secrets/<email>', methods=["POST","GET"])
@login_required
def secrets(email):
    print("AUTHENTICATED...")
    #input(current_user.is_authenticated)
    #logout_user(user)
    #input("USER IS AUTHENTICATED? "+str(user.is_authenticated))

    #logout_user()

    #if current_user.is_authenticated == False:
         #return app.login_manager.unauthorized()
    
    #else:
        # email = email
    name = db_obj.get_user_name_by_email(email)[0]
        # password = db_obj.get_password_by_email(email)
        # password = werkzeug.security.generate_password_hash(password, method='sha256', salt_length=8)

    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/download', methods=["GET"])
@login_required
def download():
    if current_user.is_authenticated == False:
        return app.login_manager.unauthorized()
    
    else:
        print("DOWNLOADING FILE...")
        return send_from_directory(
            app.config['UPLOAD_FOLDER'], "cheat_sheet.pdf", as_attachment=False
        )


if __name__ == "__main__":
    db_obj.mountTables()
    app.run(debug=True)
