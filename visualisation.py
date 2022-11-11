# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

#file read into pandas dataframe
data = pd.read_csv("Life Expectancy Data updated.csv")
def lineplot(y_axis, country1, country2, country3, country4):
    """
    creates a graph of Life Expectancy from 2000 to 2015 of 4
    selected countries
    """  
    plt.figure()
    plt.plot(data[y_axis], data[country1], label=country1)
    plt.plot(data[y_axis], data[country2], label=country2)
    plt.plot(data[y_axis], data[country3], label=country3)
    plt.plot(data[y_axis], data[country4], label=country4)
    plt.xlabel("Year")
    plt.xlim(2000,2015)
    plt.ylabel("Life Expectancy Rate")
    plt.legend()
    plt.savefig("lineplt.png")
    plt.show()

def hist(y_axis, country1, country2, country3, country4):
    """
    creates a histogram of life expectancy of 4 countries 
    during the time 2000 to 2015
    """    
    plt.figure()
    plt.hist(data[country1], density=True, alpha=0.7, label=country1)
    plt.hist(data[country2], density=True, alpha=0.7, label=country2)
    plt.hist(data[country3], density=True, alpha=0.7, label=country3)
    plt.hist(data[country4], density=True, alpha=0.7, label=country4)
    plt.xlabel("Life Expectancy Rate")
    plt.legend()
    plt.savefig("hist.png")
    plt.show()

def avglifeexpecancy(country):
    """
    creates a function to calculate the average life expectancy
    of each country
    """ 
    avglife=country.sum()/country.count()
    return avglife

def pie(country1, country2, country3, country4):
    """
    creates a pie chart of life expectancy of 4 countries 
    during the time 2000 to 2015
    """ 
    country1avg=avglifeexpecancy(data[country1])
    country2avg=avglifeexpecancy(data[country2])
    country3avg=avglifeexpecancy(data[country3])
    country4avg=avglifeexpecancy(data[country4])
    #list for pie chart
    avglife=[country1avg, country2avg, country3avg, country4avg]
    #list for pie chart labels
    countries = [country1, country2, country3, country4]
    plt.figure()
    plt.pie(avglife,labels=countries)
    plt.show()
    
#function calls for 3 plots
lineplot("Year", "United Kingdom", "Indonesia", "Japan", "Zimbabwe")
hist("Year", "United Kingdom", "Indonesia", "Japan", "Zimbabwe")
pie("United Kingdom", "Indonesia", "Japan", "Zimbabwe")