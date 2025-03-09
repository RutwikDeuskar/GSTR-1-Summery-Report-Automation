import pandas as pd
import numpy as np

def get_state_code(gst_number):
    try:
        return int(gst_number[0:2])
    except:
        return 0


# Extract Data
cust_master = pd.read_excel(input("Import Customer Master"))
prod_master = pd.read_excel(input("Import Product Master"))
state_code_master = pd.read_excel(input("Import state code master Master"))
main_sales_data = pd.read_excel(input("Import Sales Master"),skiprows=2)

main_template = main_sales_data
# Get Product Details
df2=main_template.merge(right=prod_master,how="left",left_on="Product Code",right_on="Product Code")
df2.drop('S.N',axis=1,inplace=True)

# Get Customer Details
df2=df2.merge(right=cust_master,how="left",left_on='GST Number',right_on='GST NUMBER OF CUSTOMER')
df2.drop(['EMAIL ID','PHONE NUMBER','GSTN STATUS'],axis=1,inplace=True)
df2.head(2)

# Find Taxable Value
df2['Basic Sale']=df2['Units Sold']*df2['PRICE']
df2['Taxable Value']=df2['Basic Sale']-df2['Discount']

# Get State Details
df2['State Code']=df2['GST Number'].apply(lambda x: get_state_code(x))
df3=df2.merge(right=state_code_master,how='left',left_on='State Code',right_on='State Code')
df3.drop('State Code', axis=1, inplace=True)

# Calculate GST
df3['IGST']=np.where(df3['Supplier State']==df3['State Name'],0,df3['Taxable Value']*df3['GST RATE'])
df3['CGST']=np.where(df3['Supplier State']!=df3['State Name'],0,df3['Taxable Value']*df3['GST RATE']/2)
df3['SGST']=np.where(df3['Supplier State']!=df3['State Name'],0,df3['Taxable Value']*df3['GST RATE']/2)
df3['Total GST']=df3['IGST']+df3['CGST']+df3['SGST']

df3 = df3.replace(np.nan, "", regex=True)

# Bifurcate b2b/b2c/cdnr
conditions=[((df3['Doc Type']=='Invoice')&(df3['GST Number']!="")),
            ((df3['Doc Type']=='Invoice')&(df3['GST Number']=="")),
            (df3['Doc Type']!='Invoice')]
results=["Table 4A - B2B","Table 5A - B2C","Table 9 - CDNR"]

df3['GSTR-1 Table']=np.select(conditions,results)

# HSN Summery
HSN_sum=df3.groupby(by='HSN Code',as_index=False)[['CGST','SGST','IGST','Total GST']].sum()

# R1 Table Summery
Table_sum=df3.pivot_table(values=['CGST','SGST','IGST','Total GST'],index=['GSTR-1 Table'],aggfunc='sum').reset_index()

# R1 Table With Rate Summery
Table_Rate_sum=df3.pivot_table(values=['CGST','SGST','IGST','Total GST'],index=['GSTR-1 Table','GST RATE'],aggfunc='sum')

# Export To Excel
writer=pd.ExcelWriter(f"{input("Store location")}\{input("File Name")}.xlsx",engine='openpyxl')
HSN_sum.to_excel(writer,sheet_name="HSN Wise",index=False)
Table_sum.to_excel(writer,sheet_name="R1 Table",index=False)
Table_Rate_sum.to_excel(writer,sheet_name="R1 Table & Rate")
df3.to_excel(writer,sheet_name="Main Data",index=False)
writer.close()
print("All Files are exported to excel")