-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 17, 2024 at 11:29 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mycollegemanager_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `dname` varchar(200) NOT NULL,
  `cname` varchar(200) NOT NULL,
  `fee` float(10,2) NOT NULL,
  `duration` int(10) NOT NULL,
  `units` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`dname`, `cname`, `fee`, `duration`, `units`) VALUES
('Arts', 'BA Fine Arts', 90000.00, 3, 'Year(s)'),
('IT', 'BCA', 400000.00, 3, 'Year(s)'),
('IT', 'MCA', 450000.00, 2, 'Year(s)');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `bookid` varchar(200) NOT NULL,
  `bookname` varchar(200) NOT NULL,
  `writer` varchar(200) NOT NULL,
  `pic` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`bookid`, `bookname`, `writer`, `pic`) VALUES
('234', 'history', 'balaji', '1723884116bookimg.jpg'),
('356', 'C++', 'balagurusamy', '1723884494img7.jpg'),
('567', 'biology', 'chandra s', '1723884367imgbook.jpg'),
('976', 'mathematics', 'ritikk', '1723884657MATH-SORIANO-BOOK-COVER-Front-1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `rollno` int(10) NOT NULL,
  `name` varchar(200) NOT NULL,
  `phone` bigint(10) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(300) NOT NULL,
  `department` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `book_issued` varchar(200) NOT NULL,
  `pic` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`rollno`, `name`, `phone`, `gender`, `dob`, `address`, `department`, `course`, `book_issued`, `pic`) VALUES
(101, 'radhika', 3453453455, 'Female', '2000-06-28', 'delhi', 'Arts', 'BA Fine Arts', 'english', '1720849050flow.jpg'),
(102, 'aman', 3453453477, 'Female', '2000-12-23', 'delhi', 'Arts', 'BA Fine Arts', 'balaguruswamy', 'default_image.png'),
(103, 'yashika', 5456456477, 'Female', '2000-12-12', 'amritsar', 'IT', 'MCA', 'lords', 'default_image.png');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  `pic` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`username`, `password`, `usertype`, `pic`) VALUES
('Koli', '789', 'Employee', 'default_image.png'),
('Madhav', '123', 'Employee', '1723530334VICTUS.png'),
('Rahul', '789', 'Admin', 'default_image.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`cname`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`bookid`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`rollno`);

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
