import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv"
data = pd.read_csv(url)

print(data.head())

city_most_cases = data.loc[data['totalCases'].idxmax()]
print("City with most COVID-19 cases:", city_most_cases['city'], "with", city_most_cases['totalCases'], "cases")

city_fewest_cases = data.loc[data['totalCases'].idxmin()]
print("City with fewest COVID-19 cases:", city_fewest_cases['city'], "with", city_fewest_cases['totalCases'], "cases")

state_data = data.groupby('state').sum().reset_index()

state_most_cases = state_data.loc[state_data['totalCases'].idxmax()]
print("State with most COVID-19 cases:", state_most_cases['state'], "with", state_most_cases['totalCases'], "cases")

state_fewest_cases = state_data.loc[state_data['totalCases'].idxmin()]
print("State with fewest COVID-19 cases:", state_fewest_cases['state'], "with", state_fewest_cases['totalCases'], "cases")

city_most_deaths = data.loc[data['deaths'].idxmax()]
print("City with most COVID-19 deaths:", city_most_deaths['city'], "with", city_most_deaths['deaths'], "deaths")

city_fewest_deaths = data.loc[data['deaths'].idxmin()]
print("City with fewest COVID-19 deaths:", city_fewest_deaths['city'], "with", city_fewest_deaths['deaths'], "deaths")

state_data['deathRate'] = state_data['deaths'] / state_data['totalCases']

state_most_deaths_per_case = state_data.loc[state_data['deathRate'].idxmax()]
print("State with most deaths per COVID-19 case:", state_most_deaths_per_case['state'], "with a death rate of", state_most_deaths_per_case['deathRate'])

state_fewest_deaths_per_case = state_data.loc[state_data['deathRate'].idxmin()]
print("State with fewest deaths per COVID-19 case:", state_fewest_deaths_per_case['state'], "with a death rate of", state_fewest_deaths_per_case['deathRate'])

total_cases_brazil = data['totalCases'].sum()
print("Total COVID-19 cases in Brazil:", total_cases_brazil)

total_deaths_brazil = data['deaths'].sum()
print("Total COVID-19 deaths in Brazil:", total_deaths_brazil)

top_5_states_deaths = state_data.nlargest(5, 'deaths')
plt.figure(figsize=(10, 6))
sns.barplot(x='state', y='deaths', data=top_5_states_deaths, palette='viridis')
plt.title('Top 5 States with Most COVID-19 Deaths')
plt.xlabel('State')
plt.ylabel('Number of Deaths')
plt.show()

bottom_5_states_deaths = state_data.nsmallest(5, 'deaths')
plt.figure(figsize=(10, 6))
sns.histplot(bottom_5_states_deaths['deaths'], bins=5, kde=False, color='blue')
plt.title('Histogram of 5 States with Fewest COVID-19 Deaths')
plt.xlabel('Number of Deaths')
plt.ylabel('Frequency')
plt.show()
