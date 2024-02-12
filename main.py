        
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

import math

from prettytable import PrettyTable


from datetime import date


from typing import Optional, List


from database import CostHandling

def duraville_project():
    
    """This function is for selection of transactions"""
    # print('1001-Search Tons Transaction per Trip Ticket')
    # print('1002-Delete Tonnage Transaction')
   
    # print('x-Exit')

    TransactionList = [
        
            
               {"Code": '2001',"Transaction":'Data Analysis'},
               {"Code": '2002',"Transaction":'Analysis Per Book'},
               {"Code": '2003',"Transaction":'Purchase Monitoring'},
               {"Code": '2004',"Transaction":'Data Exporting of Purchase Monitoring'},
               {"Code": 'x',"Transaction":'Exit'},
               
            
           
           
        ]
    

    menu = PrettyTable()
    menu.field_names=['Code','Transactions']
        
    
    for x in TransactionList:      
        menu.add_row([
            x['Code'],
            x['Transaction'],
          
        ])
    print(menu)

    ans = input('Please enter code for your Desire transaction: ')

    if ans == '2001':
        return Drdc_analyis_reporting.cost_reporting()

    elif ans == '2002':
        return Drdc_analyis_reporting.cost_reporting_total_per_project()
    elif ans == '2003':
        return Drdc_analyis_reporting.get_purchase_monitoring()

    elif ans == '2004':
        
        return Drdc_analyis_reporting.load_data_to_drdc_mysql()         

    elif ans == 'x' or ans =='X':
        exit()

class Drdc_analyis_reporting(): # this class is for DRDC analysis Reporting

    @staticmethod
    def cost_reporting():

        data_df = pd.read_excel(r'/home/joeysabusido/project/testing/excel_file/purchase_monitoring_0124.xlsx')
        
        #Get user input for date range and expense account
        date_from = input('Enter Date From (MM/DD/YYYY): ')
        date_to = input('Enter Date To (MM/DD/YYYY): ')
        expense_account = input('Enter Expense Account: ')
        project_name = input('Enter Project Name: ')

        # Convert date strings to datetime objects for comparison
        data_df['VOUCHERDATE'] = pd.to_datetime(data_df['VOUCHERDATE'])
        
        # Boolean indexing to filter the DataFrame

        # filtered_df = data_df['ACCOUNTS']
        
        filtered_df = data_df[

            (data_df['VOUCHERDATE'] >= date_from) & (data_df['VOUCHERDATE'] <= date_to) &
            (data_df['ACCOUNTS'] == expense_account)
           
           
        ]

        #Display the filtered DataFrame
        #print(filtered_df['TOTAL_AMOUNT_DUE'])

        #total_sum = filtered_df['TOTAL_AMOUNT_DUE'].sum()

        #Display the filtered DataFrame
        #print(f'Total Sum of TOTAL_AMOUNT_DUE: {total_sum}')

        print(filtered_df)
        

        

        duraville_project()



    @staticmethod
    def cost_reporting_total_per_project():

        data_df = pd.read_excel(r'/home/joeysabusido/project/testing/excel_file/purchase_monitoring_0124.xlsx')
        
        #Get user input for date range and expense account
        date_from = input('Enter Date From (MM/DD/YYYY): ')
        date_to = input('Enter Date To (MM/DD/YYYY): ')
        project_name = input('Enter Project Name: ')

        # Convert date strings to datetime objects for comparison
        data_df['VOUCHERDATE'] = pd.to_datetime(data_df['VOUCHERDATE'])
        
        # Boolean indexing to filter the DataFrame

        # filtered_df = data_df['ACCOUNTS']
        
        filtered_df = data_df[

            (data_df['VOUCHERDATE'] >= date_from) & (data_df['VOUCHERDATE'] <= date_to) &
            (data_df['Book'] == project_name)
           
           
        ]

        #print(filtered_df)
        
        total_expenses = filtered_df.groupby('Book')['netofvat'].sum().reset_index()
        formatted_amounts = total_expenses['netofvat'].apply('{:,.2f}'.format)

        print(f'Total Expense : {formatted_amounts}')

    @staticmethod
    def get_purchase_monitoring():
        """This function is for getting all the purchase monitoring report"""
        data_df = pd.read_excel(r'/home/joeysabusido/drdc_transfer/drdc_uploading_excel/excel_file/purchase_monitoring_0124.xlsx')
        pd.set_option('display.max_rows', None)

        # for index, row in data_df.iterrows():



            # print(row['EXPENSE_ACCOUNT'])

        print(data_df)
        duraville_project()

    @staticmethod
    def load_data_to_drdc_mysql():
        """This function is for exporting the data"""
        data_df = pd.read_excel(r'/home/joeysabusido/drdc_transfer/drdc_uploading_excel/excel_file/purchase_monitoring_0124.xlsx')
        pd.set_option('display.max_rows', None)


        
        data = []

        for index, row in data_df.iterrows():
            entry = {
                "voucher_date": row['VOUCHER_DATE'],
                "voucher_no": row['VOUCHER_NO'],
                "company": row['COMPANY'],
                "book": row['BOOK'],
                "supplier": row['SUPPLIER_PAYEE'],
                "vat_reg": row['VAT_REG/NON_VAT_REG'],
                "tin_no": row['TIN_NO'],
                "net_of_vat": 0.0 if math.isnan(row['NET_OF_VAT']) else row['NET_OF_VAT'],
                "amount_due":  0.0 if math.isnan(row['AMOUNT_DUE']) else row['AMOUNT_DUE'],
                "expense_account": row['EXPENSE_ACCOUNT'],
                "description": row['DESCRIPTION'],
                "inclusive_date": 0 if pd.isna(row['INCLUSIVE_DATE']) else row['INCLUSIVE_DATE'],
                "sin": 0 if pd.isna(row['SIN']) else row['SIN'],
                "can": 0 if pd.isna(row['CAN']) else row['CAN'],
                "khw_no": 0.0 if math.isnan(row['KWH_NO']) else row['KWH_NO'],
                "price": 0.0 if math.isnan(row['PRICE_KWH']) else row['PRICE_KWH'],
                "cubic_meter": 0.0 if math.isnan(row['CM3']) else row['CM3'],
                "pic": 0 if pd.isna(row['PIC']) else row['PIC'],
                "person_incharge_end_user": 0 if pd.isna(row['PERSON_ENDCHARGE']) else row['PERSON_ENDCHARGE'],
                "no_of_person": 0 if pd.isna(row['NO_OF_PERSON']) else row['NO_OF_PERSON'],
                "activity_made": 0 if pd.isna(row['ACTIVITY_MADE_TRANSPO']) else row['ACTIVITY_MADE_TRANSPO'],
                "plate_no": 0 if pd.isna(row['PLATE_NO']) else row['PLATE_NO'],
                "user": 'Jerome'

                # Add more key-value pairs as needed
            }

            data.append(entry)

            # Check the length of 'description' data before insertion
            # print(len(entry['description']))

        # print(data['voucher_date'])
            # Call the insert function for each row of data
            CostHandling.insert_cost_from_purchase_monitoring(**entry)
   


duraville_project()

        

