import matplotlib.pyplot as plt
import csv


# plt.plot( 'x', 'y1', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
# plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
# plt.plot( 'x', 'y3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")

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
fig, ax = plt.subplots(figsize=(12, 9))

# Read in data and set plots
for i in range(1,51):
    x = []
    y = []
    with open('default_runs/run{}.txt'.format(i),'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))
    ax.plot(x, y, color=get_color(i))

# Add title and axes labels
ax.set_title('Evolution of gene')
ax.set_xlabel('Generations')
ax.set_ylabel('Fitness')

# Remove borders
[ax.spines[spine].set_visible(False) for spine in ax.spines]

# Add horizontal gridlines
ax.yaxis.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Save to file
fig.savefig('plot.png')
