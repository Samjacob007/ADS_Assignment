import pandas as pd
import matplotlib.pyplot as plt

NetflixData = pd.read_csv("Dataset/NetflixUserbase.csv")

""" Convert the 'Join Date' column to a datetime object"""
NetflixData['Join Date'] = pd.to_datetime(
    NetflixData['Join Date'], format='%d/%m/%Y')

"""Extract the month and year from the 'Join Date' column as a string"""
NetflixData['Join Month'] = NetflixData['Join Date'].dt.strftime('%Y-%m')

"""Group the data by the 'Join Month' and count the number of users who joined in each month"""
monthly_user_count = NetflixData['Join Month'].value_counts().sort_index()

"""Split the data into males and females"""
male_data = NetflixData[NetflixData['Gender'] == 'Male']
female_data = NetflixData[NetflixData['Gender'] == 'Female']

"""Group the male and female data by 'Join Month' and count the number of users who joined in each month"""
male_user_count = male_data['Join Month'].value_counts().sort_index()
female_user_count = female_data['Join Month'].value_counts().sort_index()

""" Create the line plot for total users"""
def linegraph():
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_user_count.index, monthly_user_count.values,
            marker='o', linestyle='-', label='Total Users')
    plt.xlabel('Join Month')
    plt.ylabel('Number of Users')
    plt.title('Netflix Userbase Growth Over Time')
    plt.grid(True)
    plt.xticks(rotation=45)

    """Create the line plots for males and females"""

    plt.plot(male_user_count.index, male_user_count.values,
            marker='o', linestyle='-', label='Males')
    plt.plot(female_user_count.index, female_user_count.values,
            marker='o', linestyle='-', label='Females')

    """Add a legend"""
    plt.legend()

    """Display the plot"""
    plt.show()


"""Group the data by 'Subscription Type' and count the number of users in each category"""
subscription_counts = NetflixData['Subscription Type'].value_counts()

"""Create a pie chart"""
def piechart():
    plt.figure(figsize=(8, 8))
    plt.pie(subscription_counts, labels=subscription_counts.index,
            autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Subscription Types')

    """ Add a legend"""
    plt.legend()

    """Display the pie chart"""
    plt.show()


"""Group the data by 'Country' and count the number of users in each country"""
country_counts = NetflixData['Country'].value_counts()

"""Create a bar graph"""
def barchart():
    plt.figure(figsize=(12, 6))
    plt.bar(country_counts.index, country_counts)
    plt.xlabel('Country')
    plt.ylabel('Number of Users')
    plt.title('Number of Users by Country')
    plt.xticks(fontsize=6.5)
    """Add a legend"""
    plt.legend()
    print(country_counts)
    """Display the bar graph"""

    plt.show()


linegraph()
piechart()
barchart()