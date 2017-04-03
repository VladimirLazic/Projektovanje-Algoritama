import time
import numpy as np
import matplotlib.pyplot as plt

def CreatePlot(input_data, exec_time, algo_name):
    fig = plt.figure()     
    fig.suptitle(algo_name, fontsize=14, fontweight='bold')    
 
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)       
    ax.set_title('Vreme izvrsenja')
    ax.set_xlabel('Ulaz [n]')    
    ax.set_ylabel('Vreme [ms]')

    ax.plot(input_data, exec_time, '-', color='green')
    
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

    return fig

def ShowPlot():
    plt.show()
	
    # Sleep for n miliseconds
def Example_fn(n):
    print("Sleeping for ", n, " miliseconds...")
    time.sleep(n/1000) # sleep in miliseconds
    return 
    
    # Profile function Example-fn and create plot
def FirstPlot():
    # Measure exeuction time
    algo_name = "[FirstPlot] Example-fn"
    input_data = []
    exec_time = []
    for n in range(100, 1100, 100):
    	start_time = time.clock() # expressed in seconds
    	Example_fn(n)
    	end_time = time.clock()
    	exec_time.append((end_time - start_time)*1000) #get miliseconds
    	input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)

    # Profile function Example-fn and create plot	
def SecondPlot():
    # Measure exeuction time
    algo_name = "[SecondPlot] Example-fn"
    input_data = []
    exec_time = []
    
    for n in range(200, 2200, 200):
    	start_time = time.clock() # expressed in seconds
    	Example_fn(n)
    	end_time = time.clock()
    	exec_time.append((end_time - start_time)*1000) #get miliseconds
    	input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)


# Profile functions and create plots
FirstPlot()
SecondPlot()

# Show plots
ShowPlot()
