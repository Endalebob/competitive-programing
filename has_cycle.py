Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def has_cycle(head):
    li = []
    while head:
        if head in li:
            return 1
        li.append(head)
        head = head.next
    return 0