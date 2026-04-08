
import streamlit as st
import os

st.set_page_config(page_title="Agentic AI Stock App", layout="wide")
st.title("📈 Agentic AI Stock App (Phidata vs LangChain)")

# Load API key
api_key = st.text_input("Enter OpenAI API Key", type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

agent_type = st.radio("Choose Agent", ["Phidata", "LangChain"])
query = st.text_input("Enter Query", "Get stock prices for Google, Amazon")

def run_phidata(query):
    from phi.agent import Agent
    from phi.tools.yfinance import YFinanceTools

    agent = Agent(
        tools=[YFinanceTools(stock_price=True)],
        show_tool_calls=True
    )
    return agent.run(query)

def run_langchain(query):
    import yfinance as yf
    from langchain_core.tools import Tool
    from langgraph.prebuilt import create_react_agent
    from langchain_openai import ChatOpenAI

    def get_stock_price(symbol: str):
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if data.empty:
            return f"{symbol}: Data not found"
        return f"{symbol}: ${data['Close'].iloc[-1]:.2f}"

    tool = Tool(
        name="Stock_Tool",
        func=get_stock_price,
        description="Fetch current stock prices. The input to this tool must be a single stock ticker symbol like 'GOOG', 'AMZN', 'AAPL'."
    )

    llm = ChatOpenAI(temperature=0)
    
    # Modern LangChain (>0.3.0) completely replaced AgentExecutor with langgraph
    agent_executor = create_react_agent(llm, tools=[tool])
    
    result = agent_executor.invoke({"messages": [("user", query)]})
    return result["messages"][-1].content

if st.button("Run"):
    if not os.environ.get("OPENAI_API_KEY"):
        st.error("Please enter your OpenAI API Key above!")
    else:
        with st.spinner(f"Running {agent_type} Agent... Please wait."):
            try:
                if agent_type == "Phidata":
                    # Phidata's run() returns a RunResponse object, so we extract .content
                    result = run_phidata(query)
                    st.write(result.content if hasattr(result, 'content') else result)
                else:
                    # LangChain is configured to return the final string message natively
                    result = run_langchain(query)
                    st.write(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")
