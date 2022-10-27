import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')
  country = input('Selecciona un pais: ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    print('1 - Grafica de barras')
    print('2 - Grafica de torta')
    eleccion = input('Selecciona que tipo de grafica deseas ver: ')
    eleccion = int(eleccion)
    if eleccion == 1:
      charts.generate_bar_chart(labels, values)
    elif eleccion == 2:
      charts.generate_pie_chart(labels, values)
    else:
      print('Eleccion no valida, vuelva a intentarlo')

def run2():
  print('1 - Grafica de barras')
  print('2 - Grafica de torta')
  eleccion = input('Selecciona que tipo de grafica deseas ver: ')
  eleccion = int(eleccion)
  if eleccion == 1:
    labels, values = utils.get_world_percentage()
    charts.generate_bar_chart(labels, values)
  elif eleccion == 2:
    labels, values = utils.get_world_percentage()
    charts.generate_pie_chart(labels, values)
  else:
    print('Eleccion no valida, vuelva a intentarlo')
  
if __name__ == '__main__':
  print('Elige que deseas encontrar:')
  print('1 - Si deseas ver el crecimiento poblacional de un pais especifico')
  print('2 - Si deseas ver el porcentaje de poblacion por paises  de cada continente')
  eleccion = input('Eleccion = ')
  eleccion = int(eleccion)
  if eleccion == 1:
    run()
  elif eleccion == 2:
    run2()
  else:
    print('Eleccion no permitida, vuelve a intentarlo')
    
  