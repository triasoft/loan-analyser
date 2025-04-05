# creditcalc.py
# -*- coding: utf-8 -*-
# This script calculates the amortization schedule for a loan and compares different interest rates.
# It uses the annuity formula to calculate the monthly payment and generates a schedule showing the breakdown of each payment into interest and principal.
# The script also calculates the total interest paid and the time to repay the loan.

# Import necessary libraries

# Install numpy if not already installed
import numpy as np
import pandas as pd

# Function to calculate the amortization schedule
def calculate_amortization(principal, annual_rate, years, annual_payment_percentage):
    # Monthly rate
    monthly_rate = annual_rate / 12
    
    # Number of payments
    num_payments = years * 12
    
    # Berechnung der monatlichen Rate nach Annuitätenformel
    # PMT = PV * (r * (1 + r)^n) / ((1 + r)^n - 1)
    # wobei: PMT = monatliche Rate
    #        PV = Kreditsumme
    #        r = monatlicher Zinssatz
    #        n = Anzahl der Zahlungen

    monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    
    # Initialize dataframe
    amortization_schedule = pd.DataFrame({
        'Month': np.arange(1, num_payments + 1),
        'Payment': np.repeat(monthly_payment, num_payments)
    })
    
    # Calculate interest, principal paid, and remaining balance
    remaining_balance = principal
    interest_paid = []
    principal_paid = []
    balances = []
    
    for i in range(num_payments):
        interest = remaining_balance * monthly_rate
        principal_pmt = amortization_schedule.at[i, 'Payment'] - interest
        remaining_balance -= principal_pmt
        
        interest_paid.append(interest)
        principal_paid.append(principal_pmt)
        balances.append(remaining_balance)
        
        if remaining_balance <= 0:
            break
    
    amortization_schedule['Interest'] = interest_paid
    amortization_schedule['Principal'] = principal_paid
    amortization_schedule['Balance'] = balances
    
    return amortization_schedule

# Calculate amortization for the original loan amount and interest rate
loan_amount = 250000
annual_interest_rate = 3.5/ 100
years = 30  # Assuming a 30-year mortgage for this example
annual_payment_percentage = 1.75 / 100 # Tiilgungssatz

amortization_schedule = calculate_amortization(loan_amount, annual_interest_rate, years, annual_payment_percentage)

# Total interest paid and time to repay the loan
total_interest_paid_full = amortization_schedule['Interest'].sum()
time_to_repay = amortization_schedule.shape[0] // 12  # Convert months to years

total_interest_paid_full, time_to_repay

# Calculate amortization for different interest rates
loan_amount = 350000
# Kaufnebenkosten ca. 25000

years = 25
annual_payment_percentage = 2 / 100
interest_rates = [2, 3, 3.5, 3.6, 3.75, 4.0, 4.5]

results = []
for rate in interest_rates:
    annual_interest_rate = rate / 100
    schedule = calculate_amortization(loan_amount, annual_interest_rate, years, annual_payment_percentage)
    total_interest = schedule['Interest'].sum()
    time_to_repay = schedule.shape[0] // 12
    
    # Monatliche Rate aus der Annuitätenberechnung
    monthly_payment = schedule['Payment'].iloc[0]
    # Jährliche Rate ist 12 mal die monatliche Rate
    annual_payment = monthly_payment * 12
    
    results.append({
        'Zinssatz': f'{rate}%',
        'Monatliche Rate': round(monthly_payment, 2),
        'Jährliche Rate': round(annual_payment, 2),
        'Gesamtzinsen': round(total_interest, 2),
        'Rückzahlungsdauer (Jahre)': time_to_repay
    })

comparison_df = pd.DataFrame(results)
comparison_df.set_index('Zinssatz', inplace=True)

# Formatiere die Zahlen für bessere Lesbarkeit
pd.options.display.float_format = '{:,.2f}'.format

# Zeige Kreditparameter und Vergleichstabelle
print(f"Kreditparameter:")
print(f"Kreditsumme: {loan_amount:,} €")
print(f"Laufzeit: {years} Jahre")
print(f"Tilgungssatz: {annual_payment_percentage*100:.2f}%")
print("\nVergleichstabelle:")
display(comparison_df)

