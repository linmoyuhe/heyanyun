#!/usr/bin/env python3
import sys
if __name__ == '__main__':
   if len(sys.argv) != 1:
     for arg in sys.argv[1:]:
            try:
                argv_str = arg.split(':')
            except:
                print("Parameter Error")
            ID = argv_str[0]
            salary = argv_str[1]
            try:
               int_salary = int(salary)
            except:
               print("Parameter Error")
            social_security_fee = int_salary * 16.5 / 100
            tax_salary = int_salary - social_security_fee - 3500
     
            if tax_salary <= 1500:
               tax_rate, quick_deduction = 0.03, 0
            elif tax_salary <= 4500:
               tax_rate, quick_deduction = 0.1, 105
            elif tax_salary <= 9000:
               tax_rate, quick_deduction = 0.2, 555
            elif tax_salary <= 35000:
               tax_rate, quick_deduction = 0.25, 1005
            elif tax_salary <= 55000:
               tax_rate, quick_deduction = 0.3, 2755
            elif tax_salary <= 80000:
               tax_rate, quick_deduction = 0.35, 5505
            else: 
               tax_rate, quick_deduction = 0.45, 13505
            tax_payable = tax_salary * tax_rate - quick_deduction
            if tax_payable <= 0:
               tax_payable = 0
            after_tax_salary = int_salary - social_security_fee - tax_payable
            print(ID + ':' + format(after_tax_salary, '.2f'))  
   else:
       print("Parameter Error")
   sys.exit(0)

