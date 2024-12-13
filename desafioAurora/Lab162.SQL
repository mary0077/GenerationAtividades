CREATE TABLE RESTART (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(255),
    restart_city VARCHAR(100),
    graduation_date DATETIME
);

INSERT INTO RESTART (student_id, student_name, restart_city, graduation_date)
VALUES
(1, 'Ana', 'São Paulo', '2024-06-15 10:00:00'),
(2, 'João', 'Rio de Janeiro', '2024-06-16 11:30:00'),
(3, 'Carlos', 'Curitiba', '2024-06-17 09:00:00'),
(4, 'Mariana', 'Recife', '2024-06-18 15:45:00'),
(5, 'Pedro', 'Porto Alegre', '2024-06-19 14:00:00'),
(6, 'Juliana', 'Fortaleza', '2024-06-20 08:30:00'),
(7, 'Bruno', 'Manaus', '2024-06-21 13:20:00'),
(8, 'Clara', 'Belo Horizonte', '2024-06-22 16:50:00'),
(9, 'Lucas', 'Florianópolis', '2024-06-23 10:15:00'),
(10, 'Fernanda', 'Salvador', '2024-06-24 12:40:00');

SELECT * FROM RESTART;


CREATE TABLE CLOUD_PRACTITIONER (
    student_id INT PRIMARY KEY,
    certification_date DATETIME
);

INSERT INTO CLOUD_PRACTITIONER (student_id, certification_date)
VALUES
(1, '2024-07-01 09:00:00'),
(2, '2024-07-02 10:30:00'),
(3, '2024-07-03 11:00:00'),
(4, '2024-07-04 14:15:00'),
(5, '2024-07-05 15:45:00');

SELECT * FROM CLOUD_PRACTITIONER;

-- Exibir os dados combinados das duas tabelas
SELECT R.student_id, R.student_name, C.certification_date
FROM RESTART R
INNER JOIN CLOUD_PRACTITIONER C
ON R.student_id = C.student_id;

