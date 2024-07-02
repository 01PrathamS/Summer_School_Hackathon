## I'm using Tebula libray to extract features from the pdf 

import tabula 
import pandas as pd 

## extracting the data from all the pdf files 

pdf_file_path = "\data\Ele_Bond_Pur_by_politicalparty.pdf"

def extract_pdf_data(pdf_file_path):

    tabula.convert_into(pdf_file_path, "output1.csv", output_format="csv", pages='all') 

    ## reading the saved csv file 

    df = pd.read_csv("output1.csv")

    ## while extracting the pdf it also contains the column headers in each page
    ## remove all the rows with column headers
    df = df[df['Sr No.'] != 'Sr No.'] 

    ## separate the date into day, month and year to write better queries
    df['Date'] = df['Date of\rEncashment'].str.split('/').str[0].astype(int)
    df['Month'] = df['Date of\rEncashment'].str.split('/').str[1]
    df['Year'] = df['Date of\rEncashment'].str.split('/').str[2].astype(int)
    df['Denominations'] = df['Denominations'].str.replace(',', '').astype(float)

    ## drop the columns which are not required

    df = df.drop(['Sr No.','Date of\rEncashment','Account no. of\rPolitical Party','Pay Branch\rCode', 'Pay Teller'], axis=1)

    ## sql doesn't support column names with spaces so replace the spaces with underscore

    df.rename(columns={'Name of the Political Party': 'Name_of_the_Political_Party','Bond\rNumber': 'Bond_Number'}, inplace=True)

    ## replace the month names with full month names

    month_dict = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April',
                'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August',
                'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'}

    df['Month'] = df['Month'].replace(month_dict)

    ## save the cleaned data to a csv file

    df.to_csv("purchase_bond.csv", index=False)

    return 