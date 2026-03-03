def main():
    all_entered_values = []
    for values in range(3):
        while True:
            try:
                year = int(input('Please enter your year: '))
                break
            except ValueError:
                print('Year must be a number. Please enter a valid year')
                continue
        state = input('Please enter your state: ')
        while True:
            try:
                population = int(input('Please enter your population: '))
                break
            except ValueError:
                print('Population must be a number')
                continue
        all_entered_values.append([year,state,population])
    return all_entered_values

def total_population(data, target_year):
    return sum(pop for year, _, pop in data if year == target_year)

def get_target_year(data):
    years = {year for year, _, pop in data}
    while True:
        try:
            entered_year = int(input('Please enter your year: '))
        except ValueError:
            print('Please enter a valid year')
            continue
        if entered_year not in years:
            print(f'year not in list. Valid years are: {sorted(years)}')
            continue
        return entered_year

data = main()
target_year = get_target_year(data)
print (f'the total population for {target_year} is {total_population(data, target_year)}')