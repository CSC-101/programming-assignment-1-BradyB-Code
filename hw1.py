import data
import math
from data import Rectangle


# Write your functions for each part in the space below.

# Part 1
#Takes input of a string, turns it into lowercase to ensure that we check upper and lowercase letters
#use a for loop to iterate through the string to check for vowels with individual if statements
#initialize an int variable called count and up the counter for every vowel.
def vowel_count(word: str)->int:
    word1 = word.lower()
    count = 0
    for x in word1:
        if x == 'a':
            count += 1
        elif x == 'e':
            count += 1
        elif x == 'i':
            count += 1
        elif x == 'o':
            count += 1
        elif x == 'u':
            count += 1
    return count

# Part 2
#Takes a nested list as the input, iterates through the main list with a for loop
#checks if the nested loops have exactly 2 elements with an if statement
#this is all done in a list comprehension so it is saved to a list separate from the input.
def short_lists(list1: list[list[int]])->list:
    list2 = [x for x in list1 if (len(x) == 2)]
    return list2

# Part 3
#Input is a nested loop, list comprehension that checks for the nested loops with two elements
#then the for loop checks the newly created list from the comprehension and an if statement
#determines if the nested loops are in ascended pairs, if not then a place holder variable is
#used to allow the two elements to switch positions.
def ascending_pairs(list3: list[list[int]])->list:
    list_pairs = [x for x in list3 if (len(x) == 2)]
    place_holder = 0
    for y in list_pairs:
        if y[0] > y[1]:
            place_holder = y[1]
            y[1] = y[0]
            y[0] = place_holder
    return list_pairs

# Part 4
#Input is two prices from the Price class in the data file. Total cents and the residual
#dollars from the cents place is created as new variables
#use and if and elif statement to choose whether to combine the cents and add to the
#total number of dollars if the cents is over 100
#initialize new Price instance with the total dollars and cents and return that instance.
def add_prices(p1: data.Price, p2: data.Price)->data.Price:
    total_cents = 0
    dol = 0
    if p1.cents + p2.cents >= 100:
        dol = int((p1.cents + p2.cents) // 100 )
        total_cents = (p1.cents + p2.cents) % 100
    elif p1.cents + p2.cents < 100 and (p1.cents + p2.cents) >= 0:
        total_cents = p1.cents + p2.cents
    total_dollars = p1.dollars + p2.dollars + dol
    new_price = data.Price(total_dollars, total_cents)
    return new_price

# Part 5
#Input is from the Rectangle class. We find the height and width by taking the x and y coordinate,
#respectively, from the attributes of the Rectangle class
#return the absolute value of the height and width multiplied to get the area as a positive float.
def rectangle_area(r1: data.Rectangle)->float:
    height = r1.top_left.x - r1.bottom_right.x
    width = r1.bottom_right.y - r1.top_left.y
    return abs(height * width)

# Part 6
#Takes an author's name and a list containing elements of the Book class
#create a new list to store the elements of the Book class with the right author
#which will be determined with an if statement. The for loop iterates through each
#element of the input list. The if statement is True, it adds that element to the
#newly created list, which is eventually returned.
def books_by_author(name: str, books: list[data.Book])->list[data.Book]:
    books_b_a = []
    for book in books:
        if book.authors == name:
            books_b_a.append(book)
    return books_b_a

# Part 7
#Input is of the Rectangle class. We find the distance between the two x coords and the
#two y coords to calculate the hypotenuse of the rectangle. Half of the hyp is the radius
#of the circle so we create a new instance of the Circle class and set the center point
#and the radius. We then return this instance of the Circle class.
def circle_bound(r3: data.Rectangle)->data.Circle:
    x2 = abs(r3.bottom_right.x - r3.top_left.x)
    y2 = abs(r3.top_left.y - r3.bottom_right.y)
    hyp = round(math.sqrt(x2 ** 2 + y2 ** 2), 1)
    circle1 = data.Circle(data.Point(r3.bottom_right.x - x2//2, r3.top_left.y - y2//2), hyp/2)
    return circle1

# Part 8
#Input is a list of employees from the Employee class. Create a variable for the sum
#which we will use to find the average. We up the sum count through a for loop, then
#divide it by the length of the list to find the avg. Then for loop through the input
#list to check if the staff are underpaid. The list we created at the start will save
#the names of the employees that were underpaid.
def below_pay_average(employees: list[data.Employee])->list[str]:
    sum = 0
    underpaid_staff = []
    for x in employees:
        sum += x.pay_rate
    avg_pay = round(sum / len(employees), 2)
    for check in employees:
        if avg_pay > check.pay_rate:
            underpaid_staff.append(check.name)
    return underpaid_staff

