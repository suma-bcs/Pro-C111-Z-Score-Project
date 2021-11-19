# import necessary libraries
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import random

# read the csv
df = pd.read_csv("medium_data.csv")

# take the first data
data = df['reading_time'].tolist()

# take out the mean of the first data
population_mean = statistics.mean(df["reading_time"])
print("MEAN OF TOTAL DATA IS")
print(population_mean)

# take out the standard deviation of the first data
population_std_deviation = statistics.stdev(data)
print("STANDARD DEVIATION OF TOTAL DATA IS")
print(population_std_deviation)

# take out new data intervention and its mean
new_data = df['claps'].tolist()
new_data.pop(0)

new_data_mean = statistics.mean(new_data)
print("NEW INTERVENTION MEAN IS",new_data_mean)

# create a function for taking out random 30 data samples from first data
def random_set_of_data_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
       
    
    mean = statistics.mean(dataset)
    
    return mean

# take out 1,2 and 3 std_deviation for the first data
pop_1_std_deviation_start,pop_1_std_deviation_end = population_mean-population_std_deviation,population_mean+population_std_deviation
pop_2_std_deviation_start,pop_2_std_deviation_end = population_mean-(2*population_std_deviation),population_mean+(2*population_std_deviation)
pop_3_std_deviation_start,pop_3_std_deviation_end = population_mean-(3*population_std_deviation),population_mean+(3*population_std_deviation)
print("STD DEV 1 IS",pop_1_std_deviation_start,pop_1_std_deviation_end)
print("STD DEV 2 IS",pop_2_std_deviation_start,pop_2_std_deviation_end)
print("STD DEV 3 IS",pop_3_std_deviation_start,pop_3_std_deviation_end)



# FUNCTION TO PLOT GRAPH

def show_fig(mean_of_samples):
    df = mean_of_samples
    mean = statistics.mean(mean_of_samples)
    print("MEAN OF SAMPLING DISTRIBUTION",mean)
    
    # plot graph and add traces
    fig =ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))

    fig.add_trace(go.Scatter(x=[pop_1_std_deviation_start, pop_1_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
    fig.add_trace(go.Scatter(x=[pop_1_std_deviation_end, pop_1_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
    fig.add_trace(go.Scatter(x=[pop_2_std_deviation_start, pop_2_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
    fig.add_trace(go.Scatter(x=[pop_2_std_deviation_end, pop_2_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
    fig.add_trace(go.Scatter(x=[pop_3_std_deviation_start, pop_3_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
    fig.add_trace(go.Scatter(x=[pop_3_std_deviation_end, pop_3_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
    fig.add_trace(go.Scatter(x=[new_data_mean, new_data_mean], y=[0, 0.17], mode="lines", name="NEW INTERVENTION MEAN"))
    fig.show()



# FUNCTION TO GET MEAN OF 30 DATA POINTS 100 TIMES AND PLOT THE GRAPH

def setup():
    mean_of_samples = []
    for i in range(0,100):
        set_of_mean = random_set_of_data_mean(30)
        mean_of_samples.append(set_of_mean)

    show_fig(mean_of_samples)
    


# CALL SETUP
setup()

# find z score of the data
z_score = (new_data_mean-population_mean)/population_std_deviation
print("Z-SCORE OF THE DATA IS",z_score)






