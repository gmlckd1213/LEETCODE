class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__push_stack=[]
        self.__pop_stack=[]
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.__push_stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.__pop_stack:
            return self.__pop_stack.pop()
        else:
            while self.__push_stack: # Move push_stack to pop_stack
                temp=self.__push_stack.pop() 
                self.__pop_stack.append(temp) 
            return self.__pop_stack.pop()
            
            
        
        

    def peek(self) -> int:
        
        """
        Get the front element.
        """
        if self.__pop_stack:
            return self.__pop_stack[-1]
        else:
            
            while self.__push_stack: # Move push_stack to pop_stack
                temp=self.__push_stack.pop()
                self.__pop_stack.append(temp)
            return self.__pop_stack[-1]
            
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.__push_stack or self.__pop_stack else True
        