def sum_2020_entries(textfile):
    expenses=[]
    with open(textfile) as file:
        for line in file:
            expenses.append(int(line))
    expenses=set(expenses)
    for expense_1 in expenses:
        for expense_2 in expenses:
            for expense_3 in expenses:
                total=expense_1+expense_2+expense_3
                if total==2020:
                    return expense_1,expense_2,expense_3
exp1,exp2,exp3=sum_2020_entries("expenses.txt")
print(exp1*exp2*exp3)
