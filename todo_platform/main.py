import sqlite3
from flask import Flask, jsonify, redirect, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask_api import status
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
import requests
from wtforms import StringField, SubmitField, Label, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)




class AddStepForm(FlaskForm):
    title = StringField(label='Step Name', validators=[Length(min=0, max=100), DataRequired()])
    #time_estimate = StringField(label='Time Estimate', validators=[Length(min=0, max=100)])
    #finished = BooleanField(label='Finished? 1 for True and 0 for False', validators=[Length(min=1, max=1), Regexp(r'[0,1]') ])
    done = SubmitField('Save')


class AddTaskForm(FlaskForm):
    name = StringField(label='Name', validators=[Length(min=0, max=100), DataRequired()])
    img_url = StringField(label='Img Url', validators=[Length(min=0, max=1000)])
    done = SubmitField('Save Task')





class DB_Actions():
    def __init__(self,title="",finished=False,name=""):
        self.title = title
        self.finished = finished
        self.name = name

    def connect_db(self):
        self.conn = sqlite3.connect("instance/project.db")
        self.cursor = self.conn.cursor()

            
    def disconnect_db(self):
        print("DATABASE DISCONNECTED!!!")
        self.conn.close()

    def mountTables(self):
        self.connect_db()
        print("Conectando ao Banco de Dados!")
            
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS task (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(2000) UNIQUE NOT NULL,
                img_url VARCHAR(2000) NOT NULL
                )""")
        
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS step (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                id_task INT(100) NOT NULL,
                title VARCHAR(2000) UNIQUE NOT NULL,
                finished BIT NOT NULL,
                FOREIGN KEY (id_task) REFERENCES task(id)
                )""")
                
        self.conn.commit()
        print("DATABASE CREATED!!!")
        self.disconnect_db()

    # def get_random_cafe(self):
    #     self.connect_db()

    #     random_cafe = self.cursor.execute(""" SELECT * FROM cafe ORDER BY random() LIMIT 1""").fetchone()
    #     self.conn.commit()
    #     #input(random_cafe)

    #     self.disconnect_db()

    #     return random_cafe
    
    def get_all_tasks(self):
        self.connect_db()

        all_tasks = self.cursor.execute(""" SELECT * FROM task """).fetchall()
        self.conn.commit()
        #input(all_cafe)

        self.disconnect_db()

        return all_tasks
    

    def get_all_steps_from_a_task_id(self,id):
        self.connect_db()

        all_steps = self.cursor.execute(""" SELECT * FROM step WHERE id_task=? """, [id]).fetchall()
        self.conn.commit()
        #input(all_cafe)

        self.disconnect_db()

        return all_steps
    
    def change_status_to_finished(self,id):
        self.connect_db()

        self.cursor.execute(""" UPDATE step SET finished=? WHERE id=?""", (1,id))
        self.conn.commit()
        #input(all_cafe)

        self.disconnect_db()


    def insert_new_step(self,title,id_task,finished):
        self.connect_db()

        self.cursor.execute(""" INSERT INTO step (id_task,title,finished) VALUES(?,?,?)""", (id_task,title,finished))
        self.conn.commit()

        self.disconnect_db()

    def insert_new_task(self,name,img_url):
        self.connect_db()

        self.cursor.execute(""" INSERT INTO task (name,img_url) VALUES(?,?)""", (name,img_url))
        self.conn.commit()

        self.disconnect_db()

    def delete_task(self,id):
        self.connect_db()

        self.cursor.execute(""" DELETE FROM task WHERE id=?""", [id])
        self.conn.commit()

        self.disconnect_db()



    # def get_cafe_by_location(self,location):
    #     self.connect_db()

    #     all_cafe_by_location = self.cursor.execute(""" SELECT * FROM cafe WHERE location LIKE ?""", ["%"+location+"%"]).fetchall()
    #     self.conn.commit()
    #     #input(all_cafe_by_location)

    #     self.disconnect_db()

    #     return all_cafe_by_location
    
    # def get_cafe_by_id(self,id):
    #     self.connect_db()

    #     all_cafe_by_id = self.cursor.execute(""" SELECT * FROM cafe WHERE id=?""", [id]).fetchall()
    #     self.conn.commit()
    #     #input(all_cafe_by_location)

    #     self.disconnect_db()

    #     return all_cafe_by_id



    # def update_price(self,id,new_price):
    #     self.connect_db()

    #     self.cursor.execute(""" UPDATE cafe SET coffee_price=? WHERE id=?""", (new_price,id))
    #     self.conn.commit()

    #     self.disconnect_db()

    # def delete_cafe(self,id):
    #     self.connect_db()

    #     self.cursor.execute(""" DELETE FROM cafe WHERE id=?""", [id])
    #     self.conn.commit()

    #     self.disconnect_db()

    # def get_cafe_by_conditions(self,name,location):
    #     self.connect_db()

    #     self.conn.commit()

    #     all_cafe_by_conditions = self.cursor.execute("""SELECT * FROM cafe WHERE name LIKE ? AND location LIKE ? ORDER BY id ASC;""", ("%"+name+"%","%"+location+"%")).fetchall()
        

    #     self.disconnect_db()

    #     return all_cafe_by_conditions


