from server import app
from flask import render_template, request, redirect
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
        "Item Name",
        "Manufacturer",
        "Purchase Year",
        "Durability"]

    if request.method == "POST":
        new_entry = {
            "id": data_manager.generate_item_id(route_name),
            "name": request.form["Item Name"],
            "manufacturer": request.form["Manufacturer"],
            "year": request.form["Purchase Year"],
            "durability": request.form["Durability"]}

        data_manager.add_new_element_to_database(new_entry, route_name)
        return redirect("/inventory")
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)


@app.route("/inventory/update_item", defaults={"id": None}, methods=["GET", "POST"])
@app.route("/inventory/update_item/<id>", methods=["GET", "POST"])
def update_item_inventory(id):
    route_name = "inventory"
    module = "Inventory"
    if request.method == "GET":
        table_titles = [
            "Item Name",
            "Manufacturer",
            "Purchase Year",
            "Durability"]

        item_id = str(request.args.get("item_id"))
        entry_details = data_manager.get_data_by_id(item_id, route_name)
        #if item_id not in entry_details:
            #flash()
            #return redirect(request.referrer)
        #else:
        return render_template(
            "item.html",
            route_name=route_name,
            module=module,
            table_titles=table_titles,
            item_id=item_id,
            entry_details=entry_details,
            page_action="UPDATE")
    else:
        id = id + "#&"
        entry_details = {
            "id": id,
            "name": request.form["Item Name"],
            "manufacturer": request.form["Manufacturer"],
            "year": request.form["Purchase Year"],
            "durability": request.form["Durability"]}

        data_manager.update_by_id(entry_details, route_name)
        return redirect("/inventory")

@app.route("/inventory/delete_item", methods=["POST"])
def delete_item_inventory():
    route_name = "inventory"
    item_id = request.form["item_id"]
    data_manager.delete_item_by_id(item_id, route_name)
    return redirect("/inventory")