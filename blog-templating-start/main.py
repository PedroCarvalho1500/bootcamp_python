from post import Post
from flask import Flask, render_template
import requests

app = Flask(__name__)

URL = "https://api.npoint.io/c790b4d5cab58020d391"
#request_gender = requests.get(url="https://api.genderize.io?name="+name).json()
#request_age = requests.get(url="https://api.agify.io?name="+name).json()
#<h1>{{post["title"]}}</h1>
#<h2>{{post["subtitle"]}}</h2>

    # {% for post in posts: %}
    #     {% if post["id"] == number %}
    #         <h1>{{post["title"]}}</h1>
    #         <h2>{{post["subtitle"]}}</h2>
    #     {% endif %}
    # {% endfor %}
request_posts = requests.get(url=URL).json()

@app.route('/')
def home():
    posts = []
    
    #print(request_posts.json())
    for post in request_posts:
        #print(f"HERE ONE POST {post}")
        new_post = Post(post["id"],post["title"],post["subtitle"],post["body"])
        posts.append(new_post)
    return render_template("index.html", posts=posts)


@app.route('/URL/post/<blog_id>')
def get_blog(blog_id):
    return render_template("post.html",blog_id=blog_id,complete_post=request_posts[int(blog_id)-1])



if __name__ == "__main__":
    app.run(debug=True)
