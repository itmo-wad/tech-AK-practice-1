from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo

import global_vars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/wad"
app.config['SECRET_KEY'] = "verysecretkey"
app.config['UPLOAD_FOLDER'] = "./upload"
mongo = PyMongo(app)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    global_vars.init(app_ref=app, mongo_ref=mongo)

    # import other declared routes
    import auth, signup, upload
    app.run(host='localhost', port=5000, debug=True)