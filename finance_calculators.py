#program allows user to access different financial calculators:
#investment calculator and home loan repayment calculator

import math

#User option
option = input("Please enter 'investment' to calculate the amount of interest you'll earn on your investment or 'bond' to calculate the amount you'll pay on a home loan ").lower()

#if user option is investment
if option =='investment':
    money_depositing = float(input("please state the amount you are depositing "))
    interest_rateinv = float(input("please state the interest rate as a percentage ")) /100 # to make it a %
    years_investment = int(input("please state the number of years for investment "))

    P = money_depositing
    r = interest_rateinv
    t = years_investment

    interest_option = input("please select ('simple or compund') ").lower()

    if interest_option == "simple":
        interest_option = A = P *(1 + r* t)
        print ("investment amount (simple interest)", A)

    elif interest_option =="compound":
        interest_option = A = P * math.pow ((1+r), t)
        print ("investment amount (compound interest)", A)

    else:
        print ("invalid interest option. please selct 'simple' or 'compound'.")

#if user option is bond    
elif option == "bond":
    present_value = float(input("please state the amount "))
    interest_ratebond = float(input("please state the interest rate ")) /100 # to make it a %
    monthly_interest_ratebond = interest_ratebond /12 # to get monthly interest rates
    months = int(input("please state number of months "))

    #repaid amount per month calculation
    p = present_value #made is a small letter p and capital letter P is storing "money depositing"
    i = monthly_interest_ratebond
    n = months

    repayment = (i * p)/ (1 - ( 1 + i) **(-n))
    print ("montly bond repayment", repayment)
    
else:
    print("invalid option. please select 'investment' or 'bond'.")

