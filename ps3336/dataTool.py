import matplotlib.pyplot as plt
import pandas as pd
'''
Created on Nov 30, 2016

@author: peimengsui
@desc: define functions and a class for data analysis tool
'''
def visual_income_dist(year,dataset):
    '''
    this function plots distribution over countries of the income per person for a given year
    '''
    plt.hist(dataset[year].dropna().values)
    plt.title("distribution of income per person across all countries_"+str(year))
    plt.xlabel("income_per_person")
    plt.ylabel("count")
    print("close image to continue")
    plt.show()
    plt.close()
def merge_by_year(coutries,income,year):
    '''
    this function merges the countries and income data sets for any given year
    '''
    income_year = pd.DataFrame(income[year])
    merged = pd.merge(coutries,income_year,left_index=True,right_index=True)
    merged["Country"] = merged.index
    merged.rename(columns = {year:'Income'}, inplace = True)
    return merged
class dataTool:
    '''
    this class includes tools for data analysis on income country datasets
    '''
    def __init__(self, year,dataset):
        '''
        Constructor
        '''
        self.year = year
        self.dataset = dataset
    def boxplot(self):
        self.dataset.boxplot('Income', by = 'Region')
        plt.title("boxplot of income by region_"+str(self.year))
        plt.xlabel('region')
        plt.ylabel('income_per_person')
        print("close image to continue")
        plt.savefig('boxplot_'+str(self.year)+'.jpg')
        plt.show()
    def histogram(self):
        fig = plt.figure()
        plt.hist(self.dataset["Income"].dropna().values)
        plt.title("histogram of income_"+str(self.year))
        plt.xlabel("income_per_person")
        plt.ylabel("count")
        print("close image to continue")
        fig.savefig('histogram_'+str(self.year)+'.pdf')
        plt.show()
        