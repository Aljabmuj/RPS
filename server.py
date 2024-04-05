# Name: Mujtaba Aljabery
# Date: 12/3/2023
# Program Name: server.py

# Citation for overall influence in the server and client program 
# Date: 12/03/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# Source URL:https://pymotw.com/2/socket/tcp.html

# Because we are using TCP sockets, the first programming project
# was a big influence in how this program was handled

#To handle the ASCII property for the encoding and decoding, I use UTF-8
# Citation for try and finally
# Date: 12/04/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# Source URL: https://www.freecodecamp.org/news/what-is-utf-8-character-encoding/

#include socket module 
from socket import*
#include random module for server option, which will be used for rock,paper, and scissors
import random 

# Citation for list implementation
# Date: 12/03/2023
# Copied from /OR/ Adapted from /OR/ Based on:
# Source URL:https://www.w3schools.com/python/python_lists.asp

#Lists used for error handling in the program 
options = ['rock','paper','scissor']
answer = ['rps','/q']
decision = ['yes','no']

#Create a socket 
socket = socket(AF_INET, SOCK_STREAM)

#Establish the address and port 
serv_address = ('127.0.0.1', 4200) 

socket.bind(serv_address)

#Listen for any clients 
socket.listen(1)

print("Waiting for a connection...")
c_sock, c_add = socket.accept()

print("Server recieved connection from", c_add)

print("Hello! If you would like to play, type 'rps'. Otherwise, type '\q'.")
response = c_sock.recv(1024).decode('utf-8')

#If the client response is not 'rps' or '/q'
while response not in answer: 
    print("User input: ", response) #print the response 
    print("Huh? Please try again.") #Print error statement
    response = c_sock.recv(1024).decode('utf-8') #Take in a new response 

if response == '/q': #if the client is /q 
    print("User input: ", response) #print the response 
    print("Quitting connection. See ya!") #Indicate the connection will close 
    c_sock.close() #close the socket! 
    
elif response == 'rps': #if they type rps, begin the game! 
    # Citation for try and finally
    # Date: 12/04/2023
    # Copied from /OR/ Adapted from /OR/ Based on:
    # Source URL: https://www.w3schools.com/python/gloss_python_try_finally.asp
        try: 
            while True: 
                    print("User input: ", response)
                    
                #play the game 
                    print("Rock. Paper. Scissors!!")  # print the response
                    
                 #Citation for random function 
                 # Date: 12/04/2023
                 # Copied from /OR/ Adapted from /OR/ Based on:
                 # Source: https://pynative.com/python-random-choice/
                    # Let's have some fun and refer to the server as an AI, and we can randomize its choice
                    ai_option = random.choice(options)

                    #Take the input from the client server
                    user_choice = c_sock.recv(1024).decode('utf-8')

                    while user_choice not in options:
                        print("Huh? Please try again.")
                        user_choice = c_sock.recv(1024).decode('utf-8')
                      
                    
                    #Print what the player and the server (AI) chose!
                    print("The Player chose: ", user_choice)
                    print("We choose: ", ai_option)

                    # Once the user and the server have made their choice, we can do some comparisons
                    if ai_option == user_choice: #if they are the same, make it a tie
                        final_result = "Wow, it's a tie! Good game well played!"
                        print("It's a tie!")
                        
                    elif (ai_option == 'rock' and user_choice == 'paper'): #paper beats rock!
                        final_result = "Incredible, you won! You're really good at this :D"
                        print("The player won!, paper beats rock!")
                        
                    elif (ai_option == "paper" and user_choice == 'scissor'): #scissor beats paper!
                        final_result = "Incredible, you won! You're really good at this :D"
                        print("The player won!, scissors beats  paper!")
                        
                    elif (ai_option == "scissor" and user_choice == 'rock'): #rock beats scissor!
                        final_result = "Incredible, you won! You're really good at this :D"
                        print("The player won!, rock beats scissors!")
                        
                    else: #This statement can handle the server winning against the user
                        final_result = "You lost! There's always next time!"
                        print("We won!")

                    # send the result based on the choices above
                    c_sock.send(final_result.encode('utf-8'))                    
                    
                    #after the game, see if the player wants to play again 
                    replay = c_sock.recv(1024).decode('utf-8')
                    
                    while replay not in decision: #check if the client response is not yes or no
                        print("Huh? Please try again.")
                        replay = c_sock.recv(1024).decode('utf-8')
        
                    #if replay is yes 
                    if replay == 'yes': 
                        continue #continue the program and loop! 
                    
                    elif replay == 'no': #if no, break the loop! 
                        print("Ending connection, see ya!")
                        c_sock.close() #don't forget to close 
                        break 
        finally: 
            #When everything is done, we can close the socket 
            c_sock.close() 
            socket.close()
            print("Connection ended")