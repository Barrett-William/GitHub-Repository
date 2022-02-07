def main(file):
    import csv
    import datetime as dt
    import os
    import numpy as np

    root, ext = os.path.splitext(file)
    output = root + '-new.csv'
    with open(file,'r') as csvinput,open(output, 'w') as csvoutput:

        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        rows = [next(reader)]
        for line in reader:
            line[0] = np.datetime64(dt.datetime.strptime(line[0],'%m/%d/%y').date())
            print(line[0])
            rows.append(line)

        writer.writerows(rows)

if __name__ == '__main__': main("HistoricalPricesFTSE.csv")
