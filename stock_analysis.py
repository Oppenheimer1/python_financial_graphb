from pandas_datareader import data
import datetime
from bokeh.plotting import figure, output_file, show

start=datetime.datetime(2017,11,27)
end=datetime.datetime(2017,12,4)

df = data.DataReader(name="BAC",data_source="yahoo",start=start,end=end)

def inc_dec(c,o):
	if c > o:
		value="Increase"
	elif c < o:
		value="Decrease"
	else:
		value="Equal"
	return value


df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Close-df.Open)

print(df)

p = figure(x_axis_type="datetime", width=1000, height=300,title="Candlestick Chart")
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000

p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],
       hours_12, df.Height[df.Status=="Increase"],fill_color='green',line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],
       hours_12, df.Height[df.Status=="Decrease"],fill_color="#FF3333",line_color="black")

p.segment(df.index, df.High, df.index, df.Low, color="Black")

show(p)



#p.quad
#p.quad