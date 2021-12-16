Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fizzBuzz(self, n):
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