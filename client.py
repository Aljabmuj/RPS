#Name: Mujtaba Aljabery 
#Date: 12/3/2023 
#Program Name: client.py


# Citation for overall influence in the server and client program
# Date: 12/03/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# Source URL:https://pymotw.com/2/socket/tcp.html

#Because we are using TCP sockets, the first programming project 
#was a big influence in how this program was handled 


# To handle the ASCII property for the encoding and decoding, I use UTF-8
# Citation for try and finally
# Date: 12/04/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# Source URL: https://www.freecodecamp.org/news/what-is-utf-8-character-encoding/
 

# include socket module
from socket import *
    
socket = socket(AF_INET, SOCK_STREAM)

serv_address = ('127.0.0.1', 4200) 

socket.connect(serv_address)

# Citation for list implementation 
# Date: 12/03/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# Source URL:https://www.w3schools.com/python/python_lists.asp

#List to compare input rock, paper, scissor 
choice = ['rock','paper','scissor']

#List to compare user commands
answer = ['rps','/q']

#List to handle if the game is replayed 
playagain = ['yes','no']

print("connected to:", serv_address)


User_take = input("Type in 'rps' to play a game of rock paper scissors or type in '/q' to quit.")
socket.send(User_take.encode('utf-8'))

while User_take not in answer:
    print("Huh? please try again!")
    User_take = input("Type in 'rps' to play a game of rock paper scissors or type in '/q' to quit.")
    socket.send(User_take.encode('utf-8'))
    
if User_take == ('/q'):
     print("see ya! :)")
     socket.close()

elif User_take == ('rps'):
    # Citation for try and finally 
    # Date: 12/04/2023
    # Copied from /OR/ Adapted from /OR/ Based on:
    # Source URL: https://www.w3schools.com/python/gloss_python_try_finally.asp
    try: 
        while True: 
            # Citation for taking user data 
            # Date: 12/03/2023
            # Copied from /OR/ Adapted from /OR/ Based on:
            # Source URL:https://www.geeksforgeeks.org/taking-input-in-python/
            
            #Starting off the game, get the user input 
            print("Rock. Paper. Scissors!!")
            
            user_input = input("What's your choice? please type 'rock', 'paper', or 'scissor: ")
            
            while  user_input not in choice: 
                print("Wrong! Please select the choices listed!")
                user_input = input("What's your choice? please type 'rock', 'paper', or 'scissor:")
                 
            socket.send(user_input.encode('utf-8'))
                
            final_result = socket.recv(1024).decode('utf-8')
            print(final_result)
            
            ask_user = input("Would you like to play again? enter 'yes' or 'no': ")
            
            while ask_user not in playagain: 
                print("Huh? Please try again.")
                ask_user = input("Would you like to play again? enter 'yes' or 'no': ")
                socket.send(ask_user.encode('utf-8'))
                                        
            if ask_user == 'yes': 
                socket.send(ask_user.encode('utf-8'))
                print("Time for the next round!")
                
            elif ask_user == 'no':
                socket.send(ask_user.encode('utf-8'))
                print("Ending connection, See ya!")
                socket.close()
                break
                
    finally: 
        # When everything is done, we can close the socket
        socket.close() 
        print("Connection ended")