db_obj = DB_Actions()


@app.route("/")
def home():
    db = DB_Actions()
    all_tasks = db.get_all_tasks()
    #input(all_cafes[1])
    return render_template("index.html", tasks = all_tasks)
    

@app.route('/add_task', methods=["GET", "POST"])
def add_task():
    add_task_form = AddTaskForm()
    db_obj = DB_Actions()


@app.route('/list_steps/<int:task_id>')
def list_steps(task_id):
    db_obj = DB_Actions()
    id = task_id
    all_steps = db_obj.get_all_steps_from_a_task_id(id)
    size_list = len(all_steps)
    #input(all_steps)

    return render_template('list_steps.html',all_steps=all_steps, size = size_list, id=id)


@app.route('/change_to_finish/<int:task_id>/<int:id_step>')
def change_to_finish(task_id,id_step):
    db_obj = DB_Actions()
    id = id_step
    db_obj.change_status_to_finished(id)
    #input("ENTERED...")

    return redirect('/list_steps/'+str(task_id))



@app.route('/add_new_step/<int:task_id>', methods=["POST", "GET"])
def add_new_step(task_id):
    db_obj = DB_Actions()
    add_step_form = AddStepForm()

    if(add_step_form.validate_on_submit()):
        d = {'title': add_step_form.title.data, 'finished': 0, 'id_task': task_id}
        add_step_request = requests.post(url='http://localhost:5000/add', data=d).json()
        #input(add_cafe_request)
        flash('New Step Added!')
        return render_template('/step_added.html', task_id = task_id)

    return render_template('add_step.html',form=add_step_form)



@app.route('/add_new_task', methods=["POST", "GET"])
def add_new_task():
    db_obj = DB_Actions()
    add_task_form = AddTaskForm()

    if(add_task_form.validate_on_submit()):
        d_task = {"name": add_task_form.name.data, "img_url": add_task_form.img_url.data}
        #input("HERE...")
        add_task_request = requests.post(url='http://localhost:5000/task_add', data=d_task).json()
        # input("HERE...")
        #input(add_cafe_request)
        flash('New Task Added!')
        return render_template('/task_added.html')

    return render_template('add_task.html',form=add_task_form)




@app.route('/delete_task/<int:task_id>', methods=["DELETE", "POST", "GET"])
def delete_task(task_id):
    id = task_id
    #input("ENTERED 1")
    delete_cafe_request = requests.delete(url='http://localhost:5000/delete1/'+str(id)).json()
    return redirect('/')



@app.route('/add', methods=["POST"])
def add_new():
    title = request.form["title"]
    id_task = request.form["id_task"]
    finished = request.form["finished"]
    db_obj = DB_Actions()
    db_obj.insert_new_step(title=title, id_task=id_task, finished=finished)

    return jsonify(response={
            "success": "Successfully added new step."
        })


@app.route('/task_add', methods=["POST"])
def add_task_api():
    #try:
    #input("ENTERED...")
    name = request.form["name"]
    img_url = request.form["img_url"]
    db_obj = DB_Actions()
    db_obj.insert_new_task(name=name, img_url=img_url)

    return jsonify(response={
            "success": "Successfully added new Task."
        })


@app.route('/delete1/<int:task_id>', methods=["DELETE","GET", "POST"])
def delete1(task_id):
    id = task_id
    db_obj = DB_Actions()
    try:
        db_obj.delete_task(id)
        return jsonify(response={
                "success": "Successfully delete the Task."
            })
    
    except:
        return jsonify(error={
                "Not Found": "Sorry! A Task with that id was not found in the database."
            }),status.HTTP_404_NOT_FOUND



            

# @app.route('/all', methods=["GET", "POST"])
# def get_all():
#     all_cafe = db_obj.get_all_cafes()
#     final_json = []
#     for cafe in all_cafe:
#             cafe={
#                 "can_take_calls":cafe[8],
#                 "coffee_price":cafe[10],
#                 "has_socket":cafe[5],
#                 "has_toillet":cafe[6],
#                 "has_wifi":cafe[7],
#                 "id":cafe[0],
#                 "img_url":cafe[3],
#                 "location":cafe[4],
#                 "map_url":cafe[2],
#                 "name":cafe[1],
#                 "seats":cafe[9]
#                 }
                
        
#             final_json.append(cafe)


#     return jsonify(final_json)



