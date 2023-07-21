class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myStack = []
        for i in operations:
            if i == "C":
                myStack.pop()
            elif i == "+":
                myStack.append(myStack[-1] + myStack[-2])
            elif i == "D":
                myStack.append(myStack[-1] * 2)
            else:
                myStack.append(int(i))
        return sum(myStack)