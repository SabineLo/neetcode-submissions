class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {')' : '(', ']' : '[', '}' :'{'} #the order is this way because the open always going to be first so easy to pair them since we know its in stack already 
        for c in s:
            if c in closedToOpen:
                if stack and stack[-1] == closedToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False



