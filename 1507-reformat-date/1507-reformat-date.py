class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": '01', "Feb": '02', 
                 "Mar": '03', "Apr": '04', 
                 "May": '05', "Jun": '06', 
                 "Jul": '07', "Aug": '08', 
                 "Sep": '09', "Oct": '10', 
                 "Nov": '11', "Dec": '12'}
        m = date.split()
        DD = m[0][:-2].zfill(2)
        YY = m[-1]
        MM = month[m[1]]
        return "-".join([YY,MM,DD])