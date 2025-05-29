# nova-sp-sentiment-analysis

This project aims to enhance stock market forecasting using a combination of financial news sentiment analysis and technical stock indicators. By integrating qualitative (news sentiment) and quantitative (price data) factors, we analyze the relationship between investor sentiment and stock performance to develop actionable investment insights.

---

## 📁 Project Structure

``` bash

nova-sp-sentiment-analysis
├── datasets
├── images
├── notebooks
├── README.md
├── requirements.txt
├── scripts
├── src
└── test

```

---

## 🚀 Project Objectives

1. **Sentiment Analysis**  
   - Use NLP to extract sentiment from financial news headlines.
   - Quantify emotional tone (positive/negative/neutral) by stock ticker and date.

2. **Technical Analysis**  
   - Analyze stock price movements using TA-Lib indicators like RSI, MACD, and Moving Averages.
   - Explore historical data trends using PyNance and visualize with `matplotlib` / `plotly`.

3. **Correlation Analysis**  
   - Compute daily returns and correlate with news sentiment.
   - Identify leading/lagging relationships between sentiment and price changes.

4. **Investment Strategy Design**  
   - Translate analysis into practical strategies using sentiment signals for buy/sell decisions.

---

## 📊 Tools & Libraries

- **Python 3.10+**
- **pandas, numpy, matplotlib, seaborn**
- **TA-Lib, PyNance**
- **NLTK, TextBlob, VADER**
- **scikit-learn, gensim** (for NLP and topic modeling)
- **plotly, seaborn** (for visualizations)

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abrehamashebir/nova-sp-sentiment-analysis.git
   cd nova-sp-sentiment-analysis
   ```
