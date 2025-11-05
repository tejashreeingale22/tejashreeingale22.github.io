class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        else:
            stack = []
            open_brackets=['(', '[','{']
            close_brackets=[')',']','}']
            for c in s:
                if c in open_brackets:
                    stack.append(c)
                if c in close_brackets:
                    #check any elements is there in stack and if the index of that element in close_brackets is equal to the index of the element which is present in the stack from open_brackets then pop the element from the stack
                    if stack and close_brackets.index(c) == open_brackets.index(stack[-1]):
                        stack.pop()
                    else:
                        return False
            if len(stack)!=0:
                return False
                
            return True
