from server import app
from flask import render_template, request
import data_manager

@app.route("/inventory")
def start_module_inventory():
    module = "Inventory"
    route_name = "inventory"

    return render_template(
        'general.html',
        module=module,
        route_name=route_name)


@app.route("/inventory/database_content")
def show_inventory_table():
    module = "Inventory"
    table = "inventory"
    content = data_manager.get_module_content(table)
    table_titles = [
        "Item ID",
        "Item Name",
        "Manufacturer",
        "Purchase Year",
        "Durability"]

    return render_template(
        "content.html",
        content=content,
        module=module,
        table_titles=table_titles)



@app.route("/inventory/add_item", methods=["GET", "POST"])
def add_item_inventory():
    route_name = "inventory"
    module = "Inventory"
    table_titles = [
        "Item ID",
        "Item Name",
        "Manufacturer",
        "Purchase Year",
        "Durability"]

    if request.method == "POST":
        pass
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)