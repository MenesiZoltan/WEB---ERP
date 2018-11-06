from server import app
from flask import render_template, request
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
        "Transaction ID",
        "Transaction Month",
        "Transaction Day",
        "Transaction Year",
        "Transaction Type",
        "Transaction Value"]

    if request.method == "POST":
        pass
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)