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
    df = pd.read_csv(f"image_analysis_csv_files\\water\\{k}_Plot Values.csv")
    df['Radius_[pixels]'] = df['Radius_[pixels]'] / 28
    df['X_Fit:_Gaussian'] = df['X_Fit:_Gaussian'] / 28
    water_dfs.append(df)

# from reference, 1mm = 28pixels, measured on FIJI (ImageJ)

#############################################################
# reference graph
df_ref = pd.read_csv("image_analysis_csv_files\\water\\ref_Plot Values.csv")
df_ref['Radius_[pixels]'] = df_ref['Radius_[pixels]'] / 28
df_ref['X_Fit:_Gaussian'] = df_ref['X_Fit:_Gaussian'] / 28
df_ref['Normalized_Integrated_Intensity'] = df_ref['Normalized_Integrated_Intensity']

plt.figure()
sns.lineplot(data=df_ref, x='Radius_[pixels]', y='Normalized_Integrated_Intensity', color='black', linewidth=1, label='Radial Profile')
sns.lineplot(data=df_ref, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75, label='Gaussian Fit')

plt.title(r'Reference Radial Intensity Profile $I_{\text{ref}}(r)$')
plt.xlabel('Radius (mm)')
plt.ylabel('Normalized Integrated Intensity')
plt.xticks(np.arange(0,12,1))
plt.yticks(np.arange(20,130, 10))
plt.minorticks_on()

plt.savefig("radial_profiles\\ref_water_graph.png", bbox_inches='tight', dpi=150)

#########################################################
# graphs for each one
i = 1
for df in water_dfs:
    if i == 1:
        plt.figure()
        sns.lineplot(data=df, x='Radius_[pixels]', y='Normalized_Integrated_Intensity', color='black', linewidth=1, label='Radial Profile')
        sns.lineplot(data=df, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75, label='Gaussian Fit')
    else:
        plt.figure()
        sns.lineplot(data=df, x='Radius_[pixels]', y='Normalized_Integrated_Intensity', color='black', linewidth=1, label='Gaussian Fit')
        sns.lineplot(data=df, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75, label='Gaussian Fit')

    plt.title(fr'Radial Intensity Profile {i} $I_{i}(r)$')
    plt.xlabel('Radius (mm)')
    plt.ylabel('Normalized Integrated Intensity')
    plt.xticks(np.arange(0,12,1))
    plt.yticks(np.arange(20,160, 10))
    plt.minorticks_on()
    
    plt.savefig(f"radial_profiles\\water_graph_{i}.png", bbox_inches='tight', dpi=150)
    i += 1

################################################################
# all water graphs overlaid

i = 1
for df in water_dfs:
    if i == 1:
        plt.figure()
        sns.lineplot(data=df, x='Radius_[pixels]', y='Normalized_Integrated_Intensity', color='black', linewidth=1, label='Aerosol')
        #sns.lineplot(data=df, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75, label='Gaussian Fit')
    else:
        sns.lineplot(data=df, x='Radius_[pixels]', y='Normalized_Integrated_Intensity', color='black', linewidth=1)
        #sns.lineplot(data=df, x='X_Fit:_Gaussian', y='Fit:_Gaussian', color='blue', linewidth=0.75)

    plt.title(r'Radial Intensity Profiles Overlaid $\Sigma^{16}_{i=1} I_{i}(r)$')
    plt.xlabel('Radius (mm)')
    plt.ylabel('Normalized Integrated Intensity')
    plt.xticks(np.arange(0,12,1))
    plt.yticks(np.arange(20,160, 10))
    plt.minorticks_on()
    
    i += 1

sns.lineplot(data=df_ref, x='Radius_[pixels]', y='Normalized_Integrated_Intensity', color='blue', linewidth=1, label='Reference')

plt.savefig('radial_profiles\\ref_vs_aerosol_sum.png', bbox_inches='tight', dpi=150)
