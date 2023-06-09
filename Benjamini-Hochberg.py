import pandas as pd

def BHProcedure(df_pvals, alpha):
    df_hold = df_pvals.sort_values(by=['p'])
    pvals = df_hold['p'].tolist()
    FDRrate = [
        alpha * ((pvals.index(pvalue)+1)/len(pvals))
        for pvalue in pvals
    ]
    df_hold['FDRrate'] = FDRrate
    significant = []
    for p, FDRrate in zip(df_hold['p'].tolist(), df_hold['FDRrate'].tolist()):
        if p < FDRrate:
            significant.append(True)
        else:
            significant.append(False)
    if significant[0] == False:
        return "No significant results"
    else:
        sig = False
        counter = len(significant)
        while sig == False:
            counter = counter - 1
            sig = significant[counter]
        return significant, df_hold[:counter+1]
