
isbn = input('input isbn: ')

isbn_list = list(isbn)

for ind, item in enumerate(isbn_list):
    try:
        int(item)
    except:
        isbn_list.remove(item)

calculated_digit = 0

count = 0

while count < 12:
    calculated_digit += int(isbn_list[count])
    count += 1
    calculated_digit += int(isbn_list[count])*3
    count += 1

calculated_digit = calculated_digit%10

calculated_digit = 10 - calculated_digit

if calculated_digit == 10:
    calculated_digit = 0

if calculated_digit == int(isbn_list[12]):
    print(isbn, 'is valid')
else:
    print(isbn, 'is invalid')
