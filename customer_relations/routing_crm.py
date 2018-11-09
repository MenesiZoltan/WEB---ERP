from server import app
from flask import render_template, request, redirect
import data_manager


@app.route("/crm")
def start_module_crm():
    module = "Customer Relations Management"
    route_name = "crm"
    return render_template(
        'general.html',
        module=module,
        route_name=route_name)


@app.route("/crm/database_content")
def show_crm_table():
    module = "Customer Relations Management"
    table = "crm"
    content = data_manager.get_module_content(table)
    table_titles = [
        "Customer ID",
        "Customer Name",
        "Customer E-mail",
        "Customer Subscription"]

    return render_template(
        "content.html",
        content=content,
        module=module,
        table_titles=table_titles)


@app.route("/crm/add_item", methods=["GET", "POST"])
def add_item_crm():
    route_name = "crm"
    module = "Customer Relations Management"
    table_titles = [
        "Customer Name",
        "Customer E-mail",
        "Customer Subscription"]

    if request.method == "POST":
        new_entry = {
            "id": data_manager.generate_item_id(route_name),
            "name": request.form["Customer Name"],
            "email": request.form["Customer E-mail"],
            "subscription": request.form["Customer Subscription"]}
        data_manager.add_new_element_to_database(new_entry, route_name)
        return redirect("/crm")
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)


@app.route("/crm/update_item", defaults={"id": None}, methods=["GET", "POST"])
@app.route("/crm/update_item/<id>", methods=["GET", "POST"])
def update_item_crm(id):
    route_name = "crm"
    module = "Customer Relations Management"
    if request.method == "GET":
        table_titles = [
            "Customer Name",
            "Customer E-mail",
            "Customer Subscription"]

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
            "name": request.form["Customer Name"],
            "email": request.form["Customer E-mail"],
            "subscription": request.form["Customer Subscription"]}

        data_manager.update_by_id(entry_details, route_name)
        return redirect("/crm")

@app.route("/crm/delete_item", methods=["POST"])
def delete_item_crm():
    route_name = "crm"
    item_id = request.form["item_id"]
    data_manager.delete_item_by_id(item_id, route_name)
    return redirect("/crm")