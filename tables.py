populations = [
    [106,107,111,133,221,767,1766],
    [502,635,809,947,1402,3634,5268],
    [2,2,2,6,13,30,46],
    [163,203,276,408,547,729,628],
    [2,7,26,82,172,307,392],
    [16,24,38,74,167,511,809]
]
continents = [
    "Africa",
    "Asia",
    "Australia",
    "Europe",
    "North America",
    "South America"
]
headers = print(f"{"Year":<20}{"1750":<20}{"1800":<20}{"1850":<20}{"1900":<20}{"1950":<20}{"2000":<20}{"2050":<20}")

for row in range(len(populations)):
    print(f"{continents[row]:<20}",end="")
    for column in range(len(populations[0])):
        print(f"{populations[row][column]:<20}",end="")
    print()

# column totals
yearly_population_totals = []
for column in range(len(populations[0])):
    sum = 0
    for row in range(len(populations)):
        sum = sum + populations[row][column]
    yearly_population_totals.append(sum)
print(f"{"Total":<20}{yearly_population_totals[0]:<20}{yearly_population_totals[1]:<20}{yearly_population_totals[2]:<20}{yearly_population_totals[3]:<20}{yearly_population_totals[4]:<20}{yearly_population_totals[5]:<20}{yearly_population_totals[6]:<20}")