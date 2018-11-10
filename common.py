import random


def generate_random_id(sql_ids):
    list_of_ids = []
    for item in sql_ids:
        for key in item:
            list_of_ids.append(item[key])

    while True:
        generated = ''
        lowercase_letters = []
        list_of_vowels = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                          "j", "k", "l", "m", "n", "o", "p", "q", "r",
                          "s", "t", "u", "v", "w", "x", "y", "z"]

        for i in range(2):
            lowercase_letters.append(random.choice(list_of_vowels))
        generated_number = random.randint(10, 100)
        generated = lowercase_letters[0] + "H" + str(generated_number) + "J" + lowercase_letters[1]

        if generated in list_of_ids:
            continue
        else:
            return generated + "#&"



def fetch_module_titles(module_name):
    table_titles = {
        "Accounting": [
            "Transaction ID",
            "Transaction Month",
            "Transaction Day",
            "Transaction Year",
            "Transaction Type",
            "Transaction Value"],
        "Customer Relations Managmenent": [
            "Customer ID",
            "Customer Name",
            "Customer E-mail",
            "Customer Subscription"],
        "Human Resources": [
            "Employee Id",
            "Employee Name",
            "Year of Birth"],
        "Inventory": [
            "Item ID",
            "Item Name",
            "Manufacturer",
            "Purchase Year",
            "Durability"],
        "Sales": [
            "ID",
            "Title of Game Sold",
            "Price",
            "Month of Sale",
            "Day of Sale",
            "Year of Sale",
            "Customer ID"],
        "Store": [
            "Item ID",
            "Game Title",
            "Manufacturer",
            "Price",
            "Stock"]
    }
    return table_titles[module_name]