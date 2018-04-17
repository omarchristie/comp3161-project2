"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, filefolder, engine, mysql
from flask import render_template, request, redirect, url_for, flash, session, g, jsonify
from forms import LoginForm, RegistrationForm, RecipeForm, RecipesForm, FilterForm
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
import datetime
import json
import time
import random


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        # change this to actually validate the entire form submission
        # and not just one field
        username = form.username.data
        password = form.password.data
        cur =  mysql.connection.cursor()
        cur.execute('''SELECT * FROM account where username = ''' + '"'+username+'"')
        result = list(cur.fetchall())
        for row in result:
            if check_password_hash(row['pword'], password):
                session['user'] = row['username']
                flash('Logged in successfully.', 'success')
                # remember to flash a message to the user
                return redirect(url_for('profile'))  # they should be redirected to a secure-page route instead
            
        flash('Username or Password is incorrect.', 'danger')
    return render_template("login.html", form=form)
    
    
def get_illness():
    cur =  mysql.connection.cursor()
    cur.execute('SELECT * from illness')
    result = list(cur.fetchall())
    return result
    
@app.route('/test/', methods=["GET", "POST"])
def test():
    cur =  mysql.connection.cursor()
    cur.execute('SELECT * from illness')
    result = list(cur.fetchall())
    return str(result[0]['illness_id'])

