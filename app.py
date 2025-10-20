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
