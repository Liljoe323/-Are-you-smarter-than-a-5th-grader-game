#Imports
import time

#This is an array of questions, in the form of a list that includes the question and dictionary of the possible answers.
q = [["A story conveying a moral lesson is called what?", {"A": "A fable", "B": "A myth", "C": "A legend"}],
      ["The sun is a ____:", {"B": "Planet", "A": "Star", "C": "Solar system"}],
      ["What species can live on both water and land?", {"B": "Mammals", "A": "Amphibians", "C": "Fish"}],
      ["How many states make up the United States of America?", {"A": "50", "B": "51", "C": "52"}],
      ["What is the largest country by size?", {"C": "America", "B": "Antarctica", "A": "Russia"}],
      ["A hexagon has how many sides?", {"A": "6", "B": "8", "C": "5"}],
      ["What number is the Roman numeral XVI?", {"B": "14", "A": "16", "C": "56"}],
]


score = 0

#This function loops through our list of questions and asks the user to input the answer they think is correct.
#Then it checks if the user input matches the correct answer in the dictionary as associated with the key "A".
def ask_questions(score):
    print("")
    for q[0] in q:
        print("The question is: " + str(q[0][0]))
        for k in q[0][1]:
            print(str(q[0][1][k]))
        print("")
        if input("Which answer is correct? ") == (str(q[0][1]["A"])):
            score += 1
            print("Correct! Your new score is: " + str(score))
            print("")
            print("")
        else:
            print("Oh, that's incorrect! Your score is: " + str(score))
            print("")
            print("")

#This function is just to print out the main screen
def main_menu():
    print("""
    |=========================================|
    |                                         |    
    |    Are You Smarter Than a 5th Grader    |          
    |                                         |
    |    ---------------------------------    |
    |           Made by JP Bourdeau           |
    |                                         |
    |=========================================|
    """)
    time.sleep(3)

#This function is just a simple call to print out instructions for the user.
def directions():
    print("")
    print("To play this game, correctly answer questions to score points.\n"
          "Make sure to spell your answers exactly as they appear under the question.")
    time.sleep(4)


main_menu()
playing = ""
while playing.lower() != "y" or "n":
    playing = input("Do you want to play, 'Are You Smarter Than A 5th Grader'? (Y/N)")
    if playing.lower() == "y":
        directions()
        ask_questions(score)
#add final score, ask if they want to save their score to a .txt file?
        print("Thanks for playing!")
        break
    elif playing.lower() == "n":
        print("")
        print("You must already know that you're smarter than a 5th grader!")
        break

    else:
        print("")
        print("Oops, it appears that you don't want to play... Or perhaps you didn't enter 'Y' or 'N'.")
        print("")
