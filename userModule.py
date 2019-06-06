# For an online store, this would be a minimum of 6 possible menus that provide functionality such as purchasing and creating reports.

import pprint
import Data
choice =0
pp = pprint.PrettyPrinter(indent=3)


#print(type(textbooks))

def welcomeMessage():
  #for i in range(20):
  print("\n\n", 20 * "<*>-")
  print( 20*"~~~~")

  print(10*" ", "Welcome to Iryna's School Supply store!");
  print( 20*"~~~~")
  print(20 * "<*>-")
  #print("\nLet us know what brings you here. Please choose one of the following\n")


def convertCurr():
  choice = int(input("\nWould you like to convert your US dollars? \n1. Yes \n2. Not right now \n\n"))
  while(choice >=1 and choice <=2 ):
    if(choice == 1):
      currentInput = int(input("Tell us how many US dollars you would like to conver to bitcoins \n"))
      bitcoins = convertCurrency(currentInput)
      print("\nYou have ", bitcoins, " in your budget.")
      print("\n-------------------------------------\n")
      break
    elif choice == 2:
      print("\nNo worries, you will be able to do it during the payment process. Just remmember the prices are in bitcoins")
      break
    else:
      print("\nOnly 1(Yes) and 2(No) are valid choices")
      #choice = input("Would you like to convert your US dollars? \n1. Yes \n2. Not right now \n")


from itertools import chain

def printSelection():
  print("\nLet us know what brings you here. Please choose one of the following\n")
  print("Choolse from one of the following: \n1. Textbooks \n2. Stationary \n3. Pens and pensils \n4. Laptops \n5. Markers and Highlighters \n6. Devices and printers \n7. Paper and printing supplies \n8. All electronics \n9. All stationary & writing supplies \n10. All departments \n0.Exit \n\n")



def makeSelection():
  #choice = printSelection()
  choice = int(input("Please select one: "))
  while choice !=0:
    switcher = {
      1: Data.getTextbooks(),#show set of textbooks

      2: Data.getStationary(), #show set of Stationary

      3: Data.getPensAndPensils(), #show set of Pends and pensils

      4: Data.getLaptops(),#show set of Laptops

      5: Data.getMarkersAndHighlighters(),#show set of markers and highlighters

      6: Data.getDevicesAndPrinters(),#show set of computers and printers

      7: Data.getPaperAndPrintingSupps(),#show  set of paper and printing supplies

      8: Data.getElectronics(),#show a Union of computers and laptops

      9: Data.getAllStationary(),#union of Stationary and pens and pencils
      10: Data.getEverything(),

      0: set({})
    }

    #if switcher.get(choice) != None:
    return switcher.get(choice)
    #else:
     # return set({})


