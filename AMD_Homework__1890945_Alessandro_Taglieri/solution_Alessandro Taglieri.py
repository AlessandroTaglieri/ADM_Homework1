# ===== PROBLEM1 =====


# Exercise 1 - Introduction - Say "Hello, World!" With Python

print "Hello, World!" 




# Exercise 2 - Introduction - Python If-Else

#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())

if (n%2) != 0:
    print("Weird")
elif 2<=n<=5:
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
elif n>20:
    print("Not Weird")



    
# Exercise 3 - Introduction - Arithmetic Operators

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(a+b)
print(a-b)
print(a*b)




# Exercise 4 - Introduction - Python: Division

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(a//b)
print(a/b)




# Exercise 5 - Introduction - Loops

if __name__ == '__main__':
    n = int(raw_input())

for i in range(0,n):
    print(i*i)



    
# Exercise 6 - Introduction - Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4) == 0:
        if(year%100) == 0:
            if(year%400) == 0:
                 leap = True

        else:
            leap=True

    return leap




# Exercise 7 - Introduction - Print Function

if __name__ == '__main__':
    n = int(input())
z=1
for i in range(2,n+1):
    z=int('%d%d' % (z,i))
print(z)




# Exercise 8 - Basic data types - List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    solution=[]
    p=0
    for i in range(x+1): 
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k) != n:
                    solution.append([])
                    solution[p]=[i,j,k]
                    p+=1
    
    print(solution)

    
    

# Exercise 9 - Basic data types - Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    array_score = list(arr)
    max_score=max(array_score)
    solution=min(array_score)
    
    for i in array_score:
        if i!=max_score and i>solution:
            solution=i
    print(solution)

    
    
    
# Exercise 10 - Basic data types - Nested Lists

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores=[]
    for i in range(len(students)):
        scores.append(students[i][1])
    min_score=min(scores)
    solution_score=max(scores)
    for i in scores:
        if i != min_score and i<solution_score:
            solution_score=i
    solution_student=[]
    for i in range(len(students)):
        if students[i][1]==solution_score:
            solution_student.append(students[i][0])
    solution_student.sort()
    for i in solution_student:
        print(i)

    

       
# Exercise 11 - Basic data types - Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    tot=0
    a=student_marks[query_name]
    for i in a:
        tot+=+i
    print("{0:.2f}".format(tot/len(a)))

    
    
        
# Exercise 12 - Basic data types - Lists

if __name__ == '__main__':
    N = int(input())
    solution=[]
    for _ in range(N):
        string = input()
        words=string.split()

        if words[0]=="insert":
            solution.insert(int(words[1]),int(words[2]))
        elif words[0]=="print":
            print(solution)
        elif words[0]=="remove":
            solution.remove(int(words[1]))
        elif words[0]=="append":
            solution.append(int(words[1]))
        elif words[0]=="sort":
            solution.sort()
        elif words[0]=="pop":
            solution.pop()
        elif words[0]=="reverse":
            solution.reverse()
        
        
        
        
# Exercise 13 - Basic data types - Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    tup=tuple(integer_list)

    solution=hash(tup)
    print (solution)


    
    
# Exercise 14 - Strings - sWAP cASE

def swap_case(s):
    new=""
    for i in s:
        if i.islower():
            i=i.upper()
        else:
            i=i.lower()
        new+=i
    return new




# Exercise 15 - Strings - String Split and Join

def split_and_join(line):
    # write your code here
    solution=line.split(" ")
    solution="-".join(solution)
    return solution

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
    
    
    
# Exercise 16 - Strings - What's Your Name?

def print_full_name(a, b):
    print('Hello {0} {1}! You just delved into python.'.format(a,b))


    
    
# Exercise 17 - Strings - Mutations

def mutate_string(string, position, character):
    list1=list(string)
    list1[position]=character
    new_s="".join(list1)
    return new_s




# Exercise 18 - Strings - Find a string

def count_substring(string, sub_string):
    solution=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            solution+=1
    
    return solution




# Exercise 19 - Strings - String Validators

if __name__ == '__main__':
    s = input()
    c=False
    for i in s:
        if i.isalnum():
            c=True
            break
    print(c)
    c=False
    for i in s:
        if i.isalpha():
            c=True
            break
    print(c)
    c=False
    for i in s:
        if i.isdigit():
            c=True
            break
    print(c)
    c=False
    for i in s:
        if i.islower():
            c=True
            break
    print(c)
    c=False
    for i in s:
        if i.isupper():
            c=True
            break
    print(c)


    
    

