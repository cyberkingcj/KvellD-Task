import re
from tools import TOOLS

class Agent:
    def __init__(self):
        self.tools = TOOLS
        # mapping keywords to operations
        self.operation_map = {
            'add': ('add', 2),
            'plus': ('add', 2),
            'subtract': ('subtract', 2),
            'minus': ('subtract', 2),
            'multiply': ('multiply', 2),
            'times': ('multiply', 2),
            'divide': ('divide', 2),
            'uppercase': ('uppercase', 1),
            'upper': ('uppercase', 1),
            'lowercase': ('lowercase', 1),
            'lower': ('lowercase', 1),
            'reverse': ('reverse', 1),
            'concat': ('concat', 2),
            'concatenate': ('concat', 2),
        }
    
    def parse_query(self, query):
        # break down the query into individual steps
        query = query.lower().strip()
        steps = []
        
        # split on common separators like "then" and ", and"
        parts = re.split(r'(?:,?\s+then\s+|,\s+and\s+)', query)
        
        for part in parts:
            part = part.strip().rstrip(',.')
            step = self._parse_step(part)
            if step:
                steps.append(step)
        
        return steps
    
    def _parse_step(self, text):
        # figure out what operation and arguments from the text
        numbers = re.findall(r'-?\d+\.?\d*', text)
        
        # extract quoted strings for string operations
        strings = re.findall(r'["\']([^"\']*)["\']', text)
        
        # check which operation keyword is in the text
        for keyword, (op, arg_count) in self.operation_map.items():
            if keyword in text:
                if arg_count == 1:
                    # for string operations, use the string if available
                    if strings:
                        return (op, [strings[0]])
                    return (op, [])
                elif arg_count == 2:
                    # for concat, look for two strings
                    if op == 'concat' and len(strings) >= 2:
                        return (op, [strings[0], strings[1]])
                    # for numeric operations
                    if 'from' in text or 'by' in text:
                        if numbers:
                            return (op, [float(numbers[0])])
                    elif len(numbers) >= 2:
                        return (op, [float(numbers[0]), float(numbers[1])])
                    elif len(numbers) == 1:
                        return (op, [float(numbers[0])])
                break
        
        return None
    
    def execute(self, query):
        # main execution loop
        steps = self.parse_query(query)
        
        if not steps:
            raise ValueError("couldn't understand the query")
        
        result = None
        log = []
        
        for i, (operation, args) in enumerate(steps):
            try:
                # figure out the actual arguments to pass
                if result is not None and len(args) < 2:
                    if len(args) == 0:
                        actual_args = [result]
                    else:
                        actual_args = [result, args[0]]
                else:
                    actual_args = args
                
                # call the tool
                tool = self.tools.get(operation)
                if not tool:
                    raise ValueError(f"unknown operation: {operation}")
                
                result = tool(*actual_args)
                log.append(f"Step {i+1}: {operation}({', '.join(map(str, actual_args))}) = {result}")
                
            except Exception as e:
                raise RuntimeError(f"error in step {i+1} ({operation}): {str(e)}")
        
        return result, log
