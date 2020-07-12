import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type', help='which indicates the type of payments: "annuity" or "diff" (differentiated).',
                    type=str)
parser.add_argument('--payment', help='that is a monthly payment',
                    type=int)
parser.add_argument('--principal', help='is used for calculations of both types of payment. ', type=int)
parser.add_argument('--periods', help='parameter denotes the number of months and/or years needed to repay the credit.',
                    type=int)
parser.add_argument('--interest', help=' is specified without a percent sign. '
                                       'Note that it may accept a floating-point value', type=float)
args = parser.parse_args()

t = args.type
p = args.principal
a = args.payment
ci = args.interest
n = args.periods


def differentiated_payment(p, n, ci):
    i = ci / (12 * 100)
    list_of_payments = []
    for m in range(1, n + 1):
        d = (p / n) + i * (p - ((p * (m - 1)) / n))
        list_of_payments.append(math.ceil(d))
        print(f'Month {m}: paid out {math.ceil(d)}')

    overpayment = sum(list_of_payments) - p
    print()
    print(f'Overpayment = {overpayment}')


def count_of_month(p, a, ci):
    i = ci / (12 * 100)
    n = math.ceil(math.log(a / (a - i * p), (1 + i)))
    year = round(n / 12)
    month = math.ceil(n % 12)
    if month != 0:
        print(f'You need {year} years and {month} months to repay this credit!')
    elif month == 0 and year > 1:
        print(f'You need {year} years to repay this credit!')
    elif month != 0 and year == 1:
        print(f'You need {year} year and {month} months to repay this credit!')
    elif month == 0 and year == 1:
        print(f'You need {year} year to repay this credit!')
    elif year == 0 and month > 1:
        print(f'You need {month} months to repay this credit!')
    elif year == 0 and month == 1:
        print(f'You need {month} month to repay this credit!')
    overpayment = (a * n) - p
    print(f'Overpayment = {overpayment}')


def annuity_monthly_payment(p, n, ci):
    i = ci / (12 * 100)
    a = math.ceil(p * ((i * (math.pow((1 + i), n))) / (math.pow((1 + i), n) - 1)))
    print(f'Your annuity payment = {a}!')
    overpayment = math.ceil((a * n) - p)
    print(f'Overpayment = {overpayment}')


def credit_principal(a, n, ci):
    i = ci / (12 * 100)
    p = int(a / ((i * (math.pow((1 + i), n))) / (math.pow((1 + i), n) - 1)))
    print(f'Your credit principal = {p}!')
    overpayment = math.ceil((a * n) - p)
    print(f'Overpayment = {overpayment}')


if t == 'diff':
    try:
        differentiated_payment(p, n, ci)
    except TypeError:
        print('Incorrect parameters.')
elif t == 'annuity':
    try:
        if a and n:
            credit_principal(a, n, ci)
        elif p and n:
            annuity_monthly_payment(p, n, ci)
        elif p and a:
            count_of_month(p, a, ci)
    except TypeError:
        print('Incorrect parameters.')