# Exercise 20 - Strings - Text Alignment


thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


    
    

# Exercise 21 - Strings - Text Wrap

def wrap(string, max_width):
    j=0
    z=max_width
    solution=""
    for i in range(len(string)):
        solution+="{0}\n".format(string[j:z])
        j=z
        z+=max_width
    return solution




# Exercise 22 - Strings - Designer Door Mat


n=input().split()
N=int(n[0])//2
list1=[]
list2=[]
for i in range(N):
    pattern = ('.|.' * (2 * i + 1)).center(int(n[1]), '-')
    list1.append(pattern)
    
central=("WELCOME".center(int(n[1]), '-'))
list2=list1.copy()
list2.reverse()
for i in list1:
    print (i)
print(central)
for j in list2:
    print(j)


    

# Exercise 23 - Strings - String Formatting

def print_formatted(number):
    # your code goes here
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        print("{0:>{1}d} {0:>{1}o} {0:>{1}X} {0:>{1}b}".format(i,width))


        
        
# Exercise 24 - Strings - Alphabet Rangoli

import string
def print_rangoli(size):
    # your code goes here
    
    
    alphabet = string.ascii_lowercase[:size]
    
    height = ((size * 2) - 1)
    width = ((size * 4) - 3)
    lines=[]
    for i in range(height):
        lines.append(None)
    for j in range(size):
        s = alphabet[(-j - 1):]
        letters = ''.join(reversed(s)) + s[1:]
        lines[j] = lines[-j - 1] = '-'.join(letters).center(width, '-')
    for k in lines:
        print (k)
    


# Exercise 25 - Strings - Capitalize!


def solve(s):
    print(s)
    x = list(s.split(' '))
    print(x)
    sol=""
    for i in x:
        i=i.capitalize()
        sol+=i+" "
    return sol




# Exercise 26 - Strings - The Minion Game

def minion_game(string):
    # your code goes here
    vowels=['A','E','I','O','U']
    kevin=0
    stuart=0
    
    for j in range(len(string)):
        if string[j] in vowels:
            kevin+=(len(string)-j)
        else:
            stuart+=(len(string)-j)
    
    if (kevin>stuart):
        print("Kevin {0}".format(kevin))      
    elif(stuart>kevin):
         print("Stuart {0}".format(stuart))
    else:
        print("Draw")
            




# Exercise 27 - Strings - Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    l=int(n/k)
    t=[]
    u=[]
    var=0
    x=k
    for i in range(l):
        t.append(string[var:x])
        u.append("")
        var=x
        x+=k
    

    for i in range(len(t)):
        for j in t[i]:
        
            if j not in u[i]:
                u[i]+=j
        
    for i in u:
        print(i)



# Exercise 28 - Sets - Introduction to Sets


def average(array):
    
    
    solution=0
    new_set=set(array)
    solution=(sum(new_set)/len(new_set))
    return solution




# Exercise 29 - Sets - No Idea!


n=list(map(int,input().split()))
a=list(map(int,input().split()))
c=set(map(int,input().split()))
d=set(map(int,input().split()))
sol=0
sol=sum([(i in c) - (i in d) for i in a])
print(sol)




# Exercise 30 - Sets - Symmetric Difference

n=input()
list1=map(int, input().split(" "))
b=input()
list2=map(int, input().split(" "))
s=set(list1)
s2=set(list2)
solution1=s.difference(s2)
solution2=s2.difference(s)
solution=sorted(solution1.union(solution2))


for i in solution:
    print(i)


    
    
# Exercise 31 - Sets - Set .add()


N=int(input())

countries=set()

for i in range(N):
    countries.add(input())
print (len(countries))




# Exercise 32 - Sets - Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N= int(input())
word=[]
for i in range(N):
    word=input().split()
    if word[0]=="pop":
        s.pop()
    elif word[0]=="remove":
        s.remove(int(word[1]))
    elif word[0]=="discard":
        s.discard(int(word[1]))
print (sum(list(s)))

    


# Exercise 33 - Sets - Set .union() Operation

n=int(input())
s = set(input().split(" "))
b=int(input())
s2 = set(input().split(" "))
solution=s.union(s2)
print(len(solution))



