# Nutriton Guide by Jadyn Renk
### Video Demo:  https://youtu.be/2-jJXwB3Mss
### Description:

My project is a nutritional guide. It will take in your weight,height, and goal and converts it to let
you know your BMI, how many grams of protein you need, and a guide to calories. It takes user input in
multiple formats and converts it all so the program will use it correctly.

First the re library is imported.Then the main function is defined by the def main():. It first prints
out “Welcome to your nutrition guide! First we need some information.” Then it opens up a While True,
try and except loop. It tries to gather all the information and input and if there are errors it
prints “Oops you entered your info wrong” and then restarts the user from the first input. The user
is first prompted to enter their weight in pounds. It is then sent to the check_weight function to
check for user error.

Check weight function:
The check_weight function checks and cleans the user's input in multiple ways so the program can use
the input. It returns the value as a float. If the input isn't in the correct format it will return a
raise value error for the main function to handle.
The check_weight function takes in the weight as a variable. It then uses an
if statement and sets a variable called “match” and uses a := (walrus operator) to also ask if the
input matches the re.search. It checks over all the full input. First we have the parentheses and an r
to tell the python interpreter to treat it as a raw file. It then has open quotes and a “^” to start
checking from the beginning. It checks that the weight is in all numbers and isn’t larger than 3
digits and that the first number is between 1-9 and the other 2 are between 0-9. It also has an
optional space and optional lb for if the user puts that, it uses $ to match to the end and closes
quotes. The numbers are set into group 1 and if it matches it returns the float of group 1.If there is
a . in the weight then it returns the float of the weight. If neither of those work it raises a value
error. Then the program continues and promts the user for their height. It then sends it to the
check_height function

Check Height function:
The height_check function takes in the users height in multiple formats and finds the height in
inches. And returns the height as a float to the main. If the input is incorrectly formatted it raises a
value error and returns to the main.
The function takes in the height as a variable. It has a few if statements to check for different inputs.
The first one checks for the input being entered as inches. It uses the a variable called match and the
walrus operator to use to re.seach to search the input. It starts checking at thebeginning and checks that
the first number is in between 1-9 and the second between 0-9. It puts those in a group and checks for the
optional “in” and uses the $ to check all the way to the end. It also ignores the case. If it matches it
returns the first group as a float. If there is a “ ‘ “ in the height input it splits the height into ft
and inches on the ‘. It turns both the inches and ft into floats. Next the ft is multiplied by 12 and is
added together with the inches and set to the height. Then that is returned to the main as a float. Next
it checks for an input that's formatted like 5ft 6in. It first uses an if statement to check both ft and
in are in height or both foot and inches. Then it splits height into the ft and inch. Then it goes on to
split both the ft and inch to get rid of the letters. Then both are turned into floats and ft is
multiplied by 12 and then added to inches to get the height and then the height is returned. Then it has
one more if statement to check if height just has “ft” or “foot” in it. It uses the same if  statement
and match variable with re.search. It also starts checking at the beginning of the input. It checks that
the first number is between 1-9 and there is an optional space and then optional “ft”. It ignores the case
and the numbers are in a group. It sets the group to a variable called ft and turns it into a float. Then
it is multiplied by 12 and set to height and the height is returned. If not it raises a value error.
If the input doesn't work for any of those it raises a value error for the main to handle.

The Goal function:
Next the main function prompts the user for its goal. It gives three options. Gain body mass,loose weight, or
gain strength. Then sends to the goal function to be checked.The goal function just checks that the input
is one of the three options and if its not it re prompts the user. To do this I use the while true, try
loop. I then use an if statement for each of the three options. It also turns it into all lower case. If
the goal is gain body mass the function returns “You should be in a caloric surplus, eat 10% more calories
than you are currently”. If the goal is loose weight it returns “You should be in caloric deficit, eat 10%
less calories than you are currently”. Lastly if the goal is to gain strength then it returns “You should
be in a caloric surplus, eat 10% more than you are currently and lean foods only.”. If the goal doesn't
match to any one of those three it uses the else to print “Pick one of the options” and re prompts them
for the goal again. They stay in that loop until one of the options are entered correctly.

The convert protein function:
The main function then calls the convert_protein function and sends the weight variable into it.Then saves
that in a variable named protein. The convert_protien function is just there to find how much protein the
user should be eating per day. It takes in the weight variable and multiples the weight by 1.5 and puts it
into the protein variable. Then it returns the protein variable.

The convert bmi function:
Next the main function calls the covert_bmi function and sends both of the height and weight variables into
it. The function opens up a while True, try and except loop. Then it tries to divide the weight by the
height squared all multiplied by 703 and sets it equal to the bmi variable and returns it. If it can’t do
the equation it raises a value error for the main function to handle

Now the main function finally has all the information it needs! It begins printing the information for the
user. First a blank line is printed. Then it prints “Nutrition guide: “. The users weight it printed out
first and then their height in case they entered their info wrong they can clearly see. Then it prints an f
string saying “You need at least __ grams of protein a day” and prints out the amount of protein they need
in the blank space. Then it prints another f string “Your bmi is approximately __” and prints their bmi
within that. Lastly it prints the result from their goal. Then the loop breaks. If any value error is
raised within any of the functions it prints “Oops you entered in your info wrong, try again!” and
continues back to the start of the inputs. This will loop until everything is entered correctly. That is
the end of the program!

There were multiple design choices I debated on throughout coding the assignment. I first wasn't going to
allow so many different types of inputs for the height and weight, however upon getting my family members
to test my program they were being caught in the main function loop because the input was so sensitive to
spaces and letters. As I learned about regular expressions I decided to implement the re library. This
helped the functionality so much. I also debated if I should split things up into so many functions or if I
should just check the height and weight in the main function. As I added more and more checks to the height
and weight it only made sense to split them up into the multiple functions. I also kept the print lines in
the main function separate because it helped me to see each thing clearly and focus on things individually.

The other file I have included is the required test_projecy.py file. This runs through checks of the
convert bmi function, the convert protein function, and the goal function. It checks that they correctly
return a value based on the input. It also checks that the convert bmi and convert protein can take values
with a decimal in them!







