import threading
import time
from flask import Flask, render_template, request, jsonify
from supabase import create_client
from dotenv import load_dotenv
import os, markdown

load_dotenv()

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)

posts_table = supabase.table("posts")

cache = {
    "posts": [],
    "last_fetched": 0
}

def refresh_cache(interval=60):
    while True:
        try:
            response = posts_table.select('*').order('created_at', desc=True).execute()
            cache["posts"] = response.data
            cache["last_fetched"] = time.time()
            time.sleep(interval)
            print("Cache refreshed!")
        except Exception as e:
            print(f"Error refreshing cache: {e}")
            time.sleep(interval)
            
threading.Thread(target=refresh_cache, args=(60,), daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    # {{ post.text }}
    # {% if post.image %}Post Image{% endif %}
    # {{ post.content }}
    # replace those in the html with data from the database
    post_data = cache["posts"]
    print(post_data[0])
    if not post_data:
        return "Post not found", 404
    # array needs to be reversed because newest posts are first
    post_data = list(reversed(post_data))
    post = next((p for p in post_data if p['id'] == post_id), None)
    if not post:
        return "Post not found", 404
    post['content'] = markdown.markdown(post['content'])
    return render_template('post.html', post=post)

@app.route("/api/posts", methods=["GET"])
def api_posts():
    try:
        limit = int(request.args.get("limit", 5))
    except (TypeError, ValueError):
        limit = 5

    response = cache['posts'][:limit]
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
