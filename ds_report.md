# Analysis Report: Trader Behavior & Market Sentiment

**Author:** Yuvraj Aryan  
**Date:** November 19, 2025  

---

## 1. Executive Summary
This analysis explores the correlation between market sentiment (measured by the Bitcoin Fear & Greed Index) and trader behavior. By merging trade-level data with daily sentiment scores, we investigated how emotional states—ranging from "Extreme Fear" to "Extreme Greed"—impact profitability, leverage usage, and trade direction.

**Key Findings:**
- **Profitability Divergence:** Traders tend to exhibit higher variance in PnL during "Extreme Greed," suggesting that while some capitalize on momentum, many succumb to FOMO (Fear Of Missing Out) and incur significant losses.
- **Leverage Risk:** There is a noticeable increase in leverage usage as sentiment shifts towards Greed, indicating a higher appetite for risk during bullish sentiment.
- **Contrarian Opportunities:** The Long/Short ratio often becomes skewed during extreme sentiment, potentially offering contrarian signal opportunities.

---

## 2. Methodology

### 2.1 Data Acquisition & Cleaning
We utilized two primary datasets:
1.  **Trader Data:** Contains individual trade execution details, including `realizedPnL`, `leverage`, `tradeSize`, and `timestamp`.
2.  **Fear & Greed Data:** Daily sentiment values classified into buckets (e.g., "Fear", "Greed").

**Preprocessing Steps:**
- **Normalization:** Column names were standardized (lowercased, stripped of whitespace) to ensure consistency.
- **Type Conversion:** Numeric fields (`pnl`, `leverage`, `volume`) were forced to numeric types, handling non-numeric artifacts.
- **Date Alignment:** Timestamps were converted to datetime objects. A common `date` column was extracted to merge trade data with daily sentiment values.
- **Merging:** An inner join was performed on the `date` column, ensuring every analyzed trade had a corresponding sentiment score.

---

## 3. Visual Insights & Analysis

### 3.1 Profitability vs. Sentiment
*Refer to `outputs/pnl_vs_sentiment.png`*

We analyzed the distribution of Realized PnL across different sentiment categories.
- **Observation:** The boxplot reveals that "Neutral" markets often yield the most stable PnL distributions.
- **Insight:** During "Extreme Fear," panic selling often leads to realized losses (lower median PnL). Conversely, "Extreme Greed" shows a wider interquartile range, indicating that while big wins occur, big losses are also common due to overextended positions.

### 3.2 Leverage Distribution
*Refer to `outputs/leverage_distribution.png`*

A violin plot was used to visualize the density of leverage used in each sentiment bucket.
- **Observation:** The distribution of leverage is fatter (higher density) at higher values during "Greed" and "Extreme Greed."
- **Insight:** Traders are psychologically primed to take on more risk when the market is perceived as bullish. This behavior aligns with the "House Money Effect," where traders take greater risks after perceived market gains.

### 3.3 Trade Size & Volume
*Refer to `outputs/size_vs_sentiment.png`*

We examined whether traders commit more capital during specific emotional states.
- **Observation:** Median trade sizes tend to tick upwards as sentiment improves.
- **Insight:** Confidence correlates with position size. However, this also amplifies the risk profile of the aggregate market during "Greed" phases.

### 3.4 Long vs. Short Ratio
*Refer to `outputs/long_short_distribution.png`*

A stacked bar chart displays the proportion of Long vs. Short positions per sentiment category.
- **Observation:** As expected, "Greed" correlates with a higher percentage of Long positions.
- **Insight:** The market becomes crowded on one side during extremes. A high Long/Short ratio during "Extreme Greed" is often a leading indicator of a potential correction (Long Squeeze).

---

## 4. Conclusion & Recommendations

The analysis confirms that **market sentiment significantly influences trader behavior**. Traders are not rational actors; they increase risk (leverage and size) as sentiment warms and often capitulate during fear.

**Recommendations for Traders:**
1.  **Risk Management:** Implement stricter leverage caps during "Extreme Greed" to counteract the psychological urge to over-leverage.
2.  **Contrarian Strategy:** Monitor the Long/Short skew. When the crowd is overwhelmingly Long during "Extreme Greed," consider tightening stops or taking profits.
3.  **Neutrality:** The most consistent PnL performance often occurs in "Neutral" conditions. Strive to maintain a neutral psychological state regardless of market noise.

---
*Generated as part of the DS Assignment.*
