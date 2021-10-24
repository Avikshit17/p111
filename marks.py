import pandas as pd
import statistics
import plotly.figure_factory as pf
import random
import plotly.graph_objects as pg
df=pd.read_csv("studentMarks.csv")
sm=df["Math_score"].tolist()
# graph=pf.create_distplot([sm],["Student Marks"],show_hist=False)
# graph.show()

finalList=[]
def sample():
    for i in range(0,100):
        sd=[]
        pos=random.randint(0,len(sm)-1)
        data=int(sm[pos])
        sd.append(data)
    mean=statistics.mean(sd)
    finalList.append(mean)
for i in range(0,1000):
    sample()
mean=statistics.mean(finalList)
std=statistics.stdev(finalList)
fstd_sp=mean-std
fstd_ep=mean+std
sstd_sp=mean-(2*std)
sstd_ep=mean+(2*std)
tstd_sp=mean-(3*std)
tstd_ep=mean+(3*std)

graph=pf.create_distplot([finalList],["List"],show_hist=False)
graph.show()

#working with data 1

# df1=pd.read_csv("data1.csv")
# Marks1=df1["Math_score"].tolist()
# mean1=statistics.mean(Marks1)
# graph=pf.create_distplot([finalList],["List"],show_hist=False)
# graph.add_trace(pg.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="mean of data 1"))
# graph.add_trace(pg.Scatter(x=[fstd_ep,fstd_ep],y=[0,0.17],mode="lines",name="ending point of fstd"))
# graph.add_trace(pg.Scatter(x=[sstd_ep,sstd_ep],y=[0,0.17],mode="lines",name="ending point of sstd"))
# graph.add_trace(pg.Scatter(x=[tstd_ep,tstd_ep],y=[0,0.17],mode="lines",name="ending point of tstd"))
# graph.show()


#working with data 2

# df2=pd.read_csv("data2.csv")
# Marks2=df2["Math_score"].tolist()
# mean2=statistics.mean(Marks2)
# graph=pf.create_distplot([finalList],["List"],show_hist=False)
# graph.add_trace(pg.Scatter(x=[mean2,mean2],y=[0,0.17],mode="lines",name="mean of data 2"))
# graph.add_trace(pg.Scatter(x=[fstd_ep,fstd_ep],y=[0,0.17],mode="lines",name="ending point of fstd"))
# graph.add_trace(pg.Scatter(x=[sstd_ep,sstd_ep],y=[0,0.17],mode="lines",name="ending point of sstd"))
# graph.add_trace(pg.Scatter(x=[tstd_ep,tstd_ep],y=[0,0.17],mode="lines",name="ending point of tstd"))
# graph.show()

#working with data 3

# df3=pd.read_csv("data3.csv")
# Marks3=df3["Math_score"].tolist()
# mean3=statistics.mean(Marks3)
# graph=pf.create_distplot([finalList],["List"],show_hist=False)
# graph.add_trace(pg.Scatter(x=[mean3,mean3],y=[0,0.17],mode="lines",name="mean of data 3"))
# graph.add_trace(pg.Scatter(x=[fstd_ep,fstd_ep],y=[0,0.17],mode="lines",name="ending point of fstd"))
# graph.add_trace(pg.Scatter(x=[sstd_ep,sstd_ep],y=[0,0.17],mode="lines",name="ending point of sstd"))
# graph.add_trace(pg.Scatter(x=[tstd_ep,tstd_ep],y=[0,0.17],mode="lines",name="ending point of tstd"))
# graph.show()



