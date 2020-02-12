def fib(n):
	a,b=0,1
	while a<n:
		print a,
		a,b=b, b+a

def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # The method append() equivalent to result = result + [a], but more efficient.
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'): #no lo entiendo 4.7.1.
    while True:
        ok = raw_input(prompt) #These functions have an optional parameter, commonly known as prompt, which is a string that will be printed on the screen whenever the function is called.
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

def f (a,L=[]):
    L.append(a) #agrega al final de la lista 'a'
    return L

def f(a,L= None):
    if L is None: #con el if me aseguro que no interprete un parametro a externo como default  
        L = []
    L.append(a)
    return L


def make_incrementor(n): #esta funcion incrementa por el valor x a n
    return lambda x: x + n


stack #last-in, first-out

Queues#fila, cola, frist-in,first-out

s='HMDVDLAKSKVSAVSKQMNVPTEGAFKKFSAQVKFDPAKAAQGSAQMTIDVASFDLGDKMYNDQVAGKDWFDAKTYPQATFVSSAIAPAGGNKYNVTGKLTIKGKAETVTVPVTVAQNGATQTFDGVLPIKRSAFNVGTGEWKDTSIVADEVQIKFHLVAT'

b='SATYQFDPSHTYPSFEADHFGGLSVWRGKFDKSSGTVTLDRAAKTGTVDVTTDIASIHTGSAKLDEHLQTAEFFDAAKFPQANYKGTIKFDGDKPVSVVGNLTLHGVTKPLTLKIDSFKCMPHPMLKREVCGVDAVGEFSRDDFGLDYGKQYGFKMKTKLLITAEAVKQ'

wordlist = list(s)# make a list from a word

wordlist= list(b)

s.count('x') #gives you the amount of aminoacids 'x' in the sequence

set(s).intersection(b) #gives you the values that are in both lists, but nothing else.

icrosoft Windows [Version 6.2.9200]
(c) 2012 Microsoft Corporation. All rights reserved.

C:\Users\Username>cd C:\Python27

C:\Python27>python
Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win
32
Type "help", "copyright", "credits" or "license" for more information.
>>>

 WARNING: The script f2py.exe is installed in 'C:\Users\Nico\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\Scripts' 
 which is not on PATH.
 Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.