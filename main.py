from services.borrow_service import borrow_request, mark_game_returned
from services.game_service import print_all_games,create_new_game

def main():

    print("ALQUILER DE VIDEO JUEGOS")

    while True:
        print("MENU PRINCIPAL")
        print("------------------------------------")
        option =  int(input("Ingrese la opción que desea realizar: \n"+
                  "1. Realizar un prestamo \n"+
                  "2. Ver catalogo de video juegos \n"+
                  "3. Registro de devolución de juego \n" +
                  "4. Registrar un nuevo juego \n"))
        
        if ( option == 1):
            game_name = input("Ingrese el nombre del video juego a prestar: \n")
            borrow_request(game_name)
        elif( option == 2):
            print_all_games()
        elif( option == 3):
            game_name = input("Ingrese el nombre del video juego devuelto: \n")
            mark_game_returned(game_name)
        elif( option == 4):
            create_new_game()            
        else:
            print("Ingrese una opción válida.")
        
main()






