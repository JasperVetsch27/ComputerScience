#2 functions
print()
input()  # /n is called am escape character

#Variables
#Syntax
# <name> = <value>
x = 5

#Snake naming convention - all lowercase, underscore for spaces
#CONCISE: Short and descriptive 
username = "Jasper" #Define
fav_animal = "Cat"  #Define
total_poptarts = 12 #Define integer
percent_complete = 312.23   #Defime float
is_cool = True          #Define boolean
first_letter = "c"       #Define Character

username = "Vetsch" #Reassign


#Arithmetic Operators 
# +   -   *   ?   **  %   //
print(4 + 4)     #8
print("4" + "4") #44
print("cat" + "dog")    #catdog
print("cat" * 3)    #catcatcat
print("cat" + 3)     #ERROR

#Make some working programs 
#1. add two numbe rusing input
x = int(input("What is x?\n"))   #Input() always returns a string
y = int(input("What is y?\n"))   #Even if you type in a number 
print(x + y)

#1. Converts celcius to farenheight
temp_celcius = int(input("What is the temperature in Celcius?\n>)"))
temp_farenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + " degrees C equals " + temp_farenheight + " degrees F")

#Some conversion fucntions
str()
int()
float()
bin()
bool()

#The stuff that goes between the parenthesis is aclled PARAMETERS
#Parameters are the values that the function needs to run


#Functions 
#Fucntions are a lot like variables 
#They have names
#They can be recalled from memory by calling their name
#Sore informtaion 
#Variables store values, functions store code 
def potato():   #Def keyword + name + () + :
    print("potato") #Lines indented underneath are "inside" the funtion 

#Functions are not ran when they are defined 
#They must be called by their name to run
potato()    #Every function call needs open and closed parethesis
            #Even if it has no parameters

def jump(how_high):
    print("You jumped " + how_high +  " inches!")

jump(14)

def make_a_word(a, b, c, d, e, f, g, h, i, j, k):
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("z", "a", "c", "k", "o", "s", "o", "w", "s", "k", "i")

#Funations can have many many lines
def top_five_games():
    print("1. Elden Ring")
    print("2. Shadow of the the Colossus")
    print("3. Minecraft")
    print("4. Diablo 3")
    print("5. Gran Turismo 7")

#Scope: global and Local Variabales!!
#Scope refers to the context in which the variable was defined 
#GLOBAL - defined at no indentaion level 
#LOCAL - Define inside of a funation 

#Global variables can be used anywhere
todd = "Cool guy"   #Global variable- no indenation level 

def my_funtion():
    smith = "Not cool guy" #Local variable- define in a funation
    tood = "strange guy"   #Local variable even though it has the same name
    print(todd)            #prints the local variable todd
    #When you call a varaibale in a funtion 
    #It searches local variables first, then global variables

#If you want to reassign a golbal variable insdie of function
todd = "cool guy"
def my_function2():     #In this funation, whenever I call todd
    global todd            #I mean the gobal todd, not the local
    todd = "strange guy"    #Reassign todd - global 
    print(todd)             #Print todd - global

#Return functions
#Funtions can also return vlaues
#The value that is retured is sent back to where the funtion was called
#This is very similar to how a variable works
#The funtion does its work and returns an answer back
def add2(x, y):
    return x + y    #returns the sum of x and y to where the funtion was called


answer = add2(2, 10)
print(answer)