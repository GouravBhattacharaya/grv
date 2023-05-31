#question 1 solutions
a_string="gourav"
a_list=[1,2,3,4,"pwskills",6,7,8,9.99,'ten']
a_float=2.6
a_tuple="immutable stuff"

#question 2 solutions

var1=''
print('var1 is',type(var1))
var2='[ds,ml,python]'
print('var2 is',type(var2))
var3=['ds','ml','python']
print('var3 is',type(var3))
var4=1
print("var4 is",type(var4))
#var1 is <class 'str'>
#var2 is <class 'str'>
#var3 is <class 'list'>
#var4 is <class 'int'>

#question 3 
# '/ 'division opertor
print(a_float/var4)
# "%" modulus operator
print(4%2)
#this shall be zero
print(16//3)
#this is for floor division 5*3=15 nearest whole
print(2**3)
#2 raised to the power 3 is 8

#question 4 considering the earlier created a_list in question 1
for i in a_list:
    print(i,type(i))

#question 5 answer
A=25
B=5
i=0
while A>B and A%B==0 :
    A=A-B
    i=i+1
    if A==B:

        print("number of times divisible",i+1)
else :    
     print("not fully divisible")

#question 6
typ_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in typ_list:
    if i%3==0:
        print(i,"is divisible by 3")
    else:
        print(i,"is not divisible by 3")

# question7 
#the example of mutablble data type is a list
list=[1,2,3]
#the example of immutablr data type is a string
a_string="a_string"