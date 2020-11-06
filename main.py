
def create_phone_number(n):
    return '(' + ''.join([str(num) for num in n[:3]]) + ') ' + \
           ''.join([str(num) for num in n[3:6]]) + '-' + ''.join([str(num) for num in n[6:]])


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
