import os, time, sys, time, random
from re import findall

try:
    import rich, sympy, inquirer

except ModuleNotFoundError:
    os.system('pip3 install rich sympy inquirer')


import rich
from inquirer import List, prompt
from sympy import *
from sympy.abc import x,y,z,a,b,c
from rich.panel import Panel


class kalkulus1:
    
    def __init__(self, function, variabel=x, batas_limit=0, batas_atas=0, batas_bawah=0):
        
        self.func = function
        self.bLim = batas_limit
        self.bAtas = batas_atas
        self.bBawah = batas_bawah
        self.var = variabel
        
    def limit(self):
        result = limit(self.func, self.var, self.bLim)
        rich.print(Panel(str(result), title='[ hasil ]', style='green'))
    
    def equation(self):
        result = solve({self.func})
        rich.print(Panel(str(result), title='[ hasil ]', style='green'))
        
    def integral_NOdefined(self):
        result = integrate(self.func)
        pprint('hasil: '+str(result))
    
    def integral_defined(self):
        # integrate(function, (variabel, down, up))
        result = integrate(self.func, (self.var, self.bBawah, self.bAtas))
        rich.print(Panel(str(result), style='green', title='[ hasil ]'))
    
    def diferensial(self):
        result = diff(self.func)
        pprint('hasil: '+str(result))
        
class kalkulus2:
    
    def __init__(self, function='', function2='', function3='', function4='') -> str :
        
        self.func = function
        self.func2 = function2
        self.func3 = function3
        self.func4 = function4
    
    def equation2(self):
        result = solve((self.func, self.func2))
        rich.print(Panel(str(result), title='[ hasil ]', style='green'))
    
    def equation3(self):
        result = solve((self.func, self.func2, self.func3))
        rich.print(Panel(str(result), title='[ hasil ]', style='green'))
    
    def equation3(self):
        result = solve((self.func, self.func2, self.func3))
        rich.print(Panel(str(result), title='[ hasil ]', style='green'))
    
    def equation4(self):
        result = solve((self.func, self.func2, self.func3, self.func4))
        rich.print(Panel(str(result), title='[ hasil ]', style='green'))
        
    
def main_screen():
        
    if os.name == 'nt':
        os.system('cls')
        
    else : os.system('clear')
    
    data_screens = ['','Welcome to my script!',20*'=', '', '\tPersamaan Linear', '\tKalkulus', '\tMatrix']
    data_screen1 = ['','● Persamaan 1 variabel (SPLSV)','● Persamaan 2 variabel (SPLDV)',
                    '● Persamaan 3 variabel (SPLTV)','● Persamaan 4 variabel (SPLEV)'] 
    data_screen2 = ['','● Limit', '● Integral tentu',
                    '● Integral tak tentu', '● Diferensial']
    data_screen3 = ['', '● Matrix 2 x 2', '● Matrix 3 x 3', '● Matrix 4 x 4']

    choice1 = prompt([
        List ('math',
                message='pilih',
                choices=data_screens)
    ])
    
    if choice1['math'] == '\tPersamaan Linear':
        
        choice_linear = prompt([
            List(
                    name = 'math_linear',
                    choices= data_screen1)
        ])

        if findall('SPLSV', str(choice_linear['math_linear'])):
            function = input ('\nMasukkan persamaan: ')
            kalkulus1(function).equation()
            
        elif findall("SPLDV", str(choice_linear['math_linear'])):
            func1 = input ('\nMasukkan persamaan pertama: ')
            func2 = input ("Masukkan persamaan kedua: ")
            kalkulus2(func1,func2).equation2()
            
        elif findall('SPLTV', str(choice_linear['math_linear'])):
            func1 = input("\nMasukkan persamaan pertama: ")
            func2 = input('Masukkan persamaan kedua: ')
            func3 = input("Masukkan persamaan ketiga: ")
            kalkulus2(func1, func2, func3).equation3()
            
        elif findall('SPLEV', str(choice_linear['math_linear'])):
            func1 = input("\nMasukkan persamaan pertama: ")
            func2 = input('Masukkan persamaan kedua: ')
            func3 = input("Masukkan persamaan ketiga: ")
            func4 = input('Masukkan persamaan keempat: ')
            kalkulus2(func1, func2, func3, func4).equation3()
        
        else:
            print('')
            rich.print(Panel('invalid choice!', title='[ pesan error ]', style='red'));sys.exit('\n')

    elif choice1['math'] == '\tKalkulus':
        
        choice_kalkulus = prompt([
            List(
                name="math_kalkulus",
                choices= data_screen2
            )
        ])
        
        if choice_kalkulus['math_kalkulus'] == '● Limit':
            return 0
        elif choice_kalkulus['math_kalkulus'] == "● Diferensial":
            F1 = input('\nMasukkan persamaan: ')
            kalkulus1(F1).diferensial()
            
        elif findall('tentu', str(choice_kalkulus['math_kalkulus'])):
            return 0
        elif findall('tak tentu', str(choice_kalkulus['math_kalkulus'])):
            return 0

    elif choice1['math'] == '\tMatrix':
        
        choice_matrix = prompt([
            List(
                name='math_matrix',
                choices=data_screen3
            )
        ])
            
if __name__ == '__main__':
    main_screen()
            
            