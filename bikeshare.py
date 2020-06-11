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
    print('Hello! Let\'s explore some US bikeshare data!')
   
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs        
    
    while True:
        city = input("Please choose city of interest; 'chicago', 'new york city', 'washington', or 'all'\n> ").lower()
        
        if city not in CITY_DATA:
            print("\nInvalid Entry\n")
            continue
        
        else:
            break

        return city

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = input("enter a valid month 'january' to 'june' or 'all'\n ").lower()

        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('Invalid Entry')

        else:
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
    
    while True:

        day = input("Enter day of week such as 'monday' or enter 'all'\n").lower()

        if day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            print('Invalid Entry')

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
    df=pd.read_csv(CITY_DATA[city])

    
    
    
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(start_time)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('the most popular month is:',common_month)
    
    # TO DO: display the most common day of week
    
    df['day'] = df['Start Time'].dt.weekday
    common_day = df['day'].mode()[0]
    print('the most popular day is:',common_day)
    
    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('the most popular hour is:',common_hour)     
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('most popular start location is:', common_start)
    
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('most pupular end location is:', common_end)
    
    # TO DO: display most frequent combination of start station and end station trip
   
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time: ", total_travel_time)
    
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('average travel time: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    
    # TO DO: Display counts of user types
    print('User Types: ',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
            
        print('Gender Counts: ',df['Gender'].value_counts())
    else:
        print('Gender data not available')

        # TO DO: Display earliest, most recent, and most common year of birth
        
    if "Gender" in df.columns:
        birth_year = df['Birth Year']
        print('earliest birth year: ', birth_year.min())
        print('latest birth year: ', birth_year.max())
        print('popular year of birth: ', birth_year.mode())
    
    else:
        print('birth data not available')

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

        i = 0
        raw_data = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
        pd.set_option('display.max_columns',200)
        while True:            
            if raw_data == 'no':
                break
            print(df[i:i+5])
            raw = input('\nWould you like to see next rows of raw data?\n').lower()
            i += 5
            break
        
        restart = input("\nWould you like to restart? Enter 'yes' or 'no'.\n")
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
