import pandas as pd                                             # Import for: Data frame handling.

# Inputs:
# 1. df_pvals. Some dataframe which must contain the p-values with the column name 'p'. 
# This dataframe can have any other data in, the entire frame will be returned.
# 2. alpha. The Benjamini-Hochberg significance level. Suggestion: 0.05.

def BHProcedure(df_pvals, alpha):                               
    df_hold = df_pvals.sort_values(by=['p'])                        # df_hold: Sort the input dataframe by the p-values.
    pvals = df_hold['p'].tolist()                                   # pvals: Take the p-values from the frame and put them in a list.
    FDRrate = [                                                     # FDRrate: Create a list of the FDR rates as
        alpha * ((pvals.index(pvalue)+1)/len(pvals))                #          by Benjamini-Hochberg for each p-value.
        for pvalue in pvals
    ]
    df_hold['FDRrate'] = FDRrate                                    # df_hold: Add in the FDR rates into the hold dataframe.
    significant = []                                                # significant: Create an empty list to hold the significant boolean values.
    for p, FDRrate in zip(df_hold['p'].tolist(), df_hold['FDRrate'].tolist()):  # for loop: Pair the p-values and the FDR rates.
        if p < FDRrate:                                             # if: When p < FDRrate then add True otherwise False.
            significant.append(True)
        else:
            significant.append(False)
    sig = False                                                     # sig: Set a hold variable to False.
    counter = len(significant)                                      # counter: Set the counter to the length of the significance list.
    while sig == False:                                             # while: Keep going until sig == True.
        counter = counter - 1                                       # counter: Start at the end and keep going down to 0.
        sig = significant[counter]                                  # sig: Set sig to the element at the end, then end-1 etc.
    return significant, df_hold[:counter+1]                         # return: Significance list and the df_hold up until the last
                                                                    #         True in the list. This is the last significant element
                                                                    #         in the set as by the Benjamini-Hochberg procedure, where
                                                                    #         all results before then are counted as significant,
                                                                    #         regardless of whether the previous values were True or False.
