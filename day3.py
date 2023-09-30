st1 = "Hello welcome to python"
type(st1)
print(type(st1))
#checking length of st1
print(len(st1))
print("hello" in st1)
print(st1.lower())
#lower doesnt change the strings original value
#to print first character of the string
print(st1[0])
#to get characters in a range
print(st1[0:8])
#in splicing to get characters in a range the last digit isnt included ex-- [0:8] will include 0 to 7th character
print(st1[:4])
#if there's nothing at beginning it will start at 0
#if there's nothing at the beginning and afer the colon it will print the whole string
print(st1[:])
print(st1[:3])
st2 = "ello"
print(st2 in st1)
#------------------------------------------------------------------------#
t1 = (2,5,6,3,7,1)
print(len(t1))
print(t1[0:])
#tuple stores both homogenous and hetrogenous values
print(type(t1))
t2 = (2,3,4.5,"Hello")
#-1 is the last element of a string. tuple etc so.. "Hello" is -1 of tuple and 'o' is -1 of "Hello"
print(t2[-1][-1])
t3 = t1 + t2
print(t3)
print(t3[-1][2:4])
print("Hello" in t3)
#----------------------------------------------------------------------------#
c1 = [3,5,7,8]
c2 = [4,7,10.5,"hey"]
c2.append("jecrc")
print(c2)
#1st argument mein position where you wanna add the data 2nd argument mein the actucal data
c2.insert(1, 545)
print(c2)
print(t2[-1] + " " + c2[-2])
print(t2[-1] + " " + c2[-1] + " ",c2[3])