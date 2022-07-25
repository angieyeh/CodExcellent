-- MariaDB dump 10.19  Distrib 10.4.25-MariaDB, for Linux (x86_64)
--
-- Host: classmysql.engr.oregonstate.edu    Database: cs340_yeha
-- ------------------------------------------------------
-- Server version	10.6.8-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Certificates`
--

DROP TABLE IF EXISTS `Certificates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Certificates` (
  `certificate_id` int(11) NOT NULL AUTO_INCREMENT,
  `certificate_title` varchar(100) NOT NULL,
  `issue_date` date NOT NULL,
  PRIMARY KEY (`certificate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Certificates`
--

LOCK TABLES `Certificates` WRITE;
/*!40000 ALTER TABLE `Certificates` DISABLE KEYS */;
INSERT INTO `Certificates` VALUES (1,'Certificate of Completion','2022-03-17'),(2,'Certificate of Completion','2023-06-17'),(3,'Certificate of Completion','2023-06-17');
/*!40000 ALTER TABLE `Certificates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Course_Instructors`
--

DROP TABLE IF EXISTS `Course_Instructors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Course_Instructors` (
  `course_id` int(11) NOT NULL,
  `instructor_id` int(11) NOT NULL,
  PRIMARY KEY (`course_id`,`instructor_id`),
  KEY `instructor_id_idx` (`course_id`,`instructor_id`),
  KEY `instructor_id_idx1` (`instructor_id`),
  CONSTRAINT `course_id_2` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `instructor_id` FOREIGN KEY (`instructor_id`) REFERENCES `Instructors` (`instructor_id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Course_Instructors`
--

LOCK TABLES `Course_Instructors` WRITE;
/*!40000 ALTER TABLE `Course_Instructors` DISABLE KEYS */;
INSERT INTO `Course_Instructors` VALUES (1,1),(1,4),(3,2),(4,3),(6,3);
/*!40000 ALTER TABLE `Course_Instructors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Courses`
--

DROP TABLE IF EXISTS `Courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Courses` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(200) NOT NULL,
  `level` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Courses`
--

LOCK TABLES `Courses` WRITE;
/*!40000 ALTER TABLE `Courses` DISABLE KEYS */;
INSERT INTO `Courses` VALUES (1,'Intro to Programming','beginner','2023-01-09','2023-03-17',1),(2,'Intro to HTML/CSS and Javascript','beginner','2023-03-09','2023-06-17',1),(3,'Intro to Python','beginner','2022-01-09','2022-03-17',1),(4,'Database Design','intermediate','2022-01-09','2022-03-17',1),(5,'Data Structures','Intermediate','2022-01-09','2022-03-17',0),(6,'Intro to Programming','beginner','2022-01-09','2022-03-17',1);
/*!40000 ALTER TABLE `Courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Instructors`
--

DROP TABLE IF EXISTS `Instructors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Instructors` (
  `instructor_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` char(10) DEFAULT NULL,
  `pronoun` varchar(50) DEFAULT NULL,
  `instructor_title` varchar(50) NOT NULL,
  PRIMARY KEY (`instructor_id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Instructors`
--

LOCK TABLES `Instructors` WRITE;
/*!40000 ALTER TABLE `Instructors` DISABLE KEYS */;
INSERT INTO `Instructors` VALUES (1,'Charlotte Charles','charlottecharles@gmail.com','2025550109','she/her','Teacher'),(2,'Cosima Niehaus','cosima@gmail.com','2025550111',NULL,'Teacher'),(3,'Donny Hendrix','donnyhendrix@gmail.com','2025550110',NULL,'Teacher'),(4,'Robin Scherbatsky','robinscherbatsky@gmail.com','2025550111',NULL,'Teaching Assistant');
/*!40000 ALTER TABLE `Instructors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student_Enrollments`
--

DROP TABLE IF EXISTS `Student_Enrollments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Student_Enrollments` (
  `student_enrollment_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `is_enrolled` tinyint(1) NOT NULL DEFAULT 1,
  `certificate_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`student_enrollment_id`),
  KEY `course_id_idx` (`course_id`),
  KEY `student_id_idx` (`student_id`),
  KEY `certificate_id_idx` (`certificate_id`),
  CONSTRAINT `certificate_id` FOREIGN KEY (`certificate_id`) REFERENCES `Certificates` (`certificate_id`) ON DELETE SET NULL ON UPDATE NO ACTION,
  CONSTRAINT `course_id` FOREIGN KEY (`course_id`) REFERENCES `Courses` (`course_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `student_id` FOREIGN KEY (`student_id`) REFERENCES `Students` (`student_id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student_Enrollments`
--

LOCK TABLES `Student_Enrollments` WRITE;
/*!40000 ALTER TABLE `Student_Enrollments` DISABLE KEYS */;
INSERT INTO `Student_Enrollments` VALUES (1,1,1,1,1),(2,2,1,0,NULL),(3,1,3,0,NULL),(4,2,2,1,2),(5,3,2,1,3),(6,4,2,0,NULL);
/*!40000 ALTER TABLE `Student_Enrollments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` char(10) DEFAULT NULL,
  `pronoun` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES (1,'Chloe Decker','chloedecker@gmail.com','2025550108','she/her'),(2,'Ella Lopez','ellalopez@gmail.com','2025550185','she/her'),(3,'Dan Espinoza','danespinoza@gmail.com','2025550114','he/him'),(4,'Rory Gilmore','rorygilmore@gmail.com','2025555514',NULL);
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-23 22:00:19
