# -*- coding: utf-8 -*-
"""seaborn

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YAh_aPV9pB5u-QldKpOzD9g2B5mWQUP6
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

"""# **relational plots**"""

cal=sns.load_dataset('tips')
#axes level
print(cal)
#sns.scatterplot(data=cal,x='total_bill',y='tip',marker='d',size=0.5, color='red')
#figure level
sns.relplot(data=cal,x='total_bill',y='tip',hue='sex',style='day',size='size',kind='scatter',height=10, aspect=2)

sns.relplot(data=cal,x='total_bill',y='tip',hue='sex',style='day',size='size',kind='line')




a=[1,2,3,4]
b=[1,2,3,4]
sns.relplot(x=a,y=b,kind='line',marker='d',color='red',markerfacecolor='black') # hue size and style can also be used

"""# Importing Dependencies

# **facet plot**
"""

cal=sns.load_dataset('tips')
short=cal.head(5)
print(short)
# facet griding   facet griding works only on figure lvl plot it does'nt  work on axes lvl plot
sns.relplot(data=short,x='total_bill',y='tip',col='size',row='sex',kind='scatter')# col_wrap=2 number of plots in a  single row
# facet griding can also be applied on line plot

"""# ***distribution plots***

# ***histogram***
"""

how=sns.load_dataset('tips')
              # these plots  work only on single column      histplot shows us count or frequency
#print(how)
sns.displot(data=how, x='total_bill',bins=10,element='step',hue='sex',binwidth=5,color='gray',edgecolor="pink",linewidth=10)                       # distribution plots are used for  showing data distribution

#sns.histplot(data=how,x='time') #  ploting histogram on catogoric data

"""# **kernel density plot**"""

how=sns.load_dataset('tips')
sns.kdeplot(data=how,x='total_bill',hue='sex',fill='true',linestyle='dotted',color='black',
            linewidth=5,alpha=0.5) # kernel density plot
#sns.rugplot(data=how,x='total_bill',color='red') # kernel density plot

#sns.displot(data=how,x='total_bill',hue='sex',kind='kde')

"""# **rug plot**"""

sns.rugplot(data=how,x='total_bill',color='orange',height=0.5,linestyle='--',linewidth=0.1)

"""# ***2d  histogram or histogram for 2 columns***"""

sns.displot(data=how,x='total_bill',y='tip',hue='sex',kind='hist') # darker color represents  more density

"""# **2d kernal density plot or kde plot for 2 columns**"""

how=sns.load_dataset('tips')

#sns.displot(data=how,x='total_bill',y='tip',hue='sex',kind='kde',LineStyle='--',linewidth=10,palette=['red','green'],cmap='summer') # the area where lines are closed to eachother is more denser
sns.kdeplot(data=how,x='total_bill',y='tip',hue='sex',linestyle='--',palette=['green','blue'],cmap='summer',fill=True,
            linewidth=1,alpha=1)
#and viceversa

"""# **catogoric plots**
# **strip plot**
"""

sns.catplot(data=how,x='day',y='total_bill',hue='sex',kind='strip',jitter=0.2,
            color='red',linewidth=5,marker='d',size=5)
sns.stripplot(data=how,x='day',y='total_bill',hue='sex',jitter=0.2)
#sns.stripplot(data=how,x='day',y='total_bill',hue='sex',jitter=0.2)

"""# **swarm plot**"""

sns.catplot(data=how,x='day',y='total_bill',hue='sex',kind='swarm')
sns.swarmplot(data=how,x='day',y='total_bill',hue='sex',color='red',size=1,marker='d',linewidth=2) # swarm plot is same as the strip plot but it provdies  better representation

"""# **box plot**"""

how=sns.load_dataset('tips')

sns.catplot(data=how,x='day',y='total_bill',hue='sex',kind='box')
#sns.boxplot(data=how,x='day',y='total_bill',hue='sex',orient='horizontal')
#to make univarient box plot we avoid x then
sns.catplot(data=how,y='total_bill',hue='sex',kind='box',palette=['green','blue'],width=0.1,linewidth=2)

"""# **voilin plot**"""

