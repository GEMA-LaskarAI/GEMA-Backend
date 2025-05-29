CREATE TABLE gema_question_major_weights (
    id SERIAL PRIMARY KEY,
    question_id INT,
    major_id INT,
    weight INT
);