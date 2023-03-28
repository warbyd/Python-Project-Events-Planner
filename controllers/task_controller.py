from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.task import Task
import repositories.tasks_repository as task_repository
import repositories.event_repository as event_repository

tasks_blueprint = Blueprint("tasks", __name__)

# INDEX
# GET '/tasks'
# INDEX
# GET '/tasks'
@tasks_blueprint.route("/tasks")
def tasks():
    sort_by = request.args.get("sort_by")
    # tasks = task_repository.select_all()
    tasks = task_repository.get_tasks_sorted_by_due_date()

    if sort_by == "event":
        tasks.sort(key=lambda x: x.event_id.date)
    elif sort_by == "incomplete_tasks":
        tasks.sort(key=lambda x: (x.event_id.date, x.completed))

    return render_template("tasks/index.html", tasks=tasks)



@tasks_blueprint.route('/tasks/new')
def new_task():
    events = event_repository.select_all()  # fetch all events
    return render_template('tasks/new.html', events=events)


@tasks_blueprint.route("/tasks", methods=['POST'])
def create_task():
    description = request.form['description']
    event_id = request.form['event']
    task = Task(description, False, event_id)
    task_repository.save(task)
    return redirect('/tasks')


# DELETE
# DELETE '/tasks/<id>'
@tasks_blueprint.route("/tasks/<id>/delete", methods=['POST'])
def delete_task(id):
    task_repository.delete(id)
    return redirect('/tasks')


# @tasks_blueprint.route("/tasks/<id>/update", methods=['POST'])
# def update_task(id):
#     task = task_repository.select(id)
#     print(task.__dict__)
#     if task:
#         completed = request.form.get('completed') == 'True'
#         task.description = request.form.get('description')
#         task.completed = completed
#         task_repository.update(task)
#     return redirect('/tasks')

# @tasks_blueprint.route("/tasks/<id>/update", methods=['POST'])
# def update_task(id):
#     task = task_repository.select(id)
#     print(task.__dict__)
#     if task:
#         completed = request.form.get('completed') == 'True'
#         task.completed = completed
#         task_repository.update(task)
#     return redirect('/tasks')

@tasks_blueprint.route("/tasks/<id>/update", methods=['POST'])
def update_task(id):
    task = task_repository.select(id)
    if task:
        if 'description' in request.form:
            # Update task description
            completed = request.form.get('completed') == 'True'
            task.description = request.form.get('description')
            task.completed = completed
            task_repository.update(task)
            return redirect('/tasks')
        else:
            # Update task status
            task.completed = not task.completed
            task_repository.update(task)
            return redirect('/tasks')
    else:
        return redirect('/tasks')





@tasks_blueprint.route("/tasks/sort-by-due-date")
def sort_tasks_by_due_date():
    tasks = task_repository.get_tasks_sorted_by_due_date()
    return render_template("tasks/index.html", tasks=tasks)

@tasks_blueprint.route("/tasks/sort-by-due-date")
def sort_tasks_by_status(status):
    tasks = task_repository.get_tasks_sorted_by_status(status)
    return render_template("tasks/index.html", tasks=tasks)

@tasks_blueprint.route("/tasks/sort", methods=['POST'])
def sort_tasks():

    sort_by = request.form.get("sort_by")
    if sort_by == "event_date":
        return sort_tasks_by_due_date()
    elif sort_by == "status_incomplete":
        return sort_tasks_by_status("incomplete")
    elif sort_by == "status_complete":
        return sort_tasks_by_status("complete")
    
@tasks_blueprint.route("/tasks/<id>/edit")
def edit_task(id):
    task = task_repository.select(id)
    events = event_repository.select_all()  # fetch all events
    return render_template("tasks/edit.html", task=task, events=events)





      





