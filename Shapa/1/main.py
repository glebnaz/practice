from actor import actor
from performances import performances
from labor import labor

a = actor("Gleb","Nazemnov","Andreevich","glavnui","15")
p = performances("12 стульев","2015","322")
cr = labor(a,p,"Остап Бендер","20000000")
print(a)
print(p)
print(cr)
