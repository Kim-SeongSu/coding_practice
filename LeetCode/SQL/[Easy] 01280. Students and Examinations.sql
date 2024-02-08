# MySQL  &  postgreSQL
SELECT stu.student_id, stu.student_name, sub.subject_name, COALESCE(COUNT(ex.subject_name),0) AS attended_exams
FROM Students stu
    CROSS JOIN Subjects sub
    LEFT JOIN Examinations ex
    ON  stu.student_id = ex.student_id and sub.subject_name = ex.subject_name
GROUP BY stu.student_id, stu.student_name, sub.subject_name
ORDER BY stu.student_id
