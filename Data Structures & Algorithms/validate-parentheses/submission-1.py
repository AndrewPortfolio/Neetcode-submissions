class Solution:
    def isValid(self, s: str) -> bool:
        #create a stack --> insert each char into stack in s
        #pop off each char look for closing bracket 

        stack = []

        close = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in close:
                if stack and stack[-1] == close[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
           

        return True if not stack else False