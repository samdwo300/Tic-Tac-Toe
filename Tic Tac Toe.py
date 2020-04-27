# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 18:35:02 2020

@author: samdw
"""
import numpy as np
import  pandas as pd
import matplotlib as plt
import random as rd

# Create tic tac toe board
board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])


# Player one's turn
def player_one(row,col):
    board[row][col] = 'x'
    print(board)
    
# Player two's turn    
def player_two(row,col):
    board[row][col] = 'o'
    print(board)
 
    
# Define winning game    
def winning_game():
    for i in range(0,3):
        if ((board[0][i] == 'x' or board[0][i] == 'o')  and  (board[0][i] == board[1][i] and board[1][i] == board[2][i])) or ((board[i][0] == 'x' or board[i][0] == 'o') and (board[i][0] == board[i][1] and board[i][1] == board[i][2])):
            return True
            break
    if (board[1][1] == 'x' or board[1][1] == 'o') and  ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[2][0] == board[1][1] and board[1][1] == board[0][2])):
        return True
    else:
        return False
    
        
      
# Define draw
def exhausted_board():
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == '-':
                return False
                break
            elif  board[i][j] != '-':
                continue
            else:
                return False
                break
    return True
      

# Define an invalid move
def invalid_move(row,col):
    if board[row][col] == 'x' or board[row][col] == 'o':
        return True


# Define when game ends
def game_over():
    if winning_game() == False and exhausted_board() == True:
        return True
    elif winning_game() == True:
        return True
    else:
        return False


def initialize_tac_tac_toe_game():
    while game_over() == False:
        row,col = map(int, input("Player one please enter row & column: "))
        while invalid_move(row,col) == True:
            row,col = map(int, input("Invalid move please re-enter row & column: "))
        player_one(row,col)
        if winning_game() == True:
            print("Player one you win!")
            break
        if exhausted_board() == True:
            print("Tie!")
            break
        row,col = map(int, input("Player two please enter row & column: "))
        while invalid_move(row,col) == True:
            row,col = map(int, input("Invalid move please re-enter row & column: "))
        player_two(row,col)
        if winning_game() == True:
            print("Player two you win!")
            break
        if exhausted_board() == True:
            print("Tie!")
            break





initialize_tac_tac_toe_game()




















