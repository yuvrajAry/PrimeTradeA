import json
import os

notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 📊 Data Science Assignment: Trader Behavior vs. Fear & Greed\n",
    "\n",
    "**Author:** Yuvraj Aryan  \n",
    "**Goal:** Analyze how trader behavior (PnL, Leverage, Volume) aligns or diverges from the Bitcoin Fear & Greed Index.\n",
    "\n",
    "### 📌 Notebook Structure\n",
    "1. **Setup**: Create folders and download data.\n",
    "2. **Data Cleaning**: Process and merge datasets.\n",
    "3. **EDA & Visualization**: Analyze patterns and save plots.\n",
    "4. **Reporting**: Generate summary files and display the final report."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. Automatic Folder Setup & Data Download"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create necessary directories\n",
    "!mkdir -p csv_files\n",
    "!mkdir -p outputs\n",
    "\n",
    "print(\"✅ Directories created: /csv_files, /outputs\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Install gdown if not already installed\n",
    "!pip install -q gdown\n",
    "\n",
    "import gdown\n",
    "\n",
    "# Dataset URLs\n",
    "trader_data_url = 'https://drive.google.com/uc?id=1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs'\n",
    "sentiment_data_url = 'https://drive.google.com/uc?id=1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf'\n",
    "\n",
    "# Download datasets\n",
    "output_trader = 'csv_files/trader_data.csv'\n",
    "output_sentiment = 'csv_files/sentiment_data.csv'\n",
    "\n",
    "gdown.download(trader_data_url, output_trader, quiet=False)\n",
    "gdown.download(sentiment_data_url, output_sentiment, quiet=False)\n",
    "\n",
    "print(\"\\n✅ Datasets downloaded successfully.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. Data Cleaning & Processing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Set plot style\n",
    "sns.set(style=\"whitegrid\")\n",
    "plt.rcParams['figure.figsize'] = (12, 6)\n",
    "\n",
    "# Load Datasets\n",
    "df_trader = pd.read_csv('csv_files/trader_data.csv')\n",
    "df_sentiment = pd.read_csv('csv_files/sentiment_data.csv')\n",
    "\n",
    "print(\"Raw Trader Data Shape:\", df_trader.shape)\n",
    "print(\"Raw Sentiment Data Shape:\", df_sentiment.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# --- Clean Trader Data ---\n",
    "# Standardize column names\n",
    "df_trader.columns = df_trader.columns.str.lower().str.strip()\n",
    "\n",
    "# Convert timestamps to datetime\n",
    "if 'timestamp' in df_trader.columns:\n",
    "    df_trader['timestamp'] = pd.to_datetime(df_trader['timestamp'])\n",
    "    df_trader['date'] = df_trader['timestamp'].dt.date\n",
    "\n",
    "# Ensure numeric columns are correct\n",
    "numeric_cols = ['realizedpnl', 'leverage', 'tradesize', 'volume']\n",
    "for col in numeric_cols:\n",
    "    if col in df_trader.columns:\n",
    "        df_trader[col] = pd.to_numeric(df_trader[col], errors='coerce')\n",
    "\n",
    "# --- Clean Sentiment Data ---\n",
    "df_sentiment.columns = df_sentiment.columns.str.lower().str.strip()\n",
    "\n",
    "# Parse dates (handling potential different formats)\n",
    "if 'date' in df_sentiment.columns:\n",
    "    df_sentiment['date'] = pd.to_datetime(df_sentiment['date']).dt.date\n",
    "\n",
    "# Unify classification column (e.g., 'value_classification' -> 'sentiment')\n",
    "if 'value_classification' in df_sentiment.columns:\n",
    "    df_sentiment.rename(columns={'value_classification': 'sentiment'}, inplace=True)\n",
    "\n",
    "# --- Merge Datasets ---\n",
    "df_merged = pd.merge(df_trader, df_sentiment, on='date', how='inner')\n",
    "\n",
    "# Save processed data\n",
    "df_merged.to_csv('csv_files/merged_processed.csv', index=False)\n",
    "\n",
    "print(\"✅ Data merged and saved. Final Shape:\", df_merged.shape)\n",
    "df_merged.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Exploratory Data Analysis (EDA)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.1 Profitability vs. Sentiment\n",
    "Does market sentiment affect how much money traders make (or lose)?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(12, 6))\n",
    "sns.boxplot(x='sentiment', y='realizedpnl', data=df_merged, palette='coolwarm', showfliers=False)\n",
    "plt.title('Profitability (Realized PnL) vs. Market Sentiment')\n",
    "plt.xlabel('Sentiment')\n",
    "plt.ylabel('Realized PnL')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "\n",
    "# Save plot\n",
    "plt.savefig('outputs/pnl_vs_sentiment.png')\n",
    "plt.show()\n",
    "\n",
    "# Calculate stats\n",
    "pnl_stats = df_merged.groupby('sentiment')['realizedpnl'].agg(['mean', 'median', 'std', 'count'])\n",
    "pnl_stats.to_csv('csv_files/pnl_by_sentiment.csv')\n",
    "print(\"Profitability Stats:\")\n",
    "display(pnl_stats)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.2 Leverage Distribution vs. Sentiment\n",
    "Do traders take higher risks (higher leverage) when they are greedy?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(12, 6))\n",
    "sns.violinplot(x='sentiment', y='leverage', data=df_merged, palette='viridis')\n",
    "plt.title('Leverage Distribution vs. Market Sentiment')\n",
    "plt.xlabel('Sentiment')\n",
    "plt.ylabel('Leverage')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "\n",
    "# Save plot\n",
    "plt.savefig('outputs/leverage_distribution.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.3 Trade Size vs. Sentiment\n",
    "Are position sizes larger during specific market conditions?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(12, 6))\n",
    "sns.boxplot(x='sentiment', y='tradesize', data=df_merged, palette='magma', showfliers=False)\n",
    "plt.title('Trade Size vs. Market Sentiment')\n",
    "plt.xlabel('Sentiment')\n",
    "plt.ylabel('Trade Size')\n",
    "plt.xticks(rotation=45)\n",
    "plt.tight_layout()\n",
    "\n",
    "# Save plot\n",
    "plt.savefig('outputs/size_vs_sentiment.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.4 Long vs. Short Distribution\n",
    "How does the ratio of Longs to Shorts change with sentiment?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check if 'side' or 'direction' column exists\n",
    "side_col = 'side' if 'side' in df_merged.columns else 'direction'\n",
    "\n",
    "if side_col in df_merged.columns:\n",
    "    ct = pd.crosstab(df_merged['sentiment'], df_merged[side_col], normalize='index')\n",
    "    \n",
    "    ct.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='RdYlGn')\n",
    "    plt.title('Long vs. Short Distribution by Sentiment')\n",
    "    plt.xlabel('Sentiment')\n",
    "    plt.ylabel('Proportion')\n",
    "    plt.xticks(rotation=45)\n",
    "    plt.legend(title='Trade Side')\n",
    "    plt.tight_layout()\n",
    "    \n",
    "    # Save plot\n",
    "    plt.savefig('outputs/long_short_distribution.png')\n",
    "    plt.show()\n",
    "    \n",
    "    # Save CSV\n",
    "    ct.to_csv('csv_files/long_short_by_sentiment.csv')\n",
    "else:\n",
    "    print(\"⚠️ 'Side' or 'Direction' column not found in dataset.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. Final Report\n",
    "The following report summarizes the findings from the analysis above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import Markdown\n",
    "\n",
    "# Read the report file and display it\n",
    "try:\n",
    "    with open('ds_report.md', 'r') as f:\n",
    "        report_content = f.read()\n",
    "    display(Markdown(report_content))\n",
    "except FileNotFoundError:\n",
    "    print(\"⚠️ Report file 'ds_report.md' not found. Please ensure it exists in the directory.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

# Write the notebook to file
output_path = 'd:/c2/primetrade/ds_yuvraj/notebook_1.ipynb'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=1)

print(f"Notebook generated at: {output_path}")
