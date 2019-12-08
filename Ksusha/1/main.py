from typeOfCredit import types
from client import client
from credit import credit

t = types("Деловой","Быть Деловым Мальчиком",15,"12.10.2020")
c = client("Сгу","Государственная","Астраханская 83","500-599","Чумаченко")
cr = credit(t,c,"152154","9.10.2018")
print(t)
print(c)
print(cr)
