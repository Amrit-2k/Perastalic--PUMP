import utime
import machine
from machine import I2C

from Project.Lcd_Setup.lcd_api import LcdApi
from Project.Lcd_Setup.pico_i2c_lcd import I2cLcd
from Project.Variables.variableFile import VariableClass
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)



class SettingMenuClass(VariableClass):            
       
    #SPEED   
    def case_3(self):     
        lcd.clear()            
        lcd.move_to(3,0)
        lcd.putstr("Changing Speed..")
        lcd.move_to(8,2)
        speed=str(VariableClass.speed)
        lcd.putstr(speed)       

        
        
    #VOLUME        
    def case_4(self):
        lcd.clear()            
        lcd.move_to(2,0)
        lcd.putstr("Changing Volume..")
        lcd.move_to(8,2)                
        volume=str(VariableClass.volume)
        lcd.putstr(volume)
      
       
    #DIRECTION
    def case_5(self):
        lcd.clear()            
        lcd.move_to(0,0)
        lcd.putstr("Changing Direction..")
        lcd.move_to(8,2)        
        if (VariableClass.direction==True):
            lcd.putstr("Right")
        elif (VariableClass.direction==False):
            lcd.putstr("Left")            
        
       
   
  
        
    def SettingMenu(self, cases):
        method = 'case_' + str(cases)        
        return getattr(self, method)() 

