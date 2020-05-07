# Python code to generate 
# random numbers and 
# append them to a list 
import random 
import pandas as pd
import numpy



# Function to generate 
# and append them  
# start = starting range, 
# end = ending range 
# num = number of  
# elements needs to be appended 
def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 
  
# Driver Code 
num = 1000
start = 0
end = 100
po = (Rand(start, end, num)) 
# print(po)
# Generate dataframe from list and write to xlsx.
pd.DataFrame(po).to_excel('output.xlsx', header=False, index=False)


# df = pd.read_excel(r'output.xlsx', sheet_name='Sheet1', index_col=0)
# # print(df)
# toilist = []
# toilist = df.index.tolist()
# print(toilist[0])

# print (df['Index'])
# print(toilist)