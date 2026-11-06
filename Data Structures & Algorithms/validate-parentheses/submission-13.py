class Solution:
    def isValid(self, s: str) -> bool: 
        charSet = { ')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in charSet:
                if stack and stack[-1] == charSet[c]:
                    stack.pop()
                else:
                    return False        
            else:
                stack.append(c)

        return not stack


        