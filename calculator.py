#!/usr/bin/env python3
import sys
if  __name__ == '__main__':
    
 if len(sys.argv) == 2:
        salary = sys.argv[1] 
	tax_salary = int(salary) - 3500
        tax_payable = tax_salary * tax_rate - quick_deduction    
        if tax_salary < = 1500:
	   tax_rate, quick_deduction = 0.03, 0
	elif tax_salary < = 4500:
	     tax_rate, quick_deduction = 0.1, 105
	elif tax_salary < = 9000:
	     tax_rate, quick_deduction = 0.2, 555
        elif tax_salary < = 35000:
	     tax_rate, quick_deduction = 0.25, 1005	
	elif tax_salary < = 55000:
	     tax_rate, quick_deduction = 0.3, 2755
	elif tax_salary < = 80000:
	     tax_rate, quick_deduction = 0.35, 5505 
	else:
 	    tax_rate, quick_deduction = 0.45, 13505   
	    print(format(tax_payable,'.2f'))
    # except:
	   # print("Parameter Error")
    # finally:
	     sys.exit(0)
 else:
     print("Parameter error")

