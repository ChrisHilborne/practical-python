# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_payed = 0.0
extra_payment_start_month = 0
extra_payment_end_month = 0
extra_payment = 1000

month = 1
while principal > 0:
    principal = principal * (1 + rate/12) - payment
    if (principal < 0):
        print('negative principal')
        payment = principal + payment
        principal = 0
    total_payed = total_payed + payment
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_payed = total_payed + extra_payment
    print(f'{month:<4} {total_payed:10.2f<6} {principal:10.2f}'
    month = month + 1
    

print('total payed:', total_payed)
print('in', month  , 'months')
