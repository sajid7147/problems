"""You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order (names will follow Python's capitalize case format).

The input will have four lines. The first two lines correspond to the first person, while the last two lines correspond to the second person. For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. Your output should be the name of the younger of the two.
"""

from datetime import datetime

# Read the details of the first person
name1 = input()
dob1 = datetime.strptime(input(), "%d-%m-%Y")

# Read the details of the second person
name2 = input()
dob2 = datetime.strptime(input(), "%d-%m-%Y")

# Compare the dates of birth
if dob1 > dob2 or (dob1 == dob2 and name1 < name2):
    print(name1,end="")
else:
    print(name2,end="")