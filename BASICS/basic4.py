# sequecnce data type
# sequence comprises of group of elements

name = 'DEevyansh Chhabra'
city = "vRINDAVAN"
countrY = ''' INDIA ''' 
# any of the above method can be used to define string

print(name[0]) 

# if we get out of index it will show error

# -ve indexing
name1 = "Deevyansh"
print(name1[-1]) # would print h  negative indexing start from right with last right most element as -1

print(name1[-9]) # would print d

# string is geenrally said immutable once created can not be modified
  
a = "deevyansh"
b = "deevyansh"

# first deevyansh object is created now a and b will both pting to  same object so imutability in this context helps to save some space'''

# name ="DEEVYANSH CHHABRA"
# name[0] = R
# this action is not possible due to the nature of string immutability


# concatination of string
first_name = "DEEVYANSH"
last_name = "CHHABRA"

complete_name = first_name+" "+last_name
print(complete_name)

# length of string
print(len(first_name))

# slicng string : any portion of entire string is known as slicing of string
name2 = "DEEVYANSH CHHABRA"  # lets see extracting evya
print(name2[2:6]) # we will incluse one extra
# if we hv no end point

print(name2[2:])  # when u want to go till end

print(name2[:9])  # when i want ton print copmlete Deevyansh just include one extra index


print(name2[:]) # it will print full Deevyansh Chhabra

# printing Chhabra only using -ve indexing
print(len(name2))
#print(name2[-7:-1]) BECAUSE WE ALSO NEED TO GO +1 FOR LAST CHARACTER BUT IN THIS CASE IT ISNT POSSIBLE

print(name2[-7:]) # this would be the way to print CHHABRA

# lets print DEEVYANSH using -ve indexing
print(name2[-17:-7])  # -7 because we would include one space more  

str1 = "  Deevyansh"

print(str1.upper())
print(str1.lower())
print(str1.capitalize())  # will make only first character capital an other small all will be small except first
print(str1.strip()) # will remove extra space

str3 = "Hello I am DEEVYANSH , I am nice, I am wow"
print(str3.replace("I am","We are"))

 # name
 