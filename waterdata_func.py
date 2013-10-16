# This is function is called by h2_p.py 
# This downloads data from url for desired site and date ranges.
# Includes begin date, end date, appends

import numpy as np
import urllib
from datetime import datetime, date

def waterdata_func(site_num,begin_year,begin_mon,begin_date,end_year,end_mon,end_date):
    import urllib
    
    url = []
    
    #site_num = '08078000'
    begin_date = str(datetime(begin_year,begin_mon,begin_date).date())
    end_d   = str(datetime(end_year,end_mon,end_date).date())
    
    url = 'http://waterdata.usgs.gov/nwis/dv?cb_00060=on&cb_00065=on&format=rdb&period=&begin_date='+begin_date+'&end_date='+end_d+'&site_no='+site_num    
    data = urllib.urlopen(url)
    
    discharge = []
    dates = []

    for lines in data.readlines()[30:]:
        da = lines.split()
        discharge.append(float(da[3]))
        date = da[2]
        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day = int(date.split('-')[2])
            
        dates.append(datetime(year,month,day))
    

    discharges = 0.028316*np.array(discharge) # converting to cubic meter
    data_date = np.array(dates)
        
    return discharges, data_date
        
    print discharges
    print data_date
