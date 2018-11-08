from server import app
from flask import render_template, request, redirect
import data_manager

@app.route("/sales")
def start_module_sales():
    module = "Sales"
    route_name = "sales"

    return render_template(
        'general.html',
        module=module,
        route_name=route_name)


@app.route("/sales/database_content")
def show_sales_table():
    module = "Sales"
    table = "sales"
    content = data_manager.get_module_content(table)
    table_titles = [
        "ID",
        "Title of Game Sold",
        "Price",
        "Month of Sale",
        "Day of Sale",
        "Year of Sale",
        "Customer ID"]

    return render_template(
        "content.html",
        content=content,
        module=module,
        table_titles=table_titles)


@app.route("/sales/add_item", methods=["GET", "POST"])
def add_item_sales():
    route_name = "sales"
    module = "Sales"
    table_titles = [
        "Title of Game Sold",
        "Price",
        "Month of Sale",
        "Day of Sale",
        "Year of Sale",
        "Customer ID"]

    if request.method == "POST":
        new_entry = {
            "id": data_manager.generate_item_id(route_name),
            "title": request.form["Title of Game Sold"],
            "price": request.form["Price"],
            "month": request.form["Month of Sale"],
            "day": request.form["Day of Sale"],
            "year": request.form["Year of Sale"],
            "customer_id": request.form["Customer ID"]}

        data_manager.add_new_element_to_database(new_entry, route_name)
        return redirect("/sales")
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)