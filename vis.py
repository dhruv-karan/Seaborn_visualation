import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup Complete")

fifa_data = pd.read_csv('fifa_ranking.csv',index_col="rank_date", parse_dates=True)
fifa_data.head()

#Plottig 
plt.figure(figsize=(16,6))
#sns.lineplot(data=fifa_data)
