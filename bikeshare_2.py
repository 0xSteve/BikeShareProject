import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
                      month filter
        (str) day - name of the day of week to filter by, or "all" to apply no
                    day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs

    # get user input for month (all, january, february, ... , june)

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while(True):
        try:
            resp = 'n'
            city = input("What city would you like to use? \n")
            city = city.lower()

            if(city not in CITY_DATA):
                raise KeyError(city.title() + " is not a possible city." +
                               " Try again.")

            month = input("What month would you like to use? \n")
            month = month.lower()
            # Nor this one.
            if(month not in MONTHS):
                raise IndexError("Month " + month.title() + " ")

            day = input("What day would you like to use? \n")
            day = day.lower()
            if(day not in DAYS):
                raise IndexError("Day " + day.title() + " ")

            break

        except KeyboardInterrupt:  # Should I stay or should I go?
            # Given a keyboard interrupt, determine if the user wants to quit.
            resp = input("\nYou sent a keyboard interrupt! Do you want to " +
                         "quit? (y/N)\n")
            if(resp.lower() == 'y'):
                break
        except KeyError as err:
            print(str(err))
        except IndexError as err:
            print(str(err) + "is not available. Try again.")
        except Exception as ex:
            print(str(ex) + " error occurred. Try again.")

    if resp.lower() == "y":
        sys.exit()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if
    applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no
                      month filter
        (str) day - name of the day of week to filter by, or "all" to apply no
                    day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    comm_month = MONTHS[df['month'].mode()[0] - 1].title()
    print("The most common month is: " + comm_month)

    # display the most common day of week
    print("The most common day of week is: " +
          str(df['day_of_week'].mode()[0]))

    # display the most common start hour
    comm_start = df['Start Time'].dt.hour.mode()[0]
    print("The most common start time is: " + str(comm_start))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
