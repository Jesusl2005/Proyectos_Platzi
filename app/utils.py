import csv
def get_population(country_dict):
  population_dict = {
   '2022': int(country_dict['2022 Population']),
   '2020': int(country_dict['2020 Population']),
   '2015': int(country_dict['2015 Population']),
   '2010': int(country_dict['2010 Population']),
   '2000': int(country_dict['2000 Population']),
   '1990': int(country_dict['1990 Population']),
   '1980': int(country_dict['1980 Population']),
   '1970': int(country_dict['1970 Population'])
  }

  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def get_world_percentage():
  with open('./data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    reader = list(reader)
    reader = reader[1:]
    
    countries = []
    percentages = []
    counter = 0
    for row in reader:
      country = reader[counter][2]
      country = str(country)
      percentage = reader[counter][-1]
      percentage = float(percentage)
      counter += 1
      countries.append(country)
      percentages.append(percentage)
      
    world_percentage_dict = (dict(zip(countries, percentages)))
    labels = world_percentage_dict.keys()
    values = world_percentage_dict.values()
  
  return labels, values

    
    
  