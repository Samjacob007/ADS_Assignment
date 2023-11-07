import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Dataset/NetflixUserbase.csv")

male_users = df[df['Gender']=="Male"]
male_users_count = male_users.groupby("Join Date").size()

female_users = df[df['Gender']=="Female"]
female_users_count = female_users.groupby("Join Date").size()


plt.plot(female_users_count)
plt.plot(male_users_count)
plt.show()