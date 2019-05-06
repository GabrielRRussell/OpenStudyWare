import OpenStudyWare
import LawOfSines
import random

def AASRandomQuestion(count):
    questionSet = []
    for i in range(0, count):
        A = random.randint(1, 90)
        B = random.randint(1, 90)
        a = random.randint(5, 100)

        b = LawOfSines.AAS(A,a,B)
        question = "When A is " + str(A) + ", B is " + str(B) + ", and a is " + str(a) + ", what is b?"
        fakeAnswer0 = b + random.randint(0, 35)
        fakeAnswer1 = b + random.randint(0, 45)
        fakeAnswer2 = b - random.randint(0, 55)

        formattedQuestion = question + "|&" + str(b) + "|" + str(fakeAnswer0) + "|" + str(fakeAnswer1) + "|" + str(fakeAnswer2)
        
        questionSet.append(formattedQuestion)

    OpenStudyWare.askMultipleChoiceInOrder(questionSet)

count = int(input("How many questions do you want to ask?" ))
AASRandomQuestion(count)

