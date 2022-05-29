#Deison Tuiran Londoño

# calcular la ecuacion #1
def formula_1(a,b,c,d,e,f):
    return ((a+(b/c))/(d+(e/f)))

calc_1 = formula_1(1,2,3,4,5,6)
print("calc_1",calc_1)
# calcular la ecuacion #2
def formula_2(a,b,c,d):
    return (a-(b/(c-d)))
calc_2 = formula_2(1,2,3,4)
print("calc_2",calc_2)
# El tercer paso es intercambiar las variables
calc_1,calc_2 = calc_2,calc_1
print("ahora calculo #1 es",calc_1)
print("ahora calculo #2 es",calc_2)
