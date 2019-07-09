import time
import pandas as pd
import numpy as np


#Defining dictionaries

city_data = { 1: 'chicago.csv',
              2: 'new_york_city.csv',
              3: 'washington.csv' }

city_dict = {0 : 'all',
            1  : 'Chicago',
            2  : 'New York',
            3  : 'Washington D.C'}

month_data= { 0: 'all',
            1 : 'january',
            2 : 'february',
            3 : 'march',
            4 : 'april',
            5 : 'may',
            6 : 'june'}

week_data= {0 : 'all',
            1 : 'monday',
            2 : 'tuesday',
            3 : 'wednesday',
            4 : 'thursday',
            5 : 'friday',
            6 : 'saturday',
            7 : 'monday'}




print('Hello! Let\'s explore some US bikeshare data!', '\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

def get_filters():
    valid_input = False
    valid_input2 = False
    valid_input3 = False

    #Returns:
    #    (str) city - name of the city to analyze
    #    (str) month - name of the month to filter by, or "all" to apply no month filter
    #    (str) week_day - name of the day of week to filter by, or "all" to apply no day filter


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while not valid_input:
        try:
            city = input(
    'Please choose the city using the correspondent number: 1 - Chicago/ 2 - New York/ 3 - Washington D.C.\n')
            city = int(city)
            print('\n','You\'ve choosen {}.'.format(city_dict[city]))
            answer = input('Is that correct? 1 - Yes/ 2 - No\n')
            ##Checking if the user is sure about his answer
            if answer == '1' or answer.lower() == 'yes':
                valid_input = True
            else:
                valid_input = False

        except:
            print('\n','Please insert a valid number.')

# get user input for month (all, january, february, ... , june)
    while not valid_input2:
        try:
            month = input(
    'Now, please choose month: 0: all /1 : january/ 2 : february /3 : march/ 4 : april/5 : may/ 6 : june\n')
            month = int(month)
            print('\n','You\'ve choosen {}.'.format(month_data[month]))

            answer2 = input('Is that correct? 1 - Yes/ 2 - No\n')
            if answer2 == '1' or answer2 == 'Yes' or answer2 == 'yes':
                valid_input2 = True
            else:
                valid_input2 = False

        except:
            print('\n','Please insert a valid number.')

  # get user input for day of week (all, monday, tuesday, ... sunday)

    while not valid_input3:
        try:
            week_day = input(
    'Finnaly, choose the day of the week: : 0- all /1- monday/ 2- tuesday /3- wednesday/ 4- thursday/5- friday/ 6- saturday/ 7 - sunday\n')
            week_day = int(week_day)
            print('\n','You\'ve choosen {}.'.format(week_data[week_day]))
            answer3 = input('Is that correct? 1 - Yes/ 2 - No\n')
            if answer3 == '1' or answer3 == 'Yes' or answer3 == 'yes':
                valid_input3 = True
            else:
                valid_input3 = False

        except:
            print('\n','Please insert a valid number.')

    print('-'*40)
    return city, month, week_day


def load_data(city, month, week_day):
    #"""
    #Loads data for the specified city and filters by month and day if applicable.

    #Args:
       # (str) city - name of the city to analyze
       # (str) month - name of the month to filter by, or "all" to apply no month filter
       # (str) week_day - name of the day of week to filter by, or "all" to apply no day filter
    #Returns:
        #df - Pandas DataFrame containing city data filtered by month and day
    #"""


    df = pd.read_csv(city_data[city])
    return df



def time_stats(df,city,month, week_day):
    """Displays statistics on the most frequent times of travel."""


    # Creating supporting columns

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Hour'] = df['Start Time'].dt.hour
    df['DOW'] = df['Start Time'].dt.weekday + 1

    # display the most common month, filtering data if necessary
    if month == 0:

        popular_month = df['Month'].mode()[0]
        print('Most Popular Month:', month_data[popular_month].capitalize())
    else:

        df = df[(df['Month'] == month)]
        print('Most Popular Month:', month_data[month].capitalize())

    # display the most common day of week
    if week_day == 0:
        popular_week = df['DOW'].mode()[0]
        print('Most Popular Day of Week:', week_data[popular_week].capitalize(), '\n')
    else:
        df = df[(df['DOW'] == week_day)]
        print('Most Popular Day of Week:', week_data[week_day].capitalize())


    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('Most Popular Hour:', popular_hour)




def station_stats(df):
   # """Displays statistics on the most popular stations and trip."""



    # display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', pop_start_station, '\n')

    # display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', pop_end_station, '\n')

    # display most frequent combination of start station and end station trip
    df['Combined_Station'] = df['Start Station']+' - '+ df['End Station']
    pop_comb_station = df['Combined_Station'].mode()[0]
    print('Most Popular Combination of Satart and End Station:', pop_comb_station, '\n')




def trip_duration_stats(df):
    #"""Displays statistics on the total and average trip duration."""


    # display total travel time
    print('Total Travel Time:',df['Trip Duration'].sum()//360, ' hours')

    # display mean travel time
    print('Mean Travel Time:',df['Trip Duration'].mean()//60, ' minutes')




def user_stats(df, city):
    """Displays statistics on bikeshare users."""



    # Display counts of user types
    print(df['User Type'].value_counts(),'\n')

    # Display counts of gender
    if city == 3:
        print('Gender data is not avaiable for Washington.','\n')

    else:
        print(df['Gender'].value_counts(),'\n')

    # Displaying statistcs about age

    if city == 3:
        print('User data is not avaiable for Washington.','\n')

    else:
    # To turn things more interesting, I created an "Age" column, with an aproximated age of the users.
        df['Age'] = 2017 - df['Birth Year']
        #Deleting outliers
        df['Age'] = np.where((df['Age'] >= 90.0),
                       np.nan,
                       df['Age'])
        #Displaying information
        print('The medium age of the users is {} years old.'.format(int(df['Age'].mean())),'\n')
        print('The median age is {} years old.'.format(int(df['Age'].median())),'\n')
        print('The most common age is {} years old.'.format(int(df['Age'].mode()[0])),'\n')





def main():
    while True:
        city, month, week_day = get_filters()
        df = load_data(city, month, week_day)

        time_stats(df,city,month,week_day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        x = 0
        y = 5
        #asking user about raw_data


        raw_data = input('\nWould you like to see a sample of the raw data? Enter 1 - yes or 2 - no.\n')

        if raw_data.lower() == 'no' or raw_data == "2":

            break
        else:

            x += 5
            y += 5
            continue


        restart = input('\nWould you like to restart? Enter 1-yes or 2-no.\n')
        if restart.lower() != 'yes' or restart == '1':
            print('Thank you very much and please approve!!')
            break


if __name__ == "__main__":
	main()
