-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2025 at 02:14 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pydb_new`
--

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `id` int(11) NOT NULL,
  `class_name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `schedule` varchar(255) NOT NULL,
  `max_students` int(11) NOT NULL,
  `trainer_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`id`, `class_name`, `description`, `schedule`, `max_students`, `trainer_id`) VALUES
(1, 'Competition Gym', 'A class for bodybuilding enthusiasts to improve strength and fitness.', '2025-06-01 09:00:00', 15, 1),
(2, 'Yoga', 'Yoga class to relax both body and mind, improve flexibility.', '2025-06-01 08:00:00', 20, 2),
(3, 'Swimming', 'Swimming class for all levels, learn proper techniques.', '2025-06-02 10:00:00', 10, 3),
(4, 'Bodybuilding', 'Bodybuilding class for muscle gain and fat loss.', '2025-06-03 11:00:00', 12, 4),
(6, 'Bonx', 'aaa', 'Thứ 3, 5, 7 hàng tuần', 20, 6);

-- --------------------------------------------------------

--
-- Table structure for table `class_registration`
--

CREATE TABLE `class_registration` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `registration_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `class_registration`
--

INSERT INTO `class_registration` (`id`, `student_id`, `class_id`, `registration_date`) VALUES
(2, 2, 2, '2025-05-29 12:01:01'),
(3, 3, 3, '2025-05-29 12:01:01'),
(4, 4, 4, '2025-05-29 12:01:01'),
(6, 6, 1, '2025-05-29 12:01:01'),
(7, 7, 2, '2025-05-29 12:01:01'),
(8, 8, 3, '2025-05-29 12:01:01'),
(9, 9, 4, '2025-05-29 12:01:01'),
(11, 11, 1, '2025-05-29 12:01:01'),
(12, 12, 2, '2025-05-29 12:01:01'),
(13, 13, 3, '2025-05-29 12:01:01'),
(14, 14, 4, '2025-05-29 12:01:01'),
(16, 16, 1, '2025-05-29 12:01:01'),
(17, 17, 2, '2025-05-29 12:01:01'),
(18, 18, 3, '2025-05-29 12:01:01'),
(19, 19, 4, '2025-05-29 12:01:01'),
(20, 3, 2, '2025-05-29 12:01:59'),
(21, 20, 6, '2025-05-29 12:02:52');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `address` text DEFAULT NULL,
  `gender` enum('Male','Female') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `email`, `phone`, `dob`, `address`, `gender`) VALUES
(1, 'James Miller', 'james.miller@student.com', '0934567890', '2000-05-20', 'New York', 'Male'),
(2, 'Emily Johnson', 'emily.johnson@student.com', '0909876543', '2001-04-15', 'Los Angeles', 'Female'),
(3, 'Daniel Lee', 'daniel.lee@student.com', '0912345678', '1999-07-10', 'San Francisco', 'Male'),
(4, 'Michael Brown', 'michael.brown@student.com', '0932345679', '1998-12-25', 'Houston', 'Male'),
(5, 'William Davis', 'william.davis@student.com', '0943456789', '2002-03-30', 'Chicago', 'Male'),
(6, 'Ethan Wilson', 'ethan.wilson@student.com', '0954567890', '1997-01-12', 'Phoenix', 'Male'),
(7, 'Olivia Moore', 'olivia.moore@student.com', '0965678901', '1998-11-02', 'New York', 'Female'),
(8, 'Matthew Anderson', 'matthew.anderson@student.com', '0976789012', '2000-08-22', 'San Francisco', 'Male'),
(9, 'Sophia Martinez', 'sophia.martinez@student.com', '0987890123', '2001-05-05', 'Los Angeles', 'Female'),
(10, 'Isabella Taylor', 'isabella.taylor@student.com', '0998901234', '2000-09-15', 'Chicago', 'Female'),
(11, 'Lucas Thomas', 'lucas.thomas@student.com', '0911234567', '1999-06-20', 'New York', 'Male'),
(12, 'Benjamin White', 'benjamin.white@student.com', '0902345678', '1997-12-12', 'San Francisco', 'Male'),
(13, 'Ava Harris', 'ava.harris@student.com', '0933456789', '2000-02-18', 'Los Angeles', 'Female'),
(14, 'Logan Clark', 'logan.clark@student.com', '0944567890', '2002-04-10', 'Phoenix', 'Male'),
(15, 'Nathan Hall', 'nathan.hall@student.com', '0955678901', '2000-06-25', 'Houston', 'Male'),
(16, 'Mia Young', 'mia.young@student.com', '0966789012', '1998-07-10', 'Chicago', 'Female'),
(17, 'Chloe King', 'chloe.king@student.com', '0977890123', '1999-03-20', 'New York', 'Female'),
(18, 'Jack Scott', 'jack.scott@student.com', '0988901234', '2001-08-22', 'San Francisco', 'Male'),
(19, 'Henry Green', 'henry.green@student.com', '0999012345', '2000-10-30', 'Los Angeles', 'Male'),
(20, 'Nguyễn Thông Thiên', 'nguyen5@edu.student', '0772438318', '2004-08-06', 'aa', 'Male');

-- --------------------------------------------------------

--
-- Table structure for table `trainers`
--

CREATE TABLE `trainers` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `expertise` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trainers`
--

INSERT INTO `trainers` (`id`, `name`, `email`, `phone`, `dob`, `expertise`) VALUES
(1, 'Mark Adams', 'trainer1@gym.com', '0932345678', '1985-06-15', 'Professional Gym & Bodybuilding Expert'),
(2, 'Jessica Parker', 'trainer2@gym.com', '0908765432', '1990-04-10', 'Yoga and Meditation Specialist'),
(3, 'Brian Roberts', 'trainer3@swim.com', '0901234567', '1987-07-22', 'Swimming Instructor for All Levels'),
(4, 'Jason Smith', 'trainer4@bodybuilding.com', '0912345678', '1983-02-05', 'Bodybuilding, Muscle Gain & Fat Loss Expert'),
(6, 'Nguyễn Thông Thiên', 'thongthien2004@gmail.com', '012', '2004-08-04', 'aa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `trainer_id` (`trainer_id`);

--
-- Indexes for table `class_registration`
--
ALTER TABLE `class_registration`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `class_id` (`class_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `trainers`
--
ALTER TABLE `trainers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `classes`
--
ALTER TABLE `classes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `class_registration`
--
ALTER TABLE `class_registration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `trainers`
--
ALTER TABLE `trainers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `classes`
--
ALTER TABLE `classes`
  ADD CONSTRAINT `classes_ibfk_1` FOREIGN KEY (`trainer_id`) REFERENCES `trainers` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `class_registration`
--
ALTER TABLE `class_registration`
  ADD CONSTRAINT `class_registration_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `class_registration_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `classes` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
