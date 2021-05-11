# ==============================================================
# AUTHOR: Christian Moreano
# CREATE DATE: 5/6/21
# PURPOSE: Extract data from existing CVS files and plot a graph
# ==============================================================
# Change History:
#
#===============================================================


import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.dates as mdates

# use glob to get all the csv files 
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))

# Instantiation of empty list for file names  
file_name = []

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
custom_date_parser = lambda x: datetime.strptime(x, "%H:%M:%S.%f %Y-%m-%d")

# loop over the list of csv files
for f in csv_files:

    # read the csv file
    df = pd.read_csv(f)
    file_name.append(f.split("\\")[-1]) # Append all csv files in the current directory into list

# Interate through csv files and write graph  data to pdf file 
for x in range(len(file_name)): # BEGIN FORLOOP
    filename = file_name[x]
    file_data = pd.read_csv(filename,parse_dates=['DateTime'], date_parser=custom_date_parser)
    file_data['DateTime'] = file_data["DateTime"].dt.strftime("%H:%M")
    plt.figure(figsize=(20,10))
    data_separator = 200
    plt.plot(file_data.DateTime,file_data["Process Value"],label = 'Process Value')
    plt.title(filename, fontdict = font1)
    plt.xlabel("Time(H:M)",fontdict = font2)
    plt.ylabel("Temperature(°F)", fontdict = font2)

    plt.yticks(np.arange(60,200,10)) # Assuming temperature ranges from 60-200
    plt.xticks(file_data.DateTime[::data_separator], rotation= 90)

    
    plt.grid() # Display Grid based on X Axis data
    plt.legend() # Display Graph Legend
    plt.savefig(filename+".pdf") 
    plt.close() # Close file
# END OF FORLOOP