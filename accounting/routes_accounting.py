from server import app
from flask import render_template, request, redirect
import data_manager

@app.route("/accounting")
def start_module_accounting():
    module = "Accounting"
    route_name = "accounting"
    return render_template(
        'general.html',
        module=module,
        route_name=route_name)


@app.route("/accounting/database_content")
def show_accounting_table():
    module = "Accounting"
    table = "accounting"
    content = data_manager.get_module_content(table)
    table_titles = [
        "Transaction ID",
        "Transaction Month",
        "Transaction Day",
        "Transaction Year",
        "Transaction Type",
        "Transaction Value"]

    return render_template(
        "content.html",
        content=content,
        module=module,
        table_titles=table_titles)


@app.route("/accounting/add_item", methods=["GET", "POST"])
def add_item_accounting():
    route_name = "accounting"
    module = "Accounting"
    table_titles = [
        "Transaction Month",
        "Transaction Day",
        "Transaction Year",
        "Transaction Type",
        "Transaction Value"]

    if request.method == "POST":
        new_entry = {
            "id": data_manager.generate_item_id(route_name),
            "month": request.form["Transaction Month"],
            "day": request.form["Transaction Day"],
            "year": request.form["Transaction Year"],
            "type": request.form["Transaction Type"],
            "value": request.form["Transaction Value"]}
        data_manager.add_new_element_to_database(new_entry, route_name)
        return redirect("/accounting")
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)