import socket
import UsbControl.LightCrafter6500Device as lc
import ast

host = ''
port = 6340

storedValue = "How are you doing?"

def setupServer():
    # Create socket and bind to host and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    try:
        s.bind((host,port))
    except socket.error as mgs:
        print(mgs)
    print('Socket bind complete')
    return s

def setupConnection():
    # Specify number of listeners
    s.listen(1)
    conn, address = s.accept()
    print("Connected to " + address[0] + ":" + str(address[1]))
    return conn

def dataTransfer(conn):
    # Loop for sending and recieving data until told not to
    while True:
        #Recieve the data
        # "Buffer size need to be modified

        data = conn.recv(1024)

        # Split the data such that you seperate the command
        # Can be replaced with handling of an JSON object
        dataMessage = data.split(' ',1)
        command = dataMessage[0]
        print("Incomming command: " + data)
        
        # Test for all the different commands
            
        if command == 'REPEAT':
            print "We have entered the REPEAT statement"
            reply = dataMessage[1]

        elif command == 'EXIT':
            print("Our client has left us :(")
            break

        elif command == 'LOAD':
            print "We have entered the LOAD statement"
            lc_dmd = lc.LC6500Device()
            pattern_list = list(ast.literal_eval(dataMessage[1])) # typeset string to array
            lc_dmd.pattern_on_the_fly(pattern_list)
            reply = "Patterns succesfully uploaded. DMD ready to use."

        elif command == 'KILL':
            lc_dmd = lc.LC6500Device()
            lc_dmd.power_mode('standby')
            print(" Our server is shutting down.")
            s.close()
            break
        
        else:
            reply = 'Unknown Command'
        # Send the reply back to the client
        conn.sendall(reply)
        #conn.sendall(str.encode(reply))
    print("Close connection")
    conn.close()


s = setupServer()

while True:
    try:
        # wait for a new connection
        conn = setupConnection()
        # handle data communication when connection is established
        dataTransfer(conn)
    except:
        print("SERVER Closed")
        break
