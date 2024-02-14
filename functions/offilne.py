import os
import subprocess as sp
path={
    'notepad':'C:\\Users\\ASUS\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe',
    'calculator':r'C:\Windows\System32\calc.exe',
    'microsoftword':r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
    }

#open notepad
def notepad():
    os.startfile(path['notepad'])

#open calculator
def calculator(): 
    os.startfile(path['calculator'])

#open microsoft word 
def microsoftword():
    os.startfile(path['microsoftword'])
#open cmd
def cmd():
    os.system('start cmd')
