import os, time, sys, time, random
from re import findall

try:
    import rich, sympy, inquirer, fractions

except ModuleNotFoundError:
    os.system('pip3 install rich sympy inquirer fractions')


import rich
from inquirer import List, prompt
from sympy import *
from sympy.abc import x,y,z,a,b,c
from rich.panel import Panel
from fractions import Fraction

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
        print('\nhasil integral:\n')
        pprint(result); print('')
    
    def integral_defined(self):
        # integrate(function, (variabel, down, up))
        result = integrate(self.func, (self.var, self.bBawah, self.bAtas))
        rich.print(Panel(str(result), style='green', title='[ hasil ]'))
    
    def diferensial(self):
        result = diff(self.func)
        print('\nhasil turunan:\n')
        pprint(result); print('')
        
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
    
    def equation4(self):
        result = solve((self.func, self.func2, self.func3, self.func4))
        rich.print(Panel(str(result), title='[ hasil ]', style='green'))

class MATRIKS:
    
    def __init__(self, e=0, f=0, g=0, h=0, i=0, j=0, k=0, l=0, m=0, n=0, o=0, p=0, q=0, r=0, s=0, t=0):
         
        self.a = e; self.d = h; self.g = k; self.j = n; self.m = q; self.p = t 
        self.b = f; self.e = i; self.h = l; self.k = o; self.n = r
        self.c = g; self.f = j; self.i = m; self.l = p; self.o = s 
    
    def matrix22(self):
        
        Matriks = Matrix(2,2,(self.a, self.b, 
                              self.c, self.d))
        
        print('\nMatriks:\n'); pprint(Matriks)
        print(f'\nNilai determinan: {Matriks.det()}')
        print('Nilai Invers:\n')
        pprint(Matriks.inv())
        print('\nNilai Transpos:\n')
        pprint(Matriks.transpose()); print('')    
        
    def matrix33(self):
        
        Matriks = Matrix(3,3,(self.a, self.b, self.c,
                              self.d, self.e, self.f,
                              self.g, self.h, self.i))
        
        print('\nMatriks:\n'); pprint(Matriks)
        print(f'\nNilai determinan: {Matriks.det()}')
        print('Nilai Invers:\n')
        pprint(Matriks.inv())
        print('\nNilai Transpos:\n')
        pprint(Matriks.transpose()); print('')
        
    def matrix44(self):
        
        Matriks = Matrix(4,4,(self.a, self.b, self.c,self.d,
                              self.e, self.f, self.g, self.h,
                              self.i, self.j, self.k, self.l,
                              self.m, self.n, self.o, self.p))
        
        print('\nMatriks:\n'); pprint(Matriks)
        print(f'\nNilai determinan: {Matriks.det()}')
        print('Nilai Invers:\n')
        pprint(Matriks.inv())
        print('\nNilai Transpos:\n')
        pprint(Matriks.transpose()); print('')
               
def main_screen():
        
    if os.name == 'nt':
        os.system('cls')
        
    else : os.system('clear')
    
    data_screens = ['','Welcome to my script!',20*'=', '  ψ Author: BlackCid00', '', '\tPersamaan Linear', '\tKalkulus', '\tMatrix']
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
            kalkulus2(func1, func2, func3, func4).equation4()
        
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
            function = input('\nlim ')
            limit = Fraction(input('x-> '))
            kalkulus1(function, batas_limit=limit).limit()
            
        elif choice_kalkulus['math_kalkulus'] == "● Diferensial":
            F1 = input('\nMasukkan persamaan: ')
            kalkulus1(F1).diferensial()
            
        elif findall('Integral tentu', str(choice_kalkulus['math_kalkulus'])):
            function = input('\nʃ ')
            batas_atas = Fraction(input('\nBatas atas = ')).limit_denominator()
            batas_bawah = Fraction(input('Batas bawah = ')).limit_denominator()
            kalkulus1(function, batas_atas=batas_atas.limit_denominator(), batas_bawah=batas_bawah.limit_denominator()).integral_defined()
                
        elif findall('tak tentu', str(choice_kalkulus['math_kalkulus'])):
            function = input('\nʃ ')
            kalkulus1(function).integral_NOdefined()

    elif choice1['math'] == '\tMatrix':
        
        choice_matrix = prompt([
            List(
                name='math_matrix',
                choices=data_screen3
            )
        ])
        
        from example_matriks import mtx2, mtx3, mtx4
        
        if findall('2 x 2', choice_matrix['math_matrix']):
            
            print('')
            rich.print(Panel(mtx2, title='[ matrix 2 x 2 ]', style='magenta'))
            
            a = input("\na : "); b = input('b : ')
            c = input('c : '); d = input('d : ')
            
            MATRIKS(a,b,c,d).matrix22()
            
        elif findall('3 x 3', choice_matrix['math_matrix']):
            
            print('')
            rich.print(Panel(mtx3, title='[ matrix 3 x 3 ]', style='magenta'))

            a = input("\na : "); b = input('b : ')
            c = input('c : '); d = input('d : ')
            e = input('e : '); f = input('f : ')
            g = input('g : '); h = input('h : ')
            i = input('i : ')

            MATRIKS(a,b,c,d,e,f,g,h,i).matrix33()
            
        elif findall('4 x 4', choice_matrix['math_matrix']):
            print('')
            rich.print(Panel(mtx4, title='[ matrix 4 x 4 ]', style='magenta'))
            
            a = input("\na : "); b = input('b : ')
            c = input('c : '); d = input('d : ')
            e = input('e : '); f = input('f : ')
            g = input('g : '); h = input('h : ')
            i = input('i : '); j = input('j : ')
            k = input('k : '); l = input('l : ')
            m = input('m : '); n = input('n : ')
            o = input('o : '); p = input('p : ')

            MATRIKS(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p).matrix44()

if __name__ == '__main__':
    main_screen()
            
            