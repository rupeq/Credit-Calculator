from math import ceil, floor, log, pow


def select_action():
    task = input('''What do you want to calculate? 
type "n" - for count of months,
type "a" - for annuity monthly payment, 
type "p" - for credit principal: \n''')

    if task == 'n':
        get_months()
    elif task == 'a':
        get_annuity()
    elif task == 'p':
        get_principal()


def get_months():
    principal = float(input('Enter credit principal: \n'))
    monthly_payment = int(input('Enter monthly payment: \n'))
    interest = float(input('Enter credit interest: \n'))
    nominal_rate = interest / (12 * 100)

    months_to_pay = ceil(log((monthly_payment / (monthly_payment - nominal_rate * principal)), (1 + nominal_rate)))

    years = months_to_pay // 12
    months = months_to_pay % 12

    if years >= 1:
        if months >= 1:
            print(f'You need {years} years and {months} months to repay this credit!')
        else:
            print(f'You need {years} years to repay this credit!')
    else:
        print(f'You need {months} months to repay this credit!')


def get_annuity():
    principal = float(input('Enter credit principal: \n'))
    months_to_pay = int(input('Enter count of periods: \n'))
    interest = float(input('Enter credit interest: \n'))
    nominal_rate = interest / (12 * 100)

    annuity = ceil((principal * (nominal_rate * pow((1 + nominal_rate), months_to_pay))
                    / (pow((1 + nominal_rate), months_to_pay) - 1)))

    print(f'Your annuity payment = {annuity}!')


def get_principal():
    monthly_payment = float(input('Enter monthly payment: \n'))
    months_to_pay = int(input('Enter count of periods: \n'))
    interest = float(input('Enter credit interest: \n'))
    nominal_rate = interest / (12 * 100)

    principal = floor((monthly_payment / ((nominal_rate * pow((1 + nominal_rate), months_to_pay))
                                          / (pow((1 + nominal_rate), months_to_pay) - 1))))

    print(f'Your credit principal = {principal}!')


select_action()