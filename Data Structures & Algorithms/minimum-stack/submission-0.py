class MinStack:

    def __init__(self):
        self.stack_array = []
        

    def push(self, val: int) -> None:
        
        self.stack_array.append(val)
        print(self.stack_array)

    def pop(self) -> None:
        self.stack_array = self.stack_array[:-1]
        print("pop",self.stack_array)

    def top(self) -> int:
        print(self.stack_array[len(self.stack_array)-1])
        return self.stack_array[len(self.stack_array)-1]

        

    def getMin(self) -> int:
        print(sorted(self.stack_array)[0])
        return sorted(self.stack_array)[0]
        
