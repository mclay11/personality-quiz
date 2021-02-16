from tkinter import *

#Create dictionary to hold personality counts
personality_index = {"lion": 0, "otter" : 0, "retriever" : 0, "beaver" : 0}

#Create a class called "Question" that will be used to properly execute each question
class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    #Define a function to "check" the user input and add +1 to designated personality type in the index
    def check(self, letter, view):
        global right
        if(letter == "A"):
            personality_index["lion"] += 1
        if(letter == "B"):
            personality_index["otter"] +=1
        if(letter == "C"):
           personality_index["retriever"] += 1
        else:
           personality_index["beaver"] += 1
        view.after(50, lambda *args: self.unpackView(view))

    #Define a function that creates the "buttons" that display to the user and utilizes the "check" function
    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view, text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view, text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()
        
#Define a function that will print the users calculated personality type and its description
def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        keymax = max(personality_index, key = personality_index.get)
        if keymax == "lion":
            Label(window, text="Thank you for answering the questions. You got " + max(personality_index, key=personality_index.get) + "! Lions are leaders, they are decisive. They love to solve problems. They seek new adventures and opprotunities.").pack()
        if keymax == "otter":
            Label(window, text="Thank you for answering the questions. You got " + max(personality_index, key=personality_index.get) +"! Otters are excitable, fun-seeking and love to talk. They are great at motivating others and are extremely outgoing. They are very loving, and encouraging.").pack()
        if keymax == "retriever":
            Label(window, text="Thank you for answering the questions. You got " + max(personality_index, key=personality_index.get) +"! Retrievers are loyal. They can absorb the most emotional pain and punishment in a relationship and still stay commited. They are great listeners.").pack()
        if keymax == "beaver":
            Label(window, text="Thank you for answering the questions. You got " + max(personality_index, key=personality_index.get) +"! Beavers have a strong need to do things correctly. They are the kind of people who actually read instruction manuals.").pack()

    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()
    
#Create an empty dictionary to hold the questions
questions = []
#Open and read questions.txt
file = open("questions.txt", "r")
line = file.readline()
#Use a while statement to iterate through each group of answers in the file
while(line != ""):
    #Set the first line to be the question
    questionString = line
    #Create a list to hold the possible answers
    answers = []
    #for each of the 4 possible answers
    for i in range (4):
        #Add the answers to the answers list
        answers.append(file.readline())
    #Makes sure the program doesn't print out the blank lines
    space = file.readline()
    space = space[:-1]
    #Adds the question to the question list
    questions.append(Question(questionString, answers))
    line = file.readline()
    
#close questions.txt
file.close()
#Set index to -1
index = -1
#Create a variable to hold the length of questions
number_of_questions = len(questions)

window = Tk()
#Initialize the button thats going to start the quiz and after pressing it it will ask the first question
button = Button(window, text="Start Personality Quiz", command=askQuestion)
button.pack()
window.mainloop()

