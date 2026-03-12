import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAI

# ----------------------------
# Load API Key
# ----------------------------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("Google API Key not found. Please add it to your .env file.")
    st.stop()

# ----------------------------
# Initialize Gemini Model
# ----------------------------
llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

# ----------------------------
# Prompt Creator
# ----------------------------
def create_prompt(prompt_type, data_dict):

    if prompt_type == "balance_sheet":
        return f"""
You are a senior financial analyst.

Given the following Balance Sheet data:
{data_dict}

Provide:
1. Summary of assets, liabilities, equity
2. Key financial ratios
3. Liquidity position
4. Observations or risks

Keep response concise and professional.
"""

    elif prompt_type == "profit_loss":
        return f"""
You are a senior financial analyst.

Given the following Profit and Loss data:
{data_dict}

Provide:
1. Revenue trends
2. Expense breakdown
3. Profit margins
4. Growth indicators
5. Business health summary

Keep response concise.
"""

    elif prompt_type == "cash_flow":
        return f"""
You are a senior financial analyst.

Given the following Cash Flow Statement:
{data_dict}

Provide:
1. Operating cash flow insights
2. Investing activities analysis
3. Financing trends
4. Cash stability evaluation

Keep response concise.
"""

# ----------------------------
# File Upload
# ----------------------------
def upload_files():
    balance_sheet = st.file_uploader("Upload Balance Sheet", type=["csv", "xlsx"])
    profit_loss = st.file_uploader("Upload Profit & Loss Statement", type=["csv", "xlsx"])
    cash_flow = st.file_uploader("Upload Cash Flow Statement", type=["csv", "xlsx"])
    return balance_sheet, profit_loss, cash_flow

# ----------------------------
# Load File Content
# ----------------------------
def load_file(file):
    if file is not None:
        try:
            if file.name.endswith(".csv"):
                return pd.read_csv(file)
            elif file.name.endswith(".xlsx"):
                return pd.read_excel(file)
        except Exception as e:
            st.error(f"Error loading file: {e}")
    return None

# ----------------------------
# Generate Summary
# ----------------------------
def generate_summary(prompt_type, data):
    if data is not None:
        data_dict = data.to_dict()
        prompt = create_prompt(prompt_type, data_dict)
        try:
            response = llm.invoke(prompt)
            return response
        except Exception as e:
            return f"Error generating summary: {e}"
    return "No data provided."

# ----------------------------
# Visualizations
# ----------------------------
def create_visuals(data, title):
    if data is not None:
        st.subheader(title)
        st.write(data)

        numeric_data = data.select_dtypes(include=["number"])

        if not numeric_data.empty:
            st.line_chart(numeric_data)
        else:
            st.warning("No numeric columns found for visualization.")

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Gemini Pro Financial Decoder", layout="wide")

st.title("📊 Gemini Pro Financial Decoder")
st.markdown("Transform complex financial data into clear actionable insights.")

balance_sheet_file, profit_loss_file, cash_flow_file = upload_files()

if st.button("Generate Reports"):

    with st.spinner("Analyzing financial data..."):

        balance_sheet_data = load_file(balance_sheet_file)
        profit_loss_data = load_file(profit_loss_file)
        cash_flow_data = load_file(cash_flow_file)

        # Generate AI Summaries
        balance_summary = generate_summary("balance_sheet", balance_sheet_data)
        profit_summary = generate_summary("profit_loss", profit_loss_data)
        cash_summary = generate_summary("cash_flow", cash_flow_data)

        # Display Results
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Balance Sheet Summary")
            st.write(balance_summary)
            create_visuals(balance_sheet_data, "Balance Sheet Data")

        with col2:
            st.subheader("Profit & Loss Summary")
            st.write(profit_summary)
            create_visuals(profit_loss_data, "Profit & Loss Data")

        st.subheader("Cash Flow Summary")
        st.write(cash_summary)
        create_visuals(cash_flow_data, "Cash Flow Data")