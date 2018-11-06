from server import app
from flask import render_template, request
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
        "Employee Id",
        "Employee Name",
        "Year of Birth",]

    if request.method == "POST":
        pass
    return render_template(
        "item.html",
        route_name=route_name,
        module=module,
        table_titles=table_titles)