#import sys
#sys.setrecursionlimit(1500)
def convertCurrency(decimal):
  # Function to print binary number for the input decimal using recursion
  if decimal==0:
    return ''
  else:
    return convertCurrency(decimal//2) + str(decimal%2)


#--------LOGGING IN, ENCRYPTION AND CYPHER---
#What I am doing is that initially I am assigning -1 to all the indexes in the list telling that this particular state has never been visited. Once, I visit a particular state, I store its solution in the arr at that index. And if the solution state has been visited and is encountered again, I straight away return the solution possible at that index without recursing further on it.

n=26
fibonacchi = []

def fibonRecursive(n):

  if fibonacchi[n] != -1:
    return fibonacchi[n]
  if n == 0:
    fibonacchi[0] = 0
    return 0 #base case 1
  elif n == 1:
    fibonacchi[1] = 1;
    return 1  #base case 2
  else:
    fibonacchi[n] = fibonRecursive(n-1) + fibonRecursive(n-2);
    return fibonacchi[n];



for i in range(n+1):
  fibonacchi.append(-1);
fibonRecursive(n)
#print("fibonacchi recursive ", fibonacchi)

#login = input("Please enter your user name: ")#password = input("Enter you passowd: ")


#call encrypt password(password)
#fibonacchi = []

def storeInAlphabet():

  alphabet = []
  for n in range(97, 123):
    alphabet.append(chr(n))
  #print(alphabet)
  return alphabet

def createCipher():

  cipher = {};

  alphabet = storeInAlphabet()
  #print("Alphabet ", alphabet)
  cipher = dict(zip(alphabet, fibonacchi))
  #print (cipher)
  return cipher
#print("Cypher ",encryptPass())

import pandas as pd
cipher = createCipher()

df = pd.DataFrame.from_dict(cipher, orient='index', columns=['Letter'])

#print(df)

#encodes the password
import numpy as np
def encode(password):

  encodedWord = ""
  cipher = createCipher()
  digitArray = []
  for i in password:
    if i in cipher.keys():
      digitArray.append(cipher.get(i))
  print("The encoded numbers are: ")
  #testing the coded characters
  print(digitArray)
  codeArr= np.array(digitArray)
  product = np.prod(codeArr)
  return product
  #return digitArray


#-------------CART OPERATIONS--------------
cart = set({})
#Displaying the list of products
#Displaying shopping Cart .
def addToCart(item):
 # myCart = {}
  cart.add(item)
  #return cart


#create combinations of similar items from other department
from itertools import combinations
import random
#Returns a list of suggested products
def showSuggestions():
  #create combinations of everythig set
  result = combinations(Data.getEverything(), 5)
  #randomly print one combination to the user
  print("\n====================================\n")
  print("\n ~~~~~~~People also bought: ~~~~~~~~\n ")
  #print("Number of combinations", len(list(result)))
  #change hardcoded ma to the length of combinations
  randomSuggestion = random.randint(1,1533939-1)
  #print(list(result)[randomSuggestion])
  #for l in list(result):
	 # print(l)

  return list(result)[randomSuggestion]

def offerLottery():
  print("\n==========================================\n")
  print("**********Congratulations! *************\nToday you get a chance to win one free item from our online store.\n\nWould you like to see what the each item probability of winning is before your play the lottery? \nPlease enter Yes or No\n")
  choice = int(input("\n1. Yes\n2. No \n\n"))
  while(choice == None):
    if choice == 1:
      #show calculated probabilities
      print("The probability of winning each item is: \n")
      calcProbabils()
    if choice == 2:
      print("It's OK, You did not miss much =)")
      checkOutCart()
    else:
      print("Valid selections are 1  and 2. Please enter one of them")
      #userModule.checkOutCart()

import random
#Generates permutations of the usernames
from itertools import permutations


def createUserName():
  print("\n\n~~~~~ We will create a user name for you ~~~~~\n")
  firstName = str(input("Please enter yoru user name: "))
  lastName = str(input("\nPlease enter yoru first name: "))
  superHero = str(input("\nWhat is your favourite superhero? "))
  #later add the number to the permutations of the username
  numPermuts = permutations(range(50))

  userName = {firstName, lastName, superHero}

  userNamesPermuts = list(permutations(userName))
  #print("Length pf permutations", len(list(userNamesPermuts)))
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  print("These are possible user names permutations  for you: \n")
  print("Please choose one: \n")

  count = 0
  for i in userNamesPermuts:
    count += 1
    print(count, i)
  #permutsList = list(userNamesPermuts)
  #print("Length of permutations", len(userNamesPermuts))
  choice = int(input("\nYour choice: \n"))
  userNameWords = userNamesPermuts[choice - 1]
  print(userNameWords)
  userName = ""
  for word in userNameWords:
    userName += word
    userName += str(random.randint(0, 50))

  print("\nYour user name will be :  ")
  print(40 * "*")
  print("*", 7*" ", userName, 7*" ", "*")
  print(40 * "*")
  #print("UserNameList", userNamesList)


def calcProbabils():
#calculate each probabilty in current inventory
  inventory = Data.getInventory()
  totalQuantity = sum(inventory.values())
  #print(totalQuantity) - test
  print("\n~~~~Probabilities to win each item on sale are~~~~~\n")
  print(70 * "-")
  for i in inventory:
    prob = str(round(inventory.get(i)/totalQuantity, 2)* 100) + "%"

    print(i, " -- ", prob)
    #pp.pprint(i)
    #pp.pprint(prob)

#retur void just removes
def removeFromCart(item):
  cart.remove(item)



#category = set(makeSelection())

def addToCart():
  inp = input(str("Please enter items you want to add to your cart separated by come and one space \n\n"))
  category = set(makeSelection())
  items  = list(map(str, inp.split(", ")))
  everything = Data.getEverything()

  #print("Items", items)
  #loop through items
  for item in items:
    if item in category:
      cart.add(item);
    else:
      if item in everything:
        print("This item is in other department but we still can add it to your cart ")
        cart.add(item)
      else:
        print("Incorrect item")
      #substract from the inventory
  print("\n~~~~~~~~~~ Your cart: ~~~~~~~~~~~~\n", cart)
  print(40*"~")


#def checkOutCart():
 # print("\n Please kindly review your cart: \n\n")

  #pp.pprint(cart)
  #print("\n==========================================\n")


#checkOutCart()
def createPassword():
  password = str(input("Please enter your password and we will encode it: "))
  #encode(password)
  print("\nYour encoded password is: ", encode(password))

def checkOut():
  isReady = int(input("Are you ready to to proceed further? Please enter 1 or 2:   \n1. Yes \n2. No\n"))

  if isReady == 1:
    createUserName()
    createPassword()
  else:
    welcomeMessage()

#-------------------------
def showItemsInCateg():
  #category = set(userModule.makeSelection())
  category = set(makeSelection())
  print("\nHere is what store has to offer you in the section you chose: \n")
  pp.pprint(set(category))
#-------------------------


def store():
  if makeSelection() is not None:
    showItemsInCateg()
    addToCart()
    #checkOutCart()
    pp.pprint(showSuggestions())
    checkOut()
    offerLottery()
    print("\n==========================================\n")

  else:
    print("~~~~~~~~~~~~ Goodbye! ~~~~~~~~~~~~~~~\n")
    print("~~~ If you want to come back, please press Run button ~~~\n")
    print(80 * "=")
