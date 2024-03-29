#!/usr/bin/env python

import RPi.GPIO as GPIO
import signal
import sys
sys.path.append('/home/pi/Desktop/smartScan/RFID_BarCodeRpi')
from scanRFID import SimpleMFRC522
from scanRFID import MFRC522

continue_reading = True

def barcodeReader():
    shift = False
    hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l',
    16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x',
    28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9',
    39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }

    hid2 = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L',
    16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X',
    28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')',
    44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'  }
    print("<<<SCAN BASRCODE >>>>")
    while True:

       ss = ''
       done = False
       while not done:

           fp = open('/dev/hidraw0', 'rb')
           buffer = fp.read(10)
           for c in buffer:
               if ord(c) > 0:
		   #print(ord(c))
                   #Here we are replacing 40 with 43 as ending suffix
                   if int(ord(c)) == 43:
                       done = True
		       print("DONE")
                       break

                   if shift:
                       if int(ord(c)) == 2:
                           shift = True
                       else:
                           ss += hid2[ int(ord(c)) ]
                           shift = False
                   else:
                       if int(ord(c)) == 2:
                           shift = True
                       else:
			   try:
                              ss += hid[ int(ord(c)) ]
                           except KeyError:
                                  print("KeyError")
                                  break



                   #print ord(c)

                   fb = open('/home/pi/Desktop/smartScan/RFID_BarCodeRpi/barcode_output.txt', 'w')
                   fb.write(ss)
                   fb.close()
                   print("close file")
           
           print ss


def rfidReader():

    reader = SimpleMFRC522()
    print("Hold a tag near the reader")
    try:
       id, text = reader.read()
       print(id)
       print(text)
       fb = open('/home/pi/Desktop/smartScan/RFID_BarCodeRpi/rfid_output.txt', 'w')
       fb.write(str(id))
       fb.close()

    finally:
       GPIO.cleanup()


def rfidStatus():

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    # Welcome message
    print "<<<<<<<<SMART CARD STATUS HERE >>>>>>>>>"

    while continue_reading:
    
          #MIFAREReader.MFRC522_Version()
          rfidStatusCode = MIFAREReader.getStatus()
  
          if rfidStatusCode == 49:
             print("RFID DETECTED")
          else:
             print("******NO RFID FOUND ****")



#def main():
#while True:
barcodeReader()
#rfidReader()
#rfidStatus()


#if __name__ == '__main__':
    #main()
