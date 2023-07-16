import re

# 01

# [A-z]\s

string_one = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "

search_one = re.findall(r"([A-z]\s)",string_one)

print(search_one)



# 02

# L([A-z]+)

string_two = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"

search_two = re.search(r"L([A-Z][a-z]+)",string_two)

print(search_two.group(1))
print(search_two)


# 03

# (\+?\(\d{4}\)\s\d{,4}-\d{4})
string_three = """
+(0100) 600-1234
+(0100) 60-1234
(0100) 6000-1234
01006001234
0100 600 1234
(0100) 600-1
(0100) 600-12
"""
search_three = re.findall(r"(\+?\(\d{4}\)\s\d{,4}-\d{4})",string_three)

print(search_three)



# 04 

# https?://(www\.)?\w+\.(\w+)(:\d+)?(/\w+)(\.py|\.php)

string_four = """
http://www.elzero.org:8888/link.php
https://elzero.org:8888/link.php
http://www.elzero.com/link.py
https://elzero.com/link.py
http://www.elzero.net
https://elzero.net
"""

search_four = re.findall(r"(https?://(www\.)?\w+\.(\w+)(:\d+)?(/\w+)(\.py|\.php|))",string_four)
print(search_four)

for x in search_four :
    print(x[0])
    print(x[1])
    print(x[3])
    print(x[4])
    print(x[5])

# 05 

# https?
# [^abcd]
# [http|https]
# h\w+
# \wtt\w+
# h.+
# \w+p\w?

