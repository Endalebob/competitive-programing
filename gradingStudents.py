Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def gradingStudents(grades):
    newgrade = []
    for i in grades:
        if i<38:
            newgrade.append(i)
        elif i%5 == 4:
            newgrade.append(i+1)
        elif i%5 == 3:
            newgrade.append(i+2)
        else:
            newgrade.append(i)
    return newgrade