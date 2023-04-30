import logging
import random

def fuzz_abs():
    num = random.choice([-100, -1, 0, 1, 100])
    result = abs(num)
    print(f"abs({num}) = {result}")


def fuzz_sum():
    nums = [random.randint(-100, 100) for _ in range(random.randint(1, 10))]
    result = sum(nums)
    print(f"sum({nums}) = {result}")


def fuzz_ord():
    char = random.choice(['a', 'A', '1', '*', '\n'])
    result = ord(char)
    print(f"ord('{char}') = {result}")


def fuzz_len():
    s = ''.join([random.choice(['a', 'A', '1', '*', '\n']) for _ in range(random.randint(1, 10))])
    result = len(s)
    print(f"len('{s}') = {result}")

def fuzz_isnumeric():
    s = ''.join([random.choice(['1', '2', '3', 'a', 'b', 'c']) for _ in range(random.randint(1, 10))])
    result = s.isnumeric()
    print(f"{s}.isnumeric() = {result}")


for _ in range(5):
    fuzz_abs()
    fuzz_sum()
    fuzz_ord()
    fuzz_len()
    fuzz_isnumeric()
