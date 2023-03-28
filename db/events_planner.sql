-- DROP TABLE IF EXISTS tasks;
-- DROP TABLE IF EXISTS events;
-- DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NOT NULL
);


CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  location VARCHAR(255) NOT NULL,
  date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  description TEXT,
  user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description TEXT NOT NULL,
  completed BOOLEAN DEFAULT FALSE,
  event_id INT NOT NULL REFERENCES events(id) ON DELETE CASCADE
);

INSERT INTO events (title, location, date, start_time, end_time, description)
VALUES ('Birthday Party', '123 Main St', '2023-04-15', '14:00', '16:00', 'Celebrate with family and friends');

INSERT INTO events (title, location, date, start_time, end_time, description)
VALUES ('Board Meeting', '456 Oak Ave', '2023-05-01', '09:00', '11:00', 'Discuss quarterly finances');

INSERT INTO events (title, location, date, start_time, end_time, description)
VALUES ('Team Building Event', '789 Elm St', '2023-05-15', '10:00', '15:00', 'Activities to build team morale');

INSERT INTO events (title, location, date, start_time, end_time, description)
VALUES ('Product Launch', '555 Pine Ave', '2023-06-01', '19:00', '22:00', 'Announce new product line');

INSERT INTO events (title, location, date, start_time, end_time, description)
VALUES ('Charity Fundraiser', '888 Broadway', '2023-06-15', '17:00', '21:00', 'Raising funds for local charity');

INSERT INTO events (title, location, date, start_time, end_time, description)
VALUES ('Conference', '222 Park Blvd', '2023-07-01', '08:00', '17:00', 'Industry experts discussing latest trends');

INSERT INTO events (title, location, date, start_time, end_time, description)
VALUES ('Networking Event', '444 Maple St', '2023-07-15', '18:00', '21:00', 'Opportunity to meet industry peers');

INSERT INTO events (title, location, date, start_time, end_time, description)
VALUES ('Holiday Party', '777 Lakeview Dr', '2023-12-20', '18:00', '22:00', 'Celebrate the holiday season with colleagues');


INSERT INTO users (name, email, phone)
VALUES ('John Doe', 'john.doe@example.com', '555-1234');

INSERT INTO users (name, email, phone)
VALUES ('Jane Smith', 'jane.smith@example.com', '555-5678');

INSERT INTO users (name, email, phone)
VALUES ('Bob Johnson', 'bob.johnson@example.com', '555-2468');

INSERT INTO users (name, email, phone)
VALUES ('Emily Lee', 'emily.lee@example.com', '555-3690');

INSERT INTO users (name, email, phone)
VALUES ('David Chen', 'david.chen@example.com', '555-8024');

INSERT INTO users (name, email, phone)
VALUES ('Karen Kim', 'karen.kim@example.com', '555-9753');

INSERT INTO users (name, email, phone)
VALUES ('Chris Brown', 'chris.brown@example.com', '555-3847');

INSERT INTO users (name, email, phone)
VALUES ('Amy Lee', 'amy.lee@example.com', '555-7192');

INSERT INTO events (title, location, date, start_time, end_time, description, user_id)
VALUES ('John’s Birthday Party', '123 Main St', '2023-06-10', '18:00', '22:00', 'Celebrate John’s birthday with food, drinks and music!', 1);

INSERT INTO events (title, location, date, start_time, end_time, description, user_id)
VALUES ('Alice and Bob’s Wedding', '456 Oak Ave', '2023-07-15', '14:00', '20:00', 'Join us for the wedding of Alice and Bob with dinner and dancing', 2);

INSERT INTO events (title, location, date, start_time, end_time, description, user_id)
VALUES ('Girls’ Night Out', '789 Elm St', '2023-08-01', '18:00', '22:00', 'Let’s have fun together with drinks and karaoke!', 3);

INSERT INTO events (title, location, date, start_time, end_time, description, user_id)
VALUES ('Graduation Party', '555 Pine Ave', '2023-08-15', '12:00', '16:00', 'Celebrate the graduation of our friend with food, drinks and games!', 4);

INSERT INTO events (title, location, date, start_time, end_time, description, user_id)
VALUES ('Boys’ Night Out', '888 Broadway', '2023-12-15', '19:00', '23:00', 'Guys, let’s hang out and have some fun with beers and pool!', 5);

INSERT INTO events (title, location, date, start_time, end_time, description, user_id)
VALUES ('Family Reunion', '222 Park Blvd', '2024-01-15', '10:00', '18:00', 'Gather with family members and enjoy a day of fun and games!', 6);

INSERT INTO events (title, location, date, start_time, end_time, description, user_id)
VALUES ('Sorority Reunion', '444 Maple St', '2024-03-01', '18:00', '22:00', 'Let’s catch up and reminisce with fellow sorority sisters!', 7);

INSERT INTO events (title, location, date, start_time, end_time, description, user_id)
VALUES ('Game Night', '777 Lakeview Dr', '2024-05-20', '19:00', '23:00', 'Come over and have some fun playing board games and eating snacks!', 8);

ALTER TABLE users RENAME COLUMN id TO users_id;

INSERT INTO tasks (description, completed, event_id)
VALUES ('Buy decorations', false, 17);

INSERT INTO tasks (description, completed, event_id)
VALUES ('Prepare food', false, 18);

INSERT INTO tasks (description, completed, event_id)
VALUES ('Buy flowers', false, 19);

INSERT INTO tasks (description, completed, event_id)
VALUES ('Confirm guest list', false, 20);

INSERT INTO tasks (description, completed, event_id)
VALUES ('Choose karaoke songs', false, 21);

INSERT INTO tasks (description, completed, event_id)
VALUES ('Buy graduation cap and gown', false, 22);

INSERT INTO tasks (description, completed, event_id)
VALUES ('Create reunion slideshow', false, 23);

INSERT INTO tasks (description, completed, event_id)
VALUES ('Buy snacks and drinks', false, 24);
