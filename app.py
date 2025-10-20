import os, flask, flask_sqlalchemy

app = flask.Flask(__name__, static_url_path='/assets', static_folder='assets')

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(1000), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    def __repr__(self):
        return f'<Post {self.title}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    post = Post(title="Welcome to the Blog", content="This is the first post!", image=None)
    db.session.add(post)
    db.session.commit()
    return flask.render_template('index.html')

@app.route("/api/posts", methods=["GET"])
def api_posts():
    """API endpoint to get recent posts. JSON"""
    try:
        limit = int(flask.request.args.get("limit", 5))
    except (TypeError, ValueError):
        limit = 5

    posts = Post.query.order_by(Post.created_at.desc()).limit(limit).all()
    posts_data = [
        {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "image": post.image,
            "created_at": post.created_at.isoformat() if post.created_at else None
        }
        for post in posts
    ]
    return flask.jsonify(posts_data)
    


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')