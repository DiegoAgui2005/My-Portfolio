print("Bienvenido al juego piedra papel o tijera")
player_1_name = input("Jugador 1 ingresa tu nombre:")
player_2_name = input("Jugador 2 ingresa tu nombre:")
player_1_choice = input("Jugador 1, qué eliges? piedra, papel o tijera?:")
player_2_choice = input("Jugador 2, que eliges? piedra, papel o tijera?:")

valid_moves = ["piedra", "papel", "tijera"]

if player_1_choice not in valid_moves or player_2_choice not in valid_moves:
    print("Uno o ambos jugadores seleccionaron una alternativa incorrecta")
else:
    if player_1_choice == player_2_choice:
        print("Es un empate!")
    elif (player_1_choice == "piedra" and player_2_choice == "tijera") or \
         (player_1_choice == "tijera" and player_2_choice == "papel") or \
         (player_1_choice == "papel" and player_2_choice == "piedra"):
        print("Gana", player_1_name)
    else:
        print("Gana", player_2_name)