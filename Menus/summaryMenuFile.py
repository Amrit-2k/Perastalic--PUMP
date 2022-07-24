import utime
import machine
from machine import Pin
from machine import I2C
from Project.Lcd_Setup.lcd_api import LcdApi
from Project.Lcd_Setup.pico_i2c_lcd import I2cLcd
from Project.Variables.variableFile import VariableClass

upBtn = Pin(18, Pin.IN,Pin.PULL_DOWN)
downBtn = Pin(19, Pin.IN,Pin.PULL_DOWN)
selectBtn = Pin(20, Pin.IN,Pin.PULL_DOWN)

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

items=["SUMMARY","TOTAL VOLUME DONE"]



lcd.custom_char(0, bytearray([
  0x00,
  0x04,
  0x0E,
  0x1F,
  0x1F,
  0x0E,
  0x04,
  0x00
]))

lcd.custom_char(12, bytearray([
  0x00,
  0x04,
  0x08,
  0x1F,
  0x09,
  0x05,
  0x01,
  0x1F
]))


pumpSpeed = '0'


class SummaryMenuClass(VariableClass):
    
   

    def __init__(self):
        
        
        lcd.clear()
        lcd.move_to(8,0)
        lcd.putstr(items[0])        
        lcd.move_to(0,1)
        lcd.putstr(chr(0))        
        lcd.move_to(1,0)
        lcd.putstr(chr(12))        
        lcd.move_to(1,1)
        lcd.putstr(items[1])
        volume=str(VariableClass.volume)
        lcd.putstr(volume)
        
            
        
       
        
        
    



        
        
        
      

        
        
                
              
                
          
             
                           
                    
  
                
    
       
    
    
   
    
  


