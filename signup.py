from flask import render_template, request, flash, url_for, redirect
from global_vars import app, mongo


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        user = request.form['user']
        passwd = request.form['pass']
        if user == "" or passwd == "":
            flash('Empty username or password provided', 'warning')
            return render_template('signup.html')
        if mongo.db.practice1.find_one({"user": user}): #true, if there was one entry found in database
            flash('This user is already registered. Do you want to go to the <a href="' + url_for("auth") + '">authentication page</a>?', 'warning')
            return render_template('signup.html')
        else:
            mongo.db.practice1.insert_one({"user": user, "password": passwd})
            if mongo.db.practice1.find_one({"user": user, "password": passwd}):
                #adding new user to database has worked
                flash('Successfully registered! Please log in with your new access credentials', 'success')
                return redirect(url_for('auth'))
            else:
                flash('Something went wrong. Try again', 'warning')
                return render_template('signup.html')