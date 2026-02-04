from agent import Agent

def main():
    agent = Agent()
    
    # some test queries to try out
    test_queries = [
        "Add 1 and 1, then multiply with 10, then subtract 0.5 from it, and add 4.",
        "Add 5 and 3, then divide by 2",
        "uppercase 'hello world', then reverse",
        "concat 'hello' and 'world', then uppercase"
    ]
    
    print("=== Agentic Tool Orchestration Demo ===")
    print()
    
    for i, query in enumerate(test_queries, 1):
        print(f"Query {i}: {query}")
        try:
            result, log = agent.execute(query)
            print("Steps:")
            for step in log:
                print(f"  {step}")
            print(f"Final result: {result}")
            print()
        except Exception as e:
            print(f"Error: {e}")
            print()
    
    # interactive mode
    print("=== Interactive Mode ===")
    print("Type your query (or 'quit' to exit):")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            if not user_input:
                continue
            
            result, log = agent.execute(user_input)
            print()
            for step in log:
                print(f"  {step}")
            print(f"Result: {result}")
            print()
        except Exception as e:
            print(f"Error: {e}")
            print()

if __name__ == "__main__":
    main()
