# 📊 Gemini Pro Financial Decoder

Transform complex financial statements into clear, actionable insights using Google Gemini AI.

## 📌 Project Overview

The **Gemini Pro Financial Decoder** is a Streamlit-based web application that enables users to upload financial statements and automatically generate structured financial analysis.

It eliminates manual financial data review and provides:

-   AI-generated financial summaries
    
-   Key financial ratios
    
-   Business health insights
    
-   Interactive visualizations
    

This project integrates:

-   **Streamlit** for UI
    
-   **Pandas** for data processing
    
-   **Google Gemini (Generative AI)** for analysis
    

## 🎯 Problem Statement

Financial data is often complex and time-consuming to interpret.

This project addresses three major scenarios:

### 1️⃣ Overwhelmed Analyst

Automates manual financial statement review.

### 2️⃣ Non-Financial Stakeholders

Converts complex data into easy-to-understand insights.

### 3️⃣ Time-Sensitive Reporting

Generates quick financial summaries for rapid decision-making.

## 🏗️ Architecture

```
User Uploads CSV/XLSX Files  
        ↓  
Streamlit Interface  
        ↓  
Pandas Data Processing  
        ↓  
Prompt Generation  
        ↓  
Google Gemini API  
        ↓  
AI Financial Summary  
        ↓  
Data Visualization  
        ↓  
User-Friendly Output

```
## 🛠️ Technologies Used

-   Python
    
-   Streamlit
    
-   Pandas
    
-   Google Generative AI (Gemini 2.5 Flash)
    
-   python-dotenv
    

## 📂 Project Structure

gemini\_financial\_decoder/  
│  
├── app.py  
├── requirements.txt  
├── .env  
└── README.md

## 🔑 API Setup

1.  Generate API Key from Google AI Studio
    
2.  Create a `.env` file
    

GOOGLE\_API\_KEY=your\_api\_key\_here

## 📦 Installation

### 1️⃣ Create Virtual Environment

python \-m venv env

### 2️⃣ Activate

- Windows:

env\\Scripts\\activate

- Mac/Linux:

source env/bin/activate

### 3️⃣ Install Dependencies

`pip install \-r requirements.txt`

## ▶️ Run the Application

`streamlit run app.py`

The application will open at:

`http://localhost:8501`

## 📤 Supported Inputs

Users can upload:

-   Balance Sheet (CSV / XLSX)
    
-   Profit & Loss Statement (CSV / XLSX)
    
-   Cash Flow Statement (CSV / XLSX)
    

## 🤖 AI Analysis Features

### Balance Sheet Analysis

-   Assets, Liabilities, Equity Summary
    
-   Financial Ratios
    
-   Liquidity Position
    
-   Risk Observations
    

### Profit & Loss Analysis

-   Revenue Trends
    
-   Expense Breakdown
    
-   Profit Margins
    
-   Growth Indicators
    
-   Business Health Summary
    

### Cash Flow Analysis

-   Operating Cash Flow Insights
    
-   Investing Activity Analysis
    
-   Financing Trends
    
-   Cash Stability Evaluation
    

## 📊 Data Visualization

The application automatically generates:

-   Line charts for numeric columns
    
-   Structured financial tables
    
-   Trend comparisons across years
    

## 🧠 How It Works

1.  Files are uploaded via Streamlit
    
2.  Pandas converts data into structured format
    
3.  Data is converted into dictionary format
    
4.  Prompt templates are generated dynamically
    
5.  Gemini 2.5 Flash analyzes the structured financial data
    
6.  AI summary is displayed alongside charts
    

## 🚀 Key Highlights

-   Fully automated financial analysis
    
-   Real-time AI insights
    
-   Clean interactive UI
    
-   Supports industry-standard file formats
    
-   Scalable and deployable
    

## 📈 Sample Output

The application generates:

-   Structured financial summaries
    
-   Key ratio analysis
    
-   Growth trend evaluation
    
-   Business health interpretation
    
-   Interactive charts
