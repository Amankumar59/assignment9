
#Q.1- Write a Python program to read n lines of a file
f=open('test.txt','r')
lines=f.readlines()
f.close()
#print(lines)
for i in range(0,len(lines)):
    print("line",i,":",lines[i])
#Q.2- Write a Python program to count the frequency of words in a file.
from collections import Counter
file1=open('Q2.txt','r')
count = Counter(file1.read().split())
print(count)
#Q.3- Write a Python program to copy the contents of a file to another file
file1=open('test4.txt','r')
data=file1.read()
file1.close()
file2=open('test5.txt','w')
file2.write(data)
file2.close()

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

f=open('test9.txt')
g=open('test10.txt')
m=open('text11.txt','w')
data=f.read()
ty=g.read()
a=data.split()
b=ty.split()
for i in range(len(a)):
    x=a[i]+" "+b[i]
    m.write(x+"\n")
g.close()
f.close()
m.close()

#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
file=open('test1.txt','w')
for i in range(10):
    x=random.randint(1,100)    
    file.write(str(x))
    file.write(' ')
file.close()
file=open('test1.txt','r+')
line=file.read()
line=line.split()
for i in range(0,len(line)):
    line[i]=int(line[i]) 
line=sorted(line)
for i in range(0,len(line)):
    line[i]=str(line[i]) 
file.close()
file=open('test2.txt','w')
for i in line:
    file.write(i)
    file.write(" ")
file.close()
