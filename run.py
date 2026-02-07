# Main Running
# click button run as py- or python run.py
# everything will start from this page run.py

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True
    )

