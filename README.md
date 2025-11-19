# Data Science Assignment: Trader Behavior vs. Market Sentiment

## 📌 Project Overview
This project analyzes the relationship between **Bitcoin's Fear & Greed Index** and **trader behavior** (profitability, leverage, trade size, and long/short ratios). The goal is to identify whether market sentiment influences risk-taking and trading performance.

## 📂 Project Structure
```
ds_yuvraj/
├── notebook_1.ipynb               # Main analysis notebook (Colab-ready)
├── ds_report.md                   # Comprehensive analysis report
├── README.md                      # This setup guide
├── csv_files/                     # Directory for raw & processed datasets
└── outputs/                       # Directory for generated visualizations
```

## 🚀 How to Run on Google Colab
1. **Upload the Project**:
   - Upload the entire `ds_yuvraj` folder to your Google Drive or simply upload `notebook_1.ipynb` to [Google Colab](https://colab.research.google.com/).

2. **Run the Notebook**:
   - Open `notebook_1.ipynb`.
   - Run all cells sequentially (`Runtime` > `Run all`).
   - The notebook will automatically:
     - Create necessary folders (`csv_files`, `outputs`).
     - Download the datasets using `gdown`.
     - Clean and merge the data.
     - Perform Exploratory Data Analysis (EDA).
     - Save all visualizations to the `outputs/` folder.

3. **View the Report**:
   - The `ds_report.md` file contains the full executive summary and insights.
   - The notebook also includes a cell that renders this report for easy viewing.

## 📊 Datasets
The project uses two datasets (automatically downloaded):
- **Trader Data**: Individual trade records including PnL, leverage, and timestamp.
- **Fear & Greed Index**: Daily sentiment values (0-100) classifying market emotion.

## 📤 Exporting the Report
To convert `ds_report.md` to PDF:
1. Open the file in a Markdown editor (e.g., VS Code, Obsidian).
2. Use the "Export to PDF" feature.
3. Alternatively, print the rendered report from the Colab notebook.

## 📬 Submission
The final submission package includes:
- `notebook_1.ipynb` (Executed)
- `ds_report.md` (PDF version recommended)
- `outputs/` folder (containing PNG plots)
