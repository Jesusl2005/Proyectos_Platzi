import random
def main():
  
# Iniciamos dando una explicacion breve del programa
  print('JUGUEMOS: PIEDRA, PAPEL O TIJERA!')
  print(' ')
  print('*'*60)
  print(' ')
  print('INSTRUCCIONES')
  print(' ')
  print('El juego consiste en la participacion de 2 jugadores')
  print('Cada jugador elije una de las opciones')
  print('Las combinaciones ganadoras son las siguientes: ')
  print('- Piedra gana a tijera')
  print('- Tijera gana a papel')
  print('- Papel gana a piedra')
  print(' ')
  print('*'*60)
  print(' ')  
  print('Elije una de las opciones teniendo en cuenta que:')
  print('1 - Piedra')
  print('2 - Tijera')
  print('3 - Papel')
  print(' ')
  print('*'*60)
  print(' ')
  
  
  # Solicitamos los valores de los 2 jugadores
  gamesjg = 0
  gamespc = 0
  gamesgained = gamesjg + gamespc
  games = 1
  while gamesgained <= 3:
    print('ELECCION')
    print('*'*10)
    print('RONDA', games)
    print('*'*10)
    print('Jugador = ', gamesjg, 'Partidas ganadas')
    print('CPU = ', gamespc, 'Partidas ganadas')
    print(' ')
    gamer1 = input('Eleccion del jugador: ')
    gamer1 = int(gamer1)
    
    if gamer1 == 1:
      print('Piedra')
    elif gamer1 == 2:
      print('Tijera')
    elif gamer1 == 3:
      print('Papel')
    else:
      print('Eleccion no valida')
      
    eleccion = (1, 2, 3)
    gamer2 = random.choice(eleccion)
    print(' ')
    print('Eleccion de la CPU:')
    if gamer2 == 1:
      print('Piedra')
    elif gamer2 == 2:
      print('Tijera')
    elif gamer2 == 3:
      print('Papel')
  
    #Realizamos el proceso logico para determinar quien es el ganador
      
    print(' ')
    print('*'*60)
    print(' ')
    print('RESULTADO')
    print(' ')
  
    if gamer1 == 1 and gamer2 == 2:
      gamesjg += 1
      print('Ganaste')
      print(' ')
      print('FELICITACIONES')
    elif gamer1 == 1 and gamer2 == 3:
      gamespc += 1
      print('Perdiste')
      print(' ')
      print('VUELVE A INTENTARLO')
    elif gamer1 == 2 and gamer2 == 3:
      gamesjg += 1
      print('Ganaste')
      print(' ')
      print('FELICITACIONES')
    elif gamer1 == 2 and gamer2 == 1:
      gamespc += 1
      print('Perdiste')
      print(' ')
      print('VUELVE A INTENTARLO')
    elif gamer1 == 3 and gamer2 == 1:
      gamesjg += 1
      print('Ganaste')
      print(' ')
      print('FELICITACIONES')
    elif gamer1 == 3 and gamer2 == 2:
      gamespc += 1
      print('Perdiste')
      print(' ')
      print('VUELVE A INTENTARLO')
    elif gamer1 == gamer2:
      print('Es un empate')
      print(' ')
      print('VUELVE A INTENTARLO')
    else:
      print('Eleccion no valida vuelva a intentarlo')
      print(' ')
      continue
    print(' ')
    print('*'*60)
    print(' ')
    games += 1
    if gamesjg == 2:
      print('El ganador es el jugador')
      break
    if gamespc == 2:
      print('El ganador es la CPU')
      break

if (__name__  ==  '__main__'):
  main()