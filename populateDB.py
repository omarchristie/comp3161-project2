

import random
import MySQLdb
import datetime
from datetime import datetime, timedelta
import calendar
from faker import Faker
from random import randint
import hashlib
import base64
import uuid


fake = Faker()


#Establish a MySQL connection
# database = MySQLdb.connect (host="127.0.0.1", user = "root", passwd = "2601", db = "meal_planner")

#Get the cursor, which is used to traverse the database, line by line
# cursor = database.cursor()
# print("Database connection establish")
print("Populating Meal Plan Database")



MIN = 100000
DEP = 250000
MAX = 500000



#this function generates any random date between a range
# def random_date():
#   start_dt = date.today().replace(day=1, month=1, year=2012).toordinal()
#   end_dt = date.today().replace(day=31, month=12, year=2042).toordinal()
#   random_day = date.fromordinal(random.randint(start_dt, end_dt))
#   return(random_day)

    # this creates the INSERT INTO sql query, this is where the magic happens, pay close attention to the syntax to alter it to suite your database
    # Make queries depending on how many tables you have so if you have 3 tables, you are going to make 3 queries and so on
    # this also ensures each table and dependencies have the same ID when querying the db



# file = open('meal_planner_data.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
# print("adding user accounts please wait.....")

username_list=[]
profile_id_list = []

