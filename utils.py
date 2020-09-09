import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
from collections import OrderedDict
from dateutil.relativedelta import *

def TrimOutliers(dfIn, colName, floorThreshold, ceilingThreshold):
    '''
    INPUT - dfIn - pandas dataframe including outliers
            colName - column to clean up
            floorThreshold - lower bound for trimming
            ceilingThreshold - upper bound for trimming
    OUTPUT - 
            Dataframe with trimmed column
    '''
    floor = dfIn[colName].quantile(floorThreshold)
    ceiling = dfIn[colName].quantile(ceilingThreshold)

    index = dfIn[(dfIn[colName] >= ceiling)|(dfIn[colName] <= floor)].index
    dfIn.drop(index, inplace=True)
    return dfIn

def calc_ROI(principalIn, interest_rateIn, payback_yearsIn, explore_yearsIn, annual_paymentsIn, sp_returnIn, savings_rateIn, durationIn, 
             annual_incomeIn, annual_raiseIn, start_dateIn=date.today()):
    '''
    INPUT -  principalIn - Cost to attend online/bootcamp classes
             interest_rateIn - Loan interest
             payback_yearsIn - Amount of time to pay back loan
             explore_yearsIn - Time period we want to explore from start of education 
             annual_paymentsIn - Loan payments/year
             sp_returnIn  - Expected S&P return for savings going to S&P Index fund
             savings_rateIn - Amount of income saved / month
             durationIn - duration of education, in months
             annual_incomeIn - starting salary
             annual_raiseIn - Expected average annual raise
             start_dateIn - Beginning of observation period
    OUTPUT - 
            Dataframe containing the following columns
            Month - Month of observation period
            Period - Number of period (month)
            Income - Monthly income
            SP_balance - S&P balance assuming savings rate contributions and compounding
            Loan_balance - Remaining loan balance, if any
            Total - Total 'net worth'
    '''   
    # initialize the variables to keep track of the periods 
    p = 1
    i = 1
    # Set balances and income to zero
    beg_balance = 0
    end_balance = 0
    sp_balance = 0
    inc = 0
 

    while i < explore_yearsIn*12+1:
    #Calculate values for income & savings only after the individual finished schooling!
        if p <= durationIn:
            pmt = 0
            inc = 0
            sp_balance = 0
            end_balance = end_balance - principalIn / durationIn
            interest= 0
            principal_component = 0
            total = end_balance + sp_balance + inc #Should always be negative while in education 
        else:
            pmt = round(np.pmt(interest_rateIn/annual_paymentsIn, payback_yearsIn * annual_paymentsIn, principalIn), 2)
            interest = round(((interest_rateIn/annual_paymentsIn) * beg_balance), 2)
            principal_component = pmt - interest
            # Determine payment based on whether or not this period will pay off the loan
            if beg_balance < pmt: 
                end_balance = beg_balance - principal_component
            else:
                end_balance=0
            
            inc = round(annual_incomeIn / 12, 2) #Calculate monthly income
            if (p - durationIn) % 12 == 0: #Simplification: get a raise every year on your work anniversary
                annual_incomeIn = round(annual_incomeIn * (1 + annual_raiseIn), 2)
            
            sp_balance = round(((inc * savings_rateIn) + sp_balance) * (1 + sp_returnIn/12),2) #Increment S&P with savings and compound
            total = end_balance + sp_balance + inc
        
        #Yield dataframe row
        yield OrderedDict([('Month', start_dateIn),
                           ('Period', p),
                           ('Income', inc),
                           ('SP_balance', sp_balance),
                           ('Loan_Balance',end_balance),
                           ('Total', total)
                           ])
 
        p += 1
        i += 1
        start_dateIn += relativedelta(months=1)
        beg_balance = end_balance