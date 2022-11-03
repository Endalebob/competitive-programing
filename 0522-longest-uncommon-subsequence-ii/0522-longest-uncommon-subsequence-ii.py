class Solution:
    def findLUSlength(self, strings: List[str]) -> int:
        #first sort with length
        #compare every string
        strings.sort()
        strings.sort(key = lambda i:len(i))
        strings = strings[::-1]
        def checker(current,s,last):
            for k in range(last):
                start = 0
                current = strings[k]
                for i in range(len(current)):
                    if current[i] == s[start]:
                        start += 1
                        if start == len(s):
                            return True
            return False

        current = strings[0]
        i = 1
        while i < len(strings) and len(strings[i]) == len(current):
            if current == strings[i]:
                i += 1
                while i < len(strings) and checker(current,strings[i],i):
                    i += 1
                if i < len(strings):
                    current = strings[i]
                else:
                    return -1
            else:
                return len(current)
            i += 1
        return len(current)