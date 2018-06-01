from craigslist import CraigslistForSale
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

x = []
y = []
z = []
count = 0

car_data = CraigslistForSale(site='dallas', category='cta',
    filters={'max_price': 45000, 'min_price': 500, 'min_year': 2010, 'max_year': 2012, 'make': 'bmw+328i'})

for result in car_data.get_results():
    count += 1
    x.append(count)

    price = result['price']
    price = int(price[1:])
    y.append(price)

    mean = round(np.mean(y),0)
    z.append(mean)

style.use('fivethirtyeight')
plt.plot(x,z)
plt.scatter(x,y, color='#f71993')
plt.legend(('Average Car Prices', 'Car Prices'))
plt.xlabel('Number of Cars for Sale')
plt.ylabel('Price')
plt.title('2010-2012 | BMW 3281')
plt.show()
