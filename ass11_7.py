def display(no):
    if(no == 0):
        return
    display(no - 1)
    print("*" * no)
    
display(4)

"""
OUTPUT:
*
**
***
****
"""