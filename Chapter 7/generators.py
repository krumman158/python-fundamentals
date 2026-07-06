# Generators in python are special type of functions that allow you to create and iterable sequence of values. It returns a generator object. It doesnot stores the values but has the info that can create those values.

# Some  use cases:-
# Reading large files without loading the entire file into memory.
# Processing large datasets one item at a time.
# Generating infinite sequences (e.g., Fibonacci numbers, natural numbers).
# Pipelines where data is processed step by step.
# Saving memory when you don't need all values at once.

# Benefits:-
# Memory efficient: Doesn't store all values at once.
# Faster startup: Produces values only when needed.
# Works with large or infinite data.
# Improves performance for one-time iteration.



def read_file():
    with open(r"D:\CODES\python\Chapter 7\log.txt", "r") as file:
        for line in file:
            yield line.strip()

for line in read_file():
    print(line)

# Working:-
# read_file() starts.
# Reads only the first line.
# yield returns "Login Successful" and pauses.
# The for loop prints it.
# Generator resumes from where it paused.
# Reads the second line, yields it, pauses again.
# Continues until the file ends.