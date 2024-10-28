mutable_list = [3, 4, True, 'food']
print(mutable_list)
mutable_list[0] = 5
mutable_list.extend(['apple'])
print(mutable_list)
immutable_var = 1, 2, False, 'string'
print(immutable_var)
immutable_var[0] = 3 # заведомо недопустимое действие, так как
print(immutable_var) # immutable_var относится к кортежу (неизменяемым коллекциям)
