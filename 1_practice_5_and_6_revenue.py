revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    print('Деятельность фирмы является прибыльной')
    profit = revenue - costs
    profitability = revenue/profit
    print('Рентабельность (в %):', profitability * 100)
    employees = int(input('Введите кол-во сотрудников фирмы: '))
    print('Прибыль фирмы в расчёте на одного сотрудника:', profit/employees)
elif revenue < costs:
    print('Деятельность фирмы является убыточной')
