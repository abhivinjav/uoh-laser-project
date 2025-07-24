import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
###############################################################
# importing the csv data
k = 0
water_dfs = []

while k < 16:
    k += 1
    df = pd.read_csv(f"image_analysis_csv_files\\water_diameter\\{k}_Plot Values.csv")
    df['Distance_(pixels)'] = df['Distance_(pixels)'] / 26
    df['X_Fit:_Gaussian'] = df['X_Fit:_Gaussian'] / 26
    water_dfs.append(df)

# from reference, 1mm = 26pixels, measured on FIJI (ImageJ)

#############################################################
# reference graph
df_ref = pd.read_csv("image_analysis_csv_files\\water_diameter\\ref_Plot Values.csv")
df_ref['Distance_(pixels)'] = df_ref['Distance_(pixels)'] / 26
df_ref['X_Fit:_Gaussian'] = df_ref['X_Fit:_Gaussian'] / 26
df_ref['Gray_Value'] = df_ref['Gray_Value']

plt.figure()
sns.lineplot(data=df_ref, x='Distance_(pixels)', y='Gray_Value', color='black', linewidth=1, label='Radial Profile')
sns.lineplot(data=df_ref, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75, label='Gaussian Fit')

plt.title(r'Reference Radial Intensity Profile $I_{\text{ref}}(r)$')
plt.xlabel('Radius (mm)')
plt.ylabel('Normalized Integrated Intensity')
plt.xticks(np.arange(0,23,1))
plt.yticks(np.arange(20,200, 10))
plt.minorticks_on()

plt.savefig("full_radial_profiles\\full_ref_water_graph.png", bbox_inches='tight', dpi=150)

#########################################################
# graphs for each one
i = 1
for df in water_dfs:
    if i == 1:
        plt.figure()
        sns.lineplot(data=df, x='Distance_(pixels)', y='Gray_Value', color='black', linewidth=1, label='Radial Profile')
        sns.lineplot(data=df, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75, label='Gaussian Fit')
    else:
        plt.figure()
        sns.lineplot(data=df, x='Distance_(pixels)', y='Gray_Value', color='black', linewidth=1, label='Radial Profile')
        sns.lineplot(data=df, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75, label='Gaussian Fit')

    plt.title(fr'Radial Intensity Profile {i} $I_{i}(r)$')
    plt.xlabel('Radius (mm)')
    plt.ylabel('Normalized Integrated Intensity')
    plt.xticks(np.arange(0,23,1))
    plt.yticks(np.arange(20,200, 10))
    plt.minorticks_on()
    
    plt.savefig(f"full_radial_profiles\\water_diameter_graph_{i}.png", bbox_inches='tight', dpi=150)
    i += 1

################################################################
# all water graphs overlaid

i = 1
for df in water_dfs:
    if i == 1:
        plt.figure()
        sns.lineplot(data=df, x='Distance_(pixels)', y='Gray_Value', color='black', linewidth=1, label='Aerosol')
        #sns.lineplot(data=df, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75, label='Gaussian Fit')
    else:
        sns.lineplot(data=df, x='Distance_(pixels)', y='Gray_Value', color='black', linewidth=1)
        #sns.lineplot(data=df, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75)

    plt.title(r'Radial Intensity Profiles Overlaid $\Sigma^{16}_{i=1} I_{i}(r)$')
    plt.xlabel('Radius (mm)')
    plt.ylabel('Normalized Integrated Intensity')
    plt.xticks(np.arange(0,23,1))
    plt.yticks(np.arange(20,200, 10))
    plt.minorticks_on()
    
    i += 1

sns.lineplot(data=df_ref, x='Distance_(pixels)', y='Gray_Value', color='blue', linewidth=1, label='Reference')

plt.savefig('full_radial_profiles\\full_ref_vs_aerosol_sum.png', bbox_inches='tight', dpi=150)
