"""
   Min Max Stack Construction.py

   Write a MinMaxStack class for a Min Max Stack. The class should support:
      • Pushing and popping values on and off the stack.
      • Peeking at the value at the top of the stack.
      • Getting both the minimum and the maximum values in the stack at any given point in time.
      
   All class methods, when considered independently, should run in constant time and with constant space.
   
   Sample Usage
   // All operations below are performed sequentially.
   MinMaxStack(): - // instantiate a MinMaxStack
   push(5): -
   getMin(): 5
   getMax(): 5
   peek(): 5
   push(7):
   getMin(): 5
   getMax(): 7
   peek(): 7
   push(2): -
   getMin(): 2
   getMax(): 7
   peek(): 2
   pop(): 2
   pop(): 7
   getMin(): 5
   getMax(): 5
   peek(): 5

"""
# Feel free to add new properties and methods to the class.
class MinMaxStack:
	 def __init__(self):
	    self.minMaxStack = []
		 self.stack = []
		
	 # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]
	
    # O(1) time | O(1) space
    def pop(self):
		  self.minMaxStack.pop()
        return self.stack.pop()

	 # O(1) time | O(1) space
    def push(self, number):
        newMinMax = {'min': number, 'max': number}
        if len(self.minMaxStack):
			  lastMinMax = self.minMaxStack[len(self.minMaxStack)-1]
			  newMinMax['min'] = min(lastMinMax['min'], number)
			  newMinMax['max'] = max(lastMinMax['max'], number)
		  self.minMaxStack.append(newMinMax)
		  self.stack.append(number)
		
    # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack)-1]['min']
	
    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack)-1]['max']
