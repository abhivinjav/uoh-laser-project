import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
###############################################################
# importing the csv data

df = pd.read_csv("image_analysis_csv_files\\centroid_pos.csv", delimiter=',')
df['Centroid_X'] = df['Centroid_X'] / 26
df['Centroid_Y'] = df['Centroid_Y'] / 26

# remove the reference, and put it in a separate dataframe
df_ref = df[df['Image'] == 'ref']
df = df.drop(0)

#align new centroids with ref centroid as origin
df['Centroid_X'] = df['Centroid_X'] - df_ref.at[0, 'Centroid_X']
df['Centroid_Y'] = df['Centroid_Y'] - df_ref.at[0, 'Centroid_Y']


# making the scatter plot

sns.scatterplot(data=df, x='Centroid_X', y='Centroid_Y', color='black', label='Aerosol Centroids')
plt.scatter(x=[0], y=[0], color='red', label='Reference Centroid')

error=[1] * 16

plt.errorbar( df['Centroid_X'], df['Centroid_Y'], xerr=error, yerr=error, fmt='none', ecolor='black', elinewidth=1, capsize=3, label='Error = 1mm')

plt.legend()
plt.title("Centroid Positions wrt Reference Beam Centroid")
plt.xlabel('x-position (mm)')
plt.ylabel('y-position (mm)')

plt.xticks(np.arange(-2, 2.5, 0.5))
plt.yticks(np.arange(-2, 3, 0.5))
plt.minorticks_on()

plt.savefig("centroid_pos.png", bbox_inches='tight', dpi=150)