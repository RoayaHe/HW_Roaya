from collections import Counter
from itertools import islice
#Q1
with open("my_id.txt", "w+") as file:
    file.write("Name: Roaya Heib.\n")
    file.write("Age: 19.\n")
    file.write("Phone_Number: 0548344901.\n")
    file.seek(0)

#Q2
def word_count(fileName):
        with open(fileName, "r") as file:
                return Counter(file.read().split())
print("Number of words in the file :",word_count("my_id.txt"))

#Q3
def file_read_from_head(fname, nlines):
    with open(fname) as file:
        for line in islice(file, nlines):
            print(line)
file_read_from_head("my_id.txt", 3)

#Q4
def longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len]
print(longest_word("my_id.txt"))

#Q5
class py_solution:
    def reverse_words(self, sentence):
        return ' '.join(reversed(sentence.split()))
print(py_solution().reverse_words("Roaya Heib"))

#Q6
class IOString():
    def __init__(self):
        self.sentence = ""
    def get_String(self):
        self.sentence = "Roaya Heib"
    def print_String(self):
        print(self.sentence.upper())
sentence = IOString()
sentence.get_String()
sentence.print_String()

#Q7
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def rectangle_area(self):
        return self.length*self.width
New_Rectangle = Rectangle(5, 10)
print(New_Rectangle.rectangle_area())
#####################################################################################################################
#Q8
class py_solution:
   def valid_parenthese(self, _input):
        stack, char = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in _input:
            if parenthese in char:
                stack.append(parenthese)
            elif len(stack) == 0 or char[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
print(py_solution().valid_parenthese("(){}[]"))
print(py_solution().valid_parenthese("[{(}])"))

#Q9
class py_solution:
    def sub_sets(self, _set):
        return self.subsetsRecur([], sorted(_set))
    def subsetsRecur(self, current, _set):
        if _set:
            return self.subsetsRecur(current, _set[1:]) + self.subsetsRecur(current + [_set[0]], _set[1:])
        return [current]
print(py_solution().sub_sets([1, 2, 3]))