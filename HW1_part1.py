
# Python. HW_1.
# Part_1

#1) Создать переменную типа String
Str_item = 'Oleg'

#2) Создать переменную типа Integer
Int_item = 30

#3) Создать переменную типа Float
Float_item = 4.5

#4) Создать переменную типа Bytes
Bytes_item = b'Anton'

#5) Создать переменную типа List
List_item = [1,5,7]

#6) Создать переменную типа Tuple
Tuple_item = tuple('hello, world!')

#7) Создать переменную типа Set
Set_item = {1, 2, 3, 4, 5, 6}

#8. Создать переменную типа Frozen set
Frozen_set_item = frozenset({1})

#9) Создать переменную типа Dict
dict_item = {'age':25,
             'name':'Diana',
             'location':{'country':'Russia',
                         'city':'Novosibirsk'}}

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print('Str_item', '-', type(Str_item), "\n",
      'Int_item', '-',type(Int_item), "\n",
      'Float_item', '-', type(Float_item), "\n",
      'Bytes_item', '-', type(Bytes_item), "\n",
      'List_item', '-', type(List_item), "\n",
      'Tuple_item', '-', type(Tuple_item), "\n",
      'Set_item', '-', type(Set_item), "\n",
      'Frozen_set_item', '-', type(Frozen_set_item), "\n",
      'dict_item', '-', type(dict_item))

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
item1 = "Robert"
item2 = "Kate"
item3 = item1 + item2
print(item3)

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
item4 = 15
print(item1, item2, item4)

#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(item1 + ' ' + item2 + ' ' + str(item4))