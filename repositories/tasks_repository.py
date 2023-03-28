from db.run_sql import run_sql

from models.task import Task
import repositories.event_repository as event_repository


def save(task):
    sql = "INSERT INTO tasks(description, completed, event_id) VALUES (%s, %s, %s) RETURNING id"
    values = [task.description, task.completed, task.event_id]
    results = run_sql(sql, values)
    task.id = results[0]['id']
    return task


def select_all():
    tasks = []

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        event = event_repository.select(row['event_id'])
        task = Task(row['description'], row['completed'], event.id, row['id'])
        tasks.append(task)

    return tasks


def select(id):
    task = None

    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        event = event_repository.select(result['event_id'])
        task = Task(result['description'], result['completed'], event.id, result['id'])

    return task


def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(task):
    print (f"Updated Task: {task}")
    sql = "UPDATE tasks SET description = %s, completed = %s, event_id = %s WHERE id = %s"
    values = [task.description, task.completed, task.event_id, task.id]
    print (f"Values: {values}")
    run_sql(sql, values)



def get_tasks_for_event(event_id):
    tasks = []

    sql = "SELECT * FROM tasks WHERE event_id = %s"
    values = [event_id]
    results = run_sql(sql, values)

    for row in results:
        event = event_repository.select(event_id)
        task = Task(row['description'], row['completed'], row['id'], row['event_id'])
        tasks.append(task)

    return tasks

def get_tasks_sorted_by_due_date():
    tasks = []

    sql = """SELECT t.*
    FROM tasks t
    JOIN events e
    ON t.event_id = e.id
    ORDER BY e.date ASC"""
    results = run_sql(sql)

    for row in results:
        event = event_repository.select(row['event_id'])
        task = Task(row['description'], row['completed'], event, row['id'])
        tasks.append(task)

    return tasks

def get_tasks_sorted_by_status(status):
    if status == "incomplete":
        sort_order = "ASC"
    else: 
        sort_order = "DESC"

    tasks = []

    sql = f"SELECT * FROM TASKS ORDER BY completed {sort_order}"

    results = run_sql(sql)

    for row in results:
        event = event_repository.select(row['event_id'])
        task = Task(row['description'], row['completed'], event, row['id'])
        tasks.append(task)
    
    return tasks

def remove_completed_tasks_from_event(event_id):
    sql = "DELETE FROM tasks WHERE event_id = %s AND completed = true"
    values = [event_id]
    run_sql(sql, values)





     
