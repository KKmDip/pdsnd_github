#!/usr/bin/env python
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city_mapping = {
        1: 'chicago',
        2: 'new york city',
        3: 'washington'
    }


    dow_mapping={
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday',
        7: 'sunday',
        8: 'all'
    }

    month_mapping = {
        1: 'january',
        2: 'february',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'june',
        7: 'all'
    }

    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('Please choose the city you''re interested in(pick a number)\n 1) Chicago\n 2) New Your City\n 3) Washington\n')
    while True:
        if int(city) in city_mapping.keys():
            city = city_mapping[int(city)].capitalize()
            break
        else:
            city = input('Okay, this is really not that difficult. Just pick a number from 1-3.\n 1) Chicago\n 2) New Your City\n 3) Washington\n')



    month = input('Please choose the month you''re interested in(pick a number)\n 1) January\n 2) February\n 3) March\n '
                    '4) April\n 5) May\n 6) June\n 7) All\n')
    while True:
        if int(month) in month_mapping.keys():
            month = month_mapping[int(month)].capitalize()
            break
        else:
            month = input('Okay, this is really not that difficult. Just pick a number from 1-7.\n 1) January\n 2) February\n 3) March\n '
                    '4) April\n 5) May\n 6) June\n 7) All\n')



    dow = input('Please choose the day of the week you''re intersted (pick a number)\n 1) Monday\n 2) Tuesday\n 3) Wednesday\n '
                    '4) Thursday\n 5) Friday\n 6) Saturday\n 7) Sunday\n 8) All\n')
    while True:
        if int(dow) in dow_mapping.keys():
            day = dow_mapping[int(dow)].capitalize()
            break
        else:
            dow = input('Okay, this is really not that difficult. Just pick a number from 1-8.\n 1) Monday\n 2) Tuesday\n 3) Wednesday\n '
                    '4) Thursday\n 5) Friday\n 6) Saturday\n 7) Sunday\n 8) All\n')





    print('-'*80)
    if month == 'All':
        if day == 'All':
            print(f"This is your analysis for {city} for all days of the week from January to June.")
        else:
            print(f"This is your analysis for {city} for {day}s from January to June.")
    elif day == 'All':
        print(f"This is your analysis for {city} for all days of the week for the month of {month}.")
    else:
        print(f"Here is your analysis for {city} for {day}s in the month of {month}")
    print('-'*80)
    print('\n')

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    dow_mapping = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Frinday': 4,
        'Saturday': 5,
        'Sunday': 6,
        'All': 7
    }

    month_mapping = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'All': 7
    }

    # read the csv file
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the time columns from strings to pandas date-time format
    df['Start Time'] = pd.to_datetime(df['Start Time'], infer_datetime_format=True)
    df['End Time'] = pd.to_datetime(df['End Time'], infer_datetime_format=True)


    if month.lower() != 'all':
        df = df[df['Start Time'].dt.month == month_mapping[month]]

    if day.lower() != 'all':
        df = df[df['Start Time'].dt.dayofweek == dow_mapping[day]]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""


    print('-'*40)
    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('-'*40)
    print('Thank you for using this code')
    start_time = time.time()

    dow_mapping={
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    month_mapping = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June'
    }
    df['dow']=df['Start Time'].dt.weekday.map(dow_mapping)
    df['month']= df['Start Time'].dt.month.map(month_mapping)
    df['hour'] = df['Start Time'].dt.hour

    # display the most common month
    month = df.mode()['month'][0]

    # display the most common day of week
    dow = df.mode()['dow'][0]

    # display the most common start hour
    hour = df.mode()['hour'][0]
    print(f"The most common month is {month}; the most common day of the week is {dow}, and the most common start hour is {hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('\n')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('-'*40)
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print('-'*40)
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]

    print(f"\tThe most commonly used start station is {start_station}")

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]

    print(f"\tThe most commonly used end station is {end_station}")


    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]

    print(f"\tThe most frequent combination of start station and end station trip is {start_end_station}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('\n')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('-'*40)
    print('\nCalculating Trip Duration...\n')
    print('-'*40)

    start_time = time.time()

    # TO DO: display total travel time
    ttt = df['Trip Duration'].sum()

    print(f"\tTotal Travel Time is {ttt} seconds")

    # TO DO: display mean travel time
    tt_mean = df['Trip Duration'].mean()

    print(f"\tThe mean travel time is {tt_mean} seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('\n')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('-'*40)
    print('\nCalculating User Stats...\n')
    print('-'*40)
    start_time = time.time()

    if 'User Type' in df.columns:
        # Display counts of user types
        user_type = df['User Type'].dropna().unique()


        print("User type info:")
        for i in user_type:
            print('\t',i, df['User Type'].value_counts()[i])
    else:
        print("Sorry, User Type info is not provided in this dataset.\n")



    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df.mode()['Birth Year'][0])

        print("\nBirth Year info:")
        print(f"\tEarliest year of birth: {earliest}\n\tRecent year of birth: {recent}\n\tCommon year of birth: {common}")
    else:
        print("Sorry, Birth Year info is not provided in this dataset.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower().strip()
        start_loc = 0

        while view_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to see 5 more rows? Either yes or no.\n").lower().strip()
            if view_data != 'yes':\
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
