#by using comparison operators, we compare values and  use it in if statements to get a boolean answer.

def max_num(num1, num2, num3 ):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3 

print(max_num(3,6,4))         

#we can also compare strings
"""We have 
>.greater than.
=.equal to.
<. less than.
!.no equal.
>=.greater than or equal to.
<=.less than or equal to."""
             













