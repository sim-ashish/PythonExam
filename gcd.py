# Program to find the gcd of two numbers
# Input -- ten twentytwo
# Output -- two

import re
from functools import reduce
# import pdb


class GCD:

    '''Class to Create objects of gcd instances, which includes gcd and word_to_number'''

    def __init__(self: object, num1: str, num2: str) -> None:

        '''Initialize variables on the object creation time'''

        self.num_one = self.word_to_number(num1)
        self.num_two = self.word_to_number(num2)
        self.gcd_result = self.gcd(self.num_one, self.num_two) if self.num_one > self.num_two else self.gcd(self.num_two, self.num_one)

    def gcd(self: object,num1: int, num2: int) -> int:

        '''Function to return the gcd of two numbers'''

        if num2 == 0:
            return num1
        else:
            return self.gcd(num2, num1 % num2)

    def word_to_number(self: object, word: str) -> int:
        
        '''Function to return digit form of a number from word format'''

        word_dict = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

        keys_str = "|".join(word_dict.keys())           # to create a pattern, so that we can match from word

        temp_result = re.findall(keys_str, word)          # re.findall(pattern, word)

        result = reduce(lambda initial, x: initial + word_dict[x], temp_result, "")

        return int(result)

if __name__ == '__main__':
    var1 = input("Enter First Number: ")
    var2 = input("Enter Second Number: ")

    # pdb.set_trace()

    gcd_object = GCD(var1, var2)

    print(f'GCD of given numbers is {gcd_object.gcd_result}')
