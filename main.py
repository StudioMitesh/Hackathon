print("Hello! HackGwinnett 2021 - Mitesh Shah, Sanjar Zaman, and Sohum Trivedi\n")
print("Weight Management and Healthy Habits Program!\n")
print("Many people around the world have eating disorders that affect their diets detrimentally.\nThis causes many people to go to unnecessary doctor visits due to them not being aware about proper nutrition.\nWe created a program to help people know how to lose/gain weight safely, without hurting their bodies.\nDue to many factors at play related to healthy nutrition, a lot of the applications or\nprograms related to our idea are either not specific enough in their recommenation or not accurate enough.\nThis is why we are making our own program to build up and improve on this idea.\n")

def bmr(gen, w, h, a):
    if(gen == "male"):
        bmr = 13.397*w + 4.799*h - 5.677*a + 88.362
    elif(gen == "female"):
        bmr = 9.247*w + 3.098*h - 4.330*a + 447.593
    return bmr

def redoint(prompt):
  while True:
    try:
      inp = int(input(prompt))
      if(inp > 0):
        break
      else:
        print("That's not a valid option!")
        continue
    except:
      print("That's not a valid option!")
  return inp

def redolist(prompt, wanted):
  go = True
  inp = 0
  while go == True:
    inp = input(prompt)
    if(inp in wanted):
      go = False
    else:
      continue
  return inp

def redo(prompt):
  while True:
    try:
      inp = int(input(prompt))
      if(inp > 0 and inp < 7):
        break
      else:
        print("That's not a valid option!")
        continue
    except:
      print("That's not a valid option!")
  return inp

genders = ["male", "female"]
gender = redolist("Enter your gender (male or female): ", genders)
weight= float(redoint("What is your weight (in lbs): "))
height = float(redoint("What is your height (in inches): "))
age = int(redoint("What is your age: "))

weightkg = weight/2.205
heightcm = height*2.54

print(" \n1:Sedentary: little or no exercise \n2:Exercise 1-3 times/week \n3:Exercise 4-5 times/week \n4:Daily exercise or intense exercise 3-4 times/week \n5:Intense exercise 6-7 times/week \n6:Very intense exercise daily, or physical job	\n")

exercise = redo("Of the options above, what is your activity level (input the number): ")

#main
mybmr = bmr(gender, weightkg, heightcm, age)


if(exercise == 1):
    mybmr *= 1.2
elif(exercise == 2):
    mybmr *= 1.375
elif(exercise == 3):
    mybmr *= 1.465
elif(exercise == 4):
    mybmr *= 1.55
elif(exercise == 5):
    mybmr *= 1.725
elif(exercise == 6):
    mybmr *= 1.9

mybmr = round(mybmr, ndigits=1)

print("Your Basal Metobolic Rate (BMR) is: "+ str(mybmr)+"\n")

#https://www.checkyourhealth.org/eat-healthy/cal_calculator.php

goalgo = True
goal = int(redoint("What is your goal weight: "))
while goalgo == True:
    timeToLose = int(redoint("In how many days would you like to be this weight: "))

    weightToChange = goal - weight

    if(weightToChange>=0):
        #gain weight
        if ((weightToChange/(timeToLose))>0.42):
            print(" This is an unhealthy rate to gain weight please increase the time. \n")
        else:     
            mybmr += (weightToChange*3500)/timeToLose
            goalgo = False
    elif(weightToChange<0):
        #lose weight
        if ((weightToChange/(timeToLose))<-0.42):
            print(" This is an unhealthy rate to lose weight please increase the time. \n")
        else: 
            mybmr += (weightToChange*3500)/timeToLose
            goalgo = False

mybmr = round(mybmr, ndigits=1)   


print("\nWe reccomend that you eat " + str(mybmr)+" calories to reach your goal weight in your goal time.\n")


carbs = round(float(mybmr)/8, ndigits=2)
fats = round(float(mybmr)/45, ndigits=2)
proteins = round(float(mybmr)*(3/40), ndigits=2)

print("We recommend you to eat: " + str(carbs) + " grams of carbohydrates in your diet per day.\n")
print("We recommend you to eat: " + str(fats) + " grams of fat in your diet per day.\n")
print("We recommend you to eat: " + str(proteins) + " grams of protein in your diet per day.\n\n")

print("To increase the amount of calories you should eat, you could decide to work out more.\n ")

WantToEat=int(redoint("How many more calories would you like to burn with exercise: "))

print("\nHere are some examples of exercises you can do to burn " + str(WantToEat)+" Calories: ")
print("\tYou could run: "+ str(round(WantToEat/(weight*0.75), ndigits=1)) +" miles at 6 miles per hour to burn the " + str(WantToEat) + " calories")

print("\tOr you could swim: "+ str(round(WantToEat/(weight*2),ndigits=1)) +" miles at a moderate pace to burn the " + str(WantToEat) + " calories")

print("\tYou could even just walk: "+ str(round(WantToEat/(weight*.4), ndigits=1)) +" miles to burn the " + str(WantToEat) + " calories")

print("\nCongratulations on embarking on your journey to a healthier life.\nWe hope you learned something about your body and\nhave a better plan for eating healthy and acheiving your goals!")

#https://replit.com/join/pibrkhrzke-str1v3