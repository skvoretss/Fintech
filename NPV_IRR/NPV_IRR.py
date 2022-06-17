# getting value with checking mistakes
print("Please, input par value:")
par = float(input())
while par <= 0:
    print("Par value is out of range, try again:")
    par = float(input())
    
print("Please, choose type of procent - simple or compounding [s/c]:")
tp = input()
while (tp != 's') and (tp != 'c'):
    print('Wrong value for type of procent, try again [s/c]')
    tp = input()
    
print("Please, input coupon income(in procent):")
ci = float(input())
while (ci <= 0) or (ci > 100):
    print("Coupon income value is out of range, try again:")
    ci = float(input())

if tp == 'c':
    print("Please, input accrual period(in months):")
    ap = int(input())
    while (ap <= 0) or (ap > 12) or (12 % ap != 0):
        print("Accrual period value is out of range or 12%ap != 0, try again:")
        ap = int(input())
      
    print("Please, choose continuous compounding [n/y]:")
    cc = input()
    while (cc != 'n') and (cc != 'y'):
        print('Wrong value for continuous compounding, try again [n/y]')
        cc = input()
    
print("Please, input maturity date(in years):")
md = int(input())
while md <= 0:
    print("Maturity date value is out of range, try again:")
    md = int(input())
    
print("Please, input discount rate(in procent):")
r = float(input())
while (r > 100) or (r <= 0):
    print("Discount rate value is out of range, try again:")
    r = float(input())
    
# starting calculation

# CF
if tp == 's': # если процент простой
    CF = ci/100*par
        
else: # если процент сложный
    if cc == 'y': # если есть непрерывное начисление
        CF = par*exp(ci/100) - par

    else:
        times = 12/ap # считаем, сколько раз за год происходила капитализация
        CF = par*(1+(ci/100)/times)**times - par

# NPV
PV = par
FV = 0
for t in range(1, md + 1):
    df = 1/((1+r/100)**t)
    if t == md:
        CF += par
    FV += CF*df        
print("NPV = ", FV - PV)

# IRR
print("IRR_min = ", -1 + ( ((CF-par)*(md-1) + CF) / par )**(1/md) )

