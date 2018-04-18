DROP PROCEDURE IF EXISTS Recipe;
DROP PROCEDURE IF EXISTS add_Recipe;
DROP PROCEDURE IF EXISTS Comprise;
DROP PROCEDURE IF EXISTS Instruction;
DROP PROCEDURE IF EXISTS Register;
DROP PROCEDURE IF EXISTS add_account;
DROP PROCEDURE IF EXISTS GetRecipeById;
DROP PROCEDURE IF EXISTS GetRecipeInstruction;
DROP PROCEDURE IF EXISTS recipeingredient;
DROP PROCEDURE IF EXISTS GetCreationDate;

DELIMITER //
CREATE PROCEDURE Recipe(IN recipe_name varchar(300), servings int, prep_time_amt int, hour_or_mins varchar(20), recipe_type varchar(20), recipe_diet_type varchar(100), calories int, recipe_img varchar(300))
BEGIN INSERT INTO recipes(recipe_name, servings, prep_time_amt, hour_or_mins, recipe_type, recipe_diet_type, calories, recipe_img) VALUES(recipe_name, servings, prep_time_amt, hour_or_mins, recipe_type, recipe_diet_type, calories, recipe_img);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE add_Recipe(IN username varchar(20), recipe_id int, creation_date Date)
BEGIN INSERT INTO add_recipe(username, recipe_id, creation_date) VALUES(username, recipe_id, creation_date);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE Comprise(IN recipe_id int, ingredients_id int, recipe_qunt varchar(20))
BEGIN INSERT INTO comprise(recipe_id, ingredients_id, recipe_qunt) VALUES(recipe_id, ingredients_id, recipe_qunt);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE Instruction(IN recipe_id int, direction varchar(100))
BEGIN INSERT INTO instructions(recipe_id, direction) VALUES(recipe_id, direction);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE add_account(IN username varchar(255), pword varchar(255))
BEGIN INSERT INTO account(username, pword) VALUES(username, pword);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE Register(IN username varchar(255), fname varchar(255), lname varchar(255), dob DATE, email varchar(320), diet_choice varchar(50))
BEGIN INSERT INTO user_profile(username, fname, lname, dob, email, diet_choice) VALUES(username, fname, lname, dob, email, diet_choice);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetRecipeById(IN recipe_id1 int)
BEGIN (
SELECT * FROM recipes WHERE recipe_id=recipe_id1
);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetRecipeInstruction(IN recipe_id1 int)
BEGIN (
SELECT direction FROM instructions WHERE recipe_id=recipe_id1
ORDER BY instructions_id ASC
);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetCreationDate(IN recipe_id1 int)
BEGIN (
SELECT creation_date FROM add_recipe WHERE recipe_id=recipe_id1
);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE recipeingredient (IN recipe_id1 int )
BEGIN (
SELECT comprise.recipe_qunt AS unit, ingredients.measuring_unit AS measurement, ingredients.ingredients_name AS ingredient
FROM comprise JOIN ingredients
ON comprise.ingredients_id = ingredients.ingredients_id
WHERE comprise.recipe_id  = recipe_id1
);
END //
DELIMITER ;