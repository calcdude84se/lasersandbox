import serial

def activate(word):
    #ttyACM0 is the name of the arduino
    ser=serial.Serial(port='/dev/ttyACM0', baudrate=9600)
    #writes the word with a newline character
    ser.write(word+"\n")


