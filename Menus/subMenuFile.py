import utime
import machine
from machine import I2C

from Project.Lcd_Setup.lcd_api import LcdApi
from Project.Lcd_Setup.pico_i2c_lcd import I2cLcd

from Project.Menus.pumpMenuFile import PumpMenuClass
from Project.Menus.doseMenuFile import DoseMenuClass
from Project.Menus.speedMenuFile import SpeedMenuClass
from Project.Menus.volumeMenuFile import VolumeMenuClass
from Project.Menus.directionMenuFile import DirectionMenuClass
#from Project.Menus.calibrateMenuFile import CalibrateMenuClass
from Project.Menus.summaryMenuFile import SummaryMenuClass

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=machine.Pin(16), scl=machine.Pin(17), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)



class SubMenuClass:
    #PUMP
    def case_1(self):
        PumpMenuClass()       
       
    #DOSE    
    def case_2(self):
        
        DoseMenuClass()        
       
    #SPEED   
    def case_3(self):
       
        SpeedMenuClass()
        
    #VOLUME
    def case_4(self):
       
        VolumeMenuClass()
       
    #DIRECTION
    def case_5(self):
       
        DirectionMenuClass()
        
    #CALIBRATE
    def case_6(self):
        print("")
        #CalibrateMenuClass()
        
    #SUMMARY
    def case_7(self):
     
        SummaryMenuClass()
  
        
    def SubMenu(self, cases):
        method = 'case_' + str(cases)        
        return getattr(self, method)() 
