def sum_2020_entries(textfile):
    expenses=[]
    with open(textfile) as file:
        for line in file:
            expenses.append(int(line))
    expenses=set(expenses)
    for expense_1 in expenses:
        for expense_2 in expenses:
            total=expense_1+expense_2
            if total==2020:
                return expense_1,expense_2
exp1,exp2=sum_2020_entries("expenses.txt")
print(exp1*exp2)
