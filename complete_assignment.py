import math
import random
import string
from datetime import datetime, date

# ==========================================
# SECTION 1: CONDITIONAL STATEMENT
# ==========================================

# 1. Electricity Bill Calculator
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)
    if bill > 2000:
        bill += bill * 0.05  # 5% surcharge
    return bill

# 2. Loan Approval System
def loan_approval(salary, credit_score, age):
    if 21 <= age <= 60 and salary >= 30000 and credit_score >= 700:
        return "Approved"
    elif 21 <= age <= 60 and (salary >= 25000 or credit_score >= 650):
        return "Conditionally Approved"
    return "Rejected"

# 3. Number Classification
def classify_number(num):
    sign = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
    parity = "Even" if num % 2 == 0 else "Odd"
    div_3_5 = "Yes" if (num % 3 == 0 and num % 5 == 0) else "No"
    return f"Sign: {sign}, Parity: {parity}, Divisible by 3 & 5: {div_3_5}"

# 4. Exam Result Analyzer
def exam_analyzer(marks):
    if any(m < 33 for m in marks):
        return "Fail"
    pct = sum(marks) / 5
    if pct >= 60:
        return "First Division"
    elif pct >= 50:
        return "Second Division"
    elif pct >= 40:
        return "Third Division"
    return "Pass"


# ==========================================
# SECTION 2: LOOP
# ==========================================

# 1. Automorphic Number
def is_automorphic(n):
    return str(n * n).endswith(str(n))

# 2. Palindrome Number Series
def palindrome_series(start, end):
    return [num for num in range(start, end + 1) if str(num) == str(num)[::-1]]

# 3. LCM & HCF Using Loops (without built-in functions)
def lcm_and_hcf(a, b):
    smaller = a if a < b else b
    hcf = 1
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    greater = a if a > b else b
    lcm = greater
    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm += greater
    return hcf, lcm

# 4. Password Retry System
def password_retry(correct_pwd="admin123"):
    for attempt in range(3, 0, -1):
        pwd = input("Enter password: ")
        if pwd == correct_pwd:
            print("Access Granted!")
            return
        print(f"Wrong password. Attempts left: {attempt - 1}")
    print("Account Blocked after 3 failures.")

