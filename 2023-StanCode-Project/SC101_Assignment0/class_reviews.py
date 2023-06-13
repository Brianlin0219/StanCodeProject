"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    """
    TODO:
    """
    sc = input("Which class?")
    if sc != '-1':
        score = float(input("Score:"))
    maximum_001 = 0
    minimum_001 = 10
    total_001 = 0
    nums_001 = 0
    maximum_101 = 0
    minimum_101 = 10
    total_101 = 0
    nums_101 = 0
    while sc != '-1':
        if sc == 'Sc001':
            nums_001 += 1
            total_001 += score
            if score > maximum_001:
                maximum_001 = score
            if score < minimum_001:
                minimum_001 = score
        else:
            nums_101 += 1
            total_101 += score
            if score > maximum_101:
                maximum_101 = score
            if score < minimum_101:
                minimum_101 = score
        sc = input("Which class?")
        if sc != '-1':
            score = float(input("Score:"))
    print('==========SC001==========')
    if nums_001 == 0:
        print('No score for SC001')
    else:
        print('Max(001):' + str(int(maximum_001)))
        print('Min(001):' + str(int(minimum_001)))
        print('Avg(001):' + str(total_001 / nums_001))
    print('==========SC101==========')
    if nums_101 == 0:
        print('No score for SC101')
    else:
        print('Max(101):' + str(int(maximum_101)))
        print('Min(101):' + str(int(minimum_101)))
        print('Avg(101):' + str(total_101 / nums_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
