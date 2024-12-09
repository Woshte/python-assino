import pandas as pd


from data import my_data.csv
my-data = mydata_crude()
data = pd.DataFrame(data=my-data.data, columns=my-data.feature_names)
data['target'] = my-data.target


print(data.head())
print(data.info())
print(data.describe())


print(data.groupby('target').mean())


plt.figure(figsize=(10, 6))
sns.barplot(x='target', y='sepal_length', data=data)
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
plt.show()

