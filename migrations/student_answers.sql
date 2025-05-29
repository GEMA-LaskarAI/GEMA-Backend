CREATE TABLE gema_student_answers (
    id SERIAL PRIMARY KEY,
    student_id INT,
    question_id INT,
    score INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);