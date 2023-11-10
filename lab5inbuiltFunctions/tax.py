def getIncomeTax(salary):

    personalAllowance = 11850
    basicLimit = 34500
    higherLimit = 150000
    additionalLimit = 1000000


#if persons salary is less than or equal to personal allowance they are subject to no tax
#if the salary is above personal allowance code moves on to next condition
#if the salary is <= 34500 - 20% tax - subract personal allowance from salary and multiply is by 0.2
#if the salary is <= 150000
    if salary <= personalAllowance:
        tax = 0
    elif salary <= basicLimit:
        tax = (salary - personalAllowance) * 0.2
    elif salary <= higherLimit:
        tax = (basicLimit - personalAllowance) * 0.2 + (salary - basicLimit) * 0.4
    else: 
        tax = (basicLimit - personalAllowance) * 0.4 + (salary - higherLimit) * 0.45
    return tax
