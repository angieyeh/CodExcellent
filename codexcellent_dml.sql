---------------STUDENTS---------------
-- get all student_ids, names, emails, phone_numbers, pronouns to populate the Students UI
SELECT student_id , name, email, phone_number, pronoun, tutor_id FROM Students;
-- add a new Student
INSERT INTO Students (name, email, phone_number, pronoun, tutor_id) VALUES
(:name_input, :email_input, :phone_number_input, :pronoun_input, :tutor_id_from_dropdown);
-- update student data


---------------INSTRUCTORS---------------
-- get all instructor_ids, names, emails, phone_numbers, instructor_titles, pronouns to populate the Instructors UI
SELECT instructor_id , name, email, phone_number, instructor_title, pronoun FROM Instructors;
-- add a new Instructor
INSERT INTO Instructors (name, email, phone_number, instructor_title, pronoun) VALUES 
(:name_input, :email_input, :phone_number_input, :instructor_title_input_from_dropdown, :pronoun_input);
-- delete a instructor to trigger CASCADE delete in Course_Instructors (M-to-M relationship)
DELETE FROM Instructors WHERE instructor_id = :instructor_id_input;

---------------COURSES---------------
-- get all course_ids, course_names, levels, start_dates, end_dates, statuses to populate the Courses UI
SELECT course_id , course_name, level, start_date, end_date, status FROM Courses;
-- Search a course by course name
SELECT course_id , course_name, level, start_date, end_date, status FROM Courses WHERE course_name = :course_name_input_from_dropdown;
-- add a new Course
INSERT INTO Courses (course_name, level, start_date, end_date, status) VALUES 
(:course_names_input, :level_input_from_dropdown, :start_date_input, :end_date_input, :status_input_from_dropdown);

---------------CERTIFICATES---------------
-- get all certificate_id , student_name, course_name, certificate_title, issue_date to populate the Certificates UI
SELECT cert.certificate_id , st.name as student_name, co.course_name, cert.certificate_title, cert.issue_date 
	FROM Certificates cert
	INNER JOIN Student_Enrollments se ON cert.student_enrollment_id = se.student_enrollment_id
	INNER JOIN Students st ON se.student_id = st.student_id
	INNER JOIN Courses co ON se.course_id = co.course_id;
-- add a new Certificate
INSERT INTO Certificates (certificate_title, issue_date ) VALUES 
(:certificate_title_input, :issue_date_input);

---------------STUDENT_ENROLLMENT---------------
-- get all student_enrollment_ids , student_ids	, course_ids to populate the Student_Enrollments UI
SELECT se.student_enrollment_id , st.student_id, st.name as student_name, co.course_id, co.course_name, co.start_date as course_start_date, co.end_date as course_end_date, se.is_enrolled
	FROM Student_Enrollments se
	INNER JOIN Students st ON se.student_id = st.student_id
	INNER JOIN Courses co ON se.course_id = co.course_id;
-- retrieve the information of the student being up updated
SELECT student_enrollment_id, student_id, course_id, is_enrolled
	FROM Student_Enrollments 
	WHERE student_enrollment_id = :student_enrollment_id_input;
-- check if a Student_Enrollment already exists
SELECT EXISTS(SELECT 1 FROM Student_Enrollments WHERE student_id = :student_id_input AND course_id = :course_id_input) AS se_exists;
-- associate a student with a course enrollment (M-to-M relationship addition)
INSERT INTO Student_Enrollments (student_id, course_id ) VALUES 
(:student_id_input, :course_id_input);
-- update a student_enrollment's data based on submission of the Update Certificates form 
UPDATE Student_Enrollment SET student_id = :student_id_input, course_id = :course_id_input, is_enrolled = :is_enrolled_input
	WHERE student_enrollment_id = :student_enrollment_id_input;
-- delete a student_enrollment and not cause a data anomaly in the entities associated with student_enrollments (M-to-M relationship)
DELETE FROM Student_Enrollments WHERE student_enrollment_id = :student_enrollment_id_input;

---------------COURSE_INSTRUCTORS---------------
-- join Courses and Instructors tables to this table so that we can output course_name and instructor's name
SELECT Course_Instructors.course_id, Courses.course_name, Course_Instructors.instructor_id, Instructors.name, Instructor.instructor_title
FROM Course_Instructors
JOIN Courses ON Course_Instructors.course_id = Courses.course_id
JOIN Instructors ON Course_Instructors.instructor_id = Instructors.instructor_id;
-- associate a course with a instructor (M-to-M relationship addition)
INSERT INTO Course_Instructors (course_id, instructor_id) VALUES
(:course_id_input_from_dropdown, :instructor_id_input_from_dropdown);
