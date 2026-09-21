class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {'}' : '{', ']':'[', ')':'('} #why are we doing this? - the reason why this is being done is in order to check if the most recent push is there corresponding to the recent closed bracket.

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



