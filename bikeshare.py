import time
import pandas as pd
import numpy as np

CITY_DATA = { '2': 'chicago.csv',
              '1': 'new_york_city.csv',
              '3': 'washington.csv' }
monate = ('january', 'february', 'march', 'april', 'may', 'june', 'a')
tage = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'a')
staedte = ('2', '1','3')
def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    citiesRead = True
    #  get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while citiesRead:
        city = input('\nWhich City are you interest in?:\nEnter the number. \n1 - New York City, \n2 - Chicago, \n3 - Washington\n').lower()
        if city not in staedte:
            print('interesting, but i have only the 3 cities mentioned, please one of the numbers\n')
            continue
        else:
            citiesRead = False

    monthRead = True
            #get user input for month (all, january, february, ... , june)
    while monthRead:
         month = input('\nWhich month from January - June are you interested in?. Please enter a month, or a for all:\n').lower()
         if month not in monate:
            print('\n??uups, is this a month from January to June?? Please enter a valid month, or a for all:\n')
            continue
         else:
            monthRead = False

    weekRead = True
             #get user input for day of week (all, monday, tuesday, ... sunday)
    while weekRead:
        day = input('\nWhich day are you interested in? Please enter a day from Monday - Sunday, or  a for all\n').lower()
        if day not in tage:
            print('\nWhich kind of day is that? Please enter a valid day, or a for all:\n')
            continue
        else:
            weekRead = False

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

                             #Loads data for the specified city and filters by month and day if applicable.
                            # Args:
                             #   (str) city - name of the city to analyze
                             #  (str) month - name of the month to filter by, or "all" to apply no month filter
                             #   (str) day - name of the day of week to filter by, or "all" to apply no day filter
                            #Returns:
                              #  df - Pandas DataFrame containing city data filtered by month and day


    #load selected data from the csv

    df = pd.read_csv(CITY_DATA[city])
    #df = pd.read_csv('{}.csv'.format(city))

#change the 'Start Time' into datetime and geting the month and the day out and put those in a new column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

# if user choose not all in monate--> get the month
    if month != 'all':
        monate = ['january', 'february', 'march', 'april', 'may', 'june']
        month = monate.index(month) + 1
        df = df[df['month'] == month]

# if user choose not all in Tage--> get the day
    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
            #Displays statistics on the most frequent times of travel.
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

            #display the most common month
    popul_month = df['month'].mode()[0]
    print('the most common month is: ', popul_month)

           #display the most common day of week
    popul_day = df['day'].mode()[0]
    print('the most common day is: ', popul_day)

           #display the most common start hour

    df['hour']=df['Start Time'].dt.hour # kann das weg? -> nein leider nicht definiert die Stunden aus de rstartzeit
    popul_hour = df['hour'].mode()[0]
    print('the most common hour is: ', popul_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
           #Displays statistics on the most popular stations and trip.

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

            # TO DO: display most commonly used start station
    popul_start = df['Start Station'].mode()[0]
    print('the most popular start station is: ', popul_start)

            # TO DO: display most commonly used end station
    popul_end = df['End Station'].mode()[0]
    print('the most popular end station is: ', popul_end)

             # TO DO: display most frequent combination of start station and end station trip
    popul_start_end = (df['Start Station'] + ' and ' + df['End Station']).mode()[0]
    print('the most popular Start -> End combo is: ', popul_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
            #Displays statistics on the total and average trip duration.

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

            #displays total travel time
    tot_travel = sum(df['Trip Duration'])
    print('the total travel time is: ', int(tot_travel/86400), 'in days')

             # displays mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('the mean travel time is: ', int(mean_travel/60), 'in minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
            #Displays statistics on bikeshare users.
    print('\nCalculating User Stats...\n')
    start_time = time.time()

            #Displays counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)


             # Displayc counts of gender,
    try:
        user_sex =df['Gender'].value_counts()
        print('User_Gender:\n', user_sex) # No diverse ??? Nowadays it should contain diverse as well !!!
    except:
        print('No Gender info in this city')

         #Displays earliest, most recent, and most common year of birth
    try:
        alt = df['Birth Year'].min()
        print('The oldest user was born in: ', alt)
        jung = df['Birth Year'].max()
        print('The youngest user was born in: ', jung)
        mitte = df['Birth Year'].mode()[0]
        print('The most common users birthyear is: ', mitte)
    except:
        print('No birth data avalable in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # raw data show ... somehow the raw data was missing, have not seen it in the Projectquestion... but here we are :)
def raw_data(df):
    read_antwort = True
    antwort = input('Are you interested in viewing the first 5 rows of the raw data? Enter y/n \n').lower()
    fortytwo = 0
    while read_antwort:
         if antwort == 'n':
            read_antwort = False
         if antwort == '42':
            print('It looks like you found the answer to the answer of life, the universe, and everything') # one easteregg should be inside! right?
            read_antwort = False
         if antwort == 'y':
            print(df[fortytwo:fortytwo+5])
            antwort=input('there are another 5 rows available... Print? y/n\n').lower()
            fortytwo += 5
         # removed "else" -> it was about the wrong answer means not "42"

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
#Thanks for all the fish
