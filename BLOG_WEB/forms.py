from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField, Label, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

# WTForm for creating a blog post
class NewPostForm(FlaskForm):
    blog_post_title = StringField(label='Post Title', validators=[DataRequired(), Length(min=1, max=100000)])
    blog_subtitle = StringField('Post Subtitle', validators=[DataRequired(),Length(min=1, max=1000)])
    #author_name = StringField('Author\' Name', validators=[DataRequired(),Length(min=1, max=100)])
    img_url = StringField('Background Image URL', validators=[DataRequired(),Length(min=1, max=100)])
    body_content = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField('Submit Post')


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=1, max=1000)])
    email = StringField(label='Email', validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=1, max=12)])
    submit = SubmitField('Sign Me Up!')





# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Length(min=1, max=100)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=1, max=12)])
    submit = SubmitField('Let Me In!')




# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    body_content = CKEditorField("Insert your Comment Here", validators=[DataRequired()])
    submit = SubmitField('Submit Comment')