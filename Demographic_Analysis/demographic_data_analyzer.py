import pandas as pd

demo_data = pd.read_csv(r"D:/Studies/CODING/Python/ML_Exercises/Demographic_Analysis/adult.data.csv")

#How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
race_counts = demo_data.race.value_counts()

#What is the average age of men?
avg_ageof_men = demo_data[demo_data["sex"]=='Male']["age"].mean()

#What is the percentage of people who have a Bachelor's degree?
bachelors_count = demo_data[demo_data['education']=='Bachelors'].shape[0]
total_people = demo_data.shape[0]
percent_bachelors = round((bachelors_count/total_people)*100, 4)

#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = ['Bachelors','Masters', 'Doctorate']
Educated_people = demo_data[demo_data['education'].isin(advanced_education)]
Educated_people_count = Educated_people.shape[0]
high_earners_count = Educated_people[Educated_people['salary']=='>50K'].shape[0]

percent_high_earners = round((high_earners_count/Educated_people_count)*100, 4)

#What percentage of people without advanced education make more than 50K?
Uneducated_people = demo_data[~demo_data['education'].isin(advanced_education)]
Uneducated_people_count = Uneducated_people.shape[0]
Uned_high_earners_count = Uneducated_people[Uneducated_people['salary']==">50K"].shape[0]

percent_Uned_high_earners = round((Uned_high_earners_count/Uneducated_people_count)*100, 4)

#What is the minimum number of hours a person works per week?
min_hours = demo_data['hours-per-week'].min()

#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
people_with_MinHours = demo_data[demo_data['hours-per-week']==min_hours]
people_with_MinHours_count = people_with_MinHours.shape[0]
MinHours_high_earners_count = people_with_MinHours[people_with_MinHours['salary']==">50K"].shape[0]

percent_MinHours_high_earners = round((MinHours_high_earners_count/people_with_MinHours_count)*100, 4)

#What country has the highest percentage of people that earn >50K and what is that percentage?
country_count = demo_data['native-country'].value_counts()
high_earners = demo_data[demo_data['salary']==">50K"]['native-country'].value_counts()
country_percantages = round((high_earners/country_count)*100, 4)

top_country = country_percantages.idxmax()
top_percantage = country_percantages.max()
print(f"{top_country} has the highest percantage of high earners, which is: {top_percantage}%")

#Identify the most popular occupation for those who earn >50K in India.
high_earners_In_India = demo_data[(demo_data['native-country']=='India') & (demo_data['salary']=='>50K')]
popular_occupation = high_earners_In_India['occupation'].value_counts().idxmax()

print(f"{popular_occupation} is the most popular occupation for those who earn >50K in India.")