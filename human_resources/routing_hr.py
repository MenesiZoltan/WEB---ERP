from server import app
from flask import render_template, request, redirect
import data_manager


@app.route("/human_resources")
def start_module_human_resources():
    module = "Human Resources"
    route_name = "human_resources"
    return render_template(
        'general.html',
        module=module,
        route_name=route_name)


@app.route("/human_resources/database_content")
def show_hr_table():
    module = "Human Resources"
    table = "hr"
    content = data_manager.get_module_content(table)
    table_titles = [
        "Employee Id",
        "Employee Name",
        "Year of Birth",]

    return render_template(
        "content.html",
        content=content,
        module=module,
        table_titles=table_titles)


@app.route("/human_resources/add_item", methods=["GET", "POST"])
def add_item_hr():
    route_name = "human_resources"
    module = "Human Resources"
    table_titles = [
        "Employee Name",
        "Year of Birth"]

    if request.method == "POST":
        new_entry = {
            "id": data_manager.generate_item_id(route_name),
            "name": request.form["Employee Name"],
            "year_of_birth": request.form["Year of Birth"]}

        data_manager.add_new_element_to_database(new_entry, route_name)
        return redirect("/human_resources")
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)


@app.route("/human_resources/update_item", defaults={"id": None}, methods=["GET", "POST"])
@app.route("/human_resources/update_item/<id>", methods=["GET", "POST"])
def update_item_hr(id):
    route_name = "human_resources"
    module = "Human Resources"
    if request.method == "GET":
        table_titles = [
            "Employee Name",
            "Year of Birth"]

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
            "name": request.form["Employee Name"],
            "year_of_birth": request.form["Year of Birth"]}

        data_manager.update_by_id(entry_details, route_name)
        return redirect("/human_resources")