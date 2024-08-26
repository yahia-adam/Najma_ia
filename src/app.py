from flask import Flask
from flask import render_template

app = Flask("Najma ai")

@app.route("/")
def home():
    return render_template('app.html')

if __name__ == "__main__":
    app.run()
