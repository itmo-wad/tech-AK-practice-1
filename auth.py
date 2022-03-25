from flask import render_template, request, flash

from global_vars import app, mongo


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == "GET":
        return render_template('auth.html')
    else:
        user = request.form['user']
        passwd = request.form['pass']
        if mongo.db.practice1.find_one({"user": user, "password": passwd}): #true, if there was one entry found in database
            return render_template('secret.html')
        else:
            flash('Wrong username or password!', 'warning')
            return render_template('auth.html')