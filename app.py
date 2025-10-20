from flask import Flask, render_template, request, jsonify
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)

posts_table = supabase.table("posts")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    # {{ post.text }}
    # {% if post.image %}Post Image{% endif %}
    # {{ post.content }}
    # replace those in the html with data from the database
    response = posts_table.select('*').eq('id', post_id).execute()
    post_data = response.data
    if not post_data:
        return "Post not found", 404
    post = post_data[0]
    return render_template('post.html', post=post)

@app.route("/api/posts", methods=["GET"])
def api_posts():
    try:
        limit = int(request.args.get("limit", 5))
    except (TypeError, ValueError):
        limit = 5

    response = posts_table.select('*').order('created_at', desc=True).limit(limit).execute()
    posts_data = response.data
    return jsonify(posts_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
