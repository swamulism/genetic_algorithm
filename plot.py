import matplotlib.pyplot as plt
import csv

# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)    

def get_color(x):
    return tableau20[x % len(tableau20)]

# Set size of figure
fig, ax = plt.subplots(figsize=(12, 8))

# Read in data and set plots

mut = [0.1, 0.01, 0.005, 0.001]
cross = [0.7, 0.5, 0.3]

i = 0
for m in mut:
    for c in cross:
        x = []
        y = []
        with open('robby_runs/robby_m{}_c{}.txt'.format(m,c),'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=' ')
            for row in plots:
                x.append(float(row[0]))
                y.append(float(row[1]))
        ax.plot(x, y, color=get_color(i - 1), marker='.', label="Mutation rate = {}, Crossover rate = {}".format(m, c))
        i += 1

# Add title and axes labels
ax.set_title('Combinations of different params on effectivness')
ax.set_xlabel('Fitness')
ax.set_ylabel('Generation')

# Limit the range of the plot to only where the data is.    
# Avoid unnecessary whitespace.    
# plt.ylim(0, 90)    
# plt.xlim(1968, 2014)   

plt.legend()

# Remove borders
[ax.spines[spine].set_visible(False) for spine in ax.spines]

# Add horizontal gridlines
ax.yaxis.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Save to file
fig.savefig('plot2.png')
