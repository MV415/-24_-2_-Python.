# TODO Найдите количество книг, которое можно разместить на дискете
bytes = 4
symbol_ = 25
str_ = 50
s = 100
memory = 1.44
book  = bytes * symbol_ * str_ * s
len_ = memory * 1024 * 1024 // book
print("Количество книг, помещающихся на дискету:", int(len_))