# @app.route('/search_for_cafe', methods=["GET", "POST"])
# def search_for_cafe():
#     db_obj = DB_Actions()
#     search_cafe_form = SearchForCafeForm()
#     if(search_cafe_form.validate_on_submit()):
#         cafe_found = db_obj.get_cafe_by_conditions(search_cafe_form.name.data,search_cafe_form.location.data)
#         #input(cafe_found)
#         return render_template('/cafe_found.html', cafes=cafe_found)
#     return render_template('search_for_cafe.html', form=search_cafe_form)


# @app.route('/search', methods=["GET", "POST"])
# def search_by_location():
#     query_location = request.args.get("loc")
#     cafes = db_obj.get_cafe_by_location(query_location)
#     if(len(cafes) > 0 ):
#         final_json = []
#         for cafe in cafes:
#                 cafe={
#                     "can_take_calls":cafe[8],
#                     "coffee_price":cafe[10],
#                     "has_socket":cafe[5],
#                     "has_toillet":cafe[6],
#                     "has_wifi":cafe[7],
#                     "id":cafe[0],
#                     "img_url":cafe[3],
#                     "location":cafe[4],
#                     "map_url":cafe[2],
#                     "name":cafe[1],
#                     "seats":cafe[9]
#                     }
                    
            
#                 final_json.append(cafe)


#         return jsonify(final_json)     
    
#     else:
#         return jsonify(error={
#             "Not Found": "Sorry, we don't have a cafe at that location."
#         }),status.HTTP_404_NOT_FOUND


# @app.route('/delete_cafe/<int:cafe_id>', methods=["DELETE", "POST", "GET"])
# def cafe_delete(cafe_id):
#     id = cafe_id
#     delete_cafe_request = requests.delete(url='http://localhost:5000/delete/'+str(id)).json()
#     return redirect('/')


# @app.route('/delete/<int:cafe_id>', methods=["DELETE","GET", "POST"])
# def delete(cafe_id):
#     id = cafe_id

#     try:
#         db_obj.delete_cafe(id)
#         return jsonify(response={
#                 "success": "Successfully delete the Cafe."
#             })
    
#     except:
#         return jsonify(error={
#                 "Not Found": "Sorry a cafe with that id was not found in the database."
#             }),status.HTTP_404_NOT_FOUND





# @app.route('/update-price/<int:cafe_id>', methods=["PATCH"])
# def update_price(cafe_id):
#     id = cafe_id
#     coffee_price = request.form["new_price"]
#     #input(coffee_price)
#     cafe_by_id = db_obj.get_cafe_by_id(id)

#     if(len(cafe_by_id) > 0):
#         db_obj.update_price(id,coffee_price)

#         return jsonify(response={
#                 "success": "Successfully updated the price."
#             })
    
#     else:
#         return jsonify(error={
#                 "Not Found": "Sorry a cafe with that id was not found in the database."
#             }),status.HTTP_404_NOT_FOUND
    

# @app.route('/report-closed/<int:cafe_id>', methods=["DELETE"])
# def delete_cafe(cafe_id):
#     id = int(cafe_id)
#     api_key = request.args.get("api-key")
#     #input(coffee_price)

#     cafe_by_id = db_obj.get_cafe_by_id(id)
#     if api_key == "TopSecretAPIKey":
#         if(len(cafe_by_id) > 0):
#             db_obj.delete_cafe(id)

#             return jsonify(response={
#                     "success": "Successfully deleted the cafe."
#                 })
        
#         else:
#             return jsonify(error={
#                     "Not Found": "Sorry a cafe with that id was not found in the database.",
#                 }),status.HTTP_404_NOT_FOUND
    
#     else:
#         return jsonify(error={
#                 "Not Found": "Sorry, that's not allowed. Make sure you have the correct api_key."
#             }),status.HTTP_403_FORBIDDEN



# @app.route('/search/<string:loc>', methods=["GET", "POST"])
# def search_by_location(loc):
#     cafes = db_obj.get_cafe_by_location(loc)
    
#     if(len(cafes) > 0 ):
#         final_json = []
#         for cafe in cafes:
#                 cafe={
#                     "can_take_calls":cafe[8],
#                     "coffee_price":cafe[10],
#                     "has_socket":cafe[5],
#                     "has_toillet":cafe[6],
#                     "has_wifi":cafe[7],
#                     "id":cafe[0],
#                     "img_url":cafe[3],
#                     "location":cafe[4],
#                     "map_url":cafe[2],
#                     "name":cafe[1],
#                     "seats":cafe[9]
#                     }
                    
            
#                 final_json.append(cafe)


#         return jsonify(final_json)     
    
#     else:
#         return jsonify(error={
#             "Not Found": "Sorry, we don't have a cafe at that location."
#         })



## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    db_obj.mountTables()
    app.run(debug=True)
