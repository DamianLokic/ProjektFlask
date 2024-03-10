from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import PostForm
from app.models import Post

@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Post został dodany.')
        return redirect(url_for('index'))
    return render_template('create_post.html', form=form)
