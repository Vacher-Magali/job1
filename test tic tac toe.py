instruction = """ this will be our tic tac toe board

| 1 | 2 | 3 |

| 4 | 5 | 6 |

| 7 | 8 | 9 |

*instructions : 
1. Insert the spot number (1,9) to put your sign,
2. You must fill all 9 spots to get result,
3. Player 1 will go first
"""

sign_dict=[]

for i in range (9):
    sign_dict.append ("")


def print_board ( sign_dict) :
    board = f"""

    | { sign_dict [ 0]} | { sign_dict [1]} | { sign_dict [ 2 ] } |
    | { sign_dict [3] } | { sign_dict [4] } | { sign_adict [ 5] } |
    | { sign_dict [ 6]} | { sign_dict [ 7]} | { sign_dict [ 8]} |
    """
index_list = []


def take_input(player_game) : 
    while true :
        x = int (input(f'{player_name} : '))
        x -= 1
        if 0 <= x < 10 : 
            if x in index_list :
                print ( "this spot is blocked.")
                continue
            index_list.append (x)
            return x
        print ( "please enter number between 1-9")

def result_winner( sign_dict, player_one, player_two ) :
    if sign_dict [ 0] == sign_dict [1] == sign_dict [2]== 'X'\
    or sign_dict [ 3] == sign_dict [4] == sign_dict[5] == 'X'\
    or sign_dict [ 6] == sign_dict [ 7] == sign_dict [8] == 'X'\
    or sign_dict [0] == sign_dict [3] == sign_dict [ 6] == 'X'\
    or sign_dict [1] == sign_dict [4] == sign_dict [7] == 'X'\
    or sign_dict [2] == sign_dict [5] == sign_dict [8] == 'X'\
    or sign_dict [0] == sign_dict[4] == sign_dict [8] == 'X'\
    or sign_dict [2] == sign_dict [4] == sign_dict[6] == 'X' :
        print ( f" congratulations {player_one}. You win.!!")
        quit (" thank you both for joining ")
     elif sign_dict [0] == sign_dict [1] == sign_dict [2] == 'O'\
        or sign_dict [3] == sign_dict [4] == sign_dict [5] == 'O'\
        or sign_dict [6] == sign_dict [7] == sign_dict [8] == 'O'\
        or sign_dict [0] == sign_dict [3] == sign_dict [6] == 'O'\
        or sign_dict [1] == sign_dict [4] == sign_dict [7] == 'O'\
        or sign_dict[2] == sign_dict [5] == sign_dict [8] == 'O'\
        or sign_dict [0] == sign_dict [4] == sign_dict [8] == 'O'\
        or sign_dict [2] == sign_dict[4] == sign_dict [6] == 'O ' :
        print( f"congratulations {player_two}. YOU WIN. !! ")
        quit( " thank you both joining")
     else:
        return
    

    def main() :
        print( "Welcome to game : |===TIC TAC TOE===| ")
        player_one = input( " Enter player 1 name : ")
        player_two = input ("Enter player 2 name : ")

        print (f"thank you for joining Mr./Mrs. {player_ona} and Mr./Mrs. :{player_two}")
        print(instructions)
        print(f"Mr. {player_one}'s sign is -X")
        print( f"Mr. {player_one}'s sign is -O")
        print_board ( sign_dict)
        for i in range ( 0,9) : 
            if i %2 == 0:
                index= take_input(player_one)
                sign_dict[index] = 'X'
            else : 
                index = take_input(player_two)
                sign_dict [index] = 'O'

                print_board(sign_dict)
                result_winner(sign_dict, player_one, player_two)
                print( " This is a tie..!! No body won. Play again.")

        
        main()