Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  def isValid(self, s: str) -> bool:
        opp = '[{('
        clo = ']})'
        temp = []
        for i in s:
            if i in clo and len(temp)==0:
                return False
            else:
                if i in opp:
                    temp.append(i)
                else:
                    if opp.index(temp[-1])==clo.index(i):
                        temp.pop()
                    else:
                        return False
        if len(temp) == 0:
            return True
        else:
            return False