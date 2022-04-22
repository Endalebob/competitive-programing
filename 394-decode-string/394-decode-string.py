class Solution:
    def decode (self, s, index):
        self.index = index
        dec = ''
        ret = ''
        num = ''
        while self.index<len(s) and s[self.index] != ']':
            if s[self.index].isalpha():
                dec += s[self.index]
            elif s[self.index].isdigit():
                num += s[self.index]
            else:
                dec_str = self.decode(s,self.index+1)
                dec += dec_str*int(num)
                num = ''
            self.index += 1
        return dec
        
    def decodeString(self, s: str) -> str:
        return self.decode(s,0)