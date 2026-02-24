from app import create_app
from app.seed import init_db

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)
