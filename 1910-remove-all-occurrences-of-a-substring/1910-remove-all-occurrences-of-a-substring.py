class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # the index of the first occerance of the part
        # if there is no part in s it become -1
        the_first_occerance = s.find(part)

        # while there is part in s remove part
        while the_first_occerance != -1:
            left_string_after_removal = s[:the_first_occerance]
            right_string_after_removal = s[the_first_occerance+len(part):]

            # the new string become the concatenation of remaining left part and right part
            s = left_string_after_removal + right_string_after_removal
            the_first_occerance = s.find(part)
        return s