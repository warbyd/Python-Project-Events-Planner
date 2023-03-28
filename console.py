import pdb
from models.event import Event
from models.task import Task
from models.user import User
import repositories.event_repository as event_repository
import repositories.tasks_repository as task_repository
import repositories.users_repository as user_repository


task_repository.delete_all()
event_repository.delete_all()
user_repository.delete_all()

user1 = User("John Smith", "john.smith@example.com", "555-1234")
user_repository.save(user1)

user2 = User("Jane Doe", "jane.doe@example.com", "555-5678")
user_repository.save(user2)

event1 = Event("Birthday Party", "My House", "2022-05-10", "14:00", "18:00", "Come celebrate my birthday with me!", user1)
event_repository.save(event1)

event2 = Event("Graduation Ceremony", "University of Glasgow", "2022-06-23", "10:00", "12:00", "Come see me walk across the stage!", user2)
event_repository.save(event2)

task1 = Task("Buy balloons", False, event1)
task_repository.save(task1)

task2 = Task("Send invitations", False, event1)
task_repository.save(task2)

task3 = Task("Pick up gown", False, event2)
task_repository.save(task3)

task4 = Task("Make dinner reservations", False, event2)
task_repository.save(task4)

pdb.set_trace()



