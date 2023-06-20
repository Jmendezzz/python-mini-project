from store.games_store import games

from exceptions.game_exception import GameNotFoundError;



def print_all_games():
    print("CATALOGO DE VIDEOJUEGOS:")
    print("\n -----------------------------")

    for game in games:
        print(f"Nombre: {game['name']} \n" +
              f"Prestado: {'Si' if game['borrowed'] else 'No'} \n" +
              f"Precio alquiler: {game['rental_price']}"
              )
        print("-----------------------------")


def get_game_by_name(game_name):
     
     for game in games: 
         
         if(game["name"] == game_name):
             return game
         
     raise GameNotFoundError(f"No se encontró el juego: {game_name}")

def create_new_game():
    name =  input("Ingrese el nombre del juego: \n")
    rental_price = int(input(f"Ingrese el precio del alquiler del juego {name}: \n"))

    game = {
        "name": name,
        "borrowed": False,
        "rental_price":rental_price
    }
    games.append(game)
    print(f"El juego {name} ha sido regitrado exitosamente.")
