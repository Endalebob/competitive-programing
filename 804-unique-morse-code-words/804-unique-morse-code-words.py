class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        valu = set()
        ma = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in words:
            val = ''
            for j in i:
                val += ma[ord(j)-ord('a')]
            valu.add(val)
        return len(valu)