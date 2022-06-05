import db_engine

def show_menu():
    print()
    print("------------------------------------")
    print("1 - новая сделка")
    print("2 - показать сделки")
    print("3 - удалить сделки")
    print("4 - Ввести цену товара")
    print("5 - Показать товары")
    print("6 - Удалить товар")
    print("0 - конец")
    print("------------------------------------")

command = -1
while command!=0:
    show_menu()
    command = int(input())
    if command ==1:
        name = input("Vvedite Imya:")
        product = input("Vvedite Product:")
        price = int(input("Vvedite tsenu:"))
        amount = int(input("Vvedite colichestvo:"))
        db_engine.insert_deal(name, product, price, amount)
    elif command == 2:
        db_engine.show_deals()
    elif command == 3:
        db_engine.delete_all_data()
    elif command == 4:
        product = input("Vvedite product:")
        price = int(input("Vvedite tsenu:"))
        db_engine.update_price(product, price)
    elif command == 5:
        db_engine.show_prices()
    elif command == 6:
        db_engine.delete_product(input("Vvedite product:"))
    input()