# Exercise 34 - Sets - Set .intersection() Operation


n=int(input())
s=set(input().split(" "))
b=int(input())
s2=set(input().split(" "))
solution=s.intersection(s2)
print(len(solution))



# Exercise 35 - Sets - Set .difference() Operation


n=input()
s=set(input().split(" "))
b=input()
s2=set(input().split(" "))
solution=s.difference(s2)
print(len(solution))




# Exercise 36 - Sets - Set .symmetric_difference() Operation


n=input()
s=set(input().split(" "))
b=input()
s2=set(input().split(" "))
solution=s.symmetric_difference(s2)
print(len(solution))




# Exercise 37 - Sets - Set Mutations

n=input()
s=set(map(int,input().split(" ")))
N=int(input())

for i in range(N):
    words=list(input().split())
    list1=set(map(int,input().split()))
    if words[0]=="intersection_update":
        s.intersection_update(list1)
    elif words[0]=="update":
        s.update(list1)
    elif words[0]=="symmetric_difference_update":
        s.symmetric_difference_update(list1)
    elif words[0]=="difference_update":
        s.difference_update(list1)


print(sum(s))




# Exercise 38 - Sets - The Captain's Room

K = int(input())

list1 = list(map(int, input().split()))

groups = set(list1)
sum_1 = sum(list1)
sum_2 = sum(groups)
sol = sum_2 * K - sum_1

print(sol // (K - 1))




# Exercise 39 - Sets - Check Subset


N=int(input())
solution=[]
for i in range(N):
    a=int(input())
    A=set(input().split())
    b=int(input())
    B=set(input().split())
    if A.issubset(B):
        solution.append(True)
    else:
        solution.append(False)
for i in solution:
    print(i)




# Exercise 40 - Sets - Check Strict Superset


A=set(input().split())
n=int(input())
var=[]
solution=True
for i in range(n):
    var.append((set(input().split())))


for i in var:
    if i.issubset(A):
        continue
    else:
        solution=False

print(solution)




# Exercise 41 - Collections - collections.Counter()

import collections

X = int(input())
sizes = collections.Counter(map(int,input().split()))
N = int(input())
customers=[]
tot=0
for i in range(N):
    customers=input().split()

    if sizes[int(customers[0])]>0:
        sizes[int(customers[0])]-=1
        tot+=int(customers[1])
print(tot)




# Exercise 42 - Collections - DefaultDict Tutorial


from collections import defaultdict
arr=[]
arr = list(map(int,input().split()))


d = defaultdict(list)
   
for i in range(arr[0]):
    s=input()
    d[s].append(str(i + 1))
   
for i in range(arr[1]):
    s2=input()
    print(' '.join(d[s2]) or -1)




# Exercise 43 - Collections - Collections.namedtuple()


import collections

N = int(input())
col = ','.join(input().split())
Student = collections.namedtuple('Student', col)

summ = 0
for i in range(N):
    row = input().split()
    student = Student(*row)
    summ += int(student.MARKS)

print (summ/N)




# Exercise 44 - Collections - Collections.OrderedDict()


from collections import OrderedDict
N= int(input())
solution= OrderedDict()
for i in range(N):
    a = input().split()
    price= int(a[-1])
    name= " ".join(a[:-1])
    if solution.get(name):                
       solution[name] += price
    else:
       solution[name] = price
for i in solution.keys():
    print (i, solution[i])


    
    
# Exercise 45 - Collections - Word Order


from collections import OrderedDict
d=OrderedDict()
n=int(input())
s=[]
for i in range(n):
    s.append(input())
for i in s:
    key=i
    d[key]=d.get(key,0)+1

print(len(d))
print(*d.values())




# Exercise 46 - Collections - Collections.deque()

from collections import deque
n=int(input())
arr=[]
solution=deque()

for i in range(n):
    arr=input().split()
    if arr[0]=="append":
        solution.append(arr[1])
    elif arr[0]=="appendleft":
        solution.appendleft(arr[1])
    elif arr[0]=="pop":
        solution.pop()
    elif arr[0]=="popleft":
        solution.popleft()
s=""
for i in solution:
    s+=i+" "
print(s)


# Exercise 47 - Collections - Company Logo

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    ord_s=sorted(s)
    s_counter = Counter(ord_s).most_common()

    s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
    for i in range(0, 3):
        print(s_counter[i][0], s_counter[i][1])

        
        

# Exercise 48 - Collections - Piling Up!

n=int(input())
for t in range(n):
    side = int(input())
    sides = list(map(int, input().split()))
    i = 0
    while i < side - 1 and sides[i] >= sides[i + 1]:
        i += 1
    while i < side - 1 and sides[i] <= sides[i + 1]:
        i += 1
    if i==(side-1):
        print("Yes")
    else:
        print("No")
    


# Exercise 49 - Date time - Calendar Module


import calendar

date = input().strip().split()

days = list(calendar.day_name)
print (days[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))].upper())



