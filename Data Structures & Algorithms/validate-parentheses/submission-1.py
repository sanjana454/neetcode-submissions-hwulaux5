class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # stack to keep track of opening brackets

        # mapping: closing bracket → corresponding opening bracket
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        # iterate through each character in string
        for c in s:

            # if it's a closing bracket
            if c in closeToOpen:

                # check if stack is not empty AND top matches expected opening bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()  # valid pair → remove from stack
                else:
                    return False  # mismatch or no opening bracket

            else:
                # if it's an opening bracket → push to stack
                stack.append(c)

        # valid if no unmatched opening brackets remain
        return True if not stack else False