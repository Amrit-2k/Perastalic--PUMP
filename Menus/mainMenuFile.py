import utime
import machine
from machine import I2C
from Project.Lcd_Setup.lcd_api import LcdApi
from Project.Lcd_Setup.pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

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

welcome =["WELCOME HERE"]
menuItems=["MAIN MENU","PUMP     ","DOSE     ","SPEED    ","VOLUME   ","DIRECTION","CALIBRATE","SUMMARY  "]
class MainMenuClass:
    #PUMP
    def case_1(self):
        
        lcd.clear()
        
        lcd.move_to(6,0)
        lcd.putstr(menuItems[0])
        
        lcd.move_to(0,1)
        lcd.putstr(chr(0))
        
        lcd.move_to(1,1)
        lcd.putstr(menuItems[1])
        
        lcd.move_to(1,2)
        lcd.putstr(menuItems[2])
        
        lcd.move_to(1,3)
        lcd.putstr(menuItems[3])
        
    
       
    #DOSE    
    def case_2(self):
        
        lcd.clear()
        
        lcd.move_to(6,0)
        lcd.putstr(menuItems[0])
       
        lcd.move_to(1,1)
        lcd.putstr(menuItems[1])
        lcd.move_to(0,2)
        lcd.putstr(chr(0))
        lcd.move_to(1,2)
        lcd.putstr(menuItems[2])
        
        lcd.move_to(1,3)
        lcd.putstr(menuItems[3])
    #SPEED   
    def case_3(self):
        
        lcd.clear()
        
        lcd.move_to(6,0)
        lcd.putstr(menuItems[0])
        
        lcd.move_to(1,1)
        lcd.putstr(menuItems[1])
        
        lcd.move_to(1,2)
        lcd.putstr(menuItems[2])
        
        lcd.move_to(0,3)
        lcd.putstr(chr(0))
        
        lcd.move_to(1,3)
        lcd.putstr(menuItems[3])
    #VOLUME
    def case_4(self):
        lcd.clear()
        
        lcd.move_to(6,0)
        lcd.putstr(menuItems[0])
        
        lcd.move_to(1,1)
        lcd.putstr(menuItems[2])
        
        lcd.move_to(1,2)
        lcd.putstr(menuItems[3])
        
        lcd.move_to(0,3)
        lcd.putstr(chr(0))
        
        lcd.move_to(1,3)
        lcd.putstr(menuItems[4])
    #DIRECTION
    def case_5(self):
        
        lcd.clear()
        
        lcd.move_to(6,0)
        lcd.putstr(menuItems[0])
        
        lcd.move_to(1,1)
        lcd.putstr(menuItems[3])
        
        lcd.move_to(1,2)
        lcd.putstr(menuItems[4])
        
        lcd.move_to(0,3)
        lcd.putstr(chr(0))
        
        lcd.move_to(1,3)
        lcd.putstr(menuItems[5])
        
    #CALIBRATE
    def case_6(self):
        lcd.clear()
        
        lcd.move_to(6,0)
        lcd.putstr(menuItems[0])
        
        lcd.move_to(1,1)
        lcd.putstr(menuItems[4])
        
        lcd.move_to(1,2)
        lcd.putstr(menuItems[5])
        
        lcd.move_to(0,3)
        lcd.putstr(chr(0))
        
        lcd.move_to(1,3)
        lcd.putstr(menuItems[6])
    #SUMMARY
    def case_7(self):
        
        lcd.clear()
        lcd.move_to(6,0)
        lcd.putstr(menuItems[0])
       
        lcd.move_to(1,1)
        lcd.putstr(menuItems[5])
        
        lcd.move_to(1,2)
        lcd.putstr(menuItems[6])
        lcd.move_to(0,3)
        lcd.putstr(chr(0))
        lcd.move_to(1,3)
        lcd.putstr(menuItems[7])
     #WELCOME
    def case_0(self):
        lcd.move_to(6,2)
        lcd.putstr(welcome[0])
        utime.sleep_ms(5000)
        lcd.clear()
        
        
    def MainMenu(self, cases):
        method = 'case_' + str(cases)        
        return getattr(self, method)() 
