import utime
import machine
from machine import Pin
from machine import I2C
from Project.Lcd_Setup.lcd_api import LcdApi
from Project.Lcd_Setup.pico_i2c_lcd import I2cLcd
from Project.Variables.variableFile import VariableClass



directionB = Pin(10, Pin.OUT)
step = Pin(12, Pin.OUT)
enable = Pin(15 , Pin.OUT)

upBtn = Pin(18, Pin.IN,Pin.PULL_DOWN)
downBtn = Pin(19, Pin.IN,Pin.PULL_DOWN)
selectBtn = Pin(20, Pin.IN,Pin.PULL_DOWN)

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

items=["DOSE","DOSING AT...."]
class DoseMenuClass(VariableClass):    

    def __init__(self):
        doseSpeed=str(VariableClass.speed)
        doseVolume=str(VariableClass.volume)

        lcd.clear()
        lcd.move_to(8,0)
        lcd.putstr(items[0])        
        lcd.move_to(0,0)
        lcd.putstr(chr(0))        
        lcd.move_to(1,0)
        lcd.putstr(chr(12))        
        lcd.move_to(5,1)
        lcd.putstr(items[1])
        lcd.move_to(1,2)
        lcd.putstr(doseSpeed)
        lcd.move_to(3,2)
        lcd.putstr("mL/min for ")        
        lcd.move_to(15,2)
        lcd.putstr(doseVolume)
        lcd.move_to(17,2)
        lcd.putstr("mL") 
        VariableClass.direction=False
        
        print(VariableClass.direction)
        if (VariableClass.direction==False):
            self.DirectionLeft()
        elif (VariableClass.direction==True):
            
            self.DirectionRight()
    
    def DirectionRight(self):
            speed=(VariableClass.speed)
            speed=speed*1000
            volume = 0
            
        
            enable.low()
            while (selectBtn.value()==0 ):
                
                directionB.low()
                step.low()
                utime.sleep_ms(speed)
                step.high()
                directionB.high()
                utime.sleep_ms(speed)
                volume= volume + 1
                print(volume)
                if (volume==VariableClass.volume):
                    return
                elif(selectBtn.value()==1):
                    return
                
                
    def DirectionLeft(self):
            speed=(VariableClass.speed)
            speed=speed*1000
        
            enable.low()
            while (selectBtn.value()==0):
                volume = 0
                directionB.low()
                step.low()
                utime.sleep_ms(speed)
                step.high()
                directionB.high()
                utime.sleep_ms(speed)
                volume= volume + 1
                if (volume==VariableClass.volume):
                    return
                elif(selectBtn.value()==1):
                    return
            

            
         

                  
  
                
    
       
    
    
   
    
  


