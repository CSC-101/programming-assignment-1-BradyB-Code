import data
import hw1
import unittest

from data import Rectangle


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input: str = "petAl"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input: str = "FOiLed"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected, result)

    # Part 2
    def test_small_lists_1(self):
        input = [[1,0], [5, 6], [6, 7, 8]]
        result = hw1.short_lists(input)
        expected = [[1,0], [5, 6]]
        self.assertEqual(expected, result)

    def test_small_lists_2(self):
        input = [[9, 4], [5, 6, 7, 8], [6, 7, 8], [10, 5]]
        result = hw1.short_lists(input)
        expected = [[9, 4], [10, 5]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input = [[15,20], [500, 61], [6, 7, 8]]
        result = hw1.ascending_pairs(input)
        expected = [[15, 20], [61, 500]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input = [[2,5], [6, 7, 8], [1, 61], [21, 3]]
        result = hw1.ascending_pairs(input)
        expected = [[2, 5], [1, 61], [3, 21]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        input1= data.Price(5, 95)
        input2 = data.Price(12, 99)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(18, 94)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        input1= data.Price(10, 35)
        input2 = data.Price(12, 15)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(22, 50)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area_1(self):
        input = data.Rectangle(data.Point(4, 4), data.Point(0, 1))
        result = hw1.rectangle_area(input)
        expected = 12
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        input = data.Rectangle(data.Point(10, 4), data.Point(13, 2))
        result = hw1.rectangle_area(input)
        expected = 6
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        input1 = "Stephen King"
        input2 = [data.Book("Stephen King", "The Shining"), data.Book("Andy Weir", "Project Hail Mary"), data.Book("Stephen King", "IT")]
        result = hw1.books_by_author(input1, input2)
        expected = [data.Book("Stephen King", "The Shining"), data.Book("Stephen King", "IT")]
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        input1 = "J. R. R. Tolkien"
        input2 = [data.Book("J. R. R. Tolkien", "The Hobbit"), data.Book("J. R. R. Tolkien", "The Lord of The Rings"), data.Book("J. K. Rowling", "Harry Potter")]
        result = hw1.books_by_author(input1, input2)
        expected = [data.Book("J. R. R. Tolkien", "The Hobbit"), data.Book("J. R. R. Tolkien", "The Lord of The Rings")]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        input = data.Rectangle(data.Point(-6.0, 8.0), data.Point(6.0, -8.0))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(0.0,0.0), 10.0)
        self.assertEqual(expected, result)

    def test_circle_bound_2(self):
        input = data.Rectangle(data.Point(0.0, 4.0), data.Point(6.0, 0.0))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(3.0, 2.0), 3.60)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average_1(self):
        input = [data.Employee("Jared", 10), data.Employee("Steve", 30), data.Employee("Carol", 20), data.Employee("Bess", 15)]
        result = hw1.below_pay_average(input)
        expected =["Jared", "Bess"]
        self.assertEqual(expected, result)

    def test_below_pay_average_2(self):
        input = [data.Employee("Kevin", 5), data.Employee("Jeff", 51), data.Employee("Rick", 11), data.Employee("Vanessa", 26)]
        result = hw1.below_pay_average(input)
        expected =["Kevin", "Rick"]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