def password_generator():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?_=+/><,.`~"
    passlen = random.randint(5,26)
    password =  "".join(random.sample(s,passlen))
    return password

def salt_hash_password():
    password = password_generator()
    salt     = uuid.uuid4().hex
    t_sha = hashlib.sha512()
    t_sha.update(password+salt)
    hashed_password =  hashlib.sha512(password + salt).hexdigest()
    return hashed_password

diet_list=['Ovo vegetarian', 'Ovo-lacto Vegetarian','Vegan', 'Semi-vegetarian','Diabetic', 'Gluten-free','Ketogenic', 'Seventh-day Adventist', 'Carnivor', 'Normal']


for userAccountNo in range(1, (MIN+1)):
    loading_message = 'Account Number:'+' '+str(userAccountNo)
    print(loading_message)
    random_num = random.randint(0,10000000)
    fake_username=fake.user_name()+str(random_num)
    username_list.append(fake_username)

    userAccount = "INSERT INTO `account`(`username`, `pword`) VALUES ('{}','{}')".format(username_list[userAccountNo-1], salt_hash_password())
    
    try:
        #cursor.execute(userAccount)
        file.write(userAccount.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
    except:
        pass
print("Successfully added user accounts")



# f = open( "meal_planner_data.txt", "r" )
# a = []
# for line in f:
#     a.append(line)

# seen = set()
# dups = set()

# for word in a:
#     if word in seen:
#         if word not in dups:
#             print(word)
#             dups.add(word)
#     else:
#         seen.add(word)


print("adding user profiles please wait.....")

for userProfileNo in range(1, (MIN+1)):
    loading_message = 'Profile Number:'+' '+str(userProfileNo)
    print(loading_message)
    lines= open('domains.txt').read().splitlines()
    random_domain =random.choice(lines)
    email=username_list[userProfileNo-1]+'@'+fake.domain_word()+'.'+random_domain.lower()
 
    userProfile = "INSERT INTO `user_profile`(`profile_id`, `username`, `fname`, `lname`, `dob`, `email`, `diet_choice`) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(userProfileNo, username_list[userProfileNo-1], fake.first_name(), fake.last_name(), fake.date(), email, random.choice(diet_list))

    try:
        # cursor.execute(userProfile)
        file.write(userProfile.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
        profile_id_list.append(userProfileNo-1)

    except:
        pass
print("Successfully added user Profiles")

#file.close()


# file = open('meal_planner_meal_plans.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')

def future_date():
    futuredate = datetime.now() + timedelta(days=7)
    return futuredate.strftime("%Y-%m-%d")
    
plan_id_list=[]
plan_id_list2=[]
print("adding meal plans please wait.....")
for meal_plan in range(1, (DEP+1)):
    loading_message = 'Meal Plan Number:'+' '+str(meal_plan)
    print(loading_message)
    meal_plans = "INSERT INTO `week_plan`(`plan_id`, `week`) VALUES ('{}','{}')".format(meal_plan, future_date())

    try:
        #cursor.execute(meal_plans)
        file.write(meal_plans.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
        plan_id_list.append(meal_plan)
        plan_id_list2.append(meal_plan)
    except:
        pass
print("Successfully added meal plans")
#file.close()


# file = open('meal_planner_construct.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
print("adding user constructs dependencies please wait.....")


for contructs in range(0, len(plan_id_list)):
    loading_message = 'Construct Number:'+' '+str(contructs)
    print(loading_message)
    random_user = random.choice(profile_id_list)
    random_plan = random.choice(plan_id_list)

    meal_plans = "INSERT INTO `contructs`(`profile_id`, `plan_id`) VALUES ('{}','{}')".format(random_user, random_plan)

    try:
        #cursor.execute(meal_plans)
        file.write(meal_plans.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
        plan_id_list.remove(random_plan)
    except:
        pass

print("Successfully added constructs dependencies")
#file.close()


# file = open('meal_planner_illnesses.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
allegeries=['Balsam of Peru', 'Egg','Fish or shellfish','Fruit','Gluten','Garlic', 'Hot peppers','Oats','Meat','Milk','Peanut','Rice','Sesame','Soy','Sulfites','Tartrazine','Tree nut','Wheat','None']

print("adding illnesses please wait.....")
for illnessNo in range(1, len(allegeries)):
    print('illnesses Number:'+' '+str(illnessNo))
    illnesses = "INSERT INTO `illness`(`illness_id`, `illness_type`) VALUES ('{}','{}')".format(illnessNo, allegeries[illnessNo])

    try:
        #cursor.execute(illnesses)
        file.write(illnesses.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
    except:
        pass
print("Successfully added illnesses")
#file.close()

# file = open('meal_planner_illnesses_Dep.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
print("adding illnesses dependencies please wait.....")
for illnessDepNo in range(1, MIN+1):

    loading_message = 'illnesse Dep Number:'+' '+str(illnessNo)
    print(loading_message)
    random_number = random.randint(0,5)
    
    #print(illnessDepNo, random_number)
    rand_list = random.sample(range(18), random_number)
    
    if random_number == 0:
        #print('we got a 0\n')
        illnessesDep = "INSERT INTO `profile_illnesses`(`profile_id`, `illness_id`) VALUES ('{}','{}')".format(illnessDepNo,18)
        try:
            #cursor.execute(illnessesDep)
            file.write(illnessesDep.encode('utf8'))
            file.write(';'.encode('utf8'))
            file.write('\n'.encode('utf8'))
        except:
            pass
    else:
        #print('we got no 0\n')
        if not rand_list:
            break;
        else:
            random_choice = random.choice(rand_list)
            if random_choice == 0:
                illnessesDep2 = "INSERT INTO `profile_illnesses`(`profile_id`, `illness_id`) VALUES ('{}','{}')".format(illnessDepNo,(random_choice+1))

                try:
                    #cursor.execute(illnessesDep2)
                    file.write(illnessesDep2.encode('utf8'))
                    file.write(';'.encode('utf8'))
                    file.write('\n'.encode('utf8'))
                    rand_list.remove(random_choice+1)
                except:
                    pass
            else: 
                illnessesDep3 = "INSERT INTO `profile_illnesses`(`profile_id`, `illness_id`) VALUES ('{}','{}')".format(illnessDepNo,random_choice)

                try:
                    #cursor.execute(illnessesDep3)
                    file.write(illnessesDep3.encode('utf8'))
                    file.write(';'.encode('utf8'))
                    file.write('\n'.encode('utf8'))
                    rand_list.remove(random_choice)
                except:
                    pass
        
print("Successfully added illnesses Dependencies")
#file.close()


ingredients_list=['parsley','salt','pepper','oil','flour','garlic','sugar','water,','onion','olive','chicken','juice','milk','lemon','butter','egg','cheese','wheat','vegetable','vanilla','vinegar','parsley','honey','soy','wine','seeds','celery','rice','cinnamon','tomato','bread','eggs','onions','yeast','leaves','broth','tomatoes','cream','cloves','thyme','peeled','ginger','beans','soda','basil','mushrooms','apple','parmesan','yogurt','stock','bell','oats','sodium','beef','flakes','carrot','oregano','chocolate','cumini_min','paprika','sesame','mustard','spinach','corn','potatoes','coconut','carrots','nutmeg','cilantro','raisins','chili','syrup','peas','peanut','almond','walnuts','canned','lime','leaf','pineapple','margarine','cabbage','cucumber','broccoli','cornstarch','zucchini','coriander','paste','turkey','banana','bake beans','nuts','maple','cheddar','cider','scallions','lettuce','dill']

food_groups=['Vegetables and legumes/beans','Fruit','Grain (cereal) foods, mostly wholegrain and/or high cereal fibre varieties','Lean meats and poultry, fish, eggs & tofu, nuts, seeds and legumes/beans','Milk, yoghurt cheese and/or alternatives']

messuring_units=['tsp','tbsp','cup','pint','qt','gal','lb','pinch','oz', 'ml', 'litre', 'mg', 'g','kg']

# file = open('meal_planner_ingredients.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
print("adding ingredients please wait.....")
for ingredientsNo in range(0, len(ingredients_list)):
    loading_message = 'Ingredient Number:'+' '+str(ingredientsNo)
    print(loading_message)
    
    ingredients = "INSERT INTO `ingredients`(`ingredients_id`, `ingredients_name`, `food_groups`, `measuring_unit`) VALUES ('{}','{}','{}','{}')".format(ingredientsNo,random.choice(ingredients_list), random.choice(food_groups), random.choice(messuring_units))

    try:
        #cursor.execute(ingredients)
        file.write(ingredients.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
    except:
        pass
print("Successfully added ingredients")
#file.close()


# file = open('meal_planner_kitchens.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
print("adding kitchens please wait.....")
for kitchenNo in range(1, MIN+1):
    loading_message = 'kitchenNo Number:'+' '+str(ingredientsNo)
    print(loading_message)

    kitchen = "INSERT INTO `kitchen`(`kitchen_id`, `profile_id`) VALUES ('{}','{}')".format(kitchenNo,kitchenNo)
    try:
        #cursor.execute(kitchen)
        file.write(kitchen.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
    except:
        pass
print("Successfully added Kitchen")
#file.close()


# file = open('meal_planner_kitchen_contents.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
does_kitchen_have_anything = [True,False,True]
print("adding contents of kitchens please wait.....")
faction_numbers=[0,'1/4','1/3','1/2','2/3','3/4']
for containsInKitchen in range(1, (MIN+1)):
    loading_message = 'kitchenNo Number:'+' '+str(containsInKitchen)
    print(loading_message)
    anything_in_kitchen = random.choice(does_kitchen_have_anything)
    if anything_in_kitchen == False:
        #print('we got a 0\n')
        containsInKitchens = "INSERT INTO `contain`(`kitchen_id`, `ingredients_id`, `quantity`) VALUES ('{}','{}', '{}')".format(containsInKitchen,0,'N/A')
        try:
            #cursor.execute(containsInKitchens)
            file.write(containsInKitchens.encode('utf8'))
            file.write(';'.encode('utf8'))
            file.write('\n'.encode('utf8'))
        except:
            pass
    else:
        random_amt_of_ingredients = random.randint(1,len(ingredients_list))
        rand_ingredients = random.sample(range(len(ingredients_list)),random_amt_of_ingredients)
        for x in range(1, random_amt_of_ingredients+1):
            random_frac = random.choice(faction_numbers)
            if random_frac == 0:
                containsInKitchens2 = "INSERT INTO `contain`(`kitchen_id`, `ingredients_id`, `quantity`) VALUES ('{}','{}', '{}')".format(containsInKitchen,rand_ingredients[x-1],random.randint(0,10))
                try:
                    #cursor.execute(containsInKitchens2)
                    file.write(containsInKitchens2.encode('utf8'))
                    file.write(';'.encode('utf8'))
                    file.write('\n'.encode('utf8'))
                except:
                    pass
            else:
                boools = [True, False] 
                to_be_whole_number = random.choice(boools)
                some_num=random.randint(0,20)
                if to_be_whole_number == True:
                    if some_num == 0:
                        containsInKitchens3 = "INSERT INTO `contain`(`kitchen_id`, `ingredients_id`, `quantity`) VALUES ('{}','{}', '{}')".format(containsInKitchen,rand_ingredients[x-1],some_num)
                        try:
                            #cursor.execute(containsInKitchens3)
                            file.write(containsInKitchens3.encode('utf8'))
                            file.write(';'.encode('utf8'))
                            file.write('\n'.encode('utf8'))
                        except:
                            pass
                
            
                    else:
                        new_string = str(some_num) + ' ' + random_frac
                        containsInKitchens4 = "INSERT INTO `contain`(`kitchen_id`, `ingredients_id`, `quantity`) VALUES ('{}','{}', '{}')".format(containsInKitchen,rand_ingredients[x-1],new_string)
                        try:
                            #cursor.execute(containsInKitchens4)
                            file.write(containsInKitchens4.encode('utf8'))
                            file.write(';'.encode('utf8'))
                            file.write('\n'.encode('utf8'))
                        except:
                            pass
                else:
                    if some_num == 0:
                        containsInKitchens5 = "INSERT INTO `contain`(`kitchen_id`, `ingredients_id`, `quantity`) VALUES ('{}','{}', '{}')".format(containsInKitchen,rand_ingredients[x-1],some_num)
                        try:
                            #cursor.execute(containsInKitchens5)
                            file.write(containsInKitchens5.encode('utf8'))
                            file.write(';'.encode('utf8'))
                            file.write('\n'.encode('utf8'))
                        except:
                            pass
                
            
                    else:
                        containsInKitchens6 = "INSERT INTO `contain`(`kitchen_id`, `ingredients_id`, `quantity`) VALUES ('{}','{}', '{}')".format(containsInKitchen,rand_ingredients[x-1],random_frac)
                        try:
                            #cursor.execute(containsInKitchens6)
                            file.write(containsInKitchens6.encode('utf8'))
                            file.write(';'.encode('utf8'))
                            file.write('\n'.encode('utf8'))
                        except:
                            pass

print("Successfully added Contents of kitchen")
#file.close()     


recipe_list = []
recipe_list2 = []
count=0
# file = open('meal_planner_recipes.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
print("adding recipes please wait.....")
hour_or_mins=['Mins', 'Mins','Hrs', 'Mins', 'Mins', 'Mins']
recipe_type=['Breakfast', 'lunch', 'Dinner']

for recipesNo in range(1, MAX+1):
    
    loading_message = 'Recipe Number:'+' '+str(recipesNo)
    
    print(loading_message)
    recipe_img_location = 'Recipe_imgs/food_image.jpg'

    #lines= open('RecipeNames.txt').read().splitlines()
    recipe_name = 'Recipe'+' '+str(recipesNo)

    recipe_list.append(recipesNo)
    recipe_list2.append(recipesNo)
    hrs_mins = random.choice(hour_or_mins)

    if hrs_mins == 'Hrs':

        recipes = "INSERT INTO `recipes`(`recipe_id`, `recipe_name`, `servings`, `prep_time_amt`, `hour_or_mins`, `recipe_type`, `recipe_diet_type` , `calories`, `recipe_img`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(recipesNo,recipe_name, random.randint(1,7),random.randint(1,3), hrs_mins, random.choice(recipe_type),random.choice(diet_list),random.randint(200, 1000), recipe_img_location)
        try:
            #cursor.execute(recipes)
           
            count=count+1
            #recipe_list2.append(recipesNo)
            file.write(recipes.encode('utf8'))
            file.write(';'.encode('utf8'))
            file.write('\n'.encode('utf8'))
        except:
            pass
    else:
        recipes = "INSERT INTO `recipes`(`recipe_id`, `recipe_name`, `servings`, `prep_time_amt`, `hour_or_mins`, `recipe_type`, `recipe_diet_type` , `calories`, `recipe_img`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(recipesNo,recipe_name, random.randint(1,7),random.randint(1,59), hrs_mins, random.choice(recipe_type),random.choice(diet_list),random.randint(200, 1000), recipe_img_location)
        
        try:
            #cursor.execute(recipes2)
            count=count+1
            #recipe_list2.append(recipesNo)
            file.write(recipes.encode('utf8'))
            file.write(';'.encode('utf8'))
            file.write('\n'.encode('utf8'))
        except:
            pass
#file.close()
print("Successfully added recipes")
# print(count)
# print(len(recipe_list))


print("adding recipes instructions please wait.....")
# file = open('meal_planner_recipes_instructions.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
count=1
for recipeNo in range(1, MAX+1):
    loading_message = 'Recipe Number:'+' '+str(recipeNo)
    print(loading_message)
    random_directNo = random.randint(3,15)
    for directionNo in range(1, random_directNo):
        directions = "INSERT INTO `instructions`(`instructions_id`, `recipe_id`, `direction`) VALUES ('{}','{}','{}')".format(count,recipeNo, fake.sentence())
        try:
            #cursor.execute(direcions)
            file.write(directions.encode('utf8'))
            file.write(';'.encode('utf8'))
            file.write('\n'.encode('utf8'))
            count=count+1
        except:
            pass
            
print("Successfully added recipes instructions")
#file.close()



# file = open('meal_planner_comprise.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
print("adding recipes ingredients please wait.....")

for recipeIngredNo in range(1, MAX+1):
    
    loading_message = 'Recipe Number:'+' '+str(recipeIngredNo)
    print(loading_message)


    random_frac = random.choice(faction_numbers)
    random_ingediant_amt=random.randint(5,25)
    rand_selected_ingre =random.sample(range(len(ingredients_list)),random_ingediant_amt)
    #print(rand_selected_ingre
    
    if random_frac == 0:
        for x in range (1, len(rand_selected_ingre)):
            comp_instruction = "INSERT INTO `comprise`(`recipe_id`, `ingredients_id`, `recipe_qunt`) VALUES ('{}','{}','{}')".format(recipeIngredNo,rand_selected_ingre[x], random.randint(1,25))
            #print(comp_instruction)
            try:
                #cursor.execute(comp_instruction)
                file.write(comp_instruction.encode('utf8'))
                file.write(';'.encode('utf8'))
                file.write('\n'.encode('utf8'))
            except:
                pass
    else:
        to_be_whole_number = [True,False]
        if random.choice(to_be_whole_number) == False:
            for x in range (1, len(rand_selected_ingre)):
                #print(recipeIngredNo, rand_selected_ingre[x])
                new_string = str(random.randint(1,25)) + ' ' + random_frac
                comp_instruction2 = "INSERT INTO `comprise`(`recipe_id`, `ingredients_id`, `recipe_qunt`) VALUES ('{}','{}','{}')".format(recipeIngredNo,rand_selected_ingre[x], new_string )
                #print(comp_instruction2)
                try:
                    #cursor.execute(comp_instruction2)
                    file.write(comp_instruction2.encode('utf8'))
                    file.write(';'.encode('utf8'))
                    file.write('\n'.encode('utf8'))
                except:
                    pass
        else:
            for x in range (1, len(rand_selected_ingre)):
                #print(recipeIngredNo, rand_selected_ingre[x])
                comp_instruction3 = "INSERT INTO `comprise`(`recipe_id`, `ingredients_id`, `recipe_qunt`) VALUES ('{}','{}','{}')".format(recipeIngredNo,rand_selected_ingre[x], random_frac )
                #print(comp_instruction3)
                try:
                    #cursor.execute(comp_instruction3)
                    file.write(comp_instruction3.encode('utf8'))
                    file.write(';'.encode('utf8'))
                    file.write('\n'.encode('utf8'))
                except:
                    pass
print("Successfully recipes ingredients")
#file.close()


# file = open('meal_planner_creations.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
print("adding recipes creations please wait.....")
# print(len(recipe_list))               
for add_recipe in range(0, MAX):

    loading_message = 'Count:'+' '+str(add_recipe)
    print(loading_message)
    if not recipe_list:
        break 
    else:
        rand_recipe_id=random.choice(recipe_list)
        add_recipes = "INSERT INTO `add_recipe`(`username`, `recipe_id`, `creation_date`) VALUES ('{}','{}','{}')".format(random.choice(username_list),rand_recipe_id, fake.date())
        try:
            #cursor.execute(add_recipes)
            file.write(add_recipes.encode('utf8'))
            file.write(';'.encode('utf8'))
            file.write('\n'.encode('utf8'))
            recipe_list.remove(rand_recipe_id)
        except:
            pass
#print(len(recipe_list))
print("Successfully added recipes creations")                  
#file.close()

meal_list=[]
meal_list2=[]
print("adding meals  please wait.....")
# file = open('meal_planner_meals.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
for mealNo in range(1, DEP+1):
    
    loading_message = 'Meal No.:'+' '+str(mealNo)
    print(loading_message)

    meal_list.append(mealNo)
    meal_list2.append(mealNo)
    lines= open('RecipeNames.txt').read().splitlines()
    rand_meal_name =random.choice(lines)
    meals = "INSERT INTO `meals`(`meal_id`, `meal_name`, `meal_type`, `calories`) VALUES ('{}','{}','{}','{}')".format(mealNo, rand_meal_name, random.choice(recipe_type), random.randint(100,10000))
    try:
        #cursor.execute(meals)
        file.write(meals.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
    except:
        pass

print("Successfully added meals")
#file.close()

# file = open('meal_planner_creates.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
print("adding meal dependencies please wait.....")
for created_meals in range(1, DEP+1):

    loading_message  = 'Meal Dep No.:'+' '+str(created_meals)
    print(loading_message)
    
    random_meal_id = random.choice(meal_list)
    random_recipe = random.choice(recipe_list2)
    meal_list.remove(random_meal_id)

    meal_plans = "INSERT INTO `creates`(`meal_id`, `recipe_id`) VALUES ('{}','{}')".format(random_meal_id, random_recipe)

    try:
        #cursor.execute(meal_plans)
        file.write(meal_plans.encode('utf8'))
        file.write(';'.encode('utf8'))
        file.write('\n'.encode('utf8'))
        
    except:
        pass

print("Successfully added meal dependencies")
# file.close()


# file = open('meal_planner_meal_plan.sql','w') 
# file.write('use meal_planner;')
# file.write('\n')
# print("adding consist_of dependencies please wait.....")
# for consist_ofNo in range(1, DEP+1):

#     loading_message = 'Consist_of Dep No.:'+' '+str(consist_ofNo)
#     print(loading_message)
    
#     random_amt=random.randint(1,4)
#     rand_meal_sample = random.sample(range(len(meal_list2)), random_amt)

#     for x in range(1, random_amt):
#         consist_of_table = "INSERT INTO `meal_plan`(`plan_id`, `meal_id`) VALUES ('{}','{}')".format(consist_ofNo,rand_meal_sample[x])
#         try:
#             #cursor.execute(consist_of_table)
#             file.write(consist_of_table.encode('utf8'))
#             file.write(';'.encode('utf8'))
#             file.write('\n'.encode('utf8'))
#         except:
#             pass
# print("Successfully added consist_of dependencies")
#file.close()



# #Close the cursor
# cursor.close()
# # Commit the transaction
# database.commit()
# # Close the database connection
# database.close()
print("Database has been successfully populated....")
