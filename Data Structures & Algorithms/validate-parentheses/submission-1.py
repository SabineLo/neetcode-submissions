class Solution:
    #if there is a pattern and it has to be correct order? I think regex
    def isValid(self, s: str) -> bool:
        stack = []
        #help determine if closing matches open
        pattern = {")":"(","]": "[", "}" : "{" } # if its like this append and then pop if closing bracket is found can only start with open
        for c in s:
            if c in pattern: #so here its actually checking the keys 
                if stack and stack[-1] == pattern[c]: #stack[-1] is the top of our stack and wants to make sure that the value macthes the opening parenthis, making sure its not empty
                    stack.pop() #I think this is ensuring that its strating with an open parenthsies
                else:
                    return False
            else:
                stack.append(c) #because the recent parenthesis always has tomatch the closing parenthis
            #hashmap it has to be the most recent because otherwise its not valid the last value is the recent value so [(,{] { is the recent top of stack/ [-1]
    #[-1] is the last value of our list
        return True if not stack else False #Im assuming its asking if its empty