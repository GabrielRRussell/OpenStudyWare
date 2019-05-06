# OpenStudyWare
import random

def pickRandomQuestion(qSet):
    # Pick a Random Question as an Integer Value
    randomQuestion = random.randint(0, len(qSet) - 1)
    # Return the Random Question
    return qSet[randomQuestion]

def parseQuestion(line):
    # Split the Line
    line = line.split("|")
    answer = -1

    # Randomize the list of answers so that the questions are truly random.
    answerSet = line[1:]
    random.shuffle(answerSet)
    line = [line[0]] + answerSet

    # Go through each answer, and find the correct one (starts with "&")
    for i in range(1, len(line)):
        if line[i].startswith("&"):
            line[i] = line[i].replace("&", "", 1)
            answer = i
    # Return the Correct Answer, followed by the list
    return [answer, line]

def checkQuestion(userChoice, parsedQuestion):
    # Check the Users Input against the Actual Answer, return True/False
    if int(userChoice) != int(parsedQuestion[0]):
        return False
    else:
        return True

def printQuestion(question):
    print(question[1][0])
    for i in range(1, len(question[1][0:])):
        print (str(i) + ". " + question[1][i])
    choice = input("Choose one answer from 1 to " + str(len(question[1]) - 1) + ": ")
    return choice

def askMultipleChoiceInOrder(qSet):
    score = 0
    qTotal = len(qSet)
    for i in range(0, qTotal):
        parsedQ = parseQuestion(qSet[i])
        choice = printQuestion(parsedQ)
        result = checkQuestion(choice, parsedQ)
        if result == True:
            score += 1

    print ("You got " + str(score) + " out of " + str(qTotal) + " questions right!")
        

def askRandomMultipleChoice(questionSet):
    randomQ = pickRandomQuestion(questionSet)
    parsedQ = parseQuestion(randomQ)

    choice = printQuestion(parsedQ)
    result = checkQuestion(choice, parsedQ)


    if result == True:
        print ("Correct!")
    else:
        print ("Incorrect!")
    print("\n\n\n")

def wordScramble(word):
    wordList = list(word)
    random.shuffle(wordList)
    scrambledWord = "".join(wordList)
    
    userInput = input("The shuffled word is '" + str(scrambledWord) + "'. What is the original?")
    if userInput == word:
        return True
    else:
        return False

