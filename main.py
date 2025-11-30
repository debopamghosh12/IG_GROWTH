import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from agent_prompt import ig_prompt
import os
from dotenv import load_dotenv
from datetime import datetime
# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE")

# Configure the ChatOpenAI model with OpenRouter settings
llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base=api_base,
    model="gpt-3.5-turbo",  # Example OpenRouter model
    temperature=0.7
)

# Connect the prompt to the chain
chain = LLMChain(llm=llm, prompt=ig_prompt)
st.title("Investment Strategy Agent:")

# Input data for your agent
niche = st.text_input("Enter your niche:")
goal = st.text_input("Enter your goal:")

# Run the agent and print the output
# print("\n Agent's Response:\n")
# print(response['text'].strip())

# print("=" * 50)
# print("Instagram Growth Agent's Strategy".center(50))
# print("=" * 50)
# print(response['text'].strip())
# print("=" * 50)

if(st.button("Generate")):
    with st.spinner("Generating..."):
        response = chain.invoke({'goal':goal,'niche':niche})
        st.markdown("## Investment Strategy Agent's Response:")
        st.write(response['text'].strip())
# timestamp=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
# with open("agent_outputs.txt", "a", encoding="utf-8") as f:
#     f.write(f"\n\n--- New Response ({timestamp}) ---\n")
#     f.write(response['text'].strip())
#     f.write("\n" + "-"*50)
