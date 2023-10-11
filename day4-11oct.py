a = "upflairs Jaipur"
#print(a[-1:-3])
#by default step 1 of splicing a string is positive so we cant de the above method. to get a group of strings from
# -ve we need to give step 1 as -1 as shown below
#print(a[-1:-3:-1])
#to reverse a string dont define a starting or ending point but tell it to start from -1 as shown below so it will print whole string but
#starting from -1
#print(a[::-1])
###########################################
lst = [0,23,4,3,56,422,32]
lst.insert(2, 44)
#print(lst)
#lst.clear()
lst.sort()
lst[1] = 100
name = "Gautam", 2, "hello"
#print(type(name))
#print(name *2)
#tpl = (2,)
#print(type(tpl))
#print(tpl)
print(name[::-1])
print(name*2)
