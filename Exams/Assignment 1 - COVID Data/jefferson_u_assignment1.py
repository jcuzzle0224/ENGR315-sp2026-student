import sys


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data


def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    # your code here
    # sets variables for what we are searching for

    first_positive_rock = None
    first_positive_hburg = None
    search1 = "Rockingham"
    searchstate = "Virginia"
    search2 = "Harrisonburg city"

    #loops through all of the data until the first value is found
    for ent in data:
        date, county, state, fips, cases, deaths = ent
        #if the value is not found yet, set it. if it is, ignore it
        if first_positive_rock is None and county == search1 and state == searchstate and cases >= 1:
            first_positive_rock = date
        if first_positive_hburg is None and county == search2 and state == searchstate and cases >=1:
            first_positive_hburg = date
        #once both are found, stop the loop
        if first_positive_rock is not None and first_positive_hburg is not None:
            break


    return first_positive_rock, first_positive_hburg


def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # sets up search conditions
    statesearch = "Virginia"
    search1 = "Rockingham"
    search2 = "Harrisonburg city"

    # sets variables to 0 for all items
    hburg_max = 0
    rock_max = 0
    hburg_new = 0 
    rock_new = 0
    rock_prev = 0
    hburg_prev = 0
    hburg_day = None
    rock_day = None

    # your code here
    # filters through entries that were parsed
    for ent in data:
        date, county, state, fips, cases, deaths = ent
        # check proper search
        if county == search1 and state == statesearch:
            # sets the new cases to the current cases - the previous case date
            new = cases - rock_prev
            # if the new case ## is greater than the past new case number, sets the max to that number
            if new > rock_max:
                rock_max = new
                rock_day = date
            # sets the previous case to whatever the current case number is, even if rock_new wasn't updated
            rock_prev = cases
        # same cycle for hburg
        if county == search2 and state == statesearch:
            new = cases -hburg_prev
            if new > hburg_max:
                hburg_max = new
                hburg_day = date
            hburg_prev = cases
    return rock_day, hburg_day

def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    :return:
    """
    
    # your code here
    # same search terms
    statesearch = "Virginia"
    search1 = "Rockingham"
    search2 = "Harrisonburg city"

    # sets variables to 0 for all items
    rock_prev = 0
    rock_7_day = 0
    hburg_prev = 0
    hburg_7_day = 0
    # placeholder values for each day in a 7-day period
    d1 = d2 = d3 = d4 = d5 = d6 = d7 = 0
    # repeated the same values but just used h for hburg instead of d for day
    h1 = h2 = h3 = h4 = h5 = h6 = h7 = 0
    for ent in data:
        date, county, state, fips, cases, deaths = ent
        # search for state
        if state == statesearch:
            # search for county
            if county == search1:
                # sets new cases (day 0) to cases - previous day's cases
                new = cases - rock_prev
                # sets the previous case count to the current day's for next loop
                rock_prev = cases
                # sets the day placeholders with the first day being the new count, second day being "yesterday's" count, etc, etc
                d7 = d6
                d6 = d5
                d5 = d4
                d4 = d3
                d3 = d2
                d2 = d1
                d1 = new
                # sums all 7 days
                case_sum = d1 + d2 + d3 + d4 + d5 + d6 + d7
                # if the sum is larger than the prior sum, which it is for the first 7 days, set the value to the current sum
                if case_sum > rock_7_day:
                    rock_7_day = case_sum
        # same cycle for hburg but using h instead of d
        if county == search2:
                new = cases - hburg_prev
                hburg_prev = cases
                h7 = h6
                h6 = h5
                h5 = h4
                h4 = h3
                h3 = h2
                h2 = h1
                h1 = new
                case_sum = h1 + h2 + h3 + h4 + h5 + h6 + h7              
                if case_sum > hburg_7_day:
                    hburg_7_day = case_sum
    

    return rock_7_day, hburg_7_day

if __name__ == "__main__":
    data = parse_nyt_data('C:/Users/jcuzz_zici3uw/Desktop/School/PROGRAMMING/ENGR315-sp2026-student/Exams/Assignment 1 - COVID Data/us-counties.csv')

 #   for (date,county, state, fips, cases, deaths) in data:
 #       print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    print("The first cases for Rockingham County and Harrisonburg City were on:",str(first_question(data)),", respectively.")


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    print("The highest number of new cases recorded on a single day in Rockingham County and Harrisonburg were on",second_question(data),"respectively")

    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?
    # What was the worst seven day period in Rockingham County for new COVID cases (in terms of absolute number of cases)?
    print("The worst 7 day periods in Rockingham County and Harrisonburg had a total of", third_question(data), "cases, respectively")


