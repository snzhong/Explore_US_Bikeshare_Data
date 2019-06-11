import time
import pandas as pd
import numpy as np
import datetime

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
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Sorry, that was not one of the options. Please double check spelling.")
        else:
            break

    while True:
        month = input("Which month would you like to filter the data for? Type \"all\" for no month filter. ").lower()
        months = ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
        if month not in months:
            print("Sorry, that was not one of the options. Please double check spelling.")
        else:
            break

    while True:
        day = input("Which day would you like to filter the data for? Type \"all\" for no day filter. ").lower()
        days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        if day not in days:
            print("Sorry, that was not one of the options. Please double check spelling.")
        else:
            break

    print('-'*40)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # create new column for combination 'Start' and 'End' stations
    df['Start - End Station'] = df['Start Station'] + ' - ' + df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day)

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displaying the most common month
    if df['month'].nunique() > 1:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        common_month = df['month'].mode()[0]
        common_month_name = months[common_month - 1]
        print('\nThe most common month was {}.'.format(common_month_name))
    else:
        print('\nData was filtered for a specific month.')

    # displaying the most common day of week
    if df['day_of_week'].nunique() > 1:
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        common_day = df['day_of_week'].mode()[0]
        common_day_name = days[common_day]
        print('\nThe most common day was {}.'.format(common_day_name))
    else:
        print('\nData was filtered for a specific day.')

    # displaying the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nMost Frequent Start Hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displaying most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nThe most common start station was {}.'.format(common_start_station))

    # displaying most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station was {}.'.format(common_end_station))

    # displaying most frequent combination of start station and end station trip
    common_start_end_station = df['Start - End Station'].mode()[0]
    print('\nThe most common Start and End station combination was {}.'.format(common_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displaying total travel time
    total_travel_time = datetime.timedelta(seconds = df['Trip Duration'].sum().astype(np.float64))
    print('\nThe total travel time was: ', total_travel_time)

    # displaying mean travel time
    average_travel_time = str(datetime.timedelta(seconds = df['Trip Duration'].mean()))
    print('\nThe average travel time was: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # displaying counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe counts for user types are:\n', user_types)

    # displaying counts of gender
    gender = df['Gender'].value_counts()
    print('\nThe counts for gender are:\n', gender)

    # displaying earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min().astype(np.int64)
    recent_birth_year = df['Birth Year'].max().astype(np.int64)
    common_birth_year = df['Birth Year'].mode()[0].astype(np.int64)
    print('\nThe earliest birth year is: ', earliest_birth_year)
    print('\nThe most recent birth year is: ', recent_birth_year)
    print('\nThe most common birth year is: ', common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
