# tools.py - defines the available tools for the agent

class Calculator:
    # basic math operations
    def add(self, a, b):
        return float(a) + float(b)
    
    def subtract(self, a, b):
        return float(a) - float(b)
    
    def multiply(self, a, b):
        return float(a) * float(b)
    
    def divide(self, a, b):
        if float(b) == 0:
            raise ValueError("can't divide by zero!")
        return float(a) / float(b)

class StringProcessor:
    # string manipulation stuff
    def uppercase(self, text):
        return str(text).upper()
    
    def lowercase(self, text):
        return str(text).lower()
    
    def reverse(self, text):
        return str(text)[::-1]
    
    def concat(self, a, b):
        return str(a) + str(b)

# initialize tool instances
calc = Calculator()
string_proc = StringProcessor()

# map operation names to actual functions
TOOLS = {
    'add': calc.add,
    'subtract': calc.subtract,
    'multiply': calc.multiply,
    'divide': calc.divide,
    'uppercase': string_proc.uppercase,
    'lowercase': string_proc.lowercase,
    'reverse': string_proc.reverse,
    'concat': string_proc.concat,
}
