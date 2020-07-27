

"""To Check Whether Entered Number Is Palindrome Or Not"""
"""input:numVal contains a number positive or Negative"""
"""OutPut: Returns a Boolean Value(Either True or False based on the Function Logic)"""


def palindrome_check(num_val):
    new_int = 0
    result_val = False
    if num_val > 0:
        new = (str(num_val)[::-1])
        new_int = int(new.strip())
    if num_val == new_int:
        result_val = True
    print(new_int)


if __name__ == "__main__":
    palindrome_check(int(input("Enter the Number you like to check Palindrome")))
