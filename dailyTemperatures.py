Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]*len(temperatures)
        mono = [0]
        count = 0
        for i in range(1,len(temperatures)):
            count = 0
            while len(mono) > 0 and temperatures[mono[-1]]<temperatures[i]:
                c = mono.pop()
                stack[c] = i - c
                
            mono.append(i)
        return stack