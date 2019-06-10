import matplotlib.pyplot as plt


Year=[2010,2011,2012,2013,2014,2015]
Rice=[10,20,30,50,40,42]


plt.xlabel("Years")
plt.ylabel("Rice Production")
plt.title("Rice Production in India")
plt.plot(Year,Rice)
plt.show()