#voilin plot is the combination of box and kde plot
sns.catplot(data=how,x='day',y='total_bill',hue='sex',kind='violin',split='False')
sns.catplot(data=how,y='total_bill',hue='sex',kind='violin',split='False',width=0.2,linewidth=2,palette=['green','blue'],edgecolor='red')
#

"""# **bar plot**"""

import numpy as np
#color=['red','green','blue','orange']
how
x=sns.catplot(data=how,y='day',x='total_bill' ,kind='bar', ci=None,hue='sex',palette=["#FF5738", "#33FFCE"],width=0.5
) #by default it finds average
plt.show()# to make the bars horizatal swap x and y with eachother
#sns.barplot(data=how,x='day',y='total_bill',hue='sex', estimator=np.mix())    # but also we can find mean median min s deviation etc

"""# **count plot**"""

sns.catplot(data=how,x='sex',hue='day', kind='count',palette=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'],width=0.5) # to make the bars horizontal  swap x with y
#sns.barplot(data=how,y='sex',y='total_bill',hue='day')   # this plot is used to count the values in the given column that
                                                          #how many time they are occured

"""# **point plot**"""

sns.catplot(data=how,x='time',y='total_bill',hue='sex', kind='point',ci=None,linestyle='dotted',marker='d')



"""# **REG PLOT**"""

how=sns.load_dataset('tips')            # regression means the relation between the given quantities
print(how)                          #shadows within the line shows error measurement
sns.regplot(data=how,x='total_bill',y='tip',scatter_kws={'s':0.5,'color':"orange","edgecolor":"black","marker":'--'}
            ,line_kws={"lw":0.2,"color":'blue',"alpha":1,"ls":'--'})# line provides the formula to find relation between the given two qunatities

"""# **LM PLOT**"""

how=sns.load_dataset('tips')       #  lm plot is similar to regplot but  additionaly it supports hue parameter which regplot
                                   # doesn't support
sns.lmplot(data=how,x='total_bill',y='tip',hue='sex',line_kws={'ls':'--','lw':5,'color':'red','alpha':0.5},
            scatter_kws={'marker':'d','s':5,'color':"red"})

"""# **RESIDPLOT**"""

sns.residplot(data=how ,x='total_bill',y='tip',scatter_kws={'color':'red','alpha':0.5},line_kws={'linestyle':'--','linewidth':5,'color':'red','alpha':0.5})

"""# **matrix plots**

# **cluster plot**
"""

iris=sns.load_dataset('iris')
sns.clustermap(iris.iloc[:,[1,2,3]],annot=True ,col_cluster=False ) #row_ cluster can also be used

"""## **heat map **"""

x=pd.read_csv('sudais.csv')
#print(x)
y=x.pivot(index='A',columns='B',values='C')
sns.heatmap(y,linewidth=0.5,annot=True,cmap='summer')

"""# **facet grid second method**"""

import seaborn as sns
import matplotlib.pyplot as plt
x=sns.load_dataset('tips')
print(x)
g=sns.FacetGrid(data=x,col='day',row='sex',hue='size')
g.map(sns.scatterplot,'tip','total_bill')# we can use any other plot instead of scatter here
g.add_legend()
plt.figsize(fig=(12,4))

"""# **pair plot**"""

y=sns.load_dataset('iris')
sns.pairplot(y)

"""# **pair grid**"""

sns.get_dataset_names()
iris=sns.load_dataset('iris')
#print(iris)
g=sns.PairGrid(data=iris,hue='species',vars=['sepal_length','sepal_width'])
#g.map_offdiag(sns.scatterplot)
g.map_diag(sns.violinplot,palette=['red','green','blue'],width=0.2)
g.map_lower(sns.kdeplot)
g.map_upper(sns.histplot)

"""**joint plot**"""

x=sns.load_dataset('tips')
print(x)
sns.jointplot(data=x,x='total_bill',y='tip',kind='scatter',hue='sex') # there are many more values for kind here

"""# **joint grid**"""

g=sns.JointGrid(data=x,x='total_bill',y='tip',hue='sex')
g.plot(sns.histplot,sns.kdeplot)                   # grid provides more functionality
                                                   # here through grid  we can handle both graphs individually