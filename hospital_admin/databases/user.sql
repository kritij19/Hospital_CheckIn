-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 27, 2022 at 11:53 AM
-- Server version: 5.7.37
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `amitbaghel`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `User_ID` int(11) NOT NULL,
  `First_Name` varchar(255) NOT NULL,
  `Last_Name` varchar(255) NOT NULL,
  `Contact_Num` varchar(10) NOT NULL,
  `Aadhar_Num` varchar(12) NOT NULL,
  `Gender` char(1) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `StreetAddress` varchar(100) DEFAULT NULL,
  `ApartmentNumber` varchar(20) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` varchar(25) DEFAULT NULL,
  `Pincode` varchar(10) DEFAULT NULL,
  `PersonID` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`User_ID`, `First_Name`, `Last_Name`, `Contact_Num`, `Aadhar_Num`, `Gender`, `DOB`, `StreetAddress`, `ApartmentNumber`, `City`, `State`, `Pincode`, `PersonID`) VALUES
(1, 'amit', 'baghel', '8650340705', '43543543543', 'm', '2022-05-17', 'hgfhgf gfhgfhgf hgfhgf', '4353', 'agra', 'uttar pradesh', '234243', '43453'),
(2, 'amit2', 'baghel2', '8650340705', '43543543543', 'm', '2022-05-17', 'hgfhgf gfhgfhgf hgfhgf', '4353', 'agra', 'uttar pradesh', '234243', '43453'),
(3, 'amit23', 'baghel23', '8650340705', '43543543543', 'm', '2022-05-17', 'hgfhgf gfhgfhgf hgfhgf', '4353', 'agra', 'uttar pradesh', '234243', '43453'),
(4, 'amit234', 'baghel234', '8650340705', '43543543543', 'm', '2022-05-17', 'hgfhgf gfhgfhgf hgfhgf', '4353', 'agra', 'uttar pradesh', '234243', '43453'),
(5, 'amit2345', 'baghel2345', '8650340705', '43543543543', 'm', '2022-05-17', 'hgfhgf gfhgfhgf hgfhgf', '4353', 'agra', 'uttar pradesh', '234243', '43453');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`User_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
