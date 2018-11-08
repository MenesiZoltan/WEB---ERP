import database_common
import random


@database_common.connection_handler
def get_module_content(cursor, table):
    if table == "accounting":
        cursor.execute('''
                        SELECT * FROM accounting
                        ''');
        table = cursor.fetchall()
        return table

    elif table == "crm":
        cursor.execute('''
                        SELECT * FROM crm
                        ''');
        table = cursor.fetchall()
        return table

    elif table == "hr":
        cursor.execute('''
                        SELECT * FROM hr
                        ''');
        table = cursor.fetchall()
        return table

    elif table == "inventory":
        cursor.execute('''
                        SELECT * FROM inventory
                        ''');
        table = cursor.fetchall()
        return table

    elif table == "sales":
        cursor.execute('''
                        SELECT * FROM sales
                        ''');
        table = cursor.fetchall()
        return table

    elif table == "store":
        cursor.execute('''
                        SELECT * FROM store
                        ''');
        table = cursor.fetchall()
        return table


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



@database_common.connection_handler
def generate_item_id(cursor, table):
    if table == "accounting":
        cursor.execute('''
                        SELECT transaction_id FROM accounting
                        ''');
        item_ids = cursor.fetchall()

    elif table == "crm":
        cursor.execute('''
                        SELECT customer_id FROM crm
                        ''');
        item_ids = cursor.fetchall()

    elif table == "human_resources":
        cursor.execute('''
                        SELECT employee_id FROM hr
                        ''');
        item_ids = cursor.fetchall()

    elif table == "inventory":
        cursor.execute('''
                        SELECT inventory_id FROM inventory
                        ''');
        item_ids = cursor.fetchall()

    elif table == "sales":
        cursor.execute('''
                        SELECT sales_id FROM sales
                        ''');
        item_ids = cursor.fetchall()

    elif table == "store":
        cursor.execute('''
                        SELECT item_id FROM store
                        ''');
        item_ids = cursor.fetchall()

    return generate_random_id(item_ids)


@database_common.connection_handler
def add_new_element_to_database(cursor, new_entry, table):
    if table == "accounting":
        id = new_entry["id"]
        month = new_entry["month"]
        day = new_entry["day"]
        year = new_entry["year"]
        type = new_entry["type"]
        value = new_entry["value"]
        cursor.execute('''
                        INSERT INTO accounting
                        VALUES (%(id)s, %(month)s, %(day)s, %(year)s, %(type)s, %(value)s)
                        ''',
                       {'id': id, 'month': month, 'day': day, 'year': year, 'type': type, 'value': value});

    elif table == "crm":
        id = new_entry["id"]
        name = new_entry["name"]
        email = new_entry["email"]
        subscription = new_entry["subscription"]
        cursor.execute('''
                        INSERT INTO crm
                        VALUES (%(id)s, %(name)s, %(email)s, %(subscription)s)
                        ''',
                       {'id': id, 'name': name, 'email': email, 'subscription': subscription});

    elif table == "human_resources":
        id = new_entry["id"]
        name = new_entry["name"]
        dob = new_entry["year_of_birth"]
        cursor.execute('''
                        INSERT INTO hr
                        VALUES (%(id)s, %(name)s, %(dob)s)
                        ''',
                       {'id': id, 'name': name, 'dob': dob});

    elif table == "inventory":
        id = new_entry["id"]
        name = new_entry["name"]
        manufacturer = new_entry["manufacturer"]
        year = new_entry["year"]
        durability = new_entry["durability"]
        cursor.execute('''
                        INSERT INTO inventory
                        VALUES (%(id)s, %(name)s, %(manufacturer)s, %(year)s,  %(durability)s)
                        ''',
                       {'id': id, 'name': name, 'manufacturer': manufacturer, 'year': year, 'durability': durability});

    elif table == "sales":
        id = new_entry["id"]
        title = new_entry["title"]
        price = new_entry["price"]
        month = new_entry["month"]
        day = new_entry["day"]
        year = new_entry["year"]
        customer_id = new_entry["customer_id"]
        cursor.execute('''
                        INSERT INTO sales
                        VALUES (%(id)s, %(title)s, %(price)s, %(month)s, %(day)s, %(year)s, %(customer_id)s)
                        ''',
                       {'id': id, 'title': title, 'price': price, 'month': month, 'day': day, 'year': year, 'customer_id': customer_id});

    elif table == "store":
        id = new_entry["id"]
        title = new_entry["title"]
        manufacturer = new_entry["manufacturer"]
        price = new_entry["price"]
        stock = new_entry["stock"]
        cursor.execute('''
                        INSERT INTO store
                        VALUES (%(id)s, %(title)s, %(manufacturer)s, %(price)s, %(stock)s)
                        ''',
                       {'id': id, 'title': title, 'manufacturer': manufacturer, 'price': price, 'stock': stock});


@database_common.connection_handler
def get_data_by_id(cursor, entry_id, table):
    details = []
    if table == "accounting":
        cursor.execute('''
                        SELECT * FROM accounting
                        WHERE transaction_id= %(entry_id)s
                        ''',
                       {'entry_id': entry_id}),
        entry_details = cursor.fetchall()
        for element in entry_details:
            for key in element:
                details.append(element[key])
        del details[0]
        return details

    elif table == "crm":
        pass
    elif table == "human_resources":
        pass
    elif table == "inventory":
        pass
    elif table == "sales":
        pass
    elif table == "store":
        pass


@database_common.connection_handler
def update_by_id(cursor, entry_details, table):
    if table == "accounting":
        id = entry_details["id"]
        month = entry_details["month"]
        day = entry_details["day"]
        year = entry_details["year"]
        type = entry_details["type"]
        value = entry_details["value"]
        cursor.execute('''
                        UPDATE accounting
                        SET transaction_month = %(month)s, transaction_day = %(day)s,
                        transaction_year = %(year)s, transaction_type = %(type)s,
                        transaction_value = %(value)s
                        WHERE transaction_id = %(id)s;
                         ''',
                       {'id': id, 'month': month, 'day': day, 'year': year, 'type': type, 'value': value})

    if table == "crm":
        pass
    if table == "human_resources":
        pass
    if table == "inventory":
        pass
    if table == "sales":
        pass
    if table == "store":
        pass








