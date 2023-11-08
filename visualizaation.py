import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset/NetflixUserbase.csv")

# Convert the 'Join Date' column to a datetime object
df['Join Date'] = pd.to_datetime(df['Join Date'], format='%d/%m/%Y')

# Extract the month and year from the 'Join Date' column as a string
df['Join Month'] = df['Join Date'].dt.strftime('%Y-%m')

# Group the data by the 'Join Month' and count the number of users who joined in each month
monthly_user_count = df['Join Month'].value_counts().sort_index()

# Split the data into males and females
male_data = df[df['Gender'] == 'Male']
female_data = df[df['Gender'] == 'Female']

# Group the male and female data by 'Join Month' and count the number of users who joined in each month
male_user_count = male_data['Join Month'].value_counts().sort_index()
female_user_count = female_data['Join Month'].value_counts().sort_index()

# Create the line plot for total users
plt.figure(figsize=(12, 6))
plt.plot(monthly_user_count.index, monthly_user_count.values,
         marker='o', linestyle='-', label='Total Users')
plt.xlabel('Join Month')
plt.ylabel('Number of Users')
plt.title('Netflix Userbase Growth Over Time')
plt.grid(True)
plt.xticks(rotation=45)

# Create the line plots for males and females

plt.plot(male_user_count.index, male_user_count.values,
         marker='o', linestyle='-', label='Males')
plt.plot(female_user_count.index, female_user_count.values,
         marker='o', linestyle='-', label='Females')

# Add a legend
plt.legend()

# Display the plot
plt.show()


# Group the data by 'Subscription Type' and count the number of users in each category
subscription_counts = df['Subscription Type'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(subscription_counts, labels=subscription_counts.index,
        autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Subscription Types')

# Display the pie chart
plt.show()
