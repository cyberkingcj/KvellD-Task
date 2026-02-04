# LangChain vs Custom Implementation

This project includes two implementations:

## 1. Custom Implementation (main.py)
**Files**: `tools.py`, `agent.py`, `main.py`

**Pros**:
- No external dependencies
- Full control over parsing logic
- Lightweight and fast
- Easy to understand and debug
- No API costs

**Cons**:
- Limited natural language understanding
- Regex-based parsing (less flexible)
- Manual keyword mapping required

**Usage**:
```bash
python main.py
```

## 2. LangChain Implementation (langchain_agent.py)
**File**: `langchain_agent.py`

**Pros**:
- Better natural language understanding (uses LLM)
- Handles complex queries more naturally
- Built-in agent reasoning (ReAct pattern)
- Automatic tool selection
- More flexible query formats

**Cons**:
- Requires Google Gemini API key
- External dependencies (langchain, langchain-google-genai)
- API rate limits (free tier: 5 requests/minute)
- Slower (network calls to Gemini API)
- Less transparent (LLM black box)

**Setup**:
```bash
# Install dependencies
pip install langchain langchain-google-genai langgraph google-generativeai python-dotenv

# Set API key
export GOOGLE_API_KEY='your-key-here'  # Linux/Mac
set GOOGLE_API_KEY=your-key-here       # Windows

# Or use .env file
echo "GOOGLE_API_KEY=your-key-here" > .env

# Run
python langchain_agent.py
```

**Get API Key**: https://makersuite.google.com/app/apikey

## Key Differences

### Query Understanding
- **Custom**: Keyword matching ("add", "multiply", etc.)
- **LangChain**: Gemini LLM interprets natural language

### Tool Selection
- **Custom**: Regex patterns + keyword map
- **LangChain**: Gemini decides which tool to use

### Execution Flow
- **Custom**: Sequential parsing → execution
- **LangChain**: ReAct loop (Thought → Action → Observation)

### Cost
- **Custom**: Free
- **LangChain**: Free tier available (with rate limits), paid plans for higher usage

## When to Use Which?

### Use Custom Implementation when:
- You want zero dependencies
- Queries follow predictable patterns
- You need full control
- Speed is critical
- No internet connection needed

### Use LangChain Implementation when:
- You need better NLP understanding
- Queries are more conversational
- You want built-in agent reasoning
- You're okay with API rate limits
- You want to leverage LLM capabilities

## Example Comparison

**Query**: "Add 5 and 3, then multiply by 2"

**Custom Implementation**:
1. Regex splits: ["Add 5 and 3", "multiply by 2"]
2. Keyword match: "add" → Calculator.add
3. Execute: add(5, 3) = 8
4. Keyword match: "multiply" → Calculator.multiply
5. Execute: multiply(8, 2) = 16

**LangChain Implementation (with Gemini)**:
1. Gemini reads query
2. Thought: "I need to add first"
3. Action: add, Input: "5,3"
4. Observation: 8
5. Thought: "Now multiply by 2"
6. Action: multiply, Input: "8,2"
7. Observation: 16
8. Final Answer: 16

Both get the same result, but LangChain provides reasoning transparency through the ReAct pattern.

## Rate Limits (Gemini Free Tier)

- **gemini-2.5-flash**: 5 requests per minute
- **gemini-pro**: 60 requests per minute

For production use, consider upgrading to a paid plan for higher limits.
