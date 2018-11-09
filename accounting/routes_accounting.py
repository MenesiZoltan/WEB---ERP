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
        table_titles=table_titles,
        page_action="ADD")

@app.route("/accounting/update_item", defaults={"id": None}, methods=["GET", "POST"])
@app.route("/accounting/update_item/<id>", methods=["GET", "POST"])
def update_item_accounting(id):
    route_name = "accounting"
    module = "Accounting"
    if request.method == "GET":
        table_titles = [
            "Transaction Month",
            "Transaction Day",
            "Transaction Year",
            "Transaction Type",
            "Transaction Value"]
        item_id = str(request.args.get("item_id"))
        print(item_id)
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
            "month": request.form["Transaction Month"],
            "day": request.form["Transaction Day"],
            "year": request.form["Transaction Year"],
            "type": request.form["Transaction Type"],
            "value": request.form["Transaction Value"]}
        data_manager.update_by_id(entry_details, route_name)
        print(entry_details)
        return redirect("/accounting")

@app.route("/accounting/delete_item", methods=["POST"])
def delete_item_accoounting():
    route_name = "accounting"
    item_id = request.form["item_id"]
    data_manager.delete_item_by_id(item_id, route_name)
    return redirect("/accounting")


