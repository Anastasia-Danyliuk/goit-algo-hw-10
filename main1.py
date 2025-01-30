import pulp

model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total"

model += 2 * lemonade + 1 * fruit_juice <= 100
model += 1 * lemonade <= 50
model += 1 * lemonade <= 30
model += 2 * fruit_juice <= 40

model.solve()

print("Виробляти лимонаду:", lemonade.varValue)
print("Виробляти фруктового соку:", fruit_juice.varValue)
print("Максимальна кількість вироблених продуктів:", pulp.value(model.objective))