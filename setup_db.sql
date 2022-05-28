CREATE DATABASE `master` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE master;
--
-- Table structure for table `user`
--
CREATE TABLE `user` (
  `User_ID` varchar(130) NOT NULL,
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
  `PersonID` varchar(130) DEFAULT NULL,
  PRIMARY KEY (`User_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `createAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;


