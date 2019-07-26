"""
TheLoadedTrader.py
Using Python 3.7
By Lance Narbaitz

This program simulates a conversation with a trader who
deals in progress indicators
"""

import time

#Intro
print("\nYou've been traveling for days.")

print("\nYou can finally see the castle in the distance but it doesn't seem like ")
print("you've gotten any closer in several hours.")

print("\nYou think to yourself \"If only there was some way to tell how ")
print("close I'm getting. At least I'd know I'm making progress.\"")

print("\n*POOF* A strange man appears out of nowhere.")

print("\n\"Hello there, traveler! Would you like to browse my wares?\"")
print("Type 1 for yes or 2 for no:")
browse = int(input())

#Makes sure user selects appropriate value
while (browse < 1) or (browse > 2):
    print("\"I'm sorry, I didn't understand you.\"")
    browse = int(input())

#Displays trader's menu
while browse == True:
    print("\n\"What would you like to see?\"")
    print("1 - Simple Percentage (Wisdom +1)")
    print("2 - Percentage with Spinners (Dexterity +2)")
    print("3 - Loading Bar with Percentage (Defense +4)")
    print("4 - Leave")
    choice = int(input())

    #Makes sure user selects appropriate value
    while (choice < 1) or (choice > 4):
        print("\"Huh? I don't think I heard you right. Which one?\"")
        choice = int(input())

    #Logic for Simple Percentage
    if choice == 1:
        for percent in range(101):
            if percent == 100:
                print("  ", percent, "%")
            else:
                print("  ", percent, "%", end='\r')
                time.sleep(.1)

    #Logic for Percentage with Spinners
    if choice == 2:
        spinner = ["-","\\","|","/"]

        for percent in range(101):
            if percent == 100:
                print("  ",  spinner[percent % 4], percent,"%",  spinner[percent % 4])
            else:
                print(" ",  spinner[percent % 4], percent, "%",  spinner[percent % 4], end = "\r")
                time.sleep(.1)

    #Logic for Loading Bar with Percentage
    #Probably a cleaner way to do this
    if choice == 3:
        for percent in range(101):
            if percent == 100:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", "]", percent, "%")
            elif percent > 90:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            elif percent > 80:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            elif percent > 70:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u25A0", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            elif percent > 60:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            elif percent > 50:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            elif percent > 40:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u2588", u"\u2588", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            elif percent > 30:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u2588", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            elif percent > 20:
                print ("  ", "[", u"\u2588", u"\u2588", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            elif percent > 10:
                print ("  ", "[", u"\u2588", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)
            else:
                print ("  ", "[", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", u"\u25A0", "]", percent, "%", end='\r')
                time.sleep(.1)

    #Logic for Leave
    if choice == 4:
        browse = False

#Finale
print("\n\"Good luck on the rest of your journey!\" *POOF*\n")
