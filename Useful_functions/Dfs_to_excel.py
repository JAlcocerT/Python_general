from pandas import ExcelWriter
# from pandas.io.parsers import ExcelWriter

def save_xls(list_dfs, xls_path):
    with ExcelWriter(xls_path) as writer:
        for n, df in enumerate(list_dfs):
            #df.to_excel(writer,'sheet%s' % n)
            df.to_excel(writer, sheet_name = df.name)
        writer.save()
            

#The dataframes should have been named before with:
#df1.name = 'your_name_for_this_df'
#then every excel sheet will have the specified df name

save_xls([df1,df2,df3,df4,df5], "C:/Users/your/path/output_name.xlsx")
