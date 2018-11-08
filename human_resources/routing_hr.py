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