# Exercise 50 - Date time - Time Delta

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def diff(t1, t2):
    time1=datetime.strptime(t1, "%a %d %b %Y %X %z")
    time2=datetime.strptime(t2, "%a %d %b %Y %X %z")
    solution=abs(int((time1 - time2).total_seconds()))
    return solution
if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        sol = diff(t1, t2)

        print(sol)



# Exercise 51 - Exceptions -

t=int(input())
division=[]
sol=0
for i in range(t):
    division=input().split()
   
    try:
        sol=int(division[0])//int(division[1])
        print(sol)
    except Exception as e:
        print("Error Code:",e)
    


# Exercise 52 - Built-ins - Zipped!


x=input().split()

sheet = []
for _ in range(int(x[1])):
    sheet.append(map(float, input().split()))

for i in zip(*sheet):
    print(sum(i) / len(i))

    

# Exercise 53 - Built-ins - Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter


if __name__ == '__main__':
    a = input().split()

    n = int(a[0])

    m = int(a[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    num=int(input())
    for i in sorted(arr, key=itemgetter(num)):
        print(*i)
    


# Exercise 54 - Built-ins - Ginorts


n=input()
print(*sorted(n, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')




# Exercise 55 - Map and lambda function

cube = lambda x: x**3


def fibonacci(n):
    l=[0,1]
    
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
    return(l[0:n])




# Exercise 56 - Regex - Detect Floating Point Number


import re

pattern = re.compile('^[-+]?[0-9]*\.[0-9]+$')
        

n=int(input())

for i in range(n):
    s=input()
    if pattern.match(s):
        print(True)
    else:
        print(False)

        

# Exercise 57 - Regex - Re.split()

regex_pattern = r'[.,]+'



# Exercise 58 - Regex - Group(), Groups() & Groupdict()

s=input()
sol=[]
solution=""
for i in range(len(s)-1):
    if s[i].isalnum():
        if s[i] is s[i+1]:
            solution=s[i]
            break
if not solution:
    print ("-1")
else:
    print(solution)



# Exercise 59 - Regex - Re.findall() & Re.finditer()

import re
s=input()
vowels="aeiou"
consonant="mnbvcxzsdfghjklpuytrwq"

match = re.findall(r'(?<=[' + consonant + '])([' + vowels + ']{2,})(?=[' + consonant + '])', s, flags=re.I)
print('\n'.join(match or ['-1']))



# Exercise 60 - Regex - Re.start() & Re.end()

import re
S=input()
k=input()

x=re.compile(k)
m=x.search(S)

if not m:
    print('(-1, -1)')

while m:
    print('({0}, {1})'.format(m.start(), m.end() - 1))
    m = x.search(S, m.start() + 1)


    
# Exercise 61 - Regex - Regex Substitution

import re
n=int(input())

for i in range(n):
    s=input()
    a=re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or',s)
    print(a)

    

# Exercise 62 - Regex - Validating Roman Numerals

regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"



# Exercise 63 - Regex - Validating phone numbers

n=int(input())

for i in range(n):
    a="YES"
    k=input()
    if (k[0]=='7' or k[0]=='8' or k[0]=='9') and (len(k)==10):
        for j in k:
            if not j.isdigit():
                a="NO"
                break
    else:
        a="NO"
    print(a)  
        
    


# Exercise 64 - Regex - Validating and Parsing Email Addresses

import re

pattern = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'
n=int(input())

for i in range(n):
    s=input().split()
    if re.match(pattern,s[1]):
        print (s[0]+" "+s[1])


        
# Exercise 65 - Regex - Hex Color Code


import re
n=int(input())
for i in range(n):
    m = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if m:
        print(*m, sep='\n')

        

# Exercise 66 - Regex - HTML Parser - Part 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, att):
        print ('Start :', tag)
        for i in att:
            print ('->', i[0], '>', i[1])
    def handle_startendtag(self, tag, att):
        print ('Empty :', tag)
        for j in att:
            print ('->', j[0], '>', j[1])
    def handle_endtag(self, tag):
        print ('End   :', tag)

    
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())


    
# Exercise 67 - Regex - HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')

        print(comment)

    def handle_data(self, data):
        if data == '\n': return
        print('>>> Data')
        print(data)
  

  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()



# Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, att):
        print(tag)
        for i in att:
            print("-> {} > {}".format(*i))

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())

    

# Exercise 69 - Regex - Validating UID

import re
n=int(input())

for i in range(n):
    s=sorted(input())
    j=''.join(s)
    
    try:
        assert len(j) == 10
        assert re.search(r'[A-Z]{2}', j)
        assert not re.search(r'[^a-zA-Z0-9]', j)
        assert re.search(r'\d\d\d', j)
        assert not re.search(r'(.)\1', j)
        
    except:
        print('Invalid')
    else:
        print('Valid')


# Exercise 70 - Regex - Validating Credit Card Numbers

from re import compile
n=int(input())
pattern = compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]\d{3}' 
    r'(?:-?\d{4}){3}'
    r'$')
