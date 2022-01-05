#For this to work, upload StandardFirmata to the Arduino UNO board and then run main.py

import pyfirmata

comport='COM8'

board = pyfirmata.Arduino(comport)

ledL = board.get_pin('d:13:o')   
P7 = board.get_pin('d:7:o')
P8 = board.get_pin('d:8:o')
P9 = board.get_pin('d:9:o')
P10 = board.get_pin('d:10:o')

def led(total):
    if total == 0 :
        #Stop Signal
        P7.write(1)
        P8.write(1)
        P9.write(1)
        P10.write(1)

    elif total == 1 :
        #Forward Signal
        P7.write(0)
        P8.write(1)
        P9.write(1)
        P10.write(0)

    elif total == 2 :
        #Backward Signal
        P7.write(1)
        P8.write(0)
        P9.write(0)
        P10.write(1)

    elif total == 3 :
        #Right Signal
        P7.write(1)
        P8.write(1)
        P9.write(0)
        P10.write(0)

    elif total == 4 :
        #Left Signal
        P7.write(0)
        P8.write(0)
        P9.write(1)
        P10.write(1)

    else :
        #Stop Signal
        P7.write(1)
        P8.write(1)
        P9.write(1)
        P10.write(1)
