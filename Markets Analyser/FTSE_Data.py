import numpy as np, csv
import matplotlib.pyplot as plt
import math
import pandas

def main():

    #Get dates from csv
    with open("HistoricalPricesFTSE-new.csv") as f:
        csv_reader = csv.reader(f)
        list_from_csv = []
        for row in csv_reader:
            if len(row[0]) == 10:
                list_from_csv.append(row[0])

    #Format date for numpy
    d = np.array(list_from_csv, dtype='datetime64')

    #Write csv data to numpy array
    u = np.loadtxt(open("HistoricalPricesFTSE-new.csv","rb"), delimiter=",", usecols=[1,2,3,4],skiprows=1)

    #Add extra colmuns to array
    # i[0] = Open ; i[1] = High ; i[2] = Low ; i[3] = Close
    myVars ="""i[4] = (i[0] + i[3]) / 2 #Midpoint of open and close
i[5] = (i[1] + i[2]) / 2 #Midpoint of high and low
i[6] = i[1] - i[2] #Volatility
i[7] = i[6]/i[5] #Relative volatility (decimal)
i[8] = i[3]-i[0] #Daily change
i[9] = i[8]/i[4] #Relative daily change"""
    nlines = myVars.count('\n')+1
    listVars = np.zeros((len(u),nlines)) #for i in range(nlines)]
    x = np.concatenate((u, listVars),axis=1)
    for i in x:
        exec(myVars)
    
    #Simple Moving Average
    SMA = np.convolve(x[7], np.ones(len(u)), 'valid') / len(u)
    print(SMA)
    print(np.append(np.zeros(5655-5646),SMA))

    #Plot
    fig, axs = plt.subplots(2,2)
    fig.suptitle('FTSE 100 Market Price Analysis')

    axs[0,0].plot(d,x[:,4])
    axs[0,0].set_title('Market Price')

    axs[0,1].plot(d,x[:,7])
    axs[0,1].set_title('Daily Relative Volatility : (High-Low)/((High+Low)/2)')
    
    axs[1,0].plot(d,x[:,9])
    axs[1,0].set_title('Daily Relative Change, Open-Close : (Open-Close)/((Open+Close)/2)')
    
    #axs[1,1].plot(d,SMA)
    #axs[1,1].set_title('Simple 10-day Moving average of Daily Relative Volatility')

    plt.show()

if __name__ == '__main__': main()