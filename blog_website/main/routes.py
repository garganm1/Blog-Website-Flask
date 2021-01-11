from flask import render_template, request, Blueprint
from blog_website.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def hello():
    page = request.args.get('page', 1, type=int)
    postings = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template('home.html', posts=postings)

@main.route("/about")
def abt():
    return render_template('about.html', title='ABT')