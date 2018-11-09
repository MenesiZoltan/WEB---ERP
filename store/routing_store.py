from server import app
from flask import render_template, request, redirect
import data_manager


@app.route("/store")
def start_module_store():
    module = "Store"
    route_name = "store"

    return render_template(
        'general.html',
        module=module,
        route_name=route_name)


@app.route("/store/database_content")
def show_store_table():
    module = "Store"
    table = "store"
    content = data_manager.get_module_content(table)
    table_titles = [
        "Item ID",
        "Game Title",
        "Manufacturer",
        "Price",
        "Stock"]

    return render_template(
        "content.html",
        content=content,
        module=module,
        table_titles=table_titles)


@app.route("/store/add_item", methods=["GET", "POST"])
def add_item_store():
    route_name = "store"
    module = "Store"
    table_titles = [
        "Game Title",
        "Manufacturer",
        "Price",
        "Stock"]

    if request.method == "POST":
        new_entry = {
            "id": data_manager.generate_item_id(route_name),
            "title": request.form["Game Title"],
            "manufacturer": request.form["Manufacturer"],
            "price": request.form["Price"],
            "stock": request.form["Stock"]}

        data_manager.add_new_element_to_database(new_entry, route_name)
        return redirect("/store")
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)


@app.route("/store/update_item", defaults={"id": None}, methods=["GET", "POST"])
@app.route("/store/update_item/<id>", methods=["GET", "POST"])
def update_item_store(id):
    route_name = "store"
    module = "Store"
    if request.method == "GET":
        table_titles = [
            "Game Title",
            "Manufacturer",
            "Price",
            "Stock"]

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
            "title": request.form["Game Title"],
            "manufacturer": request.form["Manufacturer"],
            "price": request.form["Price"],
            "stock": request.form["Stock"]}
        data_manager.update_by_id(entry_details, route_name)
        return redirect("/store")