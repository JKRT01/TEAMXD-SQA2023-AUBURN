import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def log_abs(num, result):
    logging.debug(f"abs({num}) = {result}")

def log_sum(nums, result):
    logging.debug(f"sum({nums}) = {result}")

def log_ord(char, result):
    logging.debug(f"ord('{char}') = {result}")

def log_len(s, result):
    logging.debug(f"len('{s}') = {result}")

def log_isnumeric(s, result):
    logging.debug(f"{s}.isnumeric() = {result}")

def fuzz_abs():
    num = random.choice([-100, -1, 0, 1, 100])
    result = abs(num)
    log_abs(num, result)

def fuzz_sum():
    nums = [random.randint(-100, 100) for _ in range(random.randint(1, 10))]
    result = sum(nums)
    log_sum(nums, result)

def fuzz_ord():
    char = random.choice(['a', 'A', '1', '*', '\n'])
    result = ord(char)
    log_ord(char, result)

def fuzz_len():
    s = ''.join([random.choice(['a', 'A', '1', '*', '\n']) for _ in range(random.randint(1, 10))])
    result = len(s)
    log_len(s, result)

def fuzz_isnumeric():
    s = ''.join([random.choice(['1', '2', '3', 'a', 'b', 'c']) for _ in range(random.randint(1, 10))])
    result = s.isnumeric()
    log_isnumeric(s, result)

for _ in range(5):
    fuzz_abs()
    fuzz_sum()
    fuzz_ord()
    fuzz_len()
    fuzz_isnumeric()
