class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        words_len = len(words)
        counter = Counter(words)
        sub_str_len = word_len*words_len
        
        def is_sub_string(index):
            copy_counter = counter.copy()
            check = 0
            for i in range(index,index+sub_str_len,word_len):
                string = s[i:i+word_len]
                if string in copy_counter and copy_counter[string]>0:
                    copy_counter[string] -= 1
                    check += 1
                else:
                    return False
            return check == words_len
        ans = []
        for i in range(len(s)):
            if is_sub_string(i):
                ans.append(i)
        return ans
            