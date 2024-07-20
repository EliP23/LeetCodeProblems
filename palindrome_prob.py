class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x=str(x)
        reversed_str = []
        str_length = len(x) - 1
        i = str_length

        while i >= 0:
            reversed_str.append(x[i])
            i -= 1

        print(reversed_str)

solution = Solution()

# Test cases
test_values = [121, 5235, 303, 12321]

# Test the isPalindrome method
for value in test_values:
    solution.isPalindrome(value)
