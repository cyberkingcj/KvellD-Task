# LangChain implementation using Google Gemini
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

try:
    from langchain.agents import create_react_agent
except ImportError:
    from langgraph.prebuilt import create_react_agent

# Load .env file if it exists (optional)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Tool functions
@tool
def add(input_str: str) -> str:
    """Add two numbers. Input format: 'a,b'"""
    a, b = map(float, input_str.split(','))
    return str(a + b)

@tool
def subtract(input_str: str) -> str:
    """Subtract two numbers. Input format: 'a,b'"""
    a, b = map(float, input_str.split(','))
    return str(a - b)

@tool
def multiply(input_str: str) -> str:
    """Multiply two numbers. Input format: 'a,b'"""
    a, b = map(float, input_str.split(','))
    return str(a * b)

@tool
def divide(input_str: str) -> str:
    """Divide two numbers. Input format: 'a,b'"""
    a, b = map(float, input_str.split(','))
    if b == 0:
        return "Error: can't divide by zero"
    return str(a / b)

@tool
def uppercase(text: str) -> str:
    """Convert text to uppercase"""
    return text.upper()

@tool
def lowercase(text: str) -> str:
    """Convert text to lowercase"""
    return text.lower()

@tool
def reverse(text: str) -> str:
    """Reverse the text"""
    return text[::-1]

@tool
def concat(input_str: str) -> str:
    """Concatenate two strings. Input format: 'str1,str2'"""
    parts = input_str.split(',', 1)
    return parts[0] + parts[1]

tools = [add, subtract, multiply, divide, uppercase, lowercase, reverse, concat]

def create_langchain_agent():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    agent = create_react_agent(llm, tools)
    return agent

def main():
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set")
        print("")
        print("Option 1: Set environment variable")
        print("  export GOOGLE_API_KEY='your-key-here'  # Linux/Mac")
        print("  set GOOGLE_API_KEY=your-key-here       # Windows")
        print("")
        print("Option 2: Use .env file")
        print("  1. pip install python-dotenv")
        print("  2. Create .env file with: GOOGLE_API_KEY=your-key-here")
        print("")
        print("Get your API key from: https://makersuite.google.com/app/apikey")
        return
    
    agent = create_langchain_agent()
    
    test_queries = [
        "Add 1 and 1, then multiply the result by 10, then subtract 0.5, then add 4",
        "Add 5 and 3, then divide by 2",
    ]
    
    print("=== LangChain Agent with Gemini ===")
    print()
    
    for i, query in enumerate(test_queries, 1):
        print(f"Query {i}: {query}")
        try:
            result = agent.invoke({"messages": [("user", query)]})
            final_message = result["messages"][-1].content
            # Extract text if it's a list of content blocks
            if isinstance(final_message, list):
                final_message = ' '.join([block.get('text', '') for block in final_message if block.get('type') == 'text'])
            print(f"Final result: {final_message}")
            print()
        except Exception as e:
            print(f"Error: {e}")
            print()
    
    print("=== Interactive Mode ===")
    print("Type your query (or 'quit' to exit):")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            if not user_input:
                continue
            
            result = agent.invoke({"messages": [("user", user_input)]})
            final_message = result["messages"][-1].content
            # Extract text if it's a list of content blocks
            if isinstance(final_message, list):
                final_message = ' '.join([block.get('text', '') for block in final_message if block.get('type') == 'text'])
            print(f"Result: {final_message}")
            print()
        except Exception as e:
            print(f"Error: {e}")
            print()

if __name__ == "__main__":
    main()
