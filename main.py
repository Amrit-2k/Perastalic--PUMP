import utime
import machine
from machine import Pin
from machine import I2C
from Project.Menus.mainMenuFile import MainMenuClass
from Project.Menus.subMenuFile import SubMenuClass
from Project.Menus.settingMenuFile import SettingMenuClass
from Project.Variables.variableFile import VariableClass

upBtn = Pin(18, Pin.IN,Pin.PULL_DOWN)
downBtn = Pin(19, Pin.IN,Pin.PULL_DOWN)
selectBtn = Pin(20, Pin.IN,Pin.PULL_DOWN)

SubMenuSwitch= SubMenuClass()
mainMenuSwitch= MainMenuClass()
settingMenuSwitch = SettingMenuClass()

class MainClass(VariableClass):
    
    def __init__(self):
        mainMenuSwitch.MainMenu(1)
        self.MainMenuBtns()
    
    def MainMenuBtns(self): 
            while True:
                
                
                if(self.menuPage==1):
                   
                    
                    if (upBtn.value()==1):
                        utime.sleep_ms(100)                                                               
                        
                        self.menuLine=self.menuLine-1
                        VariableClass.menuLine = self.menuLine
                        
                        if (self.menuLine<=1):
                            self.menuLine=1                        
                        self.MainMenuPage()                       
                        
                    elif  (downBtn.value()==1):         
                        utime.sleep_ms(100)
                        
                        self.menuLine=self.menuLine+1
                        VariableClass.menuLine = self.menuLine
                        
                        if (self.menuLine>=7):
                            self.menuLine=7
                        self.MainMenuPage()                        
                        
                    elif (selectBtn.value()==1):                        
                        utime.sleep_ms(100)                        
                        self.SubMenuPage()
                        VariableClass.menuPage=2
                        
                        
                elif(self.menuPage==2):
                   
                   
                    
                    if (upBtn.value()==1):
                        utime.sleep_ms(100)
                        VariableClass.subLine=1
                                                                                           
                        self.SubMenuPage()
                        
                        
                    elif  (downBtn.value()==1):         
                        utime.sleep_ms(100)
                        VariableClass.subLine=2
                                                                                             
                        self.SubMenuPage()
                        
                        
                    elif (selectBtn.value()==1):                        
                        utime.sleep_ms(100)
                        
                        if (self.subLine==1):                            
                            self.MainMenuPage()
                            VariableClass.menuPage=1
                           
                        elif(self.subLine==2):                            
                            self.SettingsMenuPage()
                            VariableClass.menuPage=3                          
      
                elif(self.menuPage==3):
                    
                    if (upBtn.value()==1):
                        utime.sleep_ms(100)
                        if (self.menuLine==3):
                            VariableClass.speed=VariableClass.speed+0.25
                            if (self.speed>=10):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                                self.speed=10
                        elif (self.menuLine==4):
                            VariableClass.volume=VariableClass.volume+0.25
                            if (self.volume>=10):
                                self.volume=10
                        elif (self.menuLine==5):
                            VariableClass.direction=True
                        
                        self.SettingsMenuPage()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                        
                          
                        
                    elif  (downBtn.value()==1):         
                        utime.sleep_ms(100)
                        if (self.menuLine==3):
                            VariableClass.speed=VariableClass.speed-0.25
                            if (VariableClass.speed<0.25):
                                VariableClass.speed=0.25
                            
                                                       
                        elif (self.menuLine==4):
                            VariableClass.volume=VariableClass.volume-0.25
                            if (self.volume<=0.25):
                                self.volume=0.25 
                        elif (self.menuLine==5):
                            VariableClass.direction=False
                        
                        self.SettingsMenuPage()
                        
                        
                    if (selectBtn.value()==1):                        
                        utime.sleep_ms(100)                        
                        self.SubMenuPage()
                        VariableClass.settingLine=0
                        VariableClass.menuPage=2
                    
                        
                        
    def MainMenuPage(self):

        if self.menuLine<=1:
            
            mainMenuSwitch.MainMenu(1)
           
        elif self.menuLine==2:
            mainMenuSwitch.MainMenu(2)
            
        elif self.menuLine==3:
            mainMenuSwitch.MainMenu(3)
            
        elif self.menuLine==4:
            mainMenuSwitch.MainMenu(4)
           
        elif self.menuLine==5:
            mainMenuSwitch.MainMenu(5)
            
        elif self.menuLine==6:
            mainMenuSwitch.MainMenu(6)
           
        elif self.menuLine==7:
            mainMenuSwitch.MainMenu(7)
            

    def SubMenuPage(self):        
        
        if self.menuLine==1:
            
            SubMenuSwitch.SubMenu(1)
            
        elif self.menuLine==2:            
            SubMenuSwitch.SubMenu(2)            
        
        elif self.menuLine==3:            
            SubMenuSwitch.SubMenu(3)            
            
        elif self.menuLine==4:            
            SubMenuSwitch.SubMenu(4)            
            
        elif self.menuLine==5:            
            SubMenuSwitch.SubMenu(5)
            
        elif self.menuLine==6:            
            SubMenuSwitch.SubMenu(6)
                        
        elif self.menuLine==7:            
            SubMenuSwitch.SubMenu(7)
    
    def SettingsMenuPage(self):        
        
        if self.menuLine==3:            
            settingMenuSwitch.SettingMenu(3)
            
        elif self.menuLine==4:            
            settingMenuSwitch.SettingMenu(4)            
        
        elif self.menuLine==5:            
            settingMenuSwitch.SettingMenu(5)            
            
        
            
                
    
obj1= MainClass()
    
    

