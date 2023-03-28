from flask import Flask, render_template
from repositories import event_repository
from repositories import tasks_repository
from controllers.task_controller import tasks_blueprint
from controllers.event_controller import events_blueprint
from controllers.user_controller import users_blueprint

app = Flask(__name__)

app.register_blueprint(tasks_blueprint)
app.register_blueprint(events_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    upcoming_events = event_repository.get_upcoming_events(3)
    tasks_for_events = {}
    for event in upcoming_events:
        tasks_for_event = tasks_repository.get_tasks_for_event(event.id)
        tasks_for_events[event.id] = tasks_for_event
    return render_template('index.html', events=upcoming_events, tasks_for_events=tasks_for_events)





if __name__ == '__main__':
    app.run(debug=True)

