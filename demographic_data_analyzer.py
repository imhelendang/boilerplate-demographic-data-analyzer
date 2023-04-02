import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby(['race'])['race'].count()

    # What is the average age of men?
    avg_age = df.groupby(['sex'])['age'].mean()
    average_age_men = round(avg_age.Male.astype(float),1)

    # What is the percentage of people who have a Bachelor's degree?
    percent = df.education.value_counts(normalize=True).mul(100).round(1)
    percentage_bachelors = percent.Bachelors

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
  
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    filter1 = df["salary"].isin([">50K"])
    filter2 = df["education"].isin(["Bachelors", "Masters", "Doctorate" ])
    
    higher_education = df[filter1 & filter2]
    lower_education = df[filter1 & (~filter2)]

    # percentage with salary >50K
    higher_education_rich = round((higher_education.groupby(['education'])['education'].count().sum() / df[filter2].groupby(['education'])['education'].count().sum()) *100,1)
    lower_education_rich = round((lower_education.groupby(['education'])['education'].count().sum() / df[(~filter2)].groupby(['education'])['education'].count().sum()) *100,1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week'] == 1)].shape[0]

    rich_percentage = round((df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = ((df[df['salary'] != '<=50K']['native-country'].value_counts())/(df['native-country'].value_counts())*100).idxmax()
    highest_earning_country_percentage = (round((df[df['salary'] != '<=50K']['native-country'].value_counts())/(df['native-country'].value_counts())*100,1)).max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = (india_df['occupation'].value_counts()).idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
