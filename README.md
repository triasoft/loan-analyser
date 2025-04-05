# Loan Calculator Tools - README

## Overview

This package includes tools for loan calculations and comparisons:
1. `*.py` - A Python script for calculating amortization schedules and comparing interest rates
2. `*.html` - An interactive web tool for visualizing loan repayment scenarios

## 1. creditcalc.py - Loan Amortization Calculator

### Description
This Python script calculates detailed amortization schedules for loans using the annuity formula. It shows how each payment is split between principal and interest, and can compare different interest rate scenarios.

### Requirements
- Python 3.x
- pandas
- numpy

Install dependencies with:
```
pip install pandas numpy
```

### Usage
1. Open the script in a Python environment (Jupyter Notebook, VS Code, etc.)
2. Modify the parameters at the bottom of the script:
   - `loan_amount`: Total loan amount in euros
   - `years`: Loan term in years
   - `annual_payment_percentage`: Annual repayment percentage (e.g., 2 for 2%)
   - `interest_rates`: List of interest rates to compare (as percentages)

3. Run the script to see:
   - A detailed amortization schedule
   - Total interest paid
   - Time to repay the loan
   - A comparison table of different interest rates

### Example Output
The script will display:
- Loan parameters (amount, term, repayment percentage)
- Comparison table showing:
  - Interest rate
  - Monthly payment
  - Annual payment
  - Total interest
  - Repayment duration

## 2. HTML - Interactive Loan Comparison Tools

### Description
This HTML files provides a visual interface to compare loan scenarios from different banks with varying interest rates. It calculates repayment schedules and shows key metrics.

### Requirements
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (to load Plotly.js)

### Usage
1. Open the HTML file in any web browser
2. **Set Loan Parameters**:
   - Loan Amount (in euros)
   - Fixed Monthly Payment (in euros)

3. **Add Bank Profiles**:
   - Enter interest rate (as percentage)
   - Add bank name
   - Choose a display color
   - Click "Add Bank"

4. **View Results**:
   - Interactive charts showing annual interest and repayment amounts
   - Comparison table with key metrics for each bank
   - Key insights about total interest paid

### Features
- Add/remove multiple banks for comparison
- Visualize repayment schedules over time
- See the impact of interest rates on:
  - Total interest paid
  - Loan duration
  - Final payment amount
- Mobile-responsive design

### Example Workflow
1. Set loan amount to €250,000
2. Set monthly payment to €1,500
3. Add several banks with interest rates between 2-4%
4. Compare the results to see which option saves the most money

## Notes
- Both tools use standard annuity formulas for calculations
- The Python script provides raw data output
- The web tool offers visual comparisons
- For large loans or long terms, the web tool may take a moment to calculate

For any issues, please check your input values and ensure all required libraries are installed.
