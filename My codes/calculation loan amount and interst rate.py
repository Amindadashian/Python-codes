loan_principal_amount=int(input('please insert the amount of loan =  '))
number_of_installment=int(input('please insert the number of installments--->  '))
interest_rate=float(input('insert interest rate =  '))
#نرخ بهره
loan_interest=loan_principal_amount*(number_of_installment+1)*interest_rate/2400
loan_amount_paid=loan_interest+loan_principal_amount
amount_of_installment = loan_amount_paid //number_of_installment
print('loan amount paid=',loan_amount_paid, 'amount of installment =',amount_of_installment)
continue_condition=input('do you want to continiue(y/n)=  ')
#if continue_condition[0] =='n':


