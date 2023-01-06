class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        maxWidth += 1
        i = 0
        ans = []
        while i<len(words):
            curr = len(words[i])+1
            cnt = len(words[i])
            j = i+1
            while j<len(words) and curr + len(words[j])+1 <= maxWidth:
                curr += len(words[j])+1
                cnt += len(words[j])
                j += 1
            if j == len(words):
                s = ''
                for k in range(i,j):
                    s += words[k]
                    if k<j-1:
                        s += ' '
                        
                s += ' '*(maxWidth-len(s)-1)
                ans.append(s)
                break
            if j == i+1:
                
                must = maxWidth - cnt-1
                s = words[i]+' '*must
                ans.append(s)
            else:
                must = ' '*((maxWidth-cnt-1)//(j-i-1))
                rem = (maxWidth-cnt-1)%(j-i-1) 
                s = ''
                for k in range(i,j):
                    s += words[k]
                    if k<j-1:
                        s += must
                        if rem+i>k:
                            s += ' '
                ans.append(s)
            i = j
        return ans
                    