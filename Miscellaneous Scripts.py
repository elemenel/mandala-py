"""Python code to calculate and print multiples of any given number"""
# Define the given number and maximum
my_number = 396
multiple = 3
maximum = my_number * 10

# Initialize an empty list to store the multiples
multiples = []

# Iterate from the given number to the maximum, adding 3rd multiples to the list
for number in range(my_number * multiple, maximum):
    if number % my_number == 0:
        multiples.append(number)
print(multiples)


# Earth Frequencies
# def third_multiples(n, max):
#     third_multiples = []
#     for i in range(3, max + 1, 396):
#         if i <= max:
#             third_multiples.append(i)
#     return third_multiples
# my_number = 396
# print(f'Result of Third_Multiples: {third_multiples(my_number, my_number* 10)}')


# def my_multiples(value, length):
#     my_numbers =  [*range(value, length*value+1, value)]
#     return my_numbers
#     print(f'Result of m_multiples: {my_numbers}')
# my_multiples(396, 10)
# print(f'Result of my_multiples: {my_multiples}')

# value = int(input('Enter a number:   '))
# length = int(input('Enter a limit:   '))
# multiples(value, length)
# print(f'{multiples(value, length)}')


"""Simple Test of angle integrity"""


def test_angle():
    import turtle

    turtle.shape("blank")
    turtle.pensize(4)
    turtle.setup(500, 500)
    turtle.pencolor("white")
    turtle.bgcolor("black")
    turtle.speed(0)
    test_angle = turtle.numinput("Enter the test angle number", "Input Here", 90)
    while True:
        turtle.left(test_angle)
        turtle.fd(150)
        if abs(turtle.pos()) < 1:
            break


# test_angle()
