import pandas as pd 
import os 
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("data/carinfo.csv"):
    c_info = pd.DataFrame(columns = ["Name","Model","Year"])
    c_info.to_csv("data/carinfo.csv",index = False)