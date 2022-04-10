class Solution:
    def fizzBuzz(self, n):
        list1 = []
        for i in range(n):
            if (i+1)%15 == 0:
                list1.append('FizzBuzz')
            elif (i+1)%3 == 0:
                list1.append('Fizz')
            elif (i+1)%5 == 0:
                list1.append('Buzz')
            else:
                list1.append(str(i+1))
        
        return list1