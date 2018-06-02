from craigslist import CraigslistJobs, CraigslistForSale
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

x = []
y = []
z = []
w = []

count = int(0)
category = 'cta'
site = 'austin'
min_year = 2009
max_year = 2013
min_price = 5000
max_price = 25000
make = 'bmw+328i'

for_sale = CraigslistForSale(site=site, category=category,
    filters={'max_price': max_price, 'min_price': min_price,
             'min_year': min_year, 'max_year': max_year, 'make': make})

for result in for_sale.get_results():
    count += int(1)
    x.append(count)

    price = result['price']
    price = int(price[1:])
    y.append(price)

    mean = round(np.mean(y),0)
    z.append(mean)
    
    median = round(np.median(y),0)
    w.append(median)

style.use('fivethirtyeight')
fig, ax = plt.subplots()

ax.plot(x, y, 'o', color='#f71993', label = 'Cars: {}' .format(x))
ax.plot(x, z, color='#93f719', label = 'Mean: {}' .format(z))
ax.plot(x, w, color='#09def2', label = 'Mean: {}' .format(w))

box = dict(boxstyle = 'round4', fc = '#93f719', ec = '#eeeeee', lw = 1)
ax.annotate('{}'.format(mean),
            (x[-1], z[-1]),
            xytext = (x[-1] -1, z[-1] + 200) , bbox = box)   

box2 = dict(boxstyle = 'round4', fc = '#09def2', ec = '#eeeeee', lw = 1)
ax.annotate('{}'.format(median),
            (x[-1], w[-1]),
            xytext = (x[-1] -1, w[-1] -200) , bbox = box2)   

plt.legend(('Car Prices', 'Average Car Price', 'Median Car Price'))
plt.xlabel('Number of Cars for Sale')
plt.ylabel('Price')
plt.title('{} {} {} {}' .format(site, min_year, max_year, make))
plt.show()
