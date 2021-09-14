# task 3

def number_4():

    # 4
    students = int(input('how many students are there '))
    books = int(input('how many books are there '))

    books_per_student = books//students

    print('each student gets', books_per_student, 'books')
    print('there are', books%students, 'books left over')


def number_5():

    #5
    name = input('enter a name: ')
    print('that name is', len(name), 'letters long!')



question = int(input('which question: '))
if question == 4:
    number_4()
elif question == 5:
    number_5()
