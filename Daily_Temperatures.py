class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        myStack = []

        for ix, temperature in enumerate(temperatures):
            while myStack and temperature > myStack[-1][0]:
                stackTemp, stackIndex = myStack.pop()
                result[stackIndex] = ix - stackIndex
            myStack.append([temperature,ix])
        return result