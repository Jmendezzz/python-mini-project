from services.game_service import get_game_by_name
from exceptions.game_exception import GameNotFoundError
from exceptions.borrow_exception import GameIsBorrowedError, InsufficientCustomerPayment


def borrow_request(game_name_request):

    try:
        game = get_game_by_name(game_name_request)

        game_is_borrowed(game)

        customer_payment = int(input("Ingrese el pago del cliente \n"))

        validate_customer_payment(game, customer_payment)

        accept_borrow_request(game)

    except (GameNotFoundError, GameIsBorrowedError, InsufficientCustomerPayment) as e:
        print(e)


def game_is_borrowed(game):
    if (game["borrowed"]):
        raise GameIsBorrowedError(
            f"El juego {game['name']} ya está en prestamo.")


def validate_customer_payment(game, customer_payment):
    if (game["rental_price"] > customer_payment):
        raise InsufficientCustomerPayment(
            f"Pago insuficiente. El pago requerido para poder alquilar  {game['name']} es ${game['rental_price']}. Pago del cliente ${customer_payment}  ")


def accept_borrow_request(game):
    game["borrowed"] = True
    print(f"El juego {game['name']} ha sido prestado exitosamente!.")


def mark_game_returned(game_name):

    try:
        game = get_game_by_name(game_name)
        game["borrowed"] = False
        print(f"El juego {game['name']} ha sido retornado exitosamente!.")

    except GameNotFoundError as e:
        print(e)
