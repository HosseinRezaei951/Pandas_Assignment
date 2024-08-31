import numpy as np  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn 
import os
pd.options.mode.chained_assignment = None


Google_PlayStore_csvPath = 'Google-Playstore.csv'
sectionDivider =            "#"*100
subDivider =                "-"*50

def clear_screen():
    '''
    Code to clear running screen
    '''    
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

def clear_lastLine(length):
    print(" "*(length*2), end='\r', flush=True)

def _wait(waitingText):
    printString = " Please wait for " + waitingText + " ... "
    print(printString, end='\r', flush=True)
    return len(printString)
    
def _continue():
    printString = " Press enter to continue ... \n"
    input(printString)
   
def _invalid():
    printString = " Invalid input! Press enter to try again ... \n"
    input(printString)  

def difference_two_list(list_one, list_two):
    result = [i for i in list_one if i not in list_two]
    return result


if __name__ == "__main__":
    clear_screen()
    ############################################################
    ### Loading
    ############################################################ 
    print("\n\n 1. Loading data \n")

    strlength = _wait("loading")
    df = pd.read_csv(Google_PlayStore_csvPath)
    clear_lastLine(strlength)
    nrows, ncols = df.shape
    print(" ==> Google-Playstore.csv was loaded successfully.")
    print(" ==> Number of Rows: %s " %(nrows))
    print(" ==> Number of Columns: %s " %(ncols))
    print(sectionDivider)
    _continue()


    ############################################################
    ### Cleaning
    ############################################################ 
    print("\n\n 2.Cleaning data \n")

    print(" 2-1. Checking full duplicate rows: ")
    strlength = _wait("checking")
    fullDuplicate_in_df = df.duplicated()
    clear_lastLine(strlength)
    if fullDuplicate_in_df.any():
        print(" ==> Full duplicate rows: ") 
        print(df.loc[fullDuplicate_in_df], end='\n')
        
        df = df.drop_duplicates()
        print(" ==> After dropping full duplicate rows:")
        print(df)
    else:
        print(" ==> No any full duplicate rows.")
    print(subDivider)
    _continue()

    ##############################################
    columnNames = ['App Id']
    print(" 2-2. Checking duplicate by " + str(columnNames) + " column value: ")
    strlength = _wait("checking")
    duplicate_in_df = df.duplicated(columnNames)
    clear_lastLine(strlength)
    if duplicate_in_df.any():
        print(" ==> duplicate rows by " + str(columnNames) + " values: ") 
        print(df.loc[duplicate_in_df], end='\n')

        df = df.drop_duplicates(columnNames)
        print(" ==> After dropping duplicate rows by " + str(columnNames) + " values:")
        print(df)
    else:
        print(" ==> No any duplicate rows by " + str(columnNames) + " values")
    print(subDivider)
    _continue()

    ##############################################
    print(" 2-3. Checking missing values: ")
    strlength = _wait("checking")
    missingValues_in_df = df.isnull()
    clear_lastLine(strlength)
    missingValues_columnNames = [column for column, value in df.isnull().any().to_dict().items() if value == True]
    print(" ==> Columns with missing value: \n", missingValues_columnNames)

    important_missingValues_columnNames = ['Rating', 'Rating Count', 'Installs','Minimum Installs']
    unimportant_missingValues_columnNames = difference_two_list(missingValues_columnNames, important_missingValues_columnNames)
    print("\n 2-3-1 First we have to drop rows with missing value in unimportant columns.")
    print(" ==> Unimportant columns with missing value: \n", unimportant_missingValues_columnNames)
    df = df.dropna(subset=unimportant_missingValues_columnNames)

    print("\n 2-3-2 Again checking missing values: ")
    strlength = _wait("checking")
    missingValues_in_df = df.isnull()
    clear_lastLine(strlength)
    missingValues_columnNames = [column for column, value in df.isnull().any().to_dict().items() if value == True]
    print(" ==> Remaining columns with missing value: \n", missingValues_columnNames)

    print("\n 2-3-3 Now replacing NaN value of " + str(missingValues_columnNames) + " columns with mean value of each one: ")
    for column in missingValues_columnNames:
        meanValue = round(df[column].mean(skipna = True))
        df[column] = df[column].fillna(meanValue)
        print(" ==> Replacing '" + str(column) + "' column NaN values with " + str(meanValue) + " as mean value." )

    print("\n 2-3-4 Finaly checking missing values Again: ")
    strlength = _wait("checking")
    missingValues_in_df = df.isnull()
    clear_lastLine(strlength)
    missingValues_columnNames = [column for column, value in df.isnull().any().to_dict().items() if value == True]
    print(" ==> Remaining columns with missing value: \n", missingValues_columnNames)
    print(sectionDivider)    
    _continue()


    ############################################################
    ### Analysing
    ############################################################ 
    print("\n\n 3.Analysing data \n")

    print(" 3-1. Which category of Ad-Supported apps is the most popular among users? ")
    print("\n 3-1-1 First we have to extract rows with True value for 'Ad Supported' column.")
    strlength = _wait("extracting")
    AdSupported_df = df.loc[df['Ad Supported'] == True]
    clear_lastLine(strlength)
    nrows, ncols = AdSupported_df.shape
    print(" ==> 'Ad Supported' rows was extracted successfully.")
    print(" ==> Number of Rows: %s " %(nrows))
    print(" ==> Number of Columns: %s " %(ncols))

    print("\n 3-1-2 Solution: ")
    columnNames = ['WRI']
    print(" ==> First we have to adding new column as 'WRI' with multiplication the 'Rating' and \n"+\
          "     'Rating Count' and 'Maximum Installs' columns values. \n"+\
          "     Then groping 'Ad Supported' rows with same 'Category' column value with mean value of \n"+\
          "     " + str(columnNames) + " columns for each category. \n"+\
          "     At the end we can sort result by " + str(columnNames) + " column value and draw plot \n"+\
          "     for results to compare categories each other. \n")

    AdSupported_df['WRI'] = (AdSupported_df['Rating'] * AdSupported_df['Rating Count'] * AdSupported_df['Maximum Installs'])
    gropedBy_Category_df = AdSupported_df.groupby('Category')[columnNames].mean().sort_values(by=columnNames, ascending=False)
    nrows, ncols = gropedBy_Category_df.shape
    print(" ==> Number of Rows: %s " %(nrows))
    print(" ==> Number of Columns: %s " %(ncols))
    print(gropedBy_Category_df)
    gropedBy_Category_df.plot(kind='barh')
    plt.show()
    print(subDivider)
    _continue()

    ##############################################
    print(" 3-2. Which attributes affect the 'Rating' and 'Installs' attribute for Ad-Supported apps? ")
    print("\n 3-2-1 We have extracted rows with True value for 'Ad Supported' column.")

    
    print("\n 3-2-1 Solution: ")
    print(" ==> First We have to convert 'Installs' column value to numeric values. \n"+\
          "     Then we can calculate pearson correlation on dataFrame. And draw heatmap \n"+\
          "     for results to compare affect of each attributes")

    AdSupported_df["Installs"] = AdSupported_df["Installs"].str.replace(",","")
    AdSupported_df["Installs"] = AdSupported_df["Installs"].str.replace("+","")
    AdSupported_df["Installs"] = pd.to_numeric(AdSupported_df["Installs"])
    
    correlation = AdSupported_df.corr(method ='pearson')
    correlation_df = pd.DataFrame(correlation)
    sn.heatmap(correlation_df, annot = True) 
    plt.show()
    _continue()


    ##############################################
    print(" 3-3. What age-group would you target? ")
    print("\n 3-3-1 We have extracted rows with True value for 'Ad Supported' column.")

    columnNames = ['WRI']
    print("\n 3-3-2 Solution: ")
    print(" ==> Just we have to groping 'Ad Supported' rows with same 'Content Rating' column value with \n"+\
          "     mean value of " + str(columnNames) + " columns for each category. \n"+\
          "     At the end we can sort result by " + str(columnNames) + " column value and draw plot \n"+\
          "     for results to compare categories each other. \n")

    gropedBy_ContentRating_df = AdSupported_df.groupby('Content Rating')[columnNames].mean().sort_values(by=columnNames, ascending=False)
    nrows, ncols = gropedBy_ContentRating_df.shape
    print(" ==> Number of Rows: %s " %(nrows))
    print(" ==> Number of Columns: %s " %(ncols))
    print(gropedBy_ContentRating_df)
    gropedBy_ContentRating_df.plot(kind='barh')
    plt.show()
    print(subDivider)
    _continue()


    print(sectionDivider) 
    print("\n Finished ... ")   
   