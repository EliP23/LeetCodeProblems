class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_nums_dict = {"I": 1, "V" : 5, "X":  10, "L": 50, "C": 100, "D": 500, "M" : 1000}
        i = 0
        sum = 0
        while i < len(s):
            curChar = s[i]
            if i < len(s)-1:
                nextChar = s[i+1]
            else:
                nextChar = ""

            if curChar in (["I", "X", "C"]) and nextChar in (["V", "X", "L", "C", "D", "M"]):
                if (curChar == "I") and (nextChar == "V" or nextChar == "X"):
                   sum = sum - 1
                elif (curChar == "X") and (nextChar == "L" or nextChar == "C"):
                    sum = sum - 10
                elif (curChar == "C") and (nextChar == "D" or nextChar == "M"):
                    sum = sum - 100
                else:
                    sum = sum + roman_nums_dict[s[i]]
            else:
                sum = sum + roman_nums_dict[s[i]]
            
            i = i + 1
            nextChar = ""

        return sum


solution = Solution()


print(solution.romanToInt("DCXXI"))