import streamlit as st
from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo

# ✅ Load Open-Source LLM via Ollama
llm = Ollama(id="mistral")  # Make sure you have pulled mistral via ollama locally: `ollama run mistral`

# ✅ Web Search Tool
search_tool = DuckDuckGo()

# ✅ Stock Market News Agent
news_agent = Agent(
    name="News Agent",
    model=llm,
    tools=[search_tool],
    instructions=["Find the latest financial news about companies."],
    markdown=True
)

# ✅ Company Insights Agent
company_agent = Agent(
    name="Company Agent",
    model=llm,
    tools=[search_tool],
    instructions=["Provide key insights about companies, like CEO, industry, and revenue."],
    markdown=True
)

# ✅ Market Trend Analysis Agent
trend_agent = Agent(
    name="Trend Agent",
    model=llm,
    tools=[search_tool],
    instructions=["Summarize key stock market trends affecting major companies."],
    markdown=True
)

# ✅ Streamlit UI
st.title("📊 Multi-Agent Financial Analysis (Phidata & Ollama)")
company = st.text_input("Enter a company name (e.g., Tesla, Microsoft):")

if st.button("Get Insights"):
    if company:
        st.write("🔍 Fetching latest stock market news...")
        news_response = news_agent.run(f"Find latest financial news about {company}")
        
        st.write("🏢 Fetching company insights...")
        company_response = company_agent.run(f"Provide key insights about {company}, like CEO, industry, and revenue.")
        
        st.write("📈 Analyzing stock market trends...")
        trend_response = trend_agent.run("Summarize key stock market trends affecting major companies.")
        
        # Display results
        st.subheader("📰 Latest Stock Market News")
        st.markdown(news_response.content)

        st.subheader(f"🏢 Insights on {company}")
        st.markdown(company_response.content)

        st.subheader("📈 Market Trend Analysis")
        st.markdown(trend_response.content)
    else:
        st.warning("Please enter a company name.")

        