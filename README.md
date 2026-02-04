# Agentic Application with Dynamic Tool Orchestration

This is an AI agent that can understand natural language queries and automatically figure out which tools to use to solve them. It handles multi-step operations by chaining results together.

## What it does

The agent can:
- Parse natural language queries (like "add 5 and 3, then multiply by 2")
- Automatically decide which tools to use
- Chain multiple operations together
- Handle errors gracefully

## Getting Started

### Requirements
- Python 3.7 or higher
- No external libraries needed (just standard Python)

### Installation
```bash
git clone <your-repo-url>
cd "KvellD Task"
```

### Running it
```bash
# Run the demo with example queries
python main.py

# Run tests
python test_agent.py
```

## How it works

The agent has three main parts:

1. **tools.py** - Contains the actual tools (Calculator and StringProcessor)
2. **agent.py** - The brain that parses queries and decides which tools to call
3. **main.py** - Simple CLI to interact with the agent

### The Agent's Logic

When you give it a query like "Add 5 and 3, then multiply by 2":

1. It splits the query into steps using regex patterns
2. For each step, it figures out which operation you want (add, multiply, etc.)
3. It extracts the numbers from your text
4. It calls the right tool with the right arguments
5. It passes results from one step to the next
6. Returns the final answer

It uses keyword matching to figure out what you want dynamically.

## Available Tools

### Calculator
- `add(a, b)` - adds two numbers
- `subtract(a, b)` - subtracts b from a
- `multiply(a, b)` - multiplies two numbers
- `divide(a, b)` - divides a by b

### String Processor
- `uppercase(text)` - converts to uppercase
- `lowercase(text)` - converts to lowercase
- `reverse(text)` - reverses the string
- `concat(a, b)` - joins two strings

## Examples

### Example 1: Multi-step math
```
Input: "Add 1 and 1, then multiply with 10, then subtract 0.5 from it, and add 4."

Output:
Step 1: add(1.0, 1.0) = 2.0
Step 2: multiply(2.0, 10.0) = 20.0
Step 3: subtract(20.0, 0.5) = 19.5
Step 4: add(19.5, 4.0) = 23.5
Final result: 23.5
```

### Example 2: String operations
```
Input: "uppercase 'hello world', then reverse"

Output:
Step 1: uppercase(hello world) = HELLO WORLD
Step 2: reverse(HELLO WORLD) = DLROW OLLEH
Final result: DLROW OLLEH
```

### Example 3: Simple division
```
Input: "Add 5 and 3, then divide by 2"

Output:
Step 1: add(5.0, 3.0) = 8.0
Step 2: divide(8.0, 2.0) = 4.0
Final result: 4.0
```

### Example 4: Chained operations
```
Input: "concat 'hello' and 'world', then uppercase"

Output:
Step 1: concat(hello, world) = helloworld
Step 2: uppercase(helloworld) = HELLOWORLD
Final result: HELLOWORLD
```

## Adding New Tools

It's pretty straightforward to add new tools:

1. Add your function to tools.py:
```python
def power(self, a, b):
    return float(a) ** float(b)

TOOLS['power'] = calc.power
```

2. Register the keyword in agent.py:
```python
self.operation_map['power'] = ('power', 2)
```

That's it. Now the agent understands "power" operations.

## Design Decisions

### Why regex instead of NLP libraries?
- Wanted to keep it simple with no dependencies
- For structured math queries, regex works fine
- Easier to debug and understand

### Why sequential execution?
- Most math operations are naturally sequential
- Simpler to implement and reason about
- Good enough for the use case

### Trade-offs
- **Pros**: Simple, no dependencies, easy to extend, transparent execution
- **Cons**: Limited natural language understanding, can't handle complex grammar, sequential only

## Possible Improvements

Some ideas for making it better:
- Use an actual LLM for better language understanding
- Support parallel execution for independent operations
- Add support for variables ("store result as X")
- Handle conditional logic ("if X then Y")
- Add more tools (file operations, API calls, etc.)

## Error Handling

The agent handles common errors:
- Division by zero
- Invalid queries that can't be parsed
- Unknown operations
- Missing arguments

## Testing

Run the test suite:
```bash
python test_agent.py
```

Tests cover:
- Basic operations
- Multi-step chains
- Error cases
- Edge cases

## Project Structure

```
KvellD Task/
├── tools.py          # Tool definitions
├── agent.py          # Agent logic
├── main.py           # CLI interface
├── test_agent.py     # Tests
└── README.md         # This file
```

## LangChain Alternative

There's also a LangChain-based implementation available in `langchain_agent.py` that uses Google Gemini LLM for better natural language understanding. See `LANGCHAIN_COMPARISON.md` for a detailed comparison.

**To use LangChain version**:
```bash
pip install langchain langchain-google-genai langgraph google-generativeai python-dotenv
export GOOGLE_API_KEY='your-key-here'
python langchain_agent.py
```

The LangChain version provides better NLP understanding but requires a Google Gemini API key and has rate limits. The custom implementation is free and has no dependencies.
