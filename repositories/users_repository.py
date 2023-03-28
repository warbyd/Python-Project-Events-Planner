from db.run_sql import run_sql
from models.user import User
from models.event import Event

def save(user):
    sql = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s) RETURNING id"
    values = [user.name, user.email, user.phone]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['email'], row['phone'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = User(result['name'], result['email'], result['phone'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    sql = "UPDATE users SET (name, email, phone) = (%s, %s, %s) WHERE id = %s"
    values = [user.name, user.email, user.phone, user.id]
    run_sql(sql, values)
    
def select_with_events(id):
    user = None
    sql = """SELECT users.id, users.name, users.email, users.phone,
                    events.id AS event_id, events.title, events.location, events.date, events.start_time, events.end_time, events.description
             FROM users 
             JOIN events ON users.id = events.user_id
             WHERE users.id = %s"""
    values = [id]
    results = run_sql(sql, values)
    events = []
    for row in results:
        if user is None:
            user = User(row['name'], row['email'], row['phone'], row['id'])
        event = Event(row['title'], row['location'], row['date'], row['start_time'], row['end_time'], row['description'], row['event_id'])
        events.append(event)
    if user is not None:
        user.events = events
    return user