@app.route('/registration/', methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    illnesses = get_illness()

    for row in illnesses:
        illness_type = row['illness_type']
        illness_id = row['illness_id']
        form.illness.choices += [(illness_id, illness_type)]
    if request.method == "POST" and form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        password = form.password.data
        hash_password = generate_password_hash(password)
        email = form.email.data
        username = form.username.data
        dietchoice = form.diet_choice.data
        dob = form.dob.data
        illness = form.illness.data
        cur = mysql.connection.cursor()
        cur.callproc("add_account", [username, hash_password])
        cur.close()
        cur2 = mysql.connection.cursor()
        cur2.callproc("Register", [username, firstname, lastname, dob, email, dietchoice])
        cur2.close()
        mysql.connection.commit()
        firstconnection = mysql.connection.cursor()
        firstconnection.execute('''SELECT profile_id FROM user_profile where username = ''' + '"'+username+'"')
        uid = list(firstconnection.fetchall())
        firstconnection.close()
        cur3 = mysql.connection.cursor()
        cur3.execute('INSERT into profile_illnesses (profile_id, illness_id) VALUES (%s, %s)' %(uid[0]['profile_id'], illness))                                                            
        cur3.close()
        mysql.connection.commit()
        flash('Successfully added.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/profile')
def profile():
    if g.user:
        username = session['user']
        cur =  mysql.connection.cursor()
        cur.execute('''SELECT * FROM user_profile where username = ''' + '"'+username+'"')
        result = list(cur.fetchall())
        user = {'fname': result[0]['fname'], 'lname': result[0]['lname'], 'email': result[0]['email'], 'dob': result[0]['dob'], 'diet_choice': result[0]['diet_choice']}
        return render_template('profile.html', user=user)
    return redirect(url_for('home'))
    
@app.route('/Add_recipe',methods=["GET","POST"])
def addRecipe():
    form = RecipeForm()
     
    ingredient= get_ingredients()

    for row in ingredient:
        ing = row['ingredients_name']
        ingid = row['ingredients_id']
        ingu = row['measuring_unit']
        form.ingredient1.choices += [(ingid, ing + " - " + ingu)]
        form.ingredient2.choices += [(ingid, ing + " - " + ingu)]
        form.ingredient3.choices += [(ingid, ing + " - " + ingu)]
        form.ingredient4.choices += [(ingid, ing + " - " + ingu)]
        form.ingredient5.choices += [(ingid, ing + " - " + ingu)]
    if request.method=="POST" and form.validate_on_submit():
        now = datetime.datetime.now()
        recipename = form.name.data
        recipetype = form.recipetype.data
        diet_type = form.diet_type.data
        serving = form.serving.data
        preptime = form.preptime.data
        time_unit = form.time.data
        caloriecount = form.caloriecount.data
        unit1 = form.unit1.data
        ingredient1 = form.ingredient1.data
        unit2 = form.unit2.data
        ingredient2 = form.ingredient2.data
        unit3 = form.unit3.data
        ingredient3 = form.ingredient3.data
        unit4 = form.unit4.data
        ingredient4 = form.ingredient4.data
        unit5 = form.unit5.data
        ingredient5 = form.ingredient5.data
        instruction1 = form.instruction1.data
        instruction2 = form.instruction2.data
        instruction3 = form.instruction3.data
        instruction4 = form.instruction4.data
        instruction5 = form.instruction5.data
        f = form.upload.data
        filename = secure_filename(f.filename)
        username = session['user']
        cur = mysql.connection.cursor()
        cur.callproc("Recipe", [recipename,serving, preptime, time_unit, recipetype, diet_type, caloriecount, filename ])
        cur.close()
        mysql.connection.commit()#Recipe Information is added to recipe table
        f.save(os.path.join(filefolder, filename))
        cur1 = mysql.connection.cursor()
        cur1.execute('SELECT MAX(recipe_id) AS id FROM recipes')
        maxid = list(cur1.fetchall())
        cur1.close()
        recipeid = maxid[0]['id']
        cur2 = mysql.connection.cursor()
        cur2.callproc("add_Recipe", [username, recipeid, now])
        cur2.close()
        mysql.connection.commit()
        cur3 = mysql.connection.cursor()
        cur3.callproc("Comprise", [recipeid, ingredient1, unit1])
        mysql.connection.commit()
        cur3.callproc("Comprise", [recipeid, ingredient2, unit2])
        mysql.connection.commit()
        cur3.callproc("Comprise", [recipeid, ingredient3, unit3])
        mysql.connection.commit()
        cur3.callproc("Comprise", [recipeid, ingredient4, unit4])
        mysql.connection.commit()
        cur3.callproc("Comprise", [recipeid, ingredient5, unit5])
        cur3.close()
        mysql.connection.commit()
        cur4 = mysql.connection.cursor()
        cur4.callproc("Instruction", [recipeid, instruction1])
        mysql.connection.commit()
        cur4.callproc("Instruction", [recipeid, instruction2])
        mysql.connection.commit()
        cur4.callproc("Instruction", [recipeid, instruction3])
        mysql.connection.commit()
        cur4.callproc("Instruction", [recipeid, instruction4])
        mysql.connection.commit()
        cur4.callproc("Instruction", [recipeid, instruction5])
        cur4.close()
        mysql.connection.commit()
        return redirect(url_for('profile'))
    return render_template("recipe.html",form=form)
    
    
def get_ingredients():
    cur =  mysql.connection.cursor()
    cur.execute('SELECT * from ingredients')
    result = list(cur.fetchall())
    return result
    
@app.route('/recipes', methods=["GET","POST"])
def recipes():
    form = RecipesForm()
    if request.method=="POST" and form.validate_on_submit():
        cursor = mysql.connection.cursor()
        cursor.callproc("GetRecipesLike",[str(form.name.data)])
        result = list(cursor.fetchall())

        cursor.close()
        mysql.connection.commit()
        return render_template("recipes.html",form=form,recipes=result)
    return render_template("recipes.html",form=form)

@app.route('/filteredrecipes',methods=["GET","POST"])
def filteredrecipes():
    form = FilterForm()
    if request.method=="POST" and form.validate_on_submit():
        cursor = mysql.connection.cursor()
        cursor.callproc("GetUnderSpecficCalorieCount",[str(request.form['calories'])])
        result = list(cursor.fetchall())
        cursor.close()
        mysql.connection.commit()
        return render_template("recipes.html",form=form,recipes=result)
    return render_template("recipes.html",form=form)
    
@app.route('/recipedetails/<recipeid>',methods=["GET"])
def recipedetails(recipeid):
    cursor = mysql.connection.cursor()
    cursor.callproc("GetRecipeById",[str(recipeid)])
    recipes = list(cursor.fetchall())
    cursor.close()
    cursor2 = mysql.connection.cursor()
    cursor2.callproc("recipeinstruction",[str(recipeid)])
    instr = list(cursor.fetchall())
    cursor2.close()
    mysql.connection.commit()
    return render_template("recipedetails.html",recipes=recipes, instrs=instr )
    
@app.route('/generate_mealplan',methods=["GET"])
def newMealPlan():
    firstconnection = engine.connect()
    result = firstconnection.execute("select mealplanday.mealplanday_id from mealplanday")
    mealplandays = []
    for row in result:
        mealplandays.append(row['mealplanday_id'])
    firstconnection.close()
    # connection = engine.raw_connection()
    # cursor = connection.cursor()
    # # cursor.callproc("GetMealPlanForWeek", [random.choice(mealplandays)])
    # cursor.close()
    # connection.commit()
    return render_template("mealplan.html")
    
@app.route('/getmealplanrecipes/<mtype>', methods=["GET","POST"])
def getmealplanrecipes(mtype):
    form = RecipesForm(request.form)
    if request.method=="GET":
        connection = engine.raw_connection()
        cursor = connection.cursor()

        cursor.callproc("GetWeekRecipesByType",[str(mtype)])
        result = cursor.fetchall()
        print result

        cursor.close()
        connection.commit()
        recipes = []
        for row in result:
            recipes.append(row)
        print recipes
        return jsonify({"recipes":recipes})
    
    
    
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route("/logout")
def logout():
    # Logout the user and end the session
    session.pop('user', None)
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))    



###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
