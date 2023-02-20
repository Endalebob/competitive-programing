class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_partition_counts(s: str) -> List[int]:
            i, j = 0, 0
            sequence = []
            while j < len(s):
                while j < len(s) and s[j] == s[i]:
                    j += 1
                sequence.append(j - i)
                i = j
            return sequence

        sequence = get_partition_counts(s)
        
        ans = 0
        for word in words:
            start, i, j = 0, 0, 0
            flag = False
            while j < len(word) and start < len(sequence):
                if s[i] != word[j]:
                    flag = True
                    break
                k = j
                while k < len(word) and word[k] == word[j]:
                    k += 1
                count = k - j
                if count == sequence[start] or (count < sequence[start] and sequence[start] >= 3):
                    j = k
                    i += sequence[start]
                    start += 1
                    continue
                else:
                    flag = True
                    break
            if not flag and j == len(word) and start == len(sequence):
                ans += 1
        
        return ans
