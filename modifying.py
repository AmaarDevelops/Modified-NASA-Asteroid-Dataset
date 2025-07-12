import pandas as pd
import numpy as np
import os

# Get the folder where the script is running
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'neo.csv')
df = pd.read_csv(file_path)

null_values = df.isnull().sum()
total_number_of_asteroids = df['name'].nunique()

hazardous_count = df[df['hazardous'] == True].value_counts().sum()
non_hazardous_count = df[df['hazardous'] == False].value_counts().sum()

average_diameter = (df['est_diameter_min'] + df['est_diameter_max']).mean()

fastest_asteroid_speed= df['relative_velocity'].max()
fastest_asteroid = df['relative_velocity'].idxmax()
fastest_asteroid_name = df.loc[fastest_asteroid,'name']

closest_asteroid_distance = df['miss_distance'].min()
closest_asteroid = df['miss_distance'].idxmin()
closest_asteroid_name = df.loc[closest_asteroid,'name']

condition = (df['hazardous'] == True) & (df['miss_distance'] < 10000000)


df['Risk Factor'] = np.where(condition, 'High Risk', 'Low Risk')

top_10_largest_asteroid = df.sort_values(by = 'est_diameter_max' ,ascending=False).head(10)[['name','est_diameter_max']]

top_10_fastest_asteroids = df.sort_values(by='relative_velocity',ascending=False).head(10)[['name','relative_velocity']]

top_10_closest_approaches = df.sort_values(by='miss_distance', ascending=True).head(10)[['name','miss_distance']]

df.to_csv('Modified-Nasa-Dataset.csv',index=False)



print('Null Values Count:-',null_values)
print("Total number of asteroids:-",total_number_of_asteroids)
print('Hazardous:-',hazardous_count)
print('Non hazardous count:-',non_hazardous_count)
print("Average Diameter:-",average_diameter)
print("Fastest asteroid speed:-",fastest_asteroid_speed)
print("Fastest asteroids name:-",fastest_asteroid_name)
print("Closest Asteroid distance:-",closest_asteroid_distance)
print("Closest Asteroid name:-",closest_asteroid_name)
print("\nTop 10 largest asteroids:-",top_10_largest_asteroid)
print("\nTop 10 fastest asteroids:-",top_10_fastest_asteroids)
print("\nTop 10 closest asteroids:-",top_10_closest_approaches)


print("\n\nFinal:-",df)