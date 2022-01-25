import socket
from _thread import *


#intialize ip for server and port
server = "192.168.236.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


#change split the tuples
def readPosition(str):
    str = str.split(",")
    return int(str[0]), int(str[1]), int(str[2]), int(str[3]), int(str[4]), int(str[5])

#make it to tuples
def makePosition(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2]) + "," + str(tup[3]) +"," + str(tup[4]) + "," + str(tup[5])

#intialize starting posiition for ball ,paddle and score point
position = [(20,200,350,250,0,0), (670,200,350,250,0,0)]


#threaded function
def threaded_client(conn, player):
    conn.send(str.encode(makePosition(position[player])))
    reply = ""
    countRun = 0
    while True:
        try:
            #read data
            data = readPosition(conn.recv(2048).decode())


            position[player] = data
            
            if not data:
                print("Disconneted")
                break
            else:
                if player == 1:

                    reply = position[0]

                else:

                    reply = position[1]
                
                print("Received: ", data)
                print("Sending: ", reply)

            #send data
            conn.sendall(str.encode(makePosition(reply)))


        except:
            break

    print("Lost Connection")
    conn.close

currentPlayer = 0

#main
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    #call threaded function
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1