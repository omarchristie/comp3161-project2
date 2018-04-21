from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, TextField, IntegerField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message='User Name is required')])
    password = PasswordField('Password', validators=[InputRequired()])
    
class RegistrationForm(FlaskForm):
    firstname = StringField("First Name",validators=[InputRequired()])
    lastname = StringField("Last Name",validators=[InputRequired()])
    username = StringField("Username",validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(message='Email is required'), Email(message="Only Emails")])
    password = PasswordField("Password",validators=[InputRequired()])
    passwordconfirmation = PasswordField("Password Confirmation",validators=[InputRequired()])
    diet_choice = StringField("Diet Choice",validators=[InputRequired()])
    dob = DateField("Date Of Birth",format= '%Y-%m-%d',validators=[InputRequired()])
    illness = SelectField('Food-Allergies', choices=[], coerce=int, validators=[InputRequired()])
    
class RecipeForm(FlaskForm):
    name = StringField("Recipe Name",validators=[InputRequired()])
    recipetype = SelectField("Type",choices=[("Breakfast","Breakfast"),("Lunch","Lunch"),("Dinner","Dinner")])
    diet_type = StringField("Diet Type",validators=[InputRequired()])
    serving = IntegerField("Serving",validators=[InputRequired()])
    preptime = IntegerField("Preparation Time",validators=[InputRequired()])
    time= SelectField('Time unit', choices=[("Mins","Mins"), ("Hrs", "Hrs")], validators=[InputRequired()])
    caloriecount = IntegerField("Calorie Count",validators=[InputRequired()])
    unit1= StringField("Measurement", validators=[InputRequired()])
    ingredient1= SelectField('Ingredient - Unit', choices=[], coerce=int, validators=[InputRequired()])
    unit2= StringField("Measurement", validators=[InputRequired()])
    ingredient2= SelectField('Ingredient - Unit', choices=[], coerce=int, validators=[InputRequired()])
    unit3= StringField("Measurement", validators=[InputRequired()])
    ingredient3= SelectField('Ingredient - Unit', choices=[], coerce=int, validators=[InputRequired()])
    unit4= StringField("Measurement", validators=[InputRequired()])
    ingredient4= SelectField('Ingredient - Unit', choices=[], coerce=int, validators=[InputRequired()])
    unit5= StringField("Measurement", validators=[InputRequired()])
    ingredient5= SelectField('Ingredient - Unit', choices=[], coerce=int, validators=[InputRequired()])
    instruction1 = StringField("Instruction", validators=[InputRequired()])
    instruction2 = StringField("Instruction", validators=[InputRequired()])
    instruction3 = StringField("Instruction", validators=[InputRequired()])
    instruction4 = StringField("Instruction", validators=[InputRequired()])
    instruction5 = StringField("Instruction", validators=[InputRequired()])
    upload = FileField('Image', validators=[FileRequired('Please input a file'), FileAllowed(['jpg', 'png'], 'Images only!')])
    
class RecipesForm(FlaskForm):
    name = StringField("Enter a recipe name", validators=[InputRequired()])
    
class FilterForm(FlaskForm):
    calories = StringField("Enter caloriecount", validators=[InputRequired()])
    
class GenPlanForm(FlaskForm):
    calorie = StringField("Enter a calorie count")
    
    
    
    