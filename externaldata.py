import matplotlib.cbook as cbook
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mpdates
#data = cbook.get_sample_data('goog.npz', np_load=True)['price_data']
data = [('2004-08-19', 100.  , 104.06,  95.96, 100.34, 22351900, 100.34),
 ('2004-08-20', 101.01, 109.08, 100.5 , 108.31, 11428600, 108.31),
 ('2004-08-23', 110.75, 113.48, 109.05, 109.4 ,  9137200, 109.4 ),
 ('2008-10-10', 313.16, 341.89, 310.3 , 332.  , 10597800, 332.  ),
 ('2008-10-13', 355.79, 381.95, 345.75, 381.02,  8905500, 381.02),
 ('2008-10-14', 393.53, 394.5 , 357.  , 362.71,  7784800, 362.71)]
#headers = ['date', 'bar', 'baz', 'other']
#headers = ['Date', 'Open', 'High', 'Low', 'Close']
Frame=pd.DataFrame(data, index=None, columns = ['Date', 'Open', 'High','Low','Close', 'Volume', 'Divident'])
print(Frame)
fig, ax = plt.subplots()
#print(type(data[0][0]))
print(type(data[0]))
ax.plot('Date', 'Close', data=Frame)
plt.show()