class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        isValid = lambda a : 0<=a<=255
        isValid2 = lambda a : 0<=a<=4
        isValid3 = lambda a : 'a'<=a<='f' or 'A'<=a<='F'
        if ':' in queryIP:
            converted_list = queryIP.split(':')
            if len(converted_list) == 8:
                for i in converted_list:
                    if not i.isalnum() or not isValid2(len(i)):
                        return 'Neither'
                    for m in i:
                        if m.isalpha() and not isValid3(m):
                            return 'Neither'
                return "IPv6"
        elif '.' in queryIP:
            converted_list = queryIP.split('.')
            if len(converted_list) == 4:
                for i in converted_list:
                    if not i.isdigit() or not isValid(int(i)):
                        return 'Neither'
                    if len(i)>1 and i[0] == '0':
                        return 'Neither'
                return "IPv4"
        return 'Neither'
        