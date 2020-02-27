from math import exp

print('Funkcijas (1+x)*exp(x) aprēķināšana: \n')
x = float(input('Lietotājs, lūdzu, ievadi x vērtību: '))
y = (1+x)*exp(x)

print('(1 + %.2f)*exp(%.2f) = %.2f\n'%(x,x,y))

a = (1+x)*pow(x,0)/(1);
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
