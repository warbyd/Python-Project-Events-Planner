from datetime import datetime
from db.run_sql import run_sql
from models.event import Event
from models.user import User

# CREATE
def save(event):
    sql = "INSERT INTO events(title, location, date, start_time, end_time, description, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [event.title, event.location, event.date, event.start_time, event.end_time, event.description, event.user_id]
    results = run_sql(sql, values)
    event.id = results[0]['id']
    return event

def select_all():
    events = []

    sql = "SELECT events.*, users.name, users.email FROM events JOIN users ON events.user_id = users.id"
    results = run_sql(sql)
    for row in results:
        user = User(row['user_id'], row['name'], row['email'])
        event = Event(row['id'], row['title'], row['location'], row['date'], row['start_time'], row['end_time'], row['description'], user)
        events.append(event)
    return events


def select(id):
    event = None
    sql = "SELECT * FROM events WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        event = Event(result['id'], result['title'], result['location'], result['date'], result['start_time'], result['end_time'], result['description'], result['user_id'])
    return event

# UPDATE
def update(event):
    sql = "UPDATE events SET title = %s, location = %s, date = %s, start_time = %s, end_time = %s, description = %s, user_id = %s WHERE id = %s"
    values = [event.title, event.location, event.date, event.start_time, event.end_time, event.description, event.user_id, event.id]
    run_sql(sql, values)

# DELETE
def delete_all():
    sql = "DELETE FROM events"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM events WHERE id = %s"
    values = [id]
    run_sql(sql, values)

   

def get_upcoming_events(n):
    events = select_all()
    now = datetime.now()
    upcoming_events = []

    for event in events:
        event_date = datetime.combine(event.date, datetime.min.time())
        if event_date > now:
            upcoming_events.append(event)

    return sorted(upcoming_events, key=lambda x: x.date)[:n]



