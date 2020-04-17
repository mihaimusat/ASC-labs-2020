"""
Task 1 - Let's print the current time!

Objectives:
- use documentation!!!
- print
- print with %
- print without new line
- format

Print the current date and time. Also print it using % and using format().
---> see examples from 'Stringuri' section.
"""
from datetime import datetime

now = datetime.now()
print(now.strftime(("%d %B %Y %H:%M:%S")))



# Hints for date and time: datetime module for objects representing time,
# strftime function for formatting
# https://docs.python.org/2/library/datetime.html#datetime-objects
# https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

# Use only the official Python documentation to solve this exercise.
