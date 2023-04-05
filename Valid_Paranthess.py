class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)

            else:
                if len(stack) == 0:
                    return False
                else:
                    current = stack.pop()
                    if p == ")" and current != "(":
                        return False
                    elif p == "]" and current != "[":
                        return False
                    elif p == "}" and current != "{":
                        return False
        if len(stack) == 0:
            return True
        else:
            return False