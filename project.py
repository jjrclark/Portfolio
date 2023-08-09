# project.py
# Jadyn Renk

import re

def main(): # defines the main function
    print("Welcome to your nutrition guide! First we need some information!")
    while True: # opens a loop
        try:
            weight = weight_check(input("Weight in pounds: ")) # sends the weight to the check weight function
            height = height_check(input("Height: ")) # sends the height to the check height function
            goal = input("Gain body mass, loose weight, or gain strength? ") # gets their goal
            goal = goals(goal)# verifies they enter one of the options
            protein = convert_protein(weight) # converts the protein
            bmi = convert_bmi(weight,height) # converts the bmi
            #prints out all the nutrition information
            print()
            print("Nutrition guide:")
            print(weight,"Pounds")
            print(height,"in")
            print(f"You need at least {protein} grams of protein a day")
            print(f"Your bmi is approximately {bmi}")
            print(goal)
            break
        except ValueError: # if any of the functions rasies an error it will print and repromt the user
            print("Oops you entered in your info wrong, try again!")
            continue


def weight_check(weight):
    # checking that the weight is at least 2 characters and within the right range and cleans it if they enter letters
    if matches := re.search(r"^([1-9][0-9]?[0-9]?)? ??(lb)?$",weight, re.IGNORECASE):
            return float(matches.group(1)) # returns the weight as a float
    if "." in weight: # if theres a deciaml
            return float(weight) # retuns as a float
    else:
        raise ValueError # if not it raises a value error


def height_check(height):
    # chceks if the height is in inches
    if matches := re.search(r"^([(1-9][0-9])?(in)?$",height, re.IGNORECASE):
        return float(matches.group(1)) # if so it returns as a float
    if "'" in height: # if the input is in the format 5'2
        ft,inches = height.split("'") # it will split
        inches = int(inches) # turn both sides into floats
        ft = int(ft)
        ft = ft * 12 # then turn the ft into inches
        height = ft + inches # can add the inches together
        return float(height) # and return as as float
    if "ft" and "in" or "foot" and "inches" in height: # if they enter with letters
        ft,inch= height.split(" ") # it will sepertate each part to get the numbers alone
        ft,extra = ft.split("f")
        inch,extra = inch.split("i")
        ft = float(ft) # turn them into a float
        ft = ft * 12 # then turn thr ft into inches
        inch = float(inch)
        height = ft + inch # add inches togther
        return(height) # then return the height
    if "ft" or "foot" in height: # if the height is just in feet
        # it checks the format it got entered in as
        if matches := re.search(r"^([1-9])? ?(ft)? ?$",height, re.IGNORECASE):
            ft = (matches.group(1)) # grabs just the numbers
            ft = float(ft) # turns it into a float
            height = ft * 12 # turns into inches
            return height # returns the height
        else:
            raise ValueError # else it raises an error
    else:
       raise ValueError # then if non of them work it raises a value error


def convert_bmi(weight,height):
    while True: # opsna a loop and tries to calculate th bmi
        try:
            bmi = round(weight / (height*height) * 703)
            return bmi # returns the bmi
        except:
            raise ValueError # if not it raises a value error


def goals(goal):
    while True: # opens a loop
        try: # goes through all three options and checks the input is one of them
            if goal.lower() == ("gain body mass"): #
                return("You should be in a caloric surplus, eat 10% more calories than you are currently")
            if goal.lower() == ("loose weight"):
                return("You should be in a caloric deficit, eat 10% less calories than you are currently")
            if goal.lower() == ("gain strength"):
                return("You should be in a caloric surplus, eat 10% more calories and lean foods only")
            else: # if not it will reprompt the user
                print("Pick one of the options")
                goal = input("Gain body mass,loose weight, or gain strength? ")
                continue
        except:
            break


def convert_protein(weight):
    protein = weight * 1.5 # takes in the weight and calculates the protein and returns it
    return protein


if __name__ == "__main__":
    main()