"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output "Fizz" instead of the number and for the multiples of five output "Buzz".
For numbers which are multiples of both three and five output "FizzBuzz".
Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
class Solution(object):
    def fizzbuzz(self, n):
        lis= []
        for i in range(1, n+1):
            if i%15==0:
                lis.append("FizzBuzz")
            elif i%3==0:
                lis.append("Fizz")
            elif i%5==0:
                lis.append("Buzz")
            else:
                lis.append(i)
        return lis

if __name__=="__main__":
    testcases= [5, 10, 15, 31]
    obj= Solution()
    for test in testcases:
        print test, " -> ", obj.fizzbuzz(test)
