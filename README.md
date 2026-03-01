# Analysing Pharmaceutical Sales Data

## Project Description
This project analyzes pharmaceutical sales data to uncover insights about drug sales patterns, categories, and trends. This is a comprehensive data science project using Python, Pandas, and Matplotlib.

## Project Structure
```
Pharmaceutical Sales/
│
├── data/
│   └── salesdaily.csv                      # Sales data from 2014-2019
│
├── pharmaceutical_sales_analysis.ipynb     # Interactive Jupyter notebook
├── pharmaceutical_analysis.py              # Standalone Python script
├── requirements.txt                        # Python dependencies
├── .gitignore                              # Git ignore rules
└── README.md                               # Project documentation
```

## Questions Answered

1. ✅ What are the total sales quantities for each drug category (ATC code)?
2. ✅ Which individual drug brands have the highest total sales?
3. ✅ Which three drugs have the highest sales in January 2015, July 2016, September 2017?
4. ✅ Which drug has sold the most often in 2017?
5. ✅ Which drug category has the highest average daily sales?
6. ✅ Are respiratory drugs (R03) sold more during specific months?

## Technologies Used

- **Python 3** - Programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Jupyter Notebook** - Interactive development environment

## Dataset Information

**File**: `salesdaily.csv`  
**Source**: Pharmaceutical sales data  
**Period**: 2014 - 2019  
**Drug Categories (ATC Codes)**:
- M01AB - Anti-inflammatory drugs
- M01AE - Anti-inflammatory drugs
- N02BA - Analgesics
- N02BE - Analgesics
- N05B - Anxiolytics
- N05C - Hypnotics and sedatives
- R03 - Respiratory drugs
- R06 - Antihistamines

## How to Run

### Option 1: Using Jupyter Notebook (Interactive)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Launch Jupyter:
   ```bash
   jupyter notebook pharmaceutical_sales_analysis.ipynb
   ```

3. Run all cells to see interactive analysis

### Option 2: Using Python Script (Command Line)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the analysis script:
   ```bash
   python pharmaceutical_analysis.py
   ```

3. Check the current directory for output charts (output_q*.png)

## Key Insights

- N02BE category consistently shows the highest sales
- Respiratory drugs (R03) exhibit seasonal sales patterns
- Sales trends vary significantly across different months and years
- Different drug categories show distinct performance patterns

## How to Push to GitHub

1. Initialize Git repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Pharmaceutical sales analysis project"
   ```

2. Create a new repository on GitHub (github.com)

3. Link and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/pharmaceutical-sales-analysis.git
   git branch -M main
   git push -u origin main
   ```

**Note**: GitHub renders Jupyter notebooks beautifully! Your `.ipynb` file will display with all outputs and charts.

## Author
Data Analysis Project  
Created: March 2, 2026

---

*This project demonstrates practical data analysis skills including data cleaning, exploratory analysis, aggregation, and visualization.*
