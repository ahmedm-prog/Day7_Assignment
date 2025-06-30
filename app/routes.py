# app/routes.py
from flask import render_template, request, redirect, url_for, Blueprint
from app.models import User, Post
from app import db

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form.get('age')  # Optional field
        if name and email:
            user = User(name=name, email=email, age=age)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))

    users = User.query.all()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', users=users, posts=posts)

@bp.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    user_id = request.form['user_id']
    if title and content and user_id:
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('main.index'))