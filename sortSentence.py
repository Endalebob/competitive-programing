Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sortSentence(self, s):
        li = s.split()
        lii = s.split()
        
        for i in li:
            index = int(i[-1])
            st = ''
            for j in range(len(i)-1):
                st += i[j]
            st += ' '
            lii[index-1] = st
        stt = ''
        for j in lii:
            stt += j
        return stt.strip()