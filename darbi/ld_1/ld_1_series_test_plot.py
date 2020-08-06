from math import exp
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def mana_funkcija(x):
    a = (1+x)*pow(x,0)/(1)
    s = 0
    s = s + a
    k = 0
    while k < 1000:
        if k ==0:
            print('a0 = %e\tS0 =%.2f\n'%(a,s))
        k = k+1
        a = a*x/(k);
        s = s+a
        if k == 999:
            print('a999 = %Le\tS999 =%.2Lf\n'%(a,s))
        
    print('a1000 = %e\tS1000 =%.2f\n'%(a,s))

def mana_funkcija_plt(x):
    a = (1+x)*pow(x,0)/(1)
    s = 0
    s = s + a
    k = 0
    while k < 1000:
        k = k+1
        a = a*x/(k);
        s = s+a
    return s

print('Funkcijas (1+x)*exp(x) aprēķināšana: \n')
x = float(input('Lietotājs, lūdzu, ievadi x vērtību: '))            # x vērtība pieder no -∞ līdz ∞ 
y = (1+x)*exp(x)

print('(1 + %.2f)*exp(%.2f) = %.2f\n'%(x,x,y))

mana_funkcija(x)
        
print('\n')
print('\t\t1000\n')
print('\t\t----\n')
print('\t\t\\\t\t        k\n')
print('\t\t \\\t\t(1+x)*x\n')
print('f(x)=\t\t|\t    ----------------\n')
print('\t\t /\t\t   k!\n')
print('\t\t/\n')
print('\t\t----\n')
print('\t\tk=0\n')

print('\n')
print('\t\t\tx\n')
print('R=\t\t   -----------\n')
print('\t\t\tk\n')

x= np.arange(0.0,10.0,0.01)
y = (1+x)*np.exp(x)
yy = mana_funkcija_plt(x)

ax1=plt.subplot(121)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcijas f(x) grafiku, zīmēšana izmantojot funkcijas izteiksmi')
plt.grid()

box = ax1.get_position()
box.x0 = box.x0 - 0.05
box.x1 = box.x1 - 0.05
ax1.set_position(box)

ax2=plt.subplot(122)
plt.plot(x,yy)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Funkcijas f(x) grafiku, zīmēšana izmantojot Teilora rindas izteiksmi')
plt.grid()
plt.show()

