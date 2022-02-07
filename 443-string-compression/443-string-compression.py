class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        i = 0
        j = 0
        limit = len(chars) - 1
        while j < limit+1:
            hold = 1
            while j < limit and chars[j] == chars[j+1]:
                hold += 1
                j += 1
            if hold == 1:
                ans.append(chars[i])
            elif hold > 999:
                ans.append(chars[i])
                ans.append(str(hold//1000))
                ans.append(str((hold%1000)//100))
                ans.append(str((hold%100)//10))
                ans.append(str(hold%10))
            elif hold > 99:
                ans.append(chars[i])
                ans.append(str(hold//100))
                ans.append(str((hold%100)//10))
                ans.append(str(hold%10))
            elif hold > 9:
                ans.append(chars[i])
                ans.append(str(hold//10))
                ans.append(str(hold%10))
            else:
                ans.append(chars[i])
                ans.append(str(hold))
            j += 1
            i = j
        chars[:] = ans
        return len(chars)
                