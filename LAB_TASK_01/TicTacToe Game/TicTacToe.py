# TIC - Tac - Toe
'''
1. Draw a board
2. Inputs the player names
3. put sign to each player name 
4. if they dont put input between ( 1-9 ) , direct them to previous state 
5. put sign to exact spot 
6.print board after each input
7. calculate and display result 

'''

instructions = ''' 
This will be over tic tac yoe board 

    1| 2  | 3
  ---|----|---
    4| 5  | 6
  ---|----|---
    7| 8  | 9 
     
1. Insert the spot number (1-9) to put your sign.
2. You must fill all the 9 spots to get the result.
3. Player_1 will go first.
       '''
box = []
for i in range(9):
      box.append(' ')

def print_board():
     board = f'''
          {box[0]}  | {box[1]}  | {box[2]}
        -----|----|------
          {box[3]}  | {box[4]}  | {box[5]}
        -----|----|------
          {box[6]}  | {box[7]}  | {box[8]}
                                       

    
'''
     print(board)
index_list = []
def take_input(player_name):
     while True:
          try:
              x = int(input(f"{player_name}:"))
              x-=1
              if 0 <= x < 10:
                 if x in index_list:
                     print("this spott is blocked")
                     continue
                 index_list.append(x)
                 return x
              else:
                   print("PLease enter number between 1-9")
          except ValueError:
               print("Invalid input ! . Numbers only.")

    

def calculate_result(player_1,player_2):
    if  box[0] == box[1] == box[2] == 'X' or box[1] == box[4] == box[7] == 'X' or box[0] == box[4] == box[8] == 'X' or box[2] == box[5] == box[8] == 'X' or box[3] == box[4] == box[5] == 'X' or box[2] == box[4] == box[6] == 'X' or box[6] == box[7] == box[8] == 'X' or box[0] == box[3] == box[6] == 'X' :
            print(f'Congratulations {player_1}.!!! You WON.')
            print("Quit. Thank you for joining.")
            return True
    elif box[0] == box[1] == box[2] == 'O' or box[1] == box[4] == box[7] == 'O' or box[0] == box[4] == box[8] == 'O' or box[2] == box[5] == box[8] == 'O' or box[3] == box[4] == box[5] == 'O' or box[2] == box[4] == box[6] == 'O' or box[6] == box[7] == box[8] == 'O' or box[0] == box[3] == box[6] == 'O' :
             print(f'Congratulations {player_2}.!!! You WON.')
             print("Quit. Thank you for joining.")
             return True
    return False




def main():
    print("Welcome to the tic tac toe game. ")
    player_1 = input("Enter the palyer_1 name :")
    player_2 = input("Enter the player_2 name:")
    print(f"THank you for joining {player_1} and {player_2  }")

    print(instructions)
    print(f" {player_1}'s sign is - X")
    print(f"{player_2}'s sign is - O")
    print("Enter any key to start the game:")
    print_board()

    for i in range(9):
        if i % 2 == 0:
             index = take_input(player_1)
             box[index] = 'X'
        else:
             index = take_input(player_2)
             box[index] = 'O'
        print_board()
        if calculate_result(player_1,player_2):
             return

    print("This is a tie. Nobody Wonns The Match. Play Again")
             
 

main()