# 5. Star Patterns (Triangle, Pyramid, Diamond)
def print_patterns(n=4):
    print("Triangle:")
    for i in range(1, n + 1):
        print("* " * i)
    print("Pyramid:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print("Diamond:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


# ==========================================
# SECTION 3: STRING
# ==========================================

# 1. Palindrome String Check (ignore spaces & case)
def is_palindrome_string(s):
    cleaned = "".join(ch.lower() for ch in s if ch != " ")
    return cleaned == cleaned[::-1]

# 2. Longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

# 3. Check Anagrams
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

# 4. Remove duplicate characters from a string
def remove_duplicates_str(s):
    res = ""
    for ch in s:
        if ch not in res:
            res += ch
    return res

# 5. Compress string: "aaabbc" -> "a3b2c1"
def compress_string(s):
    if not s:
        return ""
    res, count = [], 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res.append(f"{s[i - 1]}{count}")
            count = 1
    res.append(f"{s[-1]}{count}")
    return "".join(res)


# ==========================================
# SECTION 4: PYTHON DATA STRUCTURE
# ==========================================

# 1. List Rotation
def rotate_list(lst, k, direction="right"):
    if not lst:
        return lst
    k %= len(lst)
    return lst[-k:] + lst[:-k] if direction == "right" else lst[k:] + lst[:k]

# 2. Remove Duplicates without Set (maintaining order)
def remove_duplicates_list(lst):
    res = []
    for item in lst:
        if item not in res:
            res.append(item)
    return res

# 3. Find Missing Number (1 to n)
def find_missing_number(lst, n):
    return (n * (n + 1) // 2) - sum(lst)

# 4. Tuple of 5 subjects
def tuple_operations():
    subjects = ("Maths", "Physics", "CS", "English", "Electronics")
    print("Third subject:", subjects[2])
    print("Total subjects:", len(subjects))
    print("Index of CS:", subjects.index("CS"))

# 5. Convert Tuple to Dictionary
def tuple_to_dict(t):
    return dict(t)

# 6. Tuple Unpacking Logic - Swap first and last elements
def swap_first_last_tuple(t):
    first, *middle, last = t
    return (last, *middle, first)

# 7. Subset Checker
def is_subset(set_a, set_b):
    return set_a.issubset(set_b)

# 8. Student Marks Analyzer
def student_marks_analyzer(marks_dict):
    topper = max(marks_dict, key=marks_dict.get)
    avg = sum(marks_dict.values()) / len(marks_dict)
    failures = [k for k, v in marks_dict.items() if v < 33]
    return topper, avg, failures

# 9. Library Management using Dictionary
class Library:
    def __init__(self):
        self.books = {"Python": 4, "Java": 2, "C++": 3}
    def add_book(self, name, qty=1):
        self.books[name] = self.books.get(name, 0) + qty
    def issue_book(self, name):
        if self.books.get(name, 0) > 0:
            self.books[name] -= 1
            return f"Issued {name}. Remaining: {self.books[name]}"
        return "Out of stock"


# ==========================================
# SECTION 5: FUNCTION AND RECURSION
# ==========================================

# 1. Factorial using loop
def factorial_loop(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# 2. Sum of first n natural numbers recursively
def sum_natural(n):
    return n if n <= 1 else n + sum_natural(n - 1)

# 3. Reverse string using recursion
def reverse_str(s):
    return s if len(s) == 0 else reverse_str(s[1:]) + s[0]

# 4. Power (x^n) using recursion
def power(x, n):
    return 1 if n == 0 else x * power(x, n - 1)


# ==========================================
# SECTION 6: ERROR AND EXCEPTION
# ==========================================

# 1. Age Validation System
def validate_age(age):
    if age < 18:
        raise ValueError("Age < 18 is not allowed.")
    return "Valid Age"

# 2. Bank Withdrawal System
def withdraw(balance, amount):
    if amount > balance:
        raise RuntimeError("Withdrawal exceeds balance!")
    return balance - amount

# 3. Password Validator with Custom Exceptions
class ShortPasswordError(Exception): pass
class NoUppercaseError(Exception): pass
class NoNumberError(Exception): pass

def validate_password(pwd):
    if len(pwd) < 8:
        raise ShortPasswordError("Length < 8")
    if not any(c.isupper() for c in pwd):
        raise NoUppercaseError("No uppercase")
    if not any(c.isdigit() for c in pwd):
        raise NoNumberError("No number")
    return "Valid Password"


# ==========================================
# SECTION 7: MODULE AND PACKAGE
# ==========================================

def modules_demo():
    # 1. math module
    print("Sqrt(16):", math.sqrt(16), "Pow(2,3):", math.pow(2, 3), "Fact(5):", math.factorial(5), "Sin(90):", math.sin(math.radians(90)))
    # 2. random module
    otp = random.randint(100000, 999999)
    pwd = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    r_list = [random.randint(1, 50) for _ in range(5)]
    print("OTP:", otp, "Random Password:", pwd, "Random List:", r_list)
    # 3. datetime module
    print("Current Date/Time:", datetime.now())
    dob = date(2006, 5, 10)
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    print("Calculated Age:", age)


# ==========================================
# SECTION 8: OBJECT ORIENTED PROGRAMMING
# ==========================================

# 1. Multilevel inheritance: Vehicle -> Car -> ElectricCar
class Vehicle:
    def start(self): return "Vehicle started"
class Car(Vehicle):
    def drive(self): return "Car driving"
class ElectricCar(Car):
    def charge(self): return "Electric Car charging"

# 2. Multiple inheritance: Teacher + Researcher -> Professor
class Teacher:
    def teach(self): return "Teaching"
class Researcher:
    def research(self): return "Researching"
class Professor(Teacher, Researcher): pass

# 3. Hierarchical inheritance: Shape -> Circle, Rectangle, Triangle
class Shape: pass
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return math.pi * self.r ** 2
class Rectangle(Shape):
    def __init__(self, l, w): self.l, self.w = l, w
    def area(self): return self.l * self.w
class Triangle(Shape):
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h

# 4. Method overriding: Animal -> Dog/Cat sound
class Animal:
    def sound(self): return "Generic sound"
class Dog(Animal):
    def sound(self): return "Bark"
class Cat(Animal):
    def sound(self): return "Meow"

# 5. Operator overloading: Add two complex numbers
class ComplexNum:
    def __init__(self, r, i): self.r, self.i = r, i
    def __add__(self, other): return ComplexNum(self.r + other.r, self.i + other.i)
    def __str__(self): return f"{self.r} + {self.i}i"

# 6. Class with Private variable (salary)
class Employee:
    def __init__(self, salary): self.__salary = salary
    def get_salary(self): return self.__salary

# 7. ATM system using encapsulation: Hide PIN and balance
class ATM:
    def __init__(self, pin, bal): self.__pin, self.__bal = pin, bal
    def withdraw(self, pin, amt):
        if pin != self.__pin: return "Wrong PIN"
        if amt > self.__bal: return "Low Balance"
        self.__bal -= amt
        return f"Remaining Balance: {self.__bal}"

# 8. Game Character Design: Base character with specialized subclasses
class Character:
    def __init__(self, name): self.name = name
    def attack(self): return "Basic Attack"
class Warrior(Character):
    def attack(self): return f"{self.name} uses Sword Slash!"
class Mage(Character):
    def attack(self): return f"{self.name} casts Fireball!"


if __name__ == "__main__":
    print("Bill for 250 units:", electricity_bill(250))
    print("Loan Status:", loan_approval(35000, 720, 25))
    print("Automorphic 25:", is_automorphic(25))
    print("Compress 'aaabbc':", compress_string("aaabbc"))
    print("Rotate [1,2,3,4,5]:", rotate_list([1, 2, 3, 4, 5], 2))
    print("Reverse 'Python':", reverse_str("Python"))
    modules_demo()
    print("Complex Addition:", ComplexNum(2, 3) + ComplexNum(4, 5))
