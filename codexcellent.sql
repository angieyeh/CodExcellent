-- phpMyAdmin SQL Dump
-- version 5.2.0-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 04, 2022 at 11:23 PM
-- Server version: 10.6.8-MariaDB-log
-- PHP Version: 7.4.30

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_fishebeg`
--

-- --------------------------------------------------------

--
-- Table structure for table `Certificates`
--

DROP TABLE IF EXISTS `Certificates`;
CREATE TABLE `Certificates` (
  `certificate_id` int(11) NOT NULL,
  `certificate_title` varchar(100) NOT NULL,
  `issue_date` date NOT NULL,
  `student_enrollment_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- RELATIONSHIPS FOR TABLE `Certificates`:
--   `student_enrollment_id`
--       `Student_Enrollments` -> `student_enrollment_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `Courses`
--

DROP TABLE IF EXISTS `Courses`;
CREATE TABLE `Courses` (
  `course_id` int(11) NOT NULL,
  `course_name` varchar(200) NOT NULL,
  `level` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- RELATIONSHIPS FOR TABLE `Courses`:
--

--
-- Dumping data for table `Courses`
--

INSERT INTO `Courses` (`course_id`, `course_name`, `level`, `start_date`, `end_date`, `status`) VALUES
(1, 'Intro to Programming', 'beginner', '2023-01-09', '2023-03-17', 1),
(2, 'Intro to HTML/CSS and Javascript', 'beginner', '2023-03-09', '2023-06-17', 1),
(3, 'Intro to Python', 'beginner', '2022-01-09', '2022-03-17', 1),
(4, 'Database Design', 'intermediate', '2022-01-09', '2022-03-17', 1),
(5, 'Data Structures', 'intermediate', '2022-01-09', '2022-03-17', 0),
(6, 'Web Development', 'intermediate', '2022-01-09', '2022-03-17', 1),
(7, 'Intro to Programming', 'beginner', '2023-01-09', '2023-03-17', 0),
(8, 'Intro to Mobile Development', 'beginner', '2022-07-27', '2022-11-02', 1),
(9, 'Intro to Mobile Development', 'advanced', '2022-07-29', '2022-12-16', 0),
(10, 'Intro to Mobile Development', 'Intermediate', '2022-07-30', '2022-07-29', 0);

-- --------------------------------------------------------

--
-- Table structure for table `Course_Instructors`
--

DROP TABLE IF EXISTS `Course_Instructors`;
CREATE TABLE `Course_Instructors` (
  `course_id` int(11) NOT NULL,
  `instructor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- RELATIONSHIPS FOR TABLE `Course_Instructors`:
--   `course_id`
--       `Courses` -> `course_id`
--   `instructor_id`
--       `Instructors` -> `instructor_id`
--

--
-- Dumping data for table `Course_Instructors`
--

INSERT INTO `Course_Instructors` (`course_id`, `instructor_id`) VALUES
(1, 1),
(1, 4),
(2, 1),
(3, 2),
(4, 3),
(6, 3);

-- --------------------------------------------------------

--
-- Table structure for table `Instructors`
--

DROP TABLE IF EXISTS `Instructors`;
CREATE TABLE `Instructors` (
  `instructor_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` char(10) DEFAULT NULL,
  `pronoun` varchar(50) DEFAULT NULL,
  `instructor_title` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- RELATIONSHIPS FOR TABLE `Instructors`:
--

--
-- Dumping data for table `Instructors`
--

INSERT INTO `Instructors` (`instructor_id`, `name`, `email`, `phone_number`, `pronoun`, `instructor_title`) VALUES
(1, 'Charlotte Charles', 'charlottecharles@gmail.com', '2025550109', 'she/her', 'Teacher'),
(2, 'Cosima Niehaus', 'cosima@gmail.com', '2025550111', NULL, 'Teacher'),
(3, 'Donny Hendrix', 'donnyhendrix@gmail.com', '2025550110', NULL, 'Teacher'),
(4, 'Robin Scherbatsky', 'robinscherbatsky@gmail.com', '2025550111', NULL, 'Teaching Assistant');

-- --------------------------------------------------------

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
CREATE TABLE `Students` (
  `student_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` char(10) DEFAULT NULL,
  `pronoun` varchar(50) DEFAULT NULL,
  `tutor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- RELATIONSHIPS FOR TABLE `Students`:
--   `tutor_id`
--       `Instructors` -> `instructor_id`
--

-- --------------------------------------------------------

--
-- Table structure for table `Student_Enrollments`
--

DROP TABLE IF EXISTS `Student_Enrollments`;
CREATE TABLE `Student_Enrollments` (
  `student_enrollment_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `is_enrolled` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- RELATIONSHIPS FOR TABLE `Student_Enrollments`:
--   `course_id`
--       `Courses` -> `course_id`
--   `student_id`
--       `Students` -> `student_id`
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Certificates`
--
ALTER TABLE `Certificates`
  ADD PRIMARY KEY (`certificate_id`),
  ADD KEY `student_enrollment_id_idx` (`student_enrollment_id`);

--
-- Indexes for table `Courses`
--
ALTER TABLE `Courses`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `Course_Instructors`
--
ALTER TABLE `Course_Instructors`
  ADD PRIMARY KEY (`course_id`,`instructor_id`),
  ADD KEY `instructor_id_idx` (`course_id`,`instructor_id`),
  ADD KEY `instructor_id_idx1` (`instructor_id`);

--
-- Indexes for table `Instructors`
--
ALTER TABLE `Instructors`
  ADD PRIMARY KEY (`instructor_id`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`);

--
-- Indexes for table `Students`
--
ALTER TABLE `Students`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`),
  ADD KEY `tutor_id_idx` (`tutor_id`);

--
-- Indexes for table `Student_Enrollments`
--
ALTER TABLE `Student_Enrollments`
  ADD PRIMARY KEY (`student_enrollment_id`),
  ADD KEY `course_id_idx` (`course_id`),
  ADD KEY `student_id_idx` (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Certificates`
--
ALTER TABLE `Certificates`
  MODIFY `certificate_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `Courses`
--
ALTER TABLE `Courses`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `Instructors`
--
ALTER TABLE `Instructors`
  MODIFY `instructor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `Students`
--
ALTER TABLE `Students`
  MODIFY `student_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `Student_Enrollments`
--
ALTER TABLE `Student_Enrollments`
  MODIFY `student_enrollment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Certificates`
--
ALTER TABLE `Certificates`
  ADD CONSTRAINT `student_enrollment_id` FOREIGN KEY (`student_enrollment_id`) REFERENCES `Student_Enrollments` (`student_enrollment_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `Course_Instructors`
--
ALTER TABLE `Course_Instructors`
  ADD CONSTRAINT `course_id_2` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `instructor_id` FOREIGN KEY (`instructor_id`) REFERENCES `Instructors` (`instructor_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `Students`
--
ALTER TABLE `Students`
  ADD CONSTRAINT `tutor_id` FOREIGN KEY (`tutor_id`) REFERENCES `Instructors` (`instructor_id`);

--
-- Constraints for table `Student_Enrollments`
--
ALTER TABLE `Student_Enrollments`
  ADD CONSTRAINT `course_id` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `student_id` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE ON UPDATE NO ACTION;
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
