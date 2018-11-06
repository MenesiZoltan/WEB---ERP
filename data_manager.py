import database_common


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
