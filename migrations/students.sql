CREATE TABLE gema_students (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    password TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);