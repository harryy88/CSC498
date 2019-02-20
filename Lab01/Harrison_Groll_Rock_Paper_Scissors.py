#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:01:19 2019

@author: harrisongroll
"""

"""CSC 498 Assignment #1 Professor N. Dellis"""
from random import randint
def HumanPlayer(GameRecord):
    ChoiceOfHumanPlayer = 0
    while (ChoiceOfHumanPlayer not in ['r','p','s','q', 'g']):
        ChoiceOfHumanPlayer = input("Enter a move (r)ock, (p)aper, (s)cissors, (g)ame (q)uit:\n=>")
    return ChoiceOfHumanPlayer 

def ComputerPlayer(GameRecord):
    moves = ['r','p','s']
    ChoiceOfComputerPlayer = randint(0,2)
    return moves[ChoiceOfComputerPlayer]
    

def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    #Return 0 if tie, 1 if computer, 2 if human 
    if ChoiceOfComputerPlayer == ChoiceOfHumanPlayer:
        return 0
    elif (ChoiceOfComputerPlayer == 'p' and ChoiceOfHumanPlayer == 'r'):
        return 1
    elif (ChoiceOfComputerPlayer == 's' and ChoiceOfHumanPlayer == 'r'):
        return 2
    elif (ChoiceOfComputerPlayer == 'r' and ChoiceOfHumanPlayer == 'p'):
        return 2
    elif (ChoiceOfComputerPlayer == 's' and ChoiceOfHumanPlayer == 'p'):
        return 1
    elif (ChoiceOfComputerPlayer == 'r' and ChoiceOfHumanPlayer == 's'):
        return 1
    return 2

def PrintOutcome(humanChoice, compChoice, outCome):
    str = ""
    if outCome == 0:
        str += "Tie Game! "
    elif outCome == 1:
        str += "Computer Wins! "
    else:
        str += "Human Wins! "
    str +=  "Computer Chose " + compChoice + " Human Chose " + humanChoice
    print(str)

def UpdateGameRecord(GameRecord, ChoiceofComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    GameRecord[0].append(Outcome)
    GameRecord[1].append(ChoiceofComputerPlayer)
    GameRecord[2].append(ChoiceOfHumanPlayer)
    

def PrintGameRecord(GameRecord):
    print("*********GAME RECORD****************")
    computerScore = humanScore = 0
    for game in GameRecord[0]:
        if game == 1:
            computerScore += 1
        elif game == 2:
            humanScore += 1
    print("Human Wins", humanScore, "Round(s)")
    print("Computer Wins", computerScore, "Round(s)")
    print("Computer\tHuman")
    for n in range((len(GameRecord[1]))):
        print (GameRecord[1][n] + "\t\t" + GameRecord[2][n])
            

def PlayGame():
    humanchoice = 0
    GameRecord = [[], [], []]
    while (humanchoice is not 'q'):
       humanchoice = HumanPlayer(GameRecord) 
       if humanchoice == 'g':
           PrintGameRecord(GameRecord)
       else:
           compChoice = ComputerPlayer(GameRecord)
           outcome = Judge(ChoiceOfComputerPlayer = compChoice,ChoiceOfHumanPlayer= humanchoice)
           print("****************OUTCOME***********************")
           PrintOutcome(humanchoice,compChoice, outcome)
           print("***********************************************")
           UpdateGameRecord(GameRecord,compChoice,humanchoice,outcome)

PlayGame()
           
           
