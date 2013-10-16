import waterdata_func as function
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, date

foo = function.waterdata_func('08078000',1959,10,1,2013,1,1)

dates = foo[1]
discharge = foo[0]

mont = np.array([dates[d].month for d in range(dates.size)])
da   = np.array([dates[d].day for d in range(dates.size)])
yea  = np.array([dates[d].year for d in range(dates.size)])

mean   = []
std    = []
           
for i in range(1,13):     
    idx = np.where(mont == i)
    dis = discharge[idx]
    
    for j in range (1,32):
        iidx = np.where(da[idx]==j)
        discharge_ave = dis[iidx]
        
        mean.append(discharge_ave.mean())
        std.append(discharge_ave.std())        

mean = np.array(mean)
std = np.array(std)

mean_dis = mean[(~np.isnan(mean))]
stdev_dis = std[(~np.isnan(std))]

upper_limit   = mean_dis+stdev_dis
lower_limit = mean_dis-stdev_dis

begin_time = datetime(2010,1,01)
end_time   = datetime(2013,1,1)
idx_start  = np.where(dates==begin_time)
idx_end    = np.where(dates==end_time)
time_date  = dates[np.where(yea==2012)]

tot_discharge = np.array([discharge[disc] for disc in range(idx_start[0],idx_end[0])])
 
mean_f =[]
upper_limit_f =[]
lower_limit_f =[]

for d in dates[idx_start[0]:idx_end[0]]:
    mean_f.append(mean[time_date==datetime(2012,d.month,d.day)])
    upper_limit_f.append(upper_limit[time_date == datetime(2012,d.month,d.day)])
    lower_limit_f.append(lower_limit[time_date==datetime(2012,d.month,d.day)])  
    
          
fig = plt.figure()
plt.plot(dates[idx_start[0]:idx_end[0]],tot_discharge,"k",linewidth=0.2,label = 'Daily')
plt.plot(dates[idx_start[0]:idx_end[0]],mean_f,label='Average')
plt.plot(dates[idx_start[0]:idx_end[0]],upper_limit_f,"-.r",label = 'Standard Deviation')
plt.plot(dates[idx_start[0]:idx_end[0]],lower_limit_f,"-.r")
plt.title('Annual Mean and Standard Deviation for Discharge', fontsize =14)
plt.xlabel('Time',fontsize = 12) 
plt.ylabel('Discharge ($m^3/s$)',fontsize = 12)
plt.xticks(rotation=90)
plt.legend(loc = 'upper right')
plt.show()
plt.savefig('USGS_waterdata_homework_2_Year2010_To_Year2012.png')

# for plotting smaller dataset change begin_time

