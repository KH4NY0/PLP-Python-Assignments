import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                       columns=iris['feature_names'] + ['target'])

# Map target numbers to species names
iris_df['species'] = iris_df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display first few rows
print("Dataset Preview:")
print(iris_df.head())

# Check data types and missing values
print("\nDataset Information:")
print(iris_df.info())

# Check for missing values
print("\nMissing Values:")
print(iris_df.isnull().sum())

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistical Summary:")
print(iris_df.describe())

# Group by species and compute mean of numerical columns
print("\nMean Values by Species:")
print(iris_df.groupby('species').mean())

# Task 3: Data Visualization
plt.figure(figsize=(15, 10))

# 1. Line Chart (showing petal length trends)
plt.subplot(2, 2, 1)
iris_df.groupby('species')['petal length (cm)'].mean().plot(kind='line', marker='o')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')

# 2. Bar Chart (average feature lengths by species)
plt.subplot(2, 2, 2)
feature_means = iris_df.groupby('species')[['sepal length (cm)', 'sepal width (cm)', 
                                            'petal length (cm)', 'petal width (cm)']].mean()
feature_means.plot(kind='bar', ax=plt.gca())
plt.title('Average Measurements by Species')
plt.xlabel('Species')
plt.ylabel('Length (cm)')
plt.legend(title='Features', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 3. Histogram (distribution of petal width)
plt.subplot(2, 2, 3)
iris_df['petal width (cm)'].hist(bins=15)
plt.title('Distribution of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')

# 4. Scatter Plot (sepal length vs petal length)
plt.subplot(2, 2, 4)
sns.scatterplot(data=iris_df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.tight_layout()
plt.show()

