from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Label
from wtforms.validators import DataRequired, Length
import requests
import sqlite3
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class EditMovieForm(FlaskForm):
    your_current_rating = StringField(label='Your rating out of e.g. 7.5', validators=[DataRequired(), Length(min=1, max=2)])
    your_review = StringField('Your Review', validators=[DataRequired(),Length(min=1, max=200)])
    done = SubmitField('Done')



class AddMovieForm(FlaskForm):
    movie_title = StringField(label='Movie Title', validators=[DataRequired(), Length(min=1, max=2000)])
    add_movie = SubmitField('Add Movie')




class API_Movie_Actions():
    def __init__(self,name):
        self.name = name
        self.base_url = "https://api.themoviedb.org/3/search/movie"
        self.headers = {
            "Accept-Encoding": "identity",
            "Authorization": "Bearer "+str(os.getenv("BEARER"))
        }

        self.params = {
            "query": self.name
        }


        self.details_movie_url = "https://api.themoviedb.org/3/movie/"
        

    def find_movie(self):
        get_movies = requests.get(url=self.base_url, headers=self.headers, params=self.params)
        return get_movies.json()

    def get_movie_details(self, movie_id):
        get_movie_details = requests.get(url=self.details_movie_url+movie_id, headers=self.headers)

        return get_movie_details.json()


#USING SQLITE3
class DB_Actions():
    def __init__(self,title="",author="",rating=0):
        self.title = title
        self.author = author
        self.rating = rating

    def connect_db(self):
        self.conn = sqlite3.connect("cinema.bd")
        self.cursor = self.conn.cursor()

            
    def disconnect_db(self):
        print("DATABASE DISCONNECTED!!!")
        self.conn.close()

    def mountTables(self):
        self.connect_db()
        print("Conectando ao Banco de Dados!")
            
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS movie (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(1000) UNIQUE NOT NULL,
                year INTEGER(5) NOT NULL,
                description VARCHAR(1000) NOT NULL,
                rating FLOAT(4),
                ranking INTEGER(2),
                review VARCHAR(1000),
                img_url VARCHAR(5000)
                )""")
                
        self.conn.commit()
        print("DATABASE CREATED!!!")
        self.disconnect_db()


    def get_all_movies(self):
        self.connect_db()
        all_movies = self.cursor.execute("""SELECT * FROM movie;""").fetchall()
        #input(all_books)
        self.conn.commit()
        self.disconnect_db()
        return all_movies

    def get_movie_by_id(self,id):
        self.connect_db()
        movie = self.cursor.execute("""SELECT * FROM movie WHERE id=?;""", (id)).fetchall()
        #input("movie FOUND: "+str(movie))
        self.conn.commit()
        self.disconnect_db()
        return movie

    def edit_movie_info(self,codigo,new_rating, new_review):
        self.connect_db()
        self.cursor.execute(""" UPDATE movie SET rating=?, review=? WHERE id=?""", (new_rating,new_review,codigo))
        self.conn.commit()

        #input(f'UPDATED...')
        #input(all_books)
        #self.conn.commit()
        self.disconnect_db()


    def delete_movie(self,id):
        self.connect_db()
        self.cursor.execute(""" DELETE FROM movie WHERE id=?""", (id))
        self.conn.commit()

        #input(f'UPDATED...')
        #input(all_books)
        self.conn.commit()
        self.disconnect_db()

    def insert_movie(self,title,year,description,img_url):
        self.connect_db()
        self.cursor.execute(""" INSERT INTO movie (title,year,description,rating,ranking,review,img_url) VALUES(?,?,?,?,?,?,?)""", (title,year,description,None, None, None,img_url))

        #input(all_books)
        self.conn.commit()
        self.disconnect_db()

    def get_id_from_movie_name(self,title):
        self.connect_db()
        movie = self.cursor.execute("""SELECT * FROM movie WHERE title=?;""", [title]).fetchall()
        self.conn.commit()
        self.disconnect_db()
        return movie[0]

    def order_ranking(self):
        self.connect_db()
        movies = self.cursor.execute("""SELECT * FROM movie ORDER BY rating ASC;""").fetchall()
        self.conn.commit()
        self.disconnect_db()
        return movies




@app.route("/")
def home():
    db_obj = DB_Actions()
    db_obj.mountTables()
    all_movies = db_obj.order_ranking()
    return render_template("index.html",all_movies=all_movies, size_array=len(all_movies))


@app.route("/edit/<id>", methods = ["POST", "GET"])
def edit(id):
    db = DB_Actions()
    edit_form = EditMovieForm()
    movie = db.get_movie_by_id(id)
    edit_form.your_current_rating.label.text = "Your rating out of "+str(movie[0][5])+" e.g. 7.5"
    
    if(edit_form.validate_on_submit()):
        #print("ENTERED")
        db.edit_movie_info(id,edit_form.your_current_rating.data,edit_form.your_review.data)
        return redirect('/')
    return render_template("edit.html",form=edit_form, movie=movie[0])



@app.route("/deleted/<id>", methods = ["POST", "GET"])
def deleted(id):
    db = DB_Actions()
    db.delete_movie(id)
    return redirect('/')


@app.route("/add", methods = ["POST", "GET"])
def add():
    db = DB_Actions()
    add_form = AddMovieForm()
    
    if(add_form.validate_on_submit()):
        request_add = API_Movie_Actions(add_form.movie_title.data)
        movies_found = request_add.find_movie()
        return render_template('/select.html', movies=movies_found)
    return render_template('add.html', form=add_form)


@app.route("/select_movie", methods = ["POST", "GET"])
def select_movie(list_of_movies):
    db = DB_Actions()

    return redirect('/selected')


@app.route("/selected/<title>/<movie_id>", methods = ["POST", "GET"])
def selected(title,movie_id):
    db = DB_Actions()
    request_details = API_Movie_Actions(title)
    movie_details = request_details.get_movie_details(movie_id=movie_id)
    new_title = title
    new_img_url = "https://image.tmdb.org/t/p/original"+str(movie_details["poster_path"])
    new_year = str(movie_details["release_date"]).split("-")[0]
    new_description = movie_details["overview"]

    db.insert_movie(new_title, new_year, new_description,img_url=new_img_url)

    id = db.get_id_from_movie_name(title=title)[0]

    return redirect('/edit/'+str(id))


if __name__ == '__main__':
    app.run(debug=True)
