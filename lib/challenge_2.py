# Defining function
def two_positive_numbers(a,b,c):
    # Checking if a , b  and c are positive
    a = a > 0
    b = b > 0
    c = c > 0
    # Adding the true and false values
    positive_count = a + b + c
    # Returning True or False depending on the value of positive_count.
    return positive_count == 2