for i in range(n):
    s=input()
    if pattern.search(s):
        print("Valid")
    else:
        print("Invalid")
    


# Exercise 71 - Regex - Validating Postal Codes

regex_integer_in_range = r"^[1-9][\d]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	



# Exercise 72 - Regex - Matrix Script

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


s=""
sol=""
for i in range(m):
    for j in range(n):
        s=matrix[j]
        sol+=s[i]

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sol))




# Exercise 73 - Xml - XML 1 - Find the Score

def get_attr_number(node):
    a=0
    for child in node:
        a+=(get_attr_number(child))
    return (len(node.attrib) + a)
   


    
# Exercise 74 - Xml - XML 2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
    for i in elem:
        depth(i, level + 1)



        
# Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        f(['+91 ' + i[-10:-5] + ' ' + i[-5:] for i in l])
    return fun




# Exercise 76 - Closures and decorators - Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        a=map(f, sorted(people, key=lambda x: int(x[2])))
        return a
    return inner




# Exercise 77 - Numpy - Arrays

def arrays(arr):
    
    a = numpy.array(arr,float)
    b = a[::-1]
    return b




# Exercise 78 - Numpy - Shape and Reshape

import numpy

n=list(map(int,input().split()))

array=numpy.array(n,int)
array.shape=(3,3)
print(array)




# Exercise 79 - Numpy - Transpose and Flatten

import numpy

s=list(map(int,input().split()))
g=[None]*s[0]


for i in range(s[0]):
    g[i]=list(map(int,input().split()))

my_array=numpy.array(g)

print (numpy.transpose(my_array))

print (my_array.flatten())




# Exercise 80 - Numpy - Concatenate

import numpy

n=list(map(int,input().split()))

a=[None]*n[0]
b=[None]*n[1]

for i in range(n[0]):
    a[i]=list(map(int,input().split()))
for j in range(n[1]):
    b[j]=list(map(int,input().split()))

array1=numpy.array(a)
array2=numpy.array(b)

print(numpy.concatenate((array1,array2),axis=0))




# Exercise 81 - Numpy - Zeros and Ones

import numpy

n=list(map(int,input().split()))


print(numpy.zeros((n), dtype=numpy.int))
print(numpy.ones((n), dtype=numpy.int))




# Exercise 82 - Numpy - Eye and Identity

import numpy
numpy.set_printoptions(sign=' ')
n=list(map(int,input().split()))

print(numpy.eye(n[0],n[1], k=0))




# Exercise 83 - Numpy - Array Mathematics

import numpy

n=list(map(int,input().split()))
x=[None]*n[0]
y=[None]*n[0]

for i in range(n[0]):
    x[i]=(list(map(int,input().split())))
for j in range(n[0]):
    y[j]=(list(map(int,input().split())))

a=numpy.array(x,int)
b=numpy.array(y,int)

print(a+b,a-b,a*b,a//b,a%b,a**b, sep='\n')




# Exercise 84 - Numpy - Floor, Ceil and Rint

import numpy
numpy.set_printoptions(sign=' ')
A=list(map(float,input().split()))
a=numpy.array(A,float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))




# Exercise 85 - Numpy - Sum and Prod

import numpy

n=list(map(int,input().split()))
x=[None]*n[0]

for i in range(n[0]):
    x[i]=list(map(int,input().split()))
my_array=numpy.array(x,int)

sum=numpy.sum(my_array, axis=0)
print(numpy.prod(sum,axis=0))




# Exercise 86 - Numpy - Min and Max

import numpy

n=list(map(int,input().split()))
x=[None]*n[0]

for i in range(n[0]):
    x[i]=list(map(int,input().split()))
my_array=numpy.array(x,int)

min1=numpy.min(my_array, axis=1)
print(numpy.max(min1))




# Exercise 87 - Numpy - Mean, Var, and Std

import numpy
n=list(map(int,input().split()))
A=[None]*n[0]
numpy.set_printoptions(legacy='1.13')
for i in range(n[0]):
    A[i]=list(map(int,input().split()))
a=numpy.array(A,int)

print(numpy.mean(a, axis=1))
print(numpy.var(a,axis=0))
print(numpy.std(a))




# Exercise 88 - Numpy - Dot and Cross

import numpy

n=int(input())
a=[None]*n
b=[None]*n
for i in range(n):
    a[i]=list(map(int,input().split()))
for j in range(n):
    b[j]=list(map(int,input().split()))
my_array=numpy.array(a,int)
my_array2=numpy.array(b,int)

sol=numpy.dot(my_array,my_array2)
print(sol)




# Exercise 89 - Numpy - Inner and Outer

import numpy
A=list(map(int,input().split()))
B=list(map(int,input().split()))
a=numpy.array(A,int)
b=numpy.array(B,int)
print(numpy.inner(a,b))
print(numpy.outer(a,b))




# Exercise 90 - Numpy - Polynomials

import numpy

n=list(map(float,input().split()))
x=float(input())

sol=numpy.polyval(n,x)
print (sol)




# Exercise 91 - Numpy - Linear Algebra

import numpy
numpy.set_printoptions(legacy='1.13')
n=int(input())
i=[]
for j in range(n):
    i.append(list(map(float,input().split())))

array=numpy.array(i,float)

print(numpy.linalg.det(array))


 
    
    
    
    
# ===== PROBLEM2 =====
 
    
# Exercise 92 - Challenges - Birthday Cake Candles

#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    m=max(ar)
    count=0
    for i in ar:
        if i==m:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


    
    
# Exercise 93 - Challenges - Kangaroo

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    a=x1+v1
    b=x2+v2
    if x1<x2 and v1<v2:
        return("NO")
    sol="NO"
    for i in range(99999):
        if a==b:
            sol="YES"
            break
        a+=v1
        b+=v2
    return(sol)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


    
    
# Exercise 94 - Challenges - Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys


def viralAdvertising(n):
    m=0
    next=5
    count=0
    for i in range(n):
        m=next//2
        count+=m
        next=m*3
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


    
# Exercise 95 - Challenges - Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

def func(c):
      
    new_s=str(c)
    if len(new_s)==1:
        return c
    else:
        d = map(int, list(new_s))
        return func(sum(d))
def superDigit(n, k):       
    d = map(int, list(n))
    count=(sum(d))
    return func(count * k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


    
    
# Exercise 96 - Challenges - Insertion Sort - Part 1

#!/bin/python3


import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    m=n-1
    a=arr[n-1]
    arr[n-1]=arr[n-2]
    

    for i in range(n):
        
        m-=1
        b=arr[m]
        if m<0:
            break
        if b<a:
            arr[m+1]=a
            print(*arr, sep=" ")
            break
        else:
            arr[m+1]=arr[m]
            print(*arr, sep=" ")
            
            
    if b >= a:
        arr[0] = a
        print(*arr, sep=" ")



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


    
    
# Exercise 97 - Challenges - Insertion Sort - Part 2

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(n):
        j = i;
        while (j > 0 and arr[j] < arr[j-1]):
            x = arr[j];
            arr[j] = arr[j-1];
            arr[j-1] = x;
            j -= 1;
        if (i != 0): 
            print(*arr, sep=" ")
            
        
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)






