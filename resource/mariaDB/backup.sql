<<<<<<< HEAD
-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2018 at 12:22 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `testdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'Cables'),
(2, 'Wireless Speakers'),
(3, 'Computing & Gaming'),
(4, 'Smartwatches'),
(5, 'VR Headsets');

-- --------------------------------------------------------

--
-- Table structure for table `prices`
--

CREATE TABLE `prices` (
  `id` int(11) NOT NULL,
  `prod_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `discount` varchar(4) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `currency_iso` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `prices`
--

INSERT INTO `prices` (`id`, `prod_id`, `price`, `discount`, `date`, `currency_iso`) VALUES
(1, 1, 399, '-17%', '2018-06-03 06:43:27', 'NPR'),
(2, 2, 749, '-25%', '2018-06-03 06:43:27', 'NPR'),
(3, 3, 750, '-63%', '2018-06-03 06:43:28', 'NPR'),
(4, 4, 1199, '-52%', '2018-06-03 06:43:28', 'NPR'),
(5, 5, 400, '-16%', '2018-06-03 06:43:28', 'NPR'),
(6, 8, 375, '-25%', '2018-06-03 06:43:28', 'NPR'),
(7, 6, 1299, '-37%', '2018-06-03 06:43:28', 'NPR'),
(8, 7, 619, '-31%', '2018-06-03 06:43:28', 'NPR'),
(9, 9, 420, '-35%', '2018-06-03 06:43:28', 'NPR'),
(10, 10, 1449, '-24%', '2018-06-03 06:43:29', 'NPR'),
(11, 11, 1249, '-55%', '2018-06-03 06:43:29', 'NPR'),
(12, 12, 1760, '-20%', '2018-06-03 06:43:29', 'NPR'),
(13, 13, 1088, '-56%', '2018-06-03 06:43:29', 'NPR'),
(14, 14, 799, '-21%', '2018-06-03 06:43:29', 'NPR'),
(15, 15, 69, '-66%', '2018-06-03 06:43:29', 'NPR'),
(16, 16, 2945, '-24%', '2018-06-03 06:43:29', 'NPR'),
(17, 17, 1249, '-51%', '2018-06-03 06:43:29', 'NPR'),
(18, 18, 1199, '-40%', '2018-06-03 06:43:29', 'NPR'),
(19, 19, 125, '-17%', '2018-06-03 06:43:29', 'NPR'),
(20, 20, 450, '-36%', '2018-06-03 06:43:29', 'NPR'),
(21, 21, 500, '-38%', '2018-06-03 06:43:29', 'NPR'),
(22, 22, 499, '-29%', '2018-06-03 06:43:29', 'NPR'),
(23, 23, 1049, '-45%', '2018-06-03 06:43:29', 'NPR'),
(24, 24, 1019, '-29%', '2018-06-03 06:43:29', 'NPR'),
(25, 25, 1499, '-32%', '2018-06-03 06:43:29', 'NPR'),
(26, 26, 500, '-38%', '2018-06-03 06:43:29', 'NPR'),
(27, 27, 1500, '-40%', '2018-06-03 06:43:29', 'NPR'),
(28, 31, 700, '-30%', '2018-06-03 06:43:29', 'NPR'),
(29, 29, 359, '-64%', '2018-06-03 06:43:29', 'NPR'),
(30, 28, 700, '-30%', '2018-06-03 06:43:29', 'NPR'),
(31, 30, 1799, '-10%', '2018-06-03 06:43:29', 'NPR'),
(32, 32, 1499, '-35%', '2018-06-03 06:43:29', 'NPR'),
(33, 33, 1149, '-43%', '2018-06-03 06:43:29', 'NPR'),
(34, 34, 1888, '-6%', '2018-06-03 06:43:29', 'NPR'),
(35, 35, 799, '-20%', '2018-06-03 06:43:29', 'NPR'),
(36, 36, 1799, '-37%', '2018-06-03 06:43:29', 'NPR'),
(37, 37, 1649, '-34%', '2018-06-03 06:43:29', 'NPR'),
(38, 40, 700, '-30%', '2018-06-03 06:43:29', 'NPR'),
(39, 39, 500, '-38%', '2018-06-03 06:43:29', 'NPR'),
(40, 38, 645, '-16%', '2018-06-03 06:43:29', 'NPR'),
(41, 41, 100, '-13%', '2018-06-03 06:43:29', 'NPR'),
(42, 42, 999, '-41%', '2018-06-03 06:43:30', 'NPR'),
(43, 43, 1349, '-39%', '2018-06-03 06:43:30', 'NPR'),
(44, 44, 1799, '-40%', '2018-06-03 06:43:30', 'NPR'),
(45, 45, 899, '-40%', '2018-06-03 06:43:30', 'NPR'),
(46, 46, 2399, '-20%', '2018-06-03 06:43:30', 'NPR'),
(47, 47, 400, '-50%', '2018-06-03 06:43:30', 'NPR'),
(48, 48, 999, '-4%', '2018-06-03 06:43:30', 'NPR'),
(49, 49, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(50, 50, 799, '-20%', '2018-06-03 06:43:30', 'NPR'),
(51, 51, 800, '-27%', '2018-06-03 06:43:30', 'NPR'),
(52, 52, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(53, 53, 340, '-48%', '2018-06-03 06:43:30', 'NPR'),
(54, 54, 1140, '-24%', '2018-06-03 06:43:30', 'NPR'),
(55, 55, 2099, '-40%', '2018-06-03 06:43:30', 'NPR'),
(56, 57, 380, '-31%', '2018-06-03 06:43:30', 'NPR'),
(57, 56, 199, '-60%', '2018-06-03 06:43:30', 'NPR'),
(58, 58, 1600, '-11%', '2018-06-03 06:43:30', 'NPR'),
(59, 59, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(60, 61, 899, '-55%', '2018-06-03 06:43:30', 'NPR'),
(61, 60, 377, '-46%', '2018-06-03 06:43:30', 'NPR'),
(62, 62, 490, '-30%', '2018-06-03 06:43:30', 'NPR'),
(63, 66, 1099, '-27%', '2018-06-03 06:43:30', 'NPR'),
(64, 64, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(65, 63, 899, '-25%', '2018-06-03 06:43:30', 'NPR'),
(66, 65, 100, '-13%', '2018-06-03 06:43:30', 'NPR'),
(67, 67, 1699, '-55%', '2018-06-03 06:43:30', 'NPR'),
(68, 68, 3999, '-20%', '2018-06-03 06:43:30', 'NPR'),
(69, 70, 1000, '-33%', '2018-06-03 06:43:30', 'NPR'),
(70, 69, 1599, '-6%', '2018-06-03 06:43:30', 'NPR'),
(71, 71, 4499, '-20%', '2018-06-03 06:43:30', 'NPR'),
(72, 73, 100, '-13%', '2018-06-03 06:43:30', 'NPR'),
(73, 72, 1199, '-39%', '2018-06-03 06:43:30', 'NPR'),
(74, 74, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(75, 75, 1649, '-15%', '2018-06-03 06:43:30', 'NPR'),
(76, 76, 849, '-43%', '2018-06-03 06:43:31', 'NPR'),
(77, 77, 2599, '-35%', '2018-06-03 06:43:31', 'NPR'),
(78, 78, 1099, '-56%', '2018-06-03 06:43:31', 'NPR'),
(79, 79, 599, '-40%', '2018-06-03 06:43:31', 'NPR'),
(80, 80, 444, '-11%', '2018-06-03 06:43:31', 'NPR'),
(81, 81, 149, '-50%', '2018-06-03 06:43:31', 'NPR'),
(82, 82, 500, '-38%', '2018-06-03 06:43:31', 'NPR'),
(83, 83, 1149, '-43%', '2018-06-03 06:43:31', 'NPR'),
(84, 84, 600, '-40%', '2018-06-03 06:43:31', 'NPR'),
(85, 85, 2199, '-12%', '2018-06-03 06:43:31', 'NPR'),
(86, 86, 500, '-38%', '2018-06-03 06:43:31', 'NPR'),
(87, 87, 1450, '-19%', '2018-06-03 06:43:31', 'NPR'),
(88, 89, 750, '-25%', '2018-06-03 06:43:31', 'NPR'),
(89, 88, 1700, '-43%', '2018-06-03 06:43:31', 'NPR'),
(90, 90, 2500, '-29%', '2018-06-03 06:43:31', 'NPR'),
(91, 91, 1299, '-26%', '2018-06-03 06:43:31', 'NPR'),
(92, 92, 899, '-10%', '2018-06-03 06:43:31', 'NPR'),
(93, 93, 120, '-14%', '2018-06-03 06:43:31', 'NPR'),
(94, 94, 500, '-38%', '2018-06-03 06:43:31', 'NPR'),
(95, 95, 639, '-28%', '2018-06-03 06:43:31', 'NPR'),
(96, 96, 99, '-34%', '2018-06-03 06:43:31', 'NPR'),
(97, 97, 500, '-33%', '2018-06-03 06:43:31', 'NPR'),
(98, 98, 1299, '-13%', '2018-06-03 06:43:31', 'NPR'),
(99, 99, 449, '-31%', '2018-06-03 06:43:31', 'NPR'),
(100, 100, 1740, '-17%', '2018-06-03 06:43:31', 'NPR'),
(101, 101, 120, '-14%', '2018-06-03 06:43:31', 'NPR'),
(102, 102, 799, '-43%', '2018-06-03 06:43:31', 'NPR'),
(103, 103, 149, '-50%', '2018-06-03 06:43:31', 'NPR'),
(104, 104, 4499, '-25%', '2018-06-03 06:43:31', 'NPR'),
(105, 105, 2499, '-29%', '2018-06-03 06:43:31', 'NPR'),
(106, 106, 500, '-38%', '2018-06-03 06:43:31', 'NPR'),
(107, 107, 475, '-26%', '2018-06-03 06:43:32', 'NPR'),
(108, 108, 4199, '-16%', '2018-06-03 06:43:32', 'NPR'),
(109, 109, 1699, '-55%', '2018-06-03 06:43:32', 'NPR'),
(110, 110, 149, '-25%', '2018-06-03 06:43:32', 'NPR'),
(111, 111, 500, '-38%', '2018-06-03 06:43:32', 'NPR'),
(112, 112, 999, '-33%', '2018-06-03 06:43:32', 'NPR'),
(113, 113, 849, '-29%', '2018-06-03 06:43:32', 'NPR'),
(114, 114, 119, '-52%', '2018-06-03 06:43:32', 'NPR'),
(115, 115, 1249, '-43%', '2018-06-03 06:43:32', 'NPR'),
(116, 117, 1490, '-25%', '2018-06-03 06:43:32', 'NPR'),
(117, 116, 399, '-60%', '2018-06-03 06:43:32', 'NPR'),
(118, 118, 7499, '-17%', '2018-06-03 06:43:32', 'NPR'),
(119, 119, 499, '-50%', '2018-06-03 06:43:32', 'NPR'),
(120, 120, 1099, '-8%', '2018-06-03 06:43:32', 'NPR'),
(121, 121, 349, '-53%', '2018-06-03 06:43:32', 'NPR'),
(122, 122, 599, '-8%', '2018-06-03 06:43:32', 'NPR'),
(123, 123, 280, '-44%', '2018-06-03 06:43:32', 'NPR'),
(124, 15, 69, '-66%', '2018-06-03 06:50:47', ' NP'),
(125, 19, 125, '-17%', '2018-06-03 06:50:47', ' NP'),
(126, 23, 1049, '-45%', '2018-06-03 06:50:47', ' NP'),
(127, 5, 400, '-16%', '2018-06-03 06:50:48', ' NP'),
(128, 1, 399, '-17%', '2018-06-03 06:50:48', ' NP'),
(129, 25, 1499, '-32%', '2018-06-03 06:50:48', ' NP'),
(130, 8, 375, '-25%', '2018-06-03 06:50:48', ' NP'),
(131, 2, 749, '-25%', '2018-06-03 06:50:48', ' NP'),
(132, 29, 359, '-64%', '2018-06-03 06:50:48', ' NP'),
(133, 9, 420, '-35%', '2018-06-03 06:50:48', ' NP'),
(134, 3, 750, '-63%', '2018-06-03 06:50:48', ' NP'),
(135, 33, 1149, '-43%', '2018-06-03 06:50:48', ' NP'),
(136, 6, 1299, '-37%', '2018-06-03 06:50:48', ' NP'),
(137, 37, 1649, '-34%', '2018-06-03 06:50:48', ' NP'),
(138, 12, 1760, '-20%', '2018-06-03 06:50:48', ' NP'),
(139, 11, 1249, '-55%', '2018-06-03 06:50:48', ' NP'),
(140, 4, 1199, '-52%', '2018-06-03 06:50:48', ' NP'),
(141, 41, 100, '-13%', '2018-06-03 06:50:48', ' NP'),
(142, 45, 899, '-40%', '2018-06-03 06:50:48', ' NP'),
(143, 16, 2945, '-24%', '2018-06-03 06:50:48', ' NP'),
(144, 13, 1088, '-56%', '2018-06-03 06:50:48', ' NP'),
(145, 7, 619, '-31%', '2018-06-03 06:50:48', ' NP'),
(146, 47, 400, '-50%', '2018-06-03 06:50:49', ' NP'),
(147, 20, 450, '-36%', '2018-06-03 06:50:49', ' NP'),
(148, 51, 800, '-27%', '2018-06-03 06:50:49', ' NP'),
(149, 10, 1449, '-24%', '2018-06-03 06:50:49', ' NP'),
(150, 17, 1249, '-51%', '2018-06-03 06:50:49', ' NP'),
(151, 24, 1019, '-29%', '2018-06-03 06:50:49', ' NP'),
(152, 56, 199, '-60%', '2018-06-03 06:50:49', ' NP'),
(153, 28, 700, '-30%', '2018-06-03 06:50:49', ' NP'),
(154, 61, 899, '-55%', '2018-06-03 06:50:49', ' NP'),
(155, 14, 799, '-21%', '2018-06-03 06:50:49', ' NP'),
(156, 21, 500, '-38%', '2018-06-03 06:50:49', ' NP'),
(157, 34, 1888, '-6%', '2018-06-03 06:50:49', ' NP'),
(158, 65, 100, '-13%', '2018-06-03 06:50:49', ' NP'),
(159, 18, 1199, '-40%', '2018-06-03 06:50:49', ' NP'),
(160, 40, 700, '-30%', '2018-06-03 06:50:49', ' NP'),
(161, 26, 500, '-38%', '2018-06-03 06:50:49', ' NP'),
(162, 22, 499, '-29%', '2018-06-03 06:50:49', ' NP'),
(163, 68, 3999, '-20%', '2018-06-03 06:50:49', ' NP'),
(164, 30, 1799, '-10%', '2018-06-03 06:50:49', ' NP'),
(165, 44, 1799, '-40%', '2018-06-03 06:50:49', ' NP'),
(166, 73, 100, '-13%', '2018-06-03 06:50:49', ' NP'),
(167, 27, 1500, '-40%', '2018-06-03 06:50:49', ' NP'),
(168, 76, 849, '-43%', '2018-06-03 06:50:49', ' NP'),
(169, 32, 1499, '-35%', '2018-06-03 06:50:49', ' NP'),
(170, 48, 999, '-4%', '2018-06-03 06:50:49', ' NP'),
(171, 31, 700, '-30%', '2018-06-03 06:50:49', ' NP'),
(172, 81, 149, '-50%', '2018-06-03 06:50:50', ' NP'),
(173, 53, 340, '-48%', '2018-06-03 06:50:50', ' NP'),
(174, 36, 1799, '-37%', '2018-06-03 06:50:50', ' NP'),
(175, 35, 799, '-20%', '2018-06-03 06:50:50', ' NP'),
(176, 84, 600, '-40%', '2018-06-03 06:50:50', ' NP'),
(177, 57, 380, '-31%', '2018-06-03 06:50:50', ' NP'),
(178, 39, 500, '-38%', '2018-06-03 06:50:50', ' NP'),
(179, 60, 377, '-46%', '2018-06-03 06:50:50', ' NP'),
(180, 38, 645, '-16%', '2018-06-03 06:50:50', ' NP'),
(181, 89, 750, '-25%', '2018-06-03 06:50:50', ' NP'),
(182, 43, 1349, '-39%', '2018-06-03 06:50:50', ' NP'),
(183, 63, 899, '-25%', '2018-06-03 06:50:50', ' NP'),
(184, 42, 999, '-41%', '2018-06-03 06:50:50', ' NP'),
(185, 49, 500, '-38%', '2018-06-03 06:50:50', ' NP'),
(186, 93, 120, '-14%', '2018-06-03 06:50:50', ' NP'),
(187, 70, 1000, '-33%', '2018-06-03 06:50:50', ' NP'),
(188, 52, 500, '-38%', '2018-06-03 06:50:50', ' NP'),
(189, 46, 2399, '-20%', '2018-06-03 06:50:50', ' NP'),
(190, 96, 99, '-34%', '2018-06-03 06:50:50', ' NP'),
(191, 72, 1199, '-39%', '2018-06-03 06:50:50', ' NP'),
(192, 55, 2099, '-40%', '2018-06-03 06:50:50', ' NP'),
(193, 50, 799, '-20%', '2018-06-03 06:50:50', ' NP'),
(194, 77, 2599, '-35%', '2018-06-03 06:50:51', ' NP'),
(195, 59, 500, '-38%', '2018-06-03 06:50:51', ' NP'),
(196, 101, 120, '-14%', '2018-06-03 06:50:51', ' NP'),
(197, 54, 1140, '-24%', '2018-06-03 06:50:51', ' NP'),
(198, 80, 444, '-11%', '2018-06-03 06:50:51', ' NP'),
(199, 103, 149, '-50%', '2018-06-03 06:50:51', ' NP'),
(200, 64, 500, '-38%', '2018-06-03 06:50:51', ' NP'),
(201, 58, 1600, '-11%', '2018-06-03 06:50:51', ' NP'),
(202, 85, 2199, '-12%', '2018-06-03 06:50:51', ' NP'),
(203, 67, 1699, '-55%', '2018-06-03 06:50:51', ' NP'),
(204, 108, 4199, '-16%', '2018-06-03 06:50:51', ' NP'),
(205, 62, 490, '-30%', '2018-06-03 06:50:51', ' NP'),
(206, 88, 1700, '-43%', '2018-06-03 06:50:51', ' NP'),
(207, 71, 4499, '-20%', '2018-06-03 06:50:51', ' NP'),
(208, 66, 1099, '-27%', '2018-06-03 06:50:51', ' NP'),
(209, 110, 149, '-25%', '2018-06-03 06:50:51', ' NP'),
(210, 74, 500, '-38%', '2018-06-03 06:50:51', ' NP'),
(211, 69, 1599, '-6%', '2018-06-03 06:50:51', ' NP'),
(212, 112, 999, '-33%', '2018-06-03 06:50:51', ' NP'),
(213, 92, 899, '-10%', '2018-06-03 06:50:51', ' NP'),
(214, 78, 1099, '-56%', '2018-06-03 06:50:52', ' NP'),
(215, 114, 119, '-52%', '2018-06-03 06:50:52', ' NP'),
(216, 75, 1649, '-15%', '2018-06-03 06:50:52', ' NP'),
(217, 97, 500, '-33%', '2018-06-03 06:50:52', ' NP'),
(218, 82, 500, '-38%', '2018-06-03 06:50:52', ' NP'),
(219, 116, 399, '-60%', '2018-06-03 06:50:52', ' NP'),
(220, 79, 599, '-40%', '2018-06-03 06:50:52', ' NP'),
(221, 86, 500, '-38%', '2018-06-03 06:50:52', ' NP'),
(222, 119, 499, '-50%', '2018-06-03 06:50:52', ' NP'),
(223, 83, 1149, '-43%', '2018-06-03 06:50:52', ' NP'),
(224, 90, 2500, '-29%', '2018-06-03 06:50:52', ' NP'),
(225, 120, 1099, '-8%', '2018-06-03 06:50:52', ' NP'),
(226, 87, 1450, '-19%', '2018-06-03 06:50:53', ' NP'),
(227, 94, 500, '-38%', '2018-06-03 06:50:53', ' NP'),
(228, 121, 349, '-53%', '2018-06-03 06:50:53', ' NP'),
(229, 91, 1299, '-26%', '2018-06-03 06:50:53', ' NP'),
(230, 98, 1299, '-13%', '2018-06-03 06:50:53', ' NP'),
(231, 122, 599, '-8%', '2018-06-03 06:50:53', ' NP'),
(232, 95, 639, '-28%', '2018-06-03 06:50:53', ' NP'),
(233, 100, 1740, '-17%', '2018-06-03 06:50:53', ' NP'),
(234, 123, 280, '-44%', '2018-06-03 06:50:53', ' NP'),
(235, 99, 449, '-31%', '2018-06-03 06:50:53', ' NP'),
(236, 104, 4499, '-25%', '2018-06-03 06:50:53', ' NP'),
(237, 102, 799, '-43%', '2018-06-03 06:50:53', ' NP'),
(238, 106, 500, '-38%', '2018-06-03 06:50:53', ' NP'),
(239, 105, 2499, '-29%', '2018-06-03 06:50:53', ' NP'),
(240, 109, 1699, '-55%', '2018-06-03 06:50:53', ' NP'),
(241, 107, 475, '-26%', '2018-06-03 06:50:53', ' NP'),
(242, 111, 500, '-38%', '2018-06-03 06:50:53', ' NP'),
(243, 113, 849, '-29%', '2018-06-03 06:50:54', ' NP'),
(244, 115, 1249, '-43%', '2018-06-03 06:50:54', ' NP'),
(245, 117, 1490, '-25%', '2018-06-03 06:50:54', ' NP'),
(246, 118, 7499, '-17%', '2018-06-03 06:50:54', ' NP');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `sku` char(19) NOT NULL,
  `product_name` text NOT NULL,
  `category` int(11) NOT NULL,
  `link` text NOT NULL,
  `image_link` text NOT NULL,
  `date_issued` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `sku`, `product_name`, `category`, `link`, `image_link`, `date_issued`, `date_updated`) VALUES
(1, 'OT776EL19M9WWNAFAMZ', 'VR Glass 3D Glasses 2nd Generation', 5, 'https://www.daraz.com.np/other-vr-glass-3d-glasses-2nd-generation-22667.html', 'https://np.daraz.io/VTwj3pEsUjAzEN6i49AEJZ8hXjw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/76/622/1.jpg?6244', '2018-06-03 06:43:27', '2018-06-03 06:50:48'),
(2, 'OT776EL1KVD8WNAFAMZ', 'Combo of VR Box + Earphone And Gaming Remote', 5, 'https://www.daraz.com.np/other-combo-of-vr-box-earphone-and-gaming-remote-22559.html', 'https://np.daraz.io/1TP1ThoB8F17UCsSoxGAh-saNyE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/95/522/1.jpg?6254', '2018-06-03 06:43:27', '2018-06-03 06:50:48'),
(3, 'OT776EL0JLF28NAFAMZ', 'VR Box Pro-3D Glasses Virtual Reality With Remote', 5, 'https://www.daraz.com.np/other-vr-box-pro-3d-glasses-virtual-reality-with-remote-21923.html', 'https://np.daraz.io/pXi9zfRaMJKHNYkaKkHBb-w9oLE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/32/912/1.jpg?6101', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(4, 'OT776EL1LIY0GNAFAMZ', 'VR Shinecon Combo Premium VR Glass + Remote', 5, 'https://www.daraz.com.np/other-vr-shinecon-combo-premium-vr-glass-remote-22669.html', 'https://np.daraz.io/XyavkDutp5ixsYV67CLaOG29dyQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/96/622/1.jpg?6243', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(5, 'OT776EL154YTCNAFAMZ', 'Portable Wireless Bluetooth Box Speaker', 2, 'https://www.daraz.com.np/other-portable-wireless-bluetooth-box-speaker-69096.html', 'https://np.daraz.io/njTrf2ftU377EVseCBOuYXDIVdI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/69/096/1.jpg?3407', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(6, 'OT776EL0I7OXSNAFAMZ', 'Bluetooth Smartwatch - D3 New', 4, 'https://www.daraz.com.np/other-bluetooth-smartwatch-d3-new-29503.html', 'https://np.daraz.io/DQ-CIGqQm2hoz_ST40WHOO8qrHM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/30/592/1.jpg?7286', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(7, 'OT776EL0Q3ZI8NAFAMZ', 'VR Box Pro - 3D Glasses Virtual Reality With Remote', 5, 'https://www.daraz.com.np/other-vr-box-pro-3d-glasses-virtual-reality-with-remote-65834.html', 'https://np.daraz.io/vQ8dkKWM5ZZTlul2Ba5TBya2lwE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/43/856/1.jpg?4484', '2018-06-03 06:43:28', '2018-06-03 06:50:49'),
(8, 'SO445EL14UNO8NAFAMZ', 'Soft Vision Music Mini Box Bluetooth Speaker', 2, 'https://www.daraz.com.np/soft-vision-music-mini-box-bluetooth-speaker-51686.html', 'https://np.daraz.io/i-pMw4ha17XdKpLQPpncy3QN4VY=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/68/615/1.jpg?0464', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(9, 'OT776EL18VF3CNAFAMZ', 'SD Support Bluetooth Portable Speaker (Color Varied)', 2, 'https://www.daraz.com.np/other-sd-support-bluetooth-portable-speaker-color-varied-96357.html', 'https://np.daraz.io/BwaSKVBm43RTUK2Ov4skgLXrN8I=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/75/369/1.jpg?4365', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(10, 'OT776EL1D8P4ONAFAMZ', 'VR Box Shinecon , Bluetooth Gaming Remote & Earphone', 5, 'https://www.daraz.com.np/other-vr-box-shinecon-bluetooth-gaming-remote-earphone-70728.html', 'https://np.daraz.io/yNIihngH3UmMFd5rLym4l7OxCVI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/82/707/1.jpg?7046', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(11, 'OT776EL0FOFG0NAFAMZ', 'Iwatch Smartwatch', 4, 'https://www.daraz.com.np/other-iwatch-smartwatch-43362.html', 'https://np.daraz.io/-Tztovh9s_W08uKpgUTcnaR3wLk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/26/334/1.jpg?2105', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(12, 'AN041EL0TJ88GNAFAMZ', 'Anker Soundcore Nano Big Sound Super Portable Wireless Bluetooth Speaker - (Silver)', 2, 'https://www.daraz.com.np/anker-soundcore-nano-big-sound-super-portable-wireless-bluetooth-speaker-silver-60694.html', 'https://np.daraz.io/S2MS7ggHYuZjhqmLopURrwLatpI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/606/1.jpg?1448', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(13, 'OT776EL17AGXSNAFAMZ', 'I6 Smartwatch With Sim And Micro Sd Slot', 4, 'https://www.daraz.com.np/other-i6-smartwatch-with-sim-and-micro-sd-slot-21727.html', 'https://np.daraz.io/ZDGDj8x3XluFG2rDauGqvm84NYY=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/72/712/1.jpg?5975', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(14, 'OT776EL0YATPCNAFAMZ', 'VR Box 2nd Generation With Bluetooth Game Pad Remote Shutter', 5, 'https://www.daraz.com.np/other-vr-box-2nd-generation-with-bluetooth-game-pad-remote-shutter-21675.html', 'https://np.daraz.io/3tmmHVYVsyHx2rHAD897EHbG68M=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/57/612/1.jpg?5945', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(15, 'OT776EL0YYM6ONAFAMZ', 'Black OTG Cable for Mobile Phones', 1, 'https://www.daraz.com.np/other-black-otg-cable-for-mobile-phones-22785.html', 'https://np.daraz.io/di2I0SVsVIpUvclbcr1cBqqhvuU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/722/1.jpg?7454', '2018-06-03 06:43:29', '2018-06-03 06:50:47'),
(16, 'JB523EL0PC23SNAFAMZ', 'JBL Go Portable Mini Bluetooth Speaker  Black', 2, 'https://www.daraz.com.np/jbl-go-portable-mini-bluetooth-speaker-black-35524.html', 'https://np.daraz.io/iSrQYrPSzujO4dDNsfeSkU6adog=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/42/553/1.jpg?1046', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(17, 'OT776EL1M6IS0NAFAMZ', 'Iwatch Smartwatch', 4, 'https://www.daraz.com.np/other-iwatch-smartwatch-22779.html', 'https://np.daraz.io/bSt6sPpKlR-_9bSZIFFjdHb1gRo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/97/722/1.jpg?8115', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(18, 'OT776EL1AUD3SNAFAMZ', 'VR Shinecon Combo Premium VR Glass + Remote', 5, 'https://www.daraz.com.np/other-vr-shinecon-combo-premium-vr-glass-remote-97687.html', 'https://np.daraz.io/usPgYI1HQkv6VqE99EEKOJEHRmA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/78/679/1.jpg?1944', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(19, 'OT776EL101CH4NAFAMZ', 'HDMI Cable (1.5m)', 1, 'https://www.daraz.com.np/other-hdmi-cable-1.5m-92506.html', 'https://np.daraz.io/0Vy0v_Pm1hvAmvTkWI3qKDOS6xE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/60/529/1.jpg?8924', '2018-06-03 06:43:29', '2018-06-03 06:50:47'),
(20, 'OT776EL1IMQJONAFAMZ', 'Mini Portable Bluetooth Speaker With Built-in Mic & LED Light', 2, 'https://www.daraz.com.np/other-mini-portable-bluetooth-speaker-with-built-in-mic-led-light-106719.html', 'https://np.daraz.io/UKcPBsWBFB9FDTZRgM10pmmqP78=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/91/7601/1.jpg?8506', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(21, 'OT776EL05NNV8NAFAMZ', 'Moto 360 2nd Gen 46mm Smart Watch Tempered Glass Anti-Scratch', 4, 'https://www.daraz.com.np/other-moto-360-2nd-gen-46mm-smart-watch-tempered-glass-anti-scratch-120590.html', 'https://np.daraz.io/5VKBmFaptJJ0N-gcCQJmbR3Mbfs=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/09/5021/1.jpg?4915', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(22, 'OT776EL180LLONAFAMZ', 'VR BOX Version 2.0 - Virtual Reality 3D Glasses', 5, 'https://www.daraz.com.np/other-vr-box-version-2.0-virtual-reality-3d-glasses-113937.html', 'https://np.daraz.io/wglZFFJm8_M1Eue2qRMqhH50SaU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/73/9311/1.jpg?9253', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(23, 'OT776EL0R6W1ONAFAMZ', 'HDMI To HDMI 15 Meter Cable', 1, 'https://www.daraz.com.np/other-hdmi-to-hdmi-15-meter-cable-117654.html', 'https://np.daraz.io/lWqItwPt6khdmAZPmHhfTJwlqog=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/45/6711/1.jpg?7825', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(24, 'OT776EL1B3028NAFAMZ', 'JY-25 USB Bluetooth Portable Speaker Support TF Card + FM Radio', 2, 'https://www.daraz.com.np/other-jy-25-usb-bluetooth-portable-speaker-support-tf-card-fm-radio-28097.html', 'https://np.daraz.io/-bspGELOuUOKaAqpydgq4aRFcc4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/082/1.jpg?2235', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(25, 'ON440EL0GHR2SNAFAMZ', 'Lightning 8-Pin To HDMI Female Video Adapter With Micro USB Charging Cable', 1, 'https://www.daraz.com.np/onlineshopgroup-lightning-8-pin-to-hdmi-female-video-adapter-with-micro-usb-charging-cable-120772.html', 'https://np.daraz.io/Ro0sbdOVotlM-CegLl4c8oUMJDE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/27/7021/1.jpg?8515', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(26, 'OT776EL0NIO0KNAFAMZ', 'Samsung Gear S2 Gear Sport Tempered Glass Screen Protector High Definition', 4, 'https://www.daraz.com.np/other-samsung-gear-s2-gear-sport-tempered-glass-screen-protector-high-definition-120593.html', 'https://np.daraz.io/uASfn9glBj813C1xtexs14Vfjzw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/39/5021/1.jpg?5276', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(27, 'OT776EL0UX2AKNAFAMZ', 'VR Shinecon Virtual Reality 3D Glasses With Gaming Remote - Black', 5, 'https://www.daraz.com.np/other-vr-shinecon-virtual-reality-3d-glasses-with-gaming-remote-black-113915.html', 'https://np.daraz.io/oPs5Pegij9OiOWBUQkMrD1oDIMg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/9311/1.jpg?7332', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(28, 'OT776EL0TINEGNAFAMZ', 'S815 Hi-Fi Music Player Wireless Bluetooth Mini Portable Speaker Super Bass', 2, 'https://www.daraz.com.np/other-s815-hi-fi-music-player-wireless-bluetooth-mini-portable-speaker-super-bass-97594.html', 'https://np.daraz.io/RoEJy3Um61CpXteRdCOYxh-vdLA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/579/1.jpg?7644', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(29, 'OT776EL0KP5M8NAFAMZ', 'HDMI To VGA Converter', 1, 'https://www.daraz.com.np/other-hdmi-to-vga-converter-66743.html', 'https://np.daraz.io/YHyFj4q_wx94p2Jw0rNdEvGc27M=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/34/766/1.jpg?4424', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(30, 'OT776EL0FTQ3WNAFAMZ', 'Q18 Smart Watch- Black', 4, 'https://www.daraz.com.np/other-q18-smart-watch-black-118562.html', 'https://np.daraz.io/WDgf_4EWCoq1xW9z5VYZhjWP4sI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/26/5811/1.jpg?0178', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(31, 'OT776EL1B3AV4NAFAMZ', 'HD VR Movie Box For Gaming And Video Play With Wireless Remote Controller', 5, 'https://www.daraz.com.np/other-hd-vr-movie-box-for-gaming-and-video-play-with-wireless-remote-controller-69097.html', 'https://np.daraz.io/TTBF_qhzuR5qp2d4mHd0cqbyxNQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/096/1.jpg?3447', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(32, 'ON440EL0YL2LWNAFAMZ', 'Smartwatch - IOS/Android - White', 4, 'https://www.daraz.com.np/onlineshopgroup-smartwatch-iosandroid-white-109085.html', 'https://np.daraz.io/Gf7CYoY5pfzzKteLDQN5vfrMHJE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/0901/1.jpg?1676', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(33, 'OT776EL0X583GNAFAMZ', 'Plastic Braided HDMI Extension Cable- 20M', 1, 'https://www.daraz.com.np/other-plastic-braided-hdmi-extension-cable-20m-117655.html', 'https://np.daraz.io/sR3fzei7-yE39tiNOS2X9mGL0kI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/55/6711/1.jpg?7825', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(34, 'OT776EL1KBEYKNAFAMZ', 'Bluetooth Sound Bar Wireless Speaker-Black', 2, 'https://www.daraz.com.np/other-bluetooth-sound-bar-wireless-speaker-black-119549.html', 'https://np.daraz.io/aapOrXNDYKdbM2g8u3OrFGoej2k=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/94/5911/1.jpg?7586', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(35, 'OT776EL17F5ZWNAFAMZ', 'VR Box With VR Wireless Game Pad - Black/White', 5, 'https://www.daraz.com.np/other-vr-box-with-vr-wireless-game-pad-blackwhite-113927.html', 'https://np.daraz.io/_avGgcS5oh1NcD5WZnWVHs0179Q=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/72/9311/1.jpg?8930', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(36, 'OT776EL0H3M1CNAFAMZ', 'Combo Of Sim Supporting Smartwatch + Bluetooth Earphone', 4, 'https://www.daraz.com.np/other-combo-of-sim-supporting-smartwatch-bluetooth-earphone-22782.html', 'https://np.daraz.io/3qtKE2JKvO7UAEUQ5HkPr1-1-ts=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/28/722/1.jpg?6226', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(37, 'OT776EL06TNFWNAFAMZ', '3 In 1 HDMI Switch- Black', 1, 'https://www.daraz.com.np/other-3-in-1-hdmi-switch-black-116411.html', 'https://np.daraz.io/savGui9YU02dqfG4G24TqUAqmAE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/11/4611/1.jpg?5541', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(38, 'OT776EL0UQFSGNAFAMZ', 'VR Box with Bluetooth Control Game Pad', 5, 'https://www.daraz.com.np/other-vr-box-with-bluetooth-control-game-pad-22615.html', 'https://np.daraz.io/V41idgwwbaTHVYrwWozdhGGlfBg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/622/1.jpg?6246', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(39, 'OT776EL1AQKLWNAFAMZ', 'Garmin Forerunner 620 2.5D Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-forerunner-620-2.5d-tempered-glass-screen-protector-120587.html', 'https://np.daraz.io/fYdZKm--tuIOgFBj9zMgMLXETaA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/78/5021/1.jpg?4797', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(40, 'OT776EL14GUU4NAFAMZ', 'S815 Hi-Fi Music Player Wireless Bluetooth Mini Speaker-Grey', 2, 'https://www.daraz.com.np/other-s815-hi-fi-music-player-wireless-bluetooth-mini-speaker-grey-117976.html', 'https://np.daraz.io/98EbdOqidLqAujDwjdJhBtqArhk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/67/9711/1.jpg?6857', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(41, 'OT776EL0UIOJONAFAMZ', 'Female To Female Jumper Wire 10cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-female-to-female-jumper-wire-10cm-20-pcs-106215.html', 'https://np.daraz.io/YBOMtx9D-plMMuAk8FJRa19LfTU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/2601/1.jpg?2188', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(42, 'OT776EL0YW9B4NAFAMZ', 'Combo of VR Box + Earphone And Gaming Remote', 5, 'https://www.daraz.com.np/other-combo-of-vr-box-earphone-and-gaming-remote-21685.html', 'https://np.daraz.io/DBSIssRJmQups2ED0xykZdprz4c=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/612/1.jpg?5941', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(43, 'ON440EL0SMQK4NAFAMZ', 'Smart Watch - i7 Supports Sim/TF Card/Camera', 4, 'https://www.daraz.com.np/onlineshopgroup-smart-watch-i7-supports-simtf-cardcamera-109084.html', 'https://np.daraz.io/9D5OYel-uo4q7orOJ86Gdgq-75E=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/48/0901/1.jpg?1636', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(44, 'OT776EL1MGF9CNAFAMZ', 'SOMHO S311 Portable Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-somho-s311-portable-bluetooth-speaker-48189.html', 'https://np.daraz.io/QLT_bsZpzsnwPQZVD0AmePYLwcc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/98/184/1.jpg?9728', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(45, 'OT776EL05L3YWNAFAMZ', 'Yash Vision Mhl To Hdmi Media Adapter Kit 6.5 Feet (2M) Universal Mhl Micro Usb To Hdmi Cable 1080P Hdtv Adapter', 1, 'https://www.daraz.com.np/other-yash-vision-mhl-to-hdmi-media-adapter-kit-6.5-feet-2m-universal-mhl-micro-usb-to-hdmi-cable-1080p-hdtv-adapter-38390.html', 'https://np.daraz.io/vKiwtq6Hs4585g0aJpomGJ71xXk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/09/383/1.jpg?5415', '2018-06-03 06:43:30', '2018-06-03 06:50:48'),
(46, 'OT776EL0FCRRONAFAMZ', 'BOBO VR Z4 Virtual Reality 3D Glasses With Headphones-White', 5, 'https://www.daraz.com.np/other-bobo-vr-z4-virtual-reality-3d-glasses-with-headphones-white-109752.html', 'https://np.daraz.io/OdZGR6ZYe8LTzppgDJysiwHU4R4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/25/7901/1.jpg?0057', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(47, 'OT776EL1AE1WWNAFAMZ', 'Multi-function USB All-in-1 Combo Hub with 4 Card Readers & 3 USB Ports', 1, 'https://www.daraz.com.np/other-multi-function-usb-all-in-1-combo-hub-with-4-card-readers-3-usb-ports-81977.html', 'https://np.daraz.io/XrEuBGf2xEvdN3Q7mp9uEocPL_4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/77/918/1.jpg?6965', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(48, 'OT776EL1H1C40NAFAMZ', 'Rugby Design Bluetooth Speaker (AUS, USB, TF, FM)', 2, 'https://www.daraz.com.np/other-rugby-design-bluetooth-speaker-aus-usb-tf-fm-28098.html', 'https://np.daraz.io/Yz1uoGnIT09PHRtFYSTIhF9TOtM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/89/082/1.jpg?2235', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(49, 'OT776EL1GOWNONAFAMZ', 'Garmin Forerunner 630 2.5D Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-forerunner-630-2.5d-tempered-glass-screen-protector-120588.html', 'https://np.daraz.io/ArL_zC4E94kBlM6L3r6Yme2qDek=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/88/5021/1.jpg?4797', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(50, 'OT776EL04J5GGNAFAMZ', 'Premium VR Box with Bluetooth Game Pad', 5, 'https://www.daraz.com.np/other-premium-vr-box-with-bluetooth-game-pad-21670.html', 'https://np.daraz.io/2dbn9Ub9yvQedFkxEeoc4w40Qww=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/07/612/1.jpg?5949', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(51, 'OT776EL0AB91ONAFAMZ', 'DVI Male To VGA Female Adapter Converter', 1, 'https://www.daraz.com.np/other-dvi-male-to-vga-female-adapter-converter-112371.html', 'https://np.daraz.io/B2affbrLTjzD3pPinIRhQ7Gfldc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/17/3211/1.jpg?5542', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(52, 'OT776EL0GYWD0NAFAMZ', 'Garmin Approach S6 Watch Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-approach-s6-watch-tempered-glass-screen-protector-120582.html', 'https://np.daraz.io/vLzMpwdQJQkKgToOil23fbejlwI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/28/5021/1.jpg?4638', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(53, 'OT776EL0UK6HCNAFAMZ', 'Mini Bluetooth Music Speaker', 2, 'https://www.daraz.com.np/other-mini-bluetooth-music-speaker-3315.html', 'https://np.daraz.io/pRoi4VJYpC00hbY7cvTZlGa0ytg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/33/1.jpg?2026', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(54, 'OT776EL0SCHNKNAFAMZ', 'VR Shinecon 3D Glasses With Wireless Remote Control Gamepad', 5, 'https://www.daraz.com.np/other-vr-shinecon-3d-glasses-with-wireless-remote-control-gamepad-21674.html', 'https://np.daraz.io/ZxlsT6NIhYWd6PPSIETy1dMkPYQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/47/612/1.jpg?5945', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(55, 'ON440EL1C58LSNAFAMZ', 'Combo of i6 and D3 Smartwatch', 4, 'https://www.daraz.com.np/onlineshopgroup-combo-of-i6-and-d3-smartwatch-66808.html', 'https://np.daraz.io/oNpQ1RQgCq5Jn1oZO4lwJ-nAQg0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/80/866/1.jpg?5507', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(56, 'OT776EL0NCDUWNAFAMZ', 'VGA Connector, 15 VGA SVGA KVM Female to Female Gender Changer Adapter', 1, 'https://www.daraz.com.np/other-vga-connector-15-vga-svga-kvm-female-to-female-gender-changer-adapter-90293.html', 'https://np.daraz.io/24mjLvgkltCBxxOi6aGUjxdxS-U=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/39/209/1.jpg?7165', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(57, 'OT776EL11PDQONAFAMZ', 'Mini Portable Bluetooth Speaker With Built-in Mic (Color & Print Varied)', 2, 'https://www.daraz.com.np/other-mini-portable-bluetooth-speaker-with-built-in-mic-color-print-varied-3336.html', 'https://np.daraz.io/t7i7r9EO3UkxBQU_gbsQC4P0iAg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/63/33/1.jpg?7585', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(58, 'SO445EL0YBIE8NAFAMZ', 'Soft Vision Bundle of 3 - VR Box Shinecon 4th Generation, Bluetooth Gaming Remote &  Earphone', 5, 'https://www.daraz.com.np/soft-vision-bundle-of-3-vr-box-shinecon-4th-generation-bluetooth-gaming-remote-earphone-44675.html', 'https://np.daraz.io/6-agZfvOsHD3vj4tIT2sxNwCAb4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/57/644/1.jpg?5213', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(59, 'OT776EL14S8K4NAFAMZ', 'Garmin Forerunner 235 2.5D Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-forerunner-235-2.5d-tempered-glass-screen-protector-120586.html', 'https://np.daraz.io/KFoXPSz8RmR0zx-v8FLlVSGCUq4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/68/5021/1.jpg?4755', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(60, 'OT776EL0UOGVONAFAMZ', 'Mini Bluetooth Speaker - White', 2, 'https://www.daraz.com.np/other-mini-bluetooth-speaker-white-103515.html', 'https://np.daraz.io/7RfeBuBuGz-yRhOSEcVIG9BMw6Q=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/5301/1.jpg?7938', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(61, 'AA370EL12WC1CNAFAMZ', 'EastVita 5Ft 1.5m HDMI To 3-RCA Video Audio AV Component Converter Adapter Cable For HDTV DVD', 1, 'https://www.daraz.com.np/other-eastvita-5ft-1.5m-hdmi-to-3-rca-video-audio-av-component-converter-adapter-cable-for-hdtv-dvd-43356.html', 'https://np.daraz.io/n0Iu4NJtlvlltMqRkxYpx938ceI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/65/334/1.jpg?6648', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(62, 'OT776EL0OM1DKNAFAMZ', 'VR Box Version 2.0 - Virtual Reality 3D Glasses', 5, 'https://www.daraz.com.np/other-vr-box-version-2.0-virtual-reality-3d-glasses-93314.html', 'https://np.daraz.io/56DuWXIckSop20HIKNqsCw9Xcsw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/41/339/1.jpg?3595', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(63, 'OT776EL0WXDM0NAFAMZ', 'Mini Hands Free Outdoor Bluetooth Speaker with Sound Quality', 2, 'https://www.daraz.com.np/other-mini-hands-free-outdoor-bluetooth-speaker-with-sound-quality-50355.html', 'https://np.daraz.io/AiGPhwrkjR_lIVF0pQqUii6oiPs=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/55/305/1.jpg?6485', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(64, 'OT776EL0TH02CNAFAMZ', 'Garmin Fenix Chronos Tempered Glass Screen Protector 2.5D High Definition 9H', 4, 'https://www.daraz.com.np/other-garmin-fenix-chronos-tempered-glass-screen-protector-2.5d-high-definition-9h-120594.html', 'https://np.daraz.io/lfTqZV0f94MEr_N5tEWzpXY6QyU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/5021/1.jpg?5315', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(65, 'OT776EL07ARYCNAFAMZ', 'Male To Female Jumper Wire 10cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-male-to-female-jumper-wire-10cm-20-pcs-106221.html', 'https://np.daraz.io/bYt1c2ztynT9VDln8nTrm6D55H4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/2601/1.jpg?2188', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(66, 'OT776EL13T64WNAFAMZ', 'VR Shinecon 3D Glasses + Wireless Remote Control Gamepad', 5, 'https://www.daraz.com.np/other-vr-shinecon-3d-glasses-wireless-remote-control-gamepad-66866.html', 'https://np.daraz.io/ftOpdeQC4Bu9eW2T7T-YHpo6BNo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/66/866/1.jpg?7206', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(67, 'OT776EL0XOWCONAFAMZ', 'X6 Curved Smart Watch', 4, 'https://www.daraz.com.np/other-x6-curved-smart-watch-98565.html', 'https://np.daraz.io/hLKRikyQOIqRm39KjtBNVYKwqk0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/56/589/1.jpg?6236', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(68, 'OT776EL0TBDWKNAFAMZ', 'USB Type C To HDMI Adapter', 1, 'https://www.daraz.com.np/other-usb-type-c-to-hdmi-adapter-104294.html', 'https://np.daraz.io/FWqESj4gxE2GrEOIfnl7zrxS7Gc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/2401/1.jpg?8338', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(69, 'OT776EL0USD8GNAFAMZ', 'VR Shinecon Combo Premium VR Glass + Remote', 5, 'https://www.daraz.com.np/other-vr-shinecon-combo-premium-vr-glass-remote-21715.html', 'https://np.daraz.io/dG1d6fYYibsnG8WLdpVYSEacNXc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/712/1.jpg?5984', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(70, 'OT776EL16Q2G4NAFAMZ', 'Metal Mini Portable Wireless Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-metal-mini-portable-wireless-bluetooth-speaker-106717.html', 'https://np.daraz.io/IMlw3ZpsmfMuW_Imt39QRKvhIE4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/71/7601/1.jpg?4105', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(71, 'OT776EL1JI138NAFAMZ', 'X2 Smart Watch Bluetooth Sport Fitness Tracker Heart Rate', 4, 'https://www.daraz.com.np/other-x2-smart-watch-bluetooth-sport-fitness-tracker-heart-rate-102239.html', 'https://np.daraz.io/7Cb-Vq1XdMAXmU0c_kgSI7DsAos=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/93/2201/1.jpg?3696', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(72, 'OT776EL07MZOWNAFAMZ', 'Portable Bluetooth Speaker With USB + TF Card + FM Radio (JY-25)', 2, 'https://www.daraz.com.np/other-portable-bluetooth-speaker-with-usb-tf-card-fm-radio-jy-25-3821.html', 'https://np.daraz.io/ywMDE6cqb4yoT8_ahIMtQ4YXJ-8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/83/1.jpg?1917', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(73, 'OT776EL10H0LGNAFAMZ', 'Male To Male Jumper Wire 10cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-male-to-male-jumper-wire-10cm-20-pcs-106216.html', 'https://np.daraz.io/QyWBkUIJr3D914Cafktnfm7CVj0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/61/2601/1.jpg?2188', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(74, 'OT776EL0C9KOKNAFAMZ', 'Citizen Watch NY0040-09EE Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-citizen-watch-ny0040-09ee-tempered-glass-screen-protector-120602.html', 'https://np.daraz.io/p2AAc5SCTyr3gNQ5M4DXqogDW7E=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/20/6021/1.jpg?5516', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(75, 'OT776EL0PO95CNAFAMZ', 'VR Shinecon with Gamepad - Pleasing Eye Effect', 5, 'https://www.daraz.com.np/other-vr-shinecon-with-gamepad-pleasing-eye-effect-22134.html', 'https://np.daraz.io/b5TG59H_DMo_hniad-0KowtOnGo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/43/122/1.jpg?6044', '2018-06-03 06:43:30', '2018-06-03 06:50:52'),
(76, 'AA370EL0A4SSKNAFAMZ', '2 in 1 Lightning Adapter Headphone For iPhone X 8/8/7/7 Plus', 1, 'https://www.daraz.com.np/other-2-in-1-lightning-adapter-headphone-for-iphone-x-8877-plus-102071.html', 'https://np.daraz.io/EMm7r6lt0A2u3iiaho8I2dVYAh0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/17/0201/1.jpg?1560', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(77, 'WK851EL13BHN0NAFAMZ', 'W-KING S20 Portable Waterproof Bluetooth Super Bass Loudspeaker- Blue', 2, 'https://www.daraz.com.np/w-king-s20-portable-waterproof-bluetooth-super-bass-loudspeaker-blue-114066.html', 'https://np.daraz.io/aqSLcGfTfKqfv2GAuoi5ta0s41k=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/66/0411/1.jpg?5734', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(78, 'OT776EL13L5K0NAFAMZ', 'I7 Bluetooth Smartwatch', 4, 'https://www.daraz.com.np/other-i7-bluetooth-smartwatch-29466.html', 'https://np.daraz.io/ybxI-3UXx-Sc-meU5GQSkK5bugE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/66/492/1.jpg?6748', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(79, 'OT776EL02GY5SNAFAMZ', 'VR Box (VR02)- White', 5, 'https://www.daraz.com.np/other-vr-box-vr02-white-5140.html', 'https://np.daraz.io/8zKZE-UYTQGhfz7ZvEhlRK-hvwE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/04/15/1.jpg?1893', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(80, 'OT776EL0O8LKWNAFAMZ', 'Music Mini Box Bluetooth Speaker - Black', 2, 'https://www.daraz.com.np/ab-tech-music-mini-box-bluetooth-speaker-black-21704.html', 'https://np.daraz.io/FVZBRo41_yxyMlAO0v2UjIPVDj0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/40/712/1.jpg?6887', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(81, 'OT776EL1AKYG4NAFAMZ', 'USB C To Micro USB Adapter Convert Connector', 1, 'https://www.daraz.com.np/other-usb-c-to-micro-usb-adapter-convert-connector-104287.html', 'https://np.daraz.io/_PFYIRZHA5RufodCjmFUFHhMqZg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/78/2401/1.jpg?7618', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(82, 'OT776EL15DO5WNAFAMZ', 'Citizen Watch BM8475 Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-citizen-watch-bm8475-tempered-glass-screen-protector-120596.html', 'https://np.daraz.io/EuvwMA2hUn3NjmRULjjueVyjwRg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/69/5021/1.jpg?5396', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(83, 'OT776EL1LN8ESNAFAMZ', 'VR Shinecon 3D Glasses + Wireless Remote Control Gamepad-Black', 5, 'https://www.daraz.com.np/other-vr-shinecon-3d-glasses-wireless-remote-control-gamepad-black-122869.html', 'https://np.daraz.io/rW_YuRGuR4JbYUozaOxR1OERV6o=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/96/8221/1.jpg?4749', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(84, 'OT776EL0WXQ18NAFAMZ', '1080P HDMI Male To VGA Female Adapter Converter Cable For PC/HDTV/Laptop', 1, 'https://www.daraz.com.np/other-1080p-hdmi-male-to-vga-female-adapter-converter-cable-for-pchdtvlaptop-112355.html', 'https://np.daraz.io/S_NXvl6kCuw-mMB656dAfKNvJZE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/55/3211/1.jpg?2447', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(85, 'OT776EL16L4Z8NAFAMZ', 'Charge 2+ Waterproof Wireless Portable Speaker - Black', 2, 'https://www.daraz.com.np/other-charge-2-waterproof-wireless-portable-speaker-black-103517.html', 'https://np.daraz.io/qycz-AF_pe8ubhuS6iZbXOxLgRE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/71/5301/1.jpg?8739', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(86, 'OT776EL0BLZX0NAFAMZ', 'Moto 360 2nd Gen 42mm Smart Watch Tempered Glass Anti-Scratch', 4, 'https://www.daraz.com.np/other-moto-360-2nd-gen-42mm-smart-watch-tempered-glass-anti-scratch-120591.html', 'https://np.daraz.io/kxdTb62fyKZowfId_35p9aLPpjI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/19/5021/1.jpg?4955', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(87, 'OT776EL062JA8NAFAMZ', 'Combo of VR Box With Gaming Remote Controller and  Earphone', 5, 'https://www.daraz.com.np/other-combo-of-vr-box-with-gaming-remote-controller-and-earphone-69101.html', 'https://np.daraz.io/S2ldOvluhBl7Wrk9uEu57AoG3uA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/196/1.jpg?3447', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(88, 'OT776EL1AD5I8NAFAMZ', 'JC 176 Dual Driver Dual Diaphragm HiFi Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-jc-176-dual-driver-dual-diaphragm-hifi-bluetooth-speaker-67877.html', 'https://np.daraz.io/goi-nmExg6rjzDhhnuX8hsTAcxA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/77/876/1.jpg?9007', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(89, 'SO445EL0REK7CNAFAMZ', 'Soft Vision 10 Meter Long HDMI To HDMI Cable', 1, 'https://www.daraz.com.np/soft-vision-10-meter-long-hdmi-to-hdmi-cable-92064.html', 'https://np.daraz.io/8AtB-xDImJ3Tdncd2zpFV6lTmlg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/46/029/1.jpg?5704', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(90, 'OT776EL1B4E7SNAFAMZ', 'X6 Bluetooth Smart Watch With Camera SIM Memory Card - (White/Black)', 4, 'https://www.daraz.com.np/other-x6-bluetooth-smart-watch-with-camera-sim-memory-card-whiteblack-74197.html', 'https://np.daraz.io/Rbu6yCJV-EarDY3sSQOqzLuRyvQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/147/1.jpg?8287', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(91, 'OT776EL0ME5LSNAFAMZ', 'VR Shinecon With Gamepad - Pleasing Eye Effect', 5, 'https://www.daraz.com.np/other-vr-shinecon-with-gamepad-pleasing-eye-effect-21673.html', 'https://np.daraz.io/w3KKXOQ_JViG1Zz8LxyQEwk_mOk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/37/612/1.jpg?5947', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(92, 'OT776EL0XD3YWNAFAMZ', 'New Design WS-Y66B Portable Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-new-design-ws-y66b-portable-bluetooth-speaker-93065.html', 'https://np.daraz.io/9ueIZm4QtbQfA_m1ubJ__soiM7Q=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/56/039/1.jpg?1887', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(93, 'OT776EL0P5S3ONAFAMZ', 'Female To Female Jumper Wire 20cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-female-to-female-jumper-wire-20cm-20-pcs-106224.html', 'https://np.daraz.io/bPWvrY9Cga3xWyCMhInpvLkQrV4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/42/2601/1.jpg?2188', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(94, 'OT776EL0MX8ESNAFAMZ', 'Garmin Forerunner 220 2.5D High Definition 9H Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-forerunner-220-2.5d-high-definition-9h-tempered-glass-screen-protector-120583.html', 'https://np.daraz.io/muh16zske-jI-gcYxDyc6UT6GgA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/38/5021/1.jpg?4638', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(95, 'OT776EL1EFO74NAFAMZ', 'VR Box with Bluetooth Control Game Pad', 5, 'https://www.daraz.com.np/bestdeals-vr-box-with-bluetooth-control-game-pad-21748.html', 'https://np.daraz.io/X-PrJfi_GpfieGqTyNb89ocB8Bg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/84/712/1.jpg?0444', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(96, 'OT776EL0M3DHKNAFAMZ', 'USB 2.0 A Female to A Female Coupler Adapter For USB Cable', 1, 'https://www.daraz.com.np/other-usb-2.0-a-female-to-a-female-coupler-adapter-for-usb-cable-90173.html', 'https://np.daraz.io/NmHWkDt2iOmkyv8Oe3EUSApAUlo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/37/109/1.jpg?8006', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(97, 'OT776EL1ETWJKNAFAMZ', 'Music Mini Box Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-music-mini-box-bluetooth-speaker-67358.html', 'https://np.daraz.io/5GYZbjFk1B8dAY2Ft4Tp_0s7k-w=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/85/376/1.jpg?6785', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(98, 'OT776EL1IMZ18NAFAMZ', 'D3 Bluetooth Smartwatch - Black', 4, 'https://www.daraz.com.np/other-d3-bluetooth-smartwatch-black-117719.html', 'https://np.daraz.io/lXBH6B1MZYf8yVH4yxj9QOOTNfE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/91/7711/1.jpg?9705', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(99, 'OT776EL0AHHI8NAFAMZ', 'VR Box (VR02)', 5, 'https://www.daraz.com.np/other-vr-box-vr02-21671.html', 'https://np.daraz.io/oRokJHdnSBMvixwxrwQ3CYyo0eQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/17/612/1.jpg?5949', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(100, 'BE416EL0TX184NAFAMZ', 'Y1 Bluetooth Smartwatch With SIM Slot', 4, 'https://www.daraz.com.np/bestchoice-y1-bluetooth-smartwatch-with-sim-slot-105205.html', 'https://np.daraz.io/I2y9cxnjTiiAr5mEYIpz8n9HTx0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/50/2501/1.jpg?0057', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(101, 'OT776EL0J7G1WNAFAMZ', 'Male To Male Jumper Wire 20cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-male-to-male-jumper-wire-20cm-20-pcs-106223.html', 'https://np.daraz.io/mMqvvHbHEfvy-D1znhCm-7FrxW8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/32/2601/1.jpg?2188', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(102, 'OT776EL0WFWR4NAFAMZ', 'VR Box With Bluetooth Control Gamepad', 5, 'https://www.daraz.com.np/other-vr-box-with-bluetooth-control-gamepad-9445.html', 'https://np.daraz.io/PUYlGVIm2ll3UF-9xS1_Wonq_mg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/54/49/1.jpg?7450', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(103, 'AA370EL0YLI1GNAFAMZ', 'USB C To Micro USB Adapter Convert Connector', 1, 'https://www.daraz.com.np/other-usb-c-to-micro-usb-adapter-convert-connector-101185.html', 'https://np.daraz.io/nj1WC_NJ3OoDPGiYrSOXKRD1T9M=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/1101/1.jpg?0042', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(104, 'ON440EL0Q2JT4NAFAMZ', 'Uwatch U11C Smart Watch Phone Bluetooth MTK2502 Remote Camera', 4, 'https://www.daraz.com.np/onlineshopgroup-uwatch-u11c-smart-watch-phone-bluetooth-mtk2502-remote-camera-98734.html', 'https://np.daraz.io/bYObczviBvNiRn5mApXm0NTIYT4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/43/789/1.jpg?2093', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(105, 'OT776EL12HI5WNAFAMZ', 'Z4 3D Glasses VR Box With Headphones-White', 5, 'https://www.daraz.com.np/other-z4-3d-glasses-vr-box-with-headphones-white-124646.html', 'https://np.daraz.io/4gQGwB9shHDV_tLl5P6DLtFbT94=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/64/6421/1.jpg?3445', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(106, 'OT776EL1MN8PGNAFAMZ', 'Moto 360 1st Gen 46mm Smart Watch Tempered Glass', 4, 'https://www.daraz.com.np/other-moto-360-1st-gen-46mm-smart-watch-tempered-glass-120589.html', 'https://np.daraz.io/uqaNMCFmlId7sZOSdzGQbcwvTVU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/98/5021/1.jpg?4876', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(107, 'OT776EL1MZYYONAFAMZ', 'VR 2.0 Generation With 360 HD Video Play Along/Motion/Detection/Rotation', 5, 'https://www.daraz.com.np/other-vr-2.0-generation-with-360-hd-video-play-alongmotiondetectionrotation-69099.html', 'https://np.daraz.io/l2NCRZTK7QOseNNrSdIemMtDp7U=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/99/096/1.jpg?3447', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(108, 'OT776EL0ZDSK4NAFAMZ', 'Apple Macbook Pro Type-C Hub Adapter 7 in 1 With HDMI', 1, 'https://www.daraz.com.np/other-apple-macbook-pro-type-c-hub-adapter-7-in-1-with-hdmi-103495.html', 'https://np.daraz.io/NsGiPsWa7ygxlJB_ttcOHUkbwZA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/59/4301/1.jpg?5538', '2018-06-03 06:43:32', '2018-06-03 06:50:51'),
(109, 'ON440EL0VE0MSNAFAMZ', 'X6 Bluetooth Smartwatch With Camera Support SIM Card', 4, 'https://www.daraz.com.np/onlineshopgroup-x6-bluetooth-smartwatch-with-camera-support-sim-card-122725.html', 'https://np.daraz.io/rKLKH1-y9hOp5CdLuqhBDnrNstI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/52/7221/1.jpg?8429', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(110, 'OT776EL0I94MWNAFAMZ', 'USB 2.0 Type A Male to A Female Extension Cable 3 Meter - Black', 1, 'https://www.daraz.com.np/other-usb-2.0-type-a-male-to-a-female-extension-cable-3-meter-black-95603.html', 'https://np.daraz.io/a5uzgsRy6G7CAWuRcCFTC9AkFBM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/30/659/1.jpg?1285', '2018-06-03 06:43:32', '2018-06-03 06:50:51'),
(111, 'OT776EL0HKBYSNAFAMZ', 'Samsung Gear S3 Tempered Glass Screen Protecto 2.5D High Definition 9H', 4, 'https://www.daraz.com.np/other-samsung-gear-s3-tempered-glass-screen-protecto-2.5d-high-definition-9h-120592.html', 'https://np.daraz.io/X266OtOLq2w8p5evYKzjBqWq5fE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/29/5021/1.jpg?5156', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(112, 'OT776EL0M7X58NAFAMZ', 'Gold Plated Mini DP To DVI VGA HDMI  3 In 1 Cable', 1, 'https://www.daraz.com.np/other-gold-plated-mini-dp-to-dvi-vga-hdmi-3-in-1-cable-112373.html', 'https://np.daraz.io/L2dMbzG-MyO0irpgXD8j_X7buEo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/37/3211/1.jpg?6262', '2018-06-03 06:43:32', '2018-06-03 06:50:52'),
(113, 'OT776EL0RTTNWNAFAMZ', 'U8 Smartwatch', 4, 'https://www.daraz.com.np/other-u8-smartwatch-114764.html', 'https://np.daraz.io/yBWcFWMO5johtaWMeRoaNGg2CZE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/46/7411/1.jpg?9253', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(114, 'KP432EL14VD4WNAFAMZ', 'Type-C Male to Micro USB Female Converter Syncing Charging', 1, 'https://www.daraz.com.np/kpitsolution-type-c-male-to-micro-usb-female-converter-syncing-charging-84686.html', 'https://np.daraz.io/2__dMvVpQqUX1XxnJwvenOOGjQ4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/68/648/1.jpg?9845', '2018-06-03 06:43:32', '2018-06-03 06:50:52'),
(115, 'OT776EL0USKY8NAFAMZ', 'Black Smartwatch - Gt08', 4, 'https://www.daraz.com.np/other-black-smartwatch-gt08-22715.html', 'https://np.daraz.io/bb4QHf2Qsr0H175YUUn42fT60qU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/722/1.jpg?2085', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(116, 'AA370EL1L6FE8NAFAMZ', '3.5mm Audio Cable Male to 2 Female Aux Cable Stereo Jack Splitter Cable Adapter', 1, 'https://www.daraz.com.np/other-3.5mm-audio-cable-male-to-2-female-aux-cable-stereo-jack-splitter-cable-adapter-83069.html', 'https://np.daraz.io/FWG2iD0HRcqyP9ncFAOaX2cVyM0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/96/038/1.jpg?1026', '2018-06-03 06:43:32', '2018-06-03 06:50:52'),
(117, 'OT776EL065LMGNAFAMZ', 'M2 Intelligence Health Bracelet - (Black)', 4, 'https://www.daraz.com.np/other-m2-intelligence-health-bracelet-black-93301.html', 'https://np.daraz.io/fxz8gGBu_j3rxMizu7idW9FvjU4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/339/1.jpg?7966', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(118, 'ON440EL04L2Z8NAFAMZ', 'Round Waterproof Blood Pressure/Heart Rate Monitor Smartwatch', 4, 'https://www.daraz.com.np/onlineshopgroup-round-waterproof-blood-pressureheart-rate-monitor-smartwatch-120770.html', 'https://np.daraz.io/xU0tOC14XnTIZFzoK8zcv40voaA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/07/7021/1.jpg?8035', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(119, 'OT776OT05YCTKNAFAMZ', 'HDMI Male to VGA + Audio Converter Cable For PC/Laptop', 1, 'https://www.daraz.com.np/other-hdmi-male-to-vga-audio-converter-cable-for-pclaptop-10001.html', 'https://np.daraz.io/2AH5oGzwgsdll8LfOMBB5siacHI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/001/1.jpg?5553', '2018-06-03 06:43:32', '2018-06-03 06:50:52'),
(120, 'OT776EL0ZDT94NAFAMZ', '1080P HDTV HDMI Male To 3 RCA Audio Video AV Cable Cord Adapter', 1, 'https://www.daraz.com.np/other-1080p-hdtv-hdmi-male-to-3-rca-audio-video-av-cable-cord-adapter-13495.html', 'https://np.daraz.io/4DwA7OWc7ANltnWMPXh3L6OPXdg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/59/431/1.jpg?5836', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(121, 'OT776OT1CEBRKNAFAMZ', '5 Meter Long HDMI To HDMI Cable', 1, 'https://www.daraz.com.np/other-5-meter-long-hdmi-to-hdmi-cable-9218.html', 'https://np.daraz.io/qATzcLa_TSTUQEoA8Fw2-3z2-98=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/81/29/1.jpg?2773', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(122, 'OT776OT0W5FFSNAFAMZ', 'HDMI-HDMI 10 Meter Cable', 1, 'https://www.daraz.com.np/other-hdmi-hdmi-10-meter-cable-10045.html', 'https://np.daraz.io/xiEiWQ2TIi49_9csF_2suZYWPqw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/54/001/1.jpg?1087', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(123, 'OT776EL0X8LXKNAFAMZ', '4ft USB 2.0 A Type Male to DC 5.5 x 2.1mm DC 5V Power Plug Connector Cable', 1, 'https://www.daraz.com.np/other-4ft-usb-2.0-a-type-male-to-dc-5.5-x-2.1mm-dc-5v-power-plug-connector-cable-92855.html', 'https://np.daraz.io/bYSlk30zlFZiaZqeqd6ME7-JOmU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/55/829/1.jpg?0885', '2018-06-03 06:43:32', '2018-06-03 06:50:53');

-- --------------------------------------------------------

--
-- Table structure for table `target_pages`
--

CREATE TABLE `target_pages` (
  `id` int(11) NOT NULL,
  `url` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `target_pages`
--

INSERT INTO `target_pages` (`id`, `url`, `description`) VALUES
(1, 'https://www.daraz.com.np/cables/', 'Cables'),
(3, 'https://www.daraz.com.np/mobiles-tablets-smartwatches', 'Mobile devices'),
(4, 'https://www.daraz.com.np/wireless-speakers/', 'Wireless Speakers'),
(5, 'https://www.daraz.com.np/vr-headsets/', 'VR Headsets');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `category_id` (`id`);

--
-- Indexes for table `prices`
--
ALTER TABLE `prices`
  ADD PRIMARY KEY (`id`),
  ADD KEY `price_link` (`prod_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sku` (`sku`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `target_pages`
--
ALTER TABLE `target_pages`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `prices`
--
ALTER TABLE `prices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=247;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=124;

--
-- AUTO_INCREMENT for table `target_pages`
--
ALTER TABLE `target_pages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `prices`
--
ALTER TABLE `prices`
  ADD CONSTRAINT `price_link` FOREIGN KEY (`prod_id`) REFERENCES `products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
=======
-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2018 at 12:22 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `testdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'Cables'),
(2, 'Wireless Speakers'),
(3, 'Computing & Gaming'),
(4, 'Smartwatches'),
(5, 'VR Headsets');

-- --------------------------------------------------------

--
-- Table structure for table `prices`
--

CREATE TABLE `prices` (
  `id` int(11) NOT NULL,
  `prod_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `discount` varchar(4) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `currency_iso` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `prices`
--

INSERT INTO `prices` (`id`, `prod_id`, `price`, `discount`, `date`, `currency_iso`) VALUES
(1, 1, 399, '-17%', '2018-06-03 06:43:27', 'NPR'),
(2, 2, 749, '-25%', '2018-06-03 06:43:27', 'NPR'),
(3, 3, 750, '-63%', '2018-06-03 06:43:28', 'NPR'),
(4, 4, 1199, '-52%', '2018-06-03 06:43:28', 'NPR'),
(5, 5, 400, '-16%', '2018-06-03 06:43:28', 'NPR'),
(6, 8, 375, '-25%', '2018-06-03 06:43:28', 'NPR'),
(7, 6, 1299, '-37%', '2018-06-03 06:43:28', 'NPR'),
(8, 7, 619, '-31%', '2018-06-03 06:43:28', 'NPR'),
(9, 9, 420, '-35%', '2018-06-03 06:43:28', 'NPR'),
(10, 10, 1449, '-24%', '2018-06-03 06:43:29', 'NPR'),
(11, 11, 1249, '-55%', '2018-06-03 06:43:29', 'NPR'),
(12, 12, 1760, '-20%', '2018-06-03 06:43:29', 'NPR'),
(13, 13, 1088, '-56%', '2018-06-03 06:43:29', 'NPR'),
(14, 14, 799, '-21%', '2018-06-03 06:43:29', 'NPR'),
(15, 15, 69, '-66%', '2018-06-03 06:43:29', 'NPR'),
(16, 16, 2945, '-24%', '2018-06-03 06:43:29', 'NPR'),
(17, 17, 1249, '-51%', '2018-06-03 06:43:29', 'NPR'),
(18, 18, 1199, '-40%', '2018-06-03 06:43:29', 'NPR'),
(19, 19, 125, '-17%', '2018-06-03 06:43:29', 'NPR'),
(20, 20, 450, '-36%', '2018-06-03 06:43:29', 'NPR'),
(21, 21, 500, '-38%', '2018-06-03 06:43:29', 'NPR'),
(22, 22, 499, '-29%', '2018-06-03 06:43:29', 'NPR'),
(23, 23, 1049, '-45%', '2018-06-03 06:43:29', 'NPR'),
(24, 24, 1019, '-29%', '2018-06-03 06:43:29', 'NPR'),
(25, 25, 1499, '-32%', '2018-06-03 06:43:29', 'NPR'),
(26, 26, 500, '-38%', '2018-06-03 06:43:29', 'NPR'),
(27, 27, 1500, '-40%', '2018-06-03 06:43:29', 'NPR'),
(28, 31, 700, '-30%', '2018-06-03 06:43:29', 'NPR'),
(29, 29, 359, '-64%', '2018-06-03 06:43:29', 'NPR'),
(30, 28, 700, '-30%', '2018-06-03 06:43:29', 'NPR'),
(31, 30, 1799, '-10%', '2018-06-03 06:43:29', 'NPR'),
(32, 32, 1499, '-35%', '2018-06-03 06:43:29', 'NPR'),
(33, 33, 1149, '-43%', '2018-06-03 06:43:29', 'NPR'),
(34, 34, 1888, '-6%', '2018-06-03 06:43:29', 'NPR'),
(35, 35, 799, '-20%', '2018-06-03 06:43:29', 'NPR'),
(36, 36, 1799, '-37%', '2018-06-03 06:43:29', 'NPR'),
(37, 37, 1649, '-34%', '2018-06-03 06:43:29', 'NPR'),
(38, 40, 700, '-30%', '2018-06-03 06:43:29', 'NPR'),
(39, 39, 500, '-38%', '2018-06-03 06:43:29', 'NPR'),
(40, 38, 645, '-16%', '2018-06-03 06:43:29', 'NPR'),
(41, 41, 100, '-13%', '2018-06-03 06:43:29', 'NPR'),
(42, 42, 999, '-41%', '2018-06-03 06:43:30', 'NPR'),
(43, 43, 1349, '-39%', '2018-06-03 06:43:30', 'NPR'),
(44, 44, 1799, '-40%', '2018-06-03 06:43:30', 'NPR'),
(45, 45, 899, '-40%', '2018-06-03 06:43:30', 'NPR'),
(46, 46, 2399, '-20%', '2018-06-03 06:43:30', 'NPR'),
(47, 47, 400, '-50%', '2018-06-03 06:43:30', 'NPR'),
(48, 48, 999, '-4%', '2018-06-03 06:43:30', 'NPR'),
(49, 49, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(50, 50, 799, '-20%', '2018-06-03 06:43:30', 'NPR'),
(51, 51, 800, '-27%', '2018-06-03 06:43:30', 'NPR'),
(52, 52, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(53, 53, 340, '-48%', '2018-06-03 06:43:30', 'NPR'),
(54, 54, 1140, '-24%', '2018-06-03 06:43:30', 'NPR'),
(55, 55, 2099, '-40%', '2018-06-03 06:43:30', 'NPR'),
(56, 57, 380, '-31%', '2018-06-03 06:43:30', 'NPR'),
(57, 56, 199, '-60%', '2018-06-03 06:43:30', 'NPR'),
(58, 58, 1600, '-11%', '2018-06-03 06:43:30', 'NPR'),
(59, 59, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(60, 61, 899, '-55%', '2018-06-03 06:43:30', 'NPR'),
(61, 60, 377, '-46%', '2018-06-03 06:43:30', 'NPR'),
(62, 62, 490, '-30%', '2018-06-03 06:43:30', 'NPR'),
(63, 66, 1099, '-27%', '2018-06-03 06:43:30', 'NPR'),
(64, 64, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(65, 63, 899, '-25%', '2018-06-03 06:43:30', 'NPR'),
(66, 65, 100, '-13%', '2018-06-03 06:43:30', 'NPR'),
(67, 67, 1699, '-55%', '2018-06-03 06:43:30', 'NPR'),
(68, 68, 3999, '-20%', '2018-06-03 06:43:30', 'NPR'),
(69, 70, 1000, '-33%', '2018-06-03 06:43:30', 'NPR'),
(70, 69, 1599, '-6%', '2018-06-03 06:43:30', 'NPR'),
(71, 71, 4499, '-20%', '2018-06-03 06:43:30', 'NPR'),
(72, 73, 100, '-13%', '2018-06-03 06:43:30', 'NPR'),
(73, 72, 1199, '-39%', '2018-06-03 06:43:30', 'NPR'),
(74, 74, 500, '-38%', '2018-06-03 06:43:30', 'NPR'),
(75, 75, 1649, '-15%', '2018-06-03 06:43:30', 'NPR'),
(76, 76, 849, '-43%', '2018-06-03 06:43:31', 'NPR'),
(77, 77, 2599, '-35%', '2018-06-03 06:43:31', 'NPR'),
(78, 78, 1099, '-56%', '2018-06-03 06:43:31', 'NPR'),
(79, 79, 599, '-40%', '2018-06-03 06:43:31', 'NPR'),
(80, 80, 444, '-11%', '2018-06-03 06:43:31', 'NPR'),
(81, 81, 149, '-50%', '2018-06-03 06:43:31', 'NPR'),
(82, 82, 500, '-38%', '2018-06-03 06:43:31', 'NPR'),
(83, 83, 1149, '-43%', '2018-06-03 06:43:31', 'NPR'),
(84, 84, 600, '-40%', '2018-06-03 06:43:31', 'NPR'),
(85, 85, 2199, '-12%', '2018-06-03 06:43:31', 'NPR'),
(86, 86, 500, '-38%', '2018-06-03 06:43:31', 'NPR'),
(87, 87, 1450, '-19%', '2018-06-03 06:43:31', 'NPR'),
(88, 89, 750, '-25%', '2018-06-03 06:43:31', 'NPR'),
(89, 88, 1700, '-43%', '2018-06-03 06:43:31', 'NPR'),
(90, 90, 2500, '-29%', '2018-06-03 06:43:31', 'NPR'),
(91, 91, 1299, '-26%', '2018-06-03 06:43:31', 'NPR'),
(92, 92, 899, '-10%', '2018-06-03 06:43:31', 'NPR'),
(93, 93, 120, '-14%', '2018-06-03 06:43:31', 'NPR'),
(94, 94, 500, '-38%', '2018-06-03 06:43:31', 'NPR'),
(95, 95, 639, '-28%', '2018-06-03 06:43:31', 'NPR'),
(96, 96, 99, '-34%', '2018-06-03 06:43:31', 'NPR'),
(97, 97, 500, '-33%', '2018-06-03 06:43:31', 'NPR'),
(98, 98, 1299, '-13%', '2018-06-03 06:43:31', 'NPR'),
(99, 99, 449, '-31%', '2018-06-03 06:43:31', 'NPR'),
(100, 100, 1740, '-17%', '2018-06-03 06:43:31', 'NPR'),
(101, 101, 120, '-14%', '2018-06-03 06:43:31', 'NPR'),
(102, 102, 799, '-43%', '2018-06-03 06:43:31', 'NPR'),
(103, 103, 149, '-50%', '2018-06-03 06:43:31', 'NPR'),
(104, 104, 4499, '-25%', '2018-06-03 06:43:31', 'NPR'),
(105, 105, 2499, '-29%', '2018-06-03 06:43:31', 'NPR'),
(106, 106, 500, '-38%', '2018-06-03 06:43:31', 'NPR'),
(107, 107, 475, '-26%', '2018-06-03 06:43:32', 'NPR'),
(108, 108, 4199, '-16%', '2018-06-03 06:43:32', 'NPR'),
(109, 109, 1699, '-55%', '2018-06-03 06:43:32', 'NPR'),
(110, 110, 149, '-25%', '2018-06-03 06:43:32', 'NPR'),
(111, 111, 500, '-38%', '2018-06-03 06:43:32', 'NPR'),
(112, 112, 999, '-33%', '2018-06-03 06:43:32', 'NPR'),
(113, 113, 849, '-29%', '2018-06-03 06:43:32', 'NPR'),
(114, 114, 119, '-52%', '2018-06-03 06:43:32', 'NPR'),
(115, 115, 1249, '-43%', '2018-06-03 06:43:32', 'NPR'),
(116, 117, 1490, '-25%', '2018-06-03 06:43:32', 'NPR'),
(117, 116, 399, '-60%', '2018-06-03 06:43:32', 'NPR'),
(118, 118, 7499, '-17%', '2018-06-03 06:43:32', 'NPR'),
(119, 119, 499, '-50%', '2018-06-03 06:43:32', 'NPR'),
(120, 120, 1099, '-8%', '2018-06-03 06:43:32', 'NPR'),
(121, 121, 349, '-53%', '2018-06-03 06:43:32', 'NPR'),
(122, 122, 599, '-8%', '2018-06-03 06:43:32', 'NPR'),
(123, 123, 280, '-44%', '2018-06-03 06:43:32', 'NPR'),
(124, 15, 69, '-66%', '2018-06-03 06:50:47', ' NP'),
(125, 19, 125, '-17%', '2018-06-03 06:50:47', ' NP'),
(126, 23, 1049, '-45%', '2018-06-03 06:50:47', ' NP'),
(127, 5, 400, '-16%', '2018-06-03 06:50:48', ' NP'),
(128, 1, 399, '-17%', '2018-06-03 06:50:48', ' NP'),
(129, 25, 1499, '-32%', '2018-06-03 06:50:48', ' NP'),
(130, 8, 375, '-25%', '2018-06-03 06:50:48', ' NP'),
(131, 2, 749, '-25%', '2018-06-03 06:50:48', ' NP'),
(132, 29, 359, '-64%', '2018-06-03 06:50:48', ' NP'),
(133, 9, 420, '-35%', '2018-06-03 06:50:48', ' NP'),
(134, 3, 750, '-63%', '2018-06-03 06:50:48', ' NP'),
(135, 33, 1149, '-43%', '2018-06-03 06:50:48', ' NP'),
(136, 6, 1299, '-37%', '2018-06-03 06:50:48', ' NP'),
(137, 37, 1649, '-34%', '2018-06-03 06:50:48', ' NP'),
(138, 12, 1760, '-20%', '2018-06-03 06:50:48', ' NP'),
(139, 11, 1249, '-55%', '2018-06-03 06:50:48', ' NP'),
(140, 4, 1199, '-52%', '2018-06-03 06:50:48', ' NP'),
(141, 41, 100, '-13%', '2018-06-03 06:50:48', ' NP'),
(142, 45, 899, '-40%', '2018-06-03 06:50:48', ' NP'),
(143, 16, 2945, '-24%', '2018-06-03 06:50:48', ' NP'),
(144, 13, 1088, '-56%', '2018-06-03 06:50:48', ' NP'),
(145, 7, 619, '-31%', '2018-06-03 06:50:48', ' NP'),
(146, 47, 400, '-50%', '2018-06-03 06:50:49', ' NP'),
(147, 20, 450, '-36%', '2018-06-03 06:50:49', ' NP'),
(148, 51, 800, '-27%', '2018-06-03 06:50:49', ' NP'),
(149, 10, 1449, '-24%', '2018-06-03 06:50:49', ' NP'),
(150, 17, 1249, '-51%', '2018-06-03 06:50:49', ' NP'),
(151, 24, 1019, '-29%', '2018-06-03 06:50:49', ' NP'),
(152, 56, 199, '-60%', '2018-06-03 06:50:49', ' NP'),
(153, 28, 700, '-30%', '2018-06-03 06:50:49', ' NP'),
(154, 61, 899, '-55%', '2018-06-03 06:50:49', ' NP'),
(155, 14, 799, '-21%', '2018-06-03 06:50:49', ' NP'),
(156, 21, 500, '-38%', '2018-06-03 06:50:49', ' NP'),
(157, 34, 1888, '-6%', '2018-06-03 06:50:49', ' NP'),
(158, 65, 100, '-13%', '2018-06-03 06:50:49', ' NP'),
(159, 18, 1199, '-40%', '2018-06-03 06:50:49', ' NP'),
(160, 40, 700, '-30%', '2018-06-03 06:50:49', ' NP'),
(161, 26, 500, '-38%', '2018-06-03 06:50:49', ' NP'),
(162, 22, 499, '-29%', '2018-06-03 06:50:49', ' NP'),
(163, 68, 3999, '-20%', '2018-06-03 06:50:49', ' NP'),
(164, 30, 1799, '-10%', '2018-06-03 06:50:49', ' NP'),
(165, 44, 1799, '-40%', '2018-06-03 06:50:49', ' NP'),
(166, 73, 100, '-13%', '2018-06-03 06:50:49', ' NP'),
(167, 27, 1500, '-40%', '2018-06-03 06:50:49', ' NP'),
(168, 76, 849, '-43%', '2018-06-03 06:50:49', ' NP'),
(169, 32, 1499, '-35%', '2018-06-03 06:50:49', ' NP'),
(170, 48, 999, '-4%', '2018-06-03 06:50:49', ' NP'),
(171, 31, 700, '-30%', '2018-06-03 06:50:49', ' NP'),
(172, 81, 149, '-50%', '2018-06-03 06:50:50', ' NP'),
(173, 53, 340, '-48%', '2018-06-03 06:50:50', ' NP'),
(174, 36, 1799, '-37%', '2018-06-03 06:50:50', ' NP'),
(175, 35, 799, '-20%', '2018-06-03 06:50:50', ' NP'),
(176, 84, 600, '-40%', '2018-06-03 06:50:50', ' NP'),
(177, 57, 380, '-31%', '2018-06-03 06:50:50', ' NP'),
(178, 39, 500, '-38%', '2018-06-03 06:50:50', ' NP'),
(179, 60, 377, '-46%', '2018-06-03 06:50:50', ' NP'),
(180, 38, 645, '-16%', '2018-06-03 06:50:50', ' NP'),
(181, 89, 750, '-25%', '2018-06-03 06:50:50', ' NP'),
(182, 43, 1349, '-39%', '2018-06-03 06:50:50', ' NP'),
(183, 63, 899, '-25%', '2018-06-03 06:50:50', ' NP'),
(184, 42, 999, '-41%', '2018-06-03 06:50:50', ' NP'),
(185, 49, 500, '-38%', '2018-06-03 06:50:50', ' NP'),
(186, 93, 120, '-14%', '2018-06-03 06:50:50', ' NP'),
(187, 70, 1000, '-33%', '2018-06-03 06:50:50', ' NP'),
(188, 52, 500, '-38%', '2018-06-03 06:50:50', ' NP'),
(189, 46, 2399, '-20%', '2018-06-03 06:50:50', ' NP'),
(190, 96, 99, '-34%', '2018-06-03 06:50:50', ' NP'),
(191, 72, 1199, '-39%', '2018-06-03 06:50:50', ' NP'),
(192, 55, 2099, '-40%', '2018-06-03 06:50:50', ' NP'),
(193, 50, 799, '-20%', '2018-06-03 06:50:50', ' NP'),
(194, 77, 2599, '-35%', '2018-06-03 06:50:51', ' NP'),
(195, 59, 500, '-38%', '2018-06-03 06:50:51', ' NP'),
(196, 101, 120, '-14%', '2018-06-03 06:50:51', ' NP'),
(197, 54, 1140, '-24%', '2018-06-03 06:50:51', ' NP'),
(198, 80, 444, '-11%', '2018-06-03 06:50:51', ' NP'),
(199, 103, 149, '-50%', '2018-06-03 06:50:51', ' NP'),
(200, 64, 500, '-38%', '2018-06-03 06:50:51', ' NP'),
(201, 58, 1600, '-11%', '2018-06-03 06:50:51', ' NP'),
(202, 85, 2199, '-12%', '2018-06-03 06:50:51', ' NP'),
(203, 67, 1699, '-55%', '2018-06-03 06:50:51', ' NP'),
(204, 108, 4199, '-16%', '2018-06-03 06:50:51', ' NP'),
(205, 62, 490, '-30%', '2018-06-03 06:50:51', ' NP'),
(206, 88, 1700, '-43%', '2018-06-03 06:50:51', ' NP'),
(207, 71, 4499, '-20%', '2018-06-03 06:50:51', ' NP'),
(208, 66, 1099, '-27%', '2018-06-03 06:50:51', ' NP'),
(209, 110, 149, '-25%', '2018-06-03 06:50:51', ' NP'),
(210, 74, 500, '-38%', '2018-06-03 06:50:51', ' NP'),
(211, 69, 1599, '-6%', '2018-06-03 06:50:51', ' NP'),
(212, 112, 999, '-33%', '2018-06-03 06:50:51', ' NP'),
(213, 92, 899, '-10%', '2018-06-03 06:50:51', ' NP'),
(214, 78, 1099, '-56%', '2018-06-03 06:50:52', ' NP'),
(215, 114, 119, '-52%', '2018-06-03 06:50:52', ' NP'),
(216, 75, 1649, '-15%', '2018-06-03 06:50:52', ' NP'),
(217, 97, 500, '-33%', '2018-06-03 06:50:52', ' NP'),
(218, 82, 500, '-38%', '2018-06-03 06:50:52', ' NP'),
(219, 116, 399, '-60%', '2018-06-03 06:50:52', ' NP'),
(220, 79, 599, '-40%', '2018-06-03 06:50:52', ' NP'),
(221, 86, 500, '-38%', '2018-06-03 06:50:52', ' NP'),
(222, 119, 499, '-50%', '2018-06-03 06:50:52', ' NP'),
(223, 83, 1149, '-43%', '2018-06-03 06:50:52', ' NP'),
(224, 90, 2500, '-29%', '2018-06-03 06:50:52', ' NP'),
(225, 120, 1099, '-8%', '2018-06-03 06:50:52', ' NP'),
(226, 87, 1450, '-19%', '2018-06-03 06:50:53', ' NP'),
(227, 94, 500, '-38%', '2018-06-03 06:50:53', ' NP'),
(228, 121, 349, '-53%', '2018-06-03 06:50:53', ' NP'),
(229, 91, 1299, '-26%', '2018-06-03 06:50:53', ' NP'),
(230, 98, 1299, '-13%', '2018-06-03 06:50:53', ' NP'),
(231, 122, 599, '-8%', '2018-06-03 06:50:53', ' NP'),
(232, 95, 639, '-28%', '2018-06-03 06:50:53', ' NP'),
(233, 100, 1740, '-17%', '2018-06-03 06:50:53', ' NP'),
(234, 123, 280, '-44%', '2018-06-03 06:50:53', ' NP'),
(235, 99, 449, '-31%', '2018-06-03 06:50:53', ' NP'),
(236, 104, 4499, '-25%', '2018-06-03 06:50:53', ' NP'),
(237, 102, 799, '-43%', '2018-06-03 06:50:53', ' NP'),
(238, 106, 500, '-38%', '2018-06-03 06:50:53', ' NP'),
(239, 105, 2499, '-29%', '2018-06-03 06:50:53', ' NP'),
(240, 109, 1699, '-55%', '2018-06-03 06:50:53', ' NP'),
(241, 107, 475, '-26%', '2018-06-03 06:50:53', ' NP'),
(242, 111, 500, '-38%', '2018-06-03 06:50:53', ' NP'),
(243, 113, 849, '-29%', '2018-06-03 06:50:54', ' NP'),
(244, 115, 1249, '-43%', '2018-06-03 06:50:54', ' NP'),
(245, 117, 1490, '-25%', '2018-06-03 06:50:54', ' NP'),
(246, 118, 7499, '-17%', '2018-06-03 06:50:54', ' NP');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `sku` char(19) NOT NULL,
  `product_name` text NOT NULL,
  `category` int(11) NOT NULL,
  `link` text NOT NULL,
  `image_link` text NOT NULL,
  `date_issued` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `sku`, `product_name`, `category`, `link`, `image_link`, `date_issued`, `date_updated`) VALUES
(1, 'OT776EL19M9WWNAFAMZ', 'VR Glass 3D Glasses 2nd Generation', 5, 'https://www.daraz.com.np/other-vr-glass-3d-glasses-2nd-generation-22667.html', 'https://np.daraz.io/VTwj3pEsUjAzEN6i49AEJZ8hXjw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/76/622/1.jpg?6244', '2018-06-03 06:43:27', '2018-06-03 06:50:48'),
(2, 'OT776EL1KVD8WNAFAMZ', 'Combo of VR Box + Earphone And Gaming Remote', 5, 'https://www.daraz.com.np/other-combo-of-vr-box-earphone-and-gaming-remote-22559.html', 'https://np.daraz.io/1TP1ThoB8F17UCsSoxGAh-saNyE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/95/522/1.jpg?6254', '2018-06-03 06:43:27', '2018-06-03 06:50:48'),
(3, 'OT776EL0JLF28NAFAMZ', 'VR Box Pro-3D Glasses Virtual Reality With Remote', 5, 'https://www.daraz.com.np/other-vr-box-pro-3d-glasses-virtual-reality-with-remote-21923.html', 'https://np.daraz.io/pXi9zfRaMJKHNYkaKkHBb-w9oLE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/32/912/1.jpg?6101', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(4, 'OT776EL1LIY0GNAFAMZ', 'VR Shinecon Combo Premium VR Glass + Remote', 5, 'https://www.daraz.com.np/other-vr-shinecon-combo-premium-vr-glass-remote-22669.html', 'https://np.daraz.io/XyavkDutp5ixsYV67CLaOG29dyQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/96/622/1.jpg?6243', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(5, 'OT776EL154YTCNAFAMZ', 'Portable Wireless Bluetooth Box Speaker', 2, 'https://www.daraz.com.np/other-portable-wireless-bluetooth-box-speaker-69096.html', 'https://np.daraz.io/njTrf2ftU377EVseCBOuYXDIVdI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/69/096/1.jpg?3407', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(6, 'OT776EL0I7OXSNAFAMZ', 'Bluetooth Smartwatch - D3 New', 4, 'https://www.daraz.com.np/other-bluetooth-smartwatch-d3-new-29503.html', 'https://np.daraz.io/DQ-CIGqQm2hoz_ST40WHOO8qrHM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/30/592/1.jpg?7286', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(7, 'OT776EL0Q3ZI8NAFAMZ', 'VR Box Pro - 3D Glasses Virtual Reality With Remote', 5, 'https://www.daraz.com.np/other-vr-box-pro-3d-glasses-virtual-reality-with-remote-65834.html', 'https://np.daraz.io/vQ8dkKWM5ZZTlul2Ba5TBya2lwE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/43/856/1.jpg?4484', '2018-06-03 06:43:28', '2018-06-03 06:50:49'),
(8, 'SO445EL14UNO8NAFAMZ', 'Soft Vision Music Mini Box Bluetooth Speaker', 2, 'https://www.daraz.com.np/soft-vision-music-mini-box-bluetooth-speaker-51686.html', 'https://np.daraz.io/i-pMw4ha17XdKpLQPpncy3QN4VY=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/68/615/1.jpg?0464', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(9, 'OT776EL18VF3CNAFAMZ', 'SD Support Bluetooth Portable Speaker (Color Varied)', 2, 'https://www.daraz.com.np/other-sd-support-bluetooth-portable-speaker-color-varied-96357.html', 'https://np.daraz.io/BwaSKVBm43RTUK2Ov4skgLXrN8I=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/75/369/1.jpg?4365', '2018-06-03 06:43:28', '2018-06-03 06:50:48'),
(10, 'OT776EL1D8P4ONAFAMZ', 'VR Box Shinecon , Bluetooth Gaming Remote & Earphone', 5, 'https://www.daraz.com.np/other-vr-box-shinecon-bluetooth-gaming-remote-earphone-70728.html', 'https://np.daraz.io/yNIihngH3UmMFd5rLym4l7OxCVI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/82/707/1.jpg?7046', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(11, 'OT776EL0FOFG0NAFAMZ', 'Iwatch Smartwatch', 4, 'https://www.daraz.com.np/other-iwatch-smartwatch-43362.html', 'https://np.daraz.io/-Tztovh9s_W08uKpgUTcnaR3wLk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/26/334/1.jpg?2105', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(12, 'AN041EL0TJ88GNAFAMZ', 'Anker Soundcore Nano Big Sound Super Portable Wireless Bluetooth Speaker - (Silver)', 2, 'https://www.daraz.com.np/anker-soundcore-nano-big-sound-super-portable-wireless-bluetooth-speaker-silver-60694.html', 'https://np.daraz.io/S2MS7ggHYuZjhqmLopURrwLatpI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/606/1.jpg?1448', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(13, 'OT776EL17AGXSNAFAMZ', 'I6 Smartwatch With Sim And Micro Sd Slot', 4, 'https://www.daraz.com.np/other-i6-smartwatch-with-sim-and-micro-sd-slot-21727.html', 'https://np.daraz.io/ZDGDj8x3XluFG2rDauGqvm84NYY=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/72/712/1.jpg?5975', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(14, 'OT776EL0YATPCNAFAMZ', 'VR Box 2nd Generation With Bluetooth Game Pad Remote Shutter', 5, 'https://www.daraz.com.np/other-vr-box-2nd-generation-with-bluetooth-game-pad-remote-shutter-21675.html', 'https://np.daraz.io/3tmmHVYVsyHx2rHAD897EHbG68M=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/57/612/1.jpg?5945', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(15, 'OT776EL0YYM6ONAFAMZ', 'Black OTG Cable for Mobile Phones', 1, 'https://www.daraz.com.np/other-black-otg-cable-for-mobile-phones-22785.html', 'https://np.daraz.io/di2I0SVsVIpUvclbcr1cBqqhvuU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/722/1.jpg?7454', '2018-06-03 06:43:29', '2018-06-03 06:50:47'),
(16, 'JB523EL0PC23SNAFAMZ', 'JBL Go Portable Mini Bluetooth Speaker  Black', 2, 'https://www.daraz.com.np/jbl-go-portable-mini-bluetooth-speaker-black-35524.html', 'https://np.daraz.io/iSrQYrPSzujO4dDNsfeSkU6adog=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/42/553/1.jpg?1046', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(17, 'OT776EL1M6IS0NAFAMZ', 'Iwatch Smartwatch', 4, 'https://www.daraz.com.np/other-iwatch-smartwatch-22779.html', 'https://np.daraz.io/bSt6sPpKlR-_9bSZIFFjdHb1gRo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/97/722/1.jpg?8115', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(18, 'OT776EL1AUD3SNAFAMZ', 'VR Shinecon Combo Premium VR Glass + Remote', 5, 'https://www.daraz.com.np/other-vr-shinecon-combo-premium-vr-glass-remote-97687.html', 'https://np.daraz.io/usPgYI1HQkv6VqE99EEKOJEHRmA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/78/679/1.jpg?1944', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(19, 'OT776EL101CH4NAFAMZ', 'HDMI Cable (1.5m)', 1, 'https://www.daraz.com.np/other-hdmi-cable-1.5m-92506.html', 'https://np.daraz.io/0Vy0v_Pm1hvAmvTkWI3qKDOS6xE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/60/529/1.jpg?8924', '2018-06-03 06:43:29', '2018-06-03 06:50:47'),
(20, 'OT776EL1IMQJONAFAMZ', 'Mini Portable Bluetooth Speaker With Built-in Mic & LED Light', 2, 'https://www.daraz.com.np/other-mini-portable-bluetooth-speaker-with-built-in-mic-led-light-106719.html', 'https://np.daraz.io/UKcPBsWBFB9FDTZRgM10pmmqP78=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/91/7601/1.jpg?8506', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(21, 'OT776EL05NNV8NAFAMZ', 'Moto 360 2nd Gen 46mm Smart Watch Tempered Glass Anti-Scratch', 4, 'https://www.daraz.com.np/other-moto-360-2nd-gen-46mm-smart-watch-tempered-glass-anti-scratch-120590.html', 'https://np.daraz.io/5VKBmFaptJJ0N-gcCQJmbR3Mbfs=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/09/5021/1.jpg?4915', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(22, 'OT776EL180LLONAFAMZ', 'VR BOX Version 2.0 - Virtual Reality 3D Glasses', 5, 'https://www.daraz.com.np/other-vr-box-version-2.0-virtual-reality-3d-glasses-113937.html', 'https://np.daraz.io/wglZFFJm8_M1Eue2qRMqhH50SaU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/73/9311/1.jpg?9253', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(23, 'OT776EL0R6W1ONAFAMZ', 'HDMI To HDMI 15 Meter Cable', 1, 'https://www.daraz.com.np/other-hdmi-to-hdmi-15-meter-cable-117654.html', 'https://np.daraz.io/lWqItwPt6khdmAZPmHhfTJwlqog=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/45/6711/1.jpg?7825', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(24, 'OT776EL1B3028NAFAMZ', 'JY-25 USB Bluetooth Portable Speaker Support TF Card + FM Radio', 2, 'https://www.daraz.com.np/other-jy-25-usb-bluetooth-portable-speaker-support-tf-card-fm-radio-28097.html', 'https://np.daraz.io/-bspGELOuUOKaAqpydgq4aRFcc4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/082/1.jpg?2235', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(25, 'ON440EL0GHR2SNAFAMZ', 'Lightning 8-Pin To HDMI Female Video Adapter With Micro USB Charging Cable', 1, 'https://www.daraz.com.np/onlineshopgroup-lightning-8-pin-to-hdmi-female-video-adapter-with-micro-usb-charging-cable-120772.html', 'https://np.daraz.io/Ro0sbdOVotlM-CegLl4c8oUMJDE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/27/7021/1.jpg?8515', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(26, 'OT776EL0NIO0KNAFAMZ', 'Samsung Gear S2 Gear Sport Tempered Glass Screen Protector High Definition', 4, 'https://www.daraz.com.np/other-samsung-gear-s2-gear-sport-tempered-glass-screen-protector-high-definition-120593.html', 'https://np.daraz.io/uASfn9glBj813C1xtexs14Vfjzw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/39/5021/1.jpg?5276', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(27, 'OT776EL0UX2AKNAFAMZ', 'VR Shinecon Virtual Reality 3D Glasses With Gaming Remote - Black', 5, 'https://www.daraz.com.np/other-vr-shinecon-virtual-reality-3d-glasses-with-gaming-remote-black-113915.html', 'https://np.daraz.io/oPs5Pegij9OiOWBUQkMrD1oDIMg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/9311/1.jpg?7332', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(28, 'OT776EL0TINEGNAFAMZ', 'S815 Hi-Fi Music Player Wireless Bluetooth Mini Portable Speaker Super Bass', 2, 'https://www.daraz.com.np/other-s815-hi-fi-music-player-wireless-bluetooth-mini-portable-speaker-super-bass-97594.html', 'https://np.daraz.io/RoEJy3Um61CpXteRdCOYxh-vdLA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/579/1.jpg?7644', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(29, 'OT776EL0KP5M8NAFAMZ', 'HDMI To VGA Converter', 1, 'https://www.daraz.com.np/other-hdmi-to-vga-converter-66743.html', 'https://np.daraz.io/YHyFj4q_wx94p2Jw0rNdEvGc27M=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/34/766/1.jpg?4424', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(30, 'OT776EL0FTQ3WNAFAMZ', 'Q18 Smart Watch- Black', 4, 'https://www.daraz.com.np/other-q18-smart-watch-black-118562.html', 'https://np.daraz.io/WDgf_4EWCoq1xW9z5VYZhjWP4sI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/26/5811/1.jpg?0178', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(31, 'OT776EL1B3AV4NAFAMZ', 'HD VR Movie Box For Gaming And Video Play With Wireless Remote Controller', 5, 'https://www.daraz.com.np/other-hd-vr-movie-box-for-gaming-and-video-play-with-wireless-remote-controller-69097.html', 'https://np.daraz.io/TTBF_qhzuR5qp2d4mHd0cqbyxNQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/096/1.jpg?3447', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(32, 'ON440EL0YL2LWNAFAMZ', 'Smartwatch - IOS/Android - White', 4, 'https://www.daraz.com.np/onlineshopgroup-smartwatch-iosandroid-white-109085.html', 'https://np.daraz.io/Gf7CYoY5pfzzKteLDQN5vfrMHJE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/0901/1.jpg?1676', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(33, 'OT776EL0X583GNAFAMZ', 'Plastic Braided HDMI Extension Cable- 20M', 1, 'https://www.daraz.com.np/other-plastic-braided-hdmi-extension-cable-20m-117655.html', 'https://np.daraz.io/sR3fzei7-yE39tiNOS2X9mGL0kI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/55/6711/1.jpg?7825', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(34, 'OT776EL1KBEYKNAFAMZ', 'Bluetooth Sound Bar Wireless Speaker-Black', 2, 'https://www.daraz.com.np/other-bluetooth-sound-bar-wireless-speaker-black-119549.html', 'https://np.daraz.io/aapOrXNDYKdbM2g8u3OrFGoej2k=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/94/5911/1.jpg?7586', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(35, 'OT776EL17F5ZWNAFAMZ', 'VR Box With VR Wireless Game Pad - Black/White', 5, 'https://www.daraz.com.np/other-vr-box-with-vr-wireless-game-pad-blackwhite-113927.html', 'https://np.daraz.io/_avGgcS5oh1NcD5WZnWVHs0179Q=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/72/9311/1.jpg?8930', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(36, 'OT776EL0H3M1CNAFAMZ', 'Combo Of Sim Supporting Smartwatch + Bluetooth Earphone', 4, 'https://www.daraz.com.np/other-combo-of-sim-supporting-smartwatch-bluetooth-earphone-22782.html', 'https://np.daraz.io/3qtKE2JKvO7UAEUQ5HkPr1-1-ts=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/28/722/1.jpg?6226', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(37, 'OT776EL06TNFWNAFAMZ', '3 In 1 HDMI Switch- Black', 1, 'https://www.daraz.com.np/other-3-in-1-hdmi-switch-black-116411.html', 'https://np.daraz.io/savGui9YU02dqfG4G24TqUAqmAE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/11/4611/1.jpg?5541', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(38, 'OT776EL0UQFSGNAFAMZ', 'VR Box with Bluetooth Control Game Pad', 5, 'https://www.daraz.com.np/other-vr-box-with-bluetooth-control-game-pad-22615.html', 'https://np.daraz.io/V41idgwwbaTHVYrwWozdhGGlfBg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/622/1.jpg?6246', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(39, 'OT776EL1AQKLWNAFAMZ', 'Garmin Forerunner 620 2.5D Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-forerunner-620-2.5d-tempered-glass-screen-protector-120587.html', 'https://np.daraz.io/fYdZKm--tuIOgFBj9zMgMLXETaA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/78/5021/1.jpg?4797', '2018-06-03 06:43:29', '2018-06-03 06:50:50'),
(40, 'OT776EL14GUU4NAFAMZ', 'S815 Hi-Fi Music Player Wireless Bluetooth Mini Speaker-Grey', 2, 'https://www.daraz.com.np/other-s815-hi-fi-music-player-wireless-bluetooth-mini-speaker-grey-117976.html', 'https://np.daraz.io/98EbdOqidLqAujDwjdJhBtqArhk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/67/9711/1.jpg?6857', '2018-06-03 06:43:29', '2018-06-03 06:50:49'),
(41, 'OT776EL0UIOJONAFAMZ', 'Female To Female Jumper Wire 10cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-female-to-female-jumper-wire-10cm-20-pcs-106215.html', 'https://np.daraz.io/YBOMtx9D-plMMuAk8FJRa19LfTU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/2601/1.jpg?2188', '2018-06-03 06:43:29', '2018-06-03 06:50:48'),
(42, 'OT776EL0YW9B4NAFAMZ', 'Combo of VR Box + Earphone And Gaming Remote', 5, 'https://www.daraz.com.np/other-combo-of-vr-box-earphone-and-gaming-remote-21685.html', 'https://np.daraz.io/DBSIssRJmQups2ED0xykZdprz4c=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/612/1.jpg?5941', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(43, 'ON440EL0SMQK4NAFAMZ', 'Smart Watch - i7 Supports Sim/TF Card/Camera', 4, 'https://www.daraz.com.np/onlineshopgroup-smart-watch-i7-supports-simtf-cardcamera-109084.html', 'https://np.daraz.io/9D5OYel-uo4q7orOJ86Gdgq-75E=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/48/0901/1.jpg?1636', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(44, 'OT776EL1MGF9CNAFAMZ', 'SOMHO S311 Portable Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-somho-s311-portable-bluetooth-speaker-48189.html', 'https://np.daraz.io/QLT_bsZpzsnwPQZVD0AmePYLwcc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/98/184/1.jpg?9728', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(45, 'OT776EL05L3YWNAFAMZ', 'Yash Vision Mhl To Hdmi Media Adapter Kit 6.5 Feet (2M) Universal Mhl Micro Usb To Hdmi Cable 1080P Hdtv Adapter', 1, 'https://www.daraz.com.np/other-yash-vision-mhl-to-hdmi-media-adapter-kit-6.5-feet-2m-universal-mhl-micro-usb-to-hdmi-cable-1080p-hdtv-adapter-38390.html', 'https://np.daraz.io/vKiwtq6Hs4585g0aJpomGJ71xXk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/09/383/1.jpg?5415', '2018-06-03 06:43:30', '2018-06-03 06:50:48'),
(46, 'OT776EL0FCRRONAFAMZ', 'BOBO VR Z4 Virtual Reality 3D Glasses With Headphones-White', 5, 'https://www.daraz.com.np/other-bobo-vr-z4-virtual-reality-3d-glasses-with-headphones-white-109752.html', 'https://np.daraz.io/OdZGR6ZYe8LTzppgDJysiwHU4R4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/25/7901/1.jpg?0057', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(47, 'OT776EL1AE1WWNAFAMZ', 'Multi-function USB All-in-1 Combo Hub with 4 Card Readers & 3 USB Ports', 1, 'https://www.daraz.com.np/other-multi-function-usb-all-in-1-combo-hub-with-4-card-readers-3-usb-ports-81977.html', 'https://np.daraz.io/XrEuBGf2xEvdN3Q7mp9uEocPL_4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/77/918/1.jpg?6965', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(48, 'OT776EL1H1C40NAFAMZ', 'Rugby Design Bluetooth Speaker (AUS, USB, TF, FM)', 2, 'https://www.daraz.com.np/other-rugby-design-bluetooth-speaker-aus-usb-tf-fm-28098.html', 'https://np.daraz.io/Yz1uoGnIT09PHRtFYSTIhF9TOtM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/89/082/1.jpg?2235', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(49, 'OT776EL1GOWNONAFAMZ', 'Garmin Forerunner 630 2.5D Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-forerunner-630-2.5d-tempered-glass-screen-protector-120588.html', 'https://np.daraz.io/ArL_zC4E94kBlM6L3r6Yme2qDek=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/88/5021/1.jpg?4797', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(50, 'OT776EL04J5GGNAFAMZ', 'Premium VR Box with Bluetooth Game Pad', 5, 'https://www.daraz.com.np/other-premium-vr-box-with-bluetooth-game-pad-21670.html', 'https://np.daraz.io/2dbn9Ub9yvQedFkxEeoc4w40Qww=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/07/612/1.jpg?5949', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(51, 'OT776EL0AB91ONAFAMZ', 'DVI Male To VGA Female Adapter Converter', 1, 'https://www.daraz.com.np/other-dvi-male-to-vga-female-adapter-converter-112371.html', 'https://np.daraz.io/B2affbrLTjzD3pPinIRhQ7Gfldc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/17/3211/1.jpg?5542', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(52, 'OT776EL0GYWD0NAFAMZ', 'Garmin Approach S6 Watch Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-approach-s6-watch-tempered-glass-screen-protector-120582.html', 'https://np.daraz.io/vLzMpwdQJQkKgToOil23fbejlwI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/28/5021/1.jpg?4638', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(53, 'OT776EL0UK6HCNAFAMZ', 'Mini Bluetooth Music Speaker', 2, 'https://www.daraz.com.np/other-mini-bluetooth-music-speaker-3315.html', 'https://np.daraz.io/pRoi4VJYpC00hbY7cvTZlGa0ytg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/33/1.jpg?2026', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(54, 'OT776EL0SCHNKNAFAMZ', 'VR Shinecon 3D Glasses With Wireless Remote Control Gamepad', 5, 'https://www.daraz.com.np/other-vr-shinecon-3d-glasses-with-wireless-remote-control-gamepad-21674.html', 'https://np.daraz.io/ZxlsT6NIhYWd6PPSIETy1dMkPYQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/47/612/1.jpg?5945', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(55, 'ON440EL1C58LSNAFAMZ', 'Combo of i6 and D3 Smartwatch', 4, 'https://www.daraz.com.np/onlineshopgroup-combo-of-i6-and-d3-smartwatch-66808.html', 'https://np.daraz.io/oNpQ1RQgCq5Jn1oZO4lwJ-nAQg0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/80/866/1.jpg?5507', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(56, 'OT776EL0NCDUWNAFAMZ', 'VGA Connector, 15 VGA SVGA KVM Female to Female Gender Changer Adapter', 1, 'https://www.daraz.com.np/other-vga-connector-15-vga-svga-kvm-female-to-female-gender-changer-adapter-90293.html', 'https://np.daraz.io/24mjLvgkltCBxxOi6aGUjxdxS-U=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/39/209/1.jpg?7165', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(57, 'OT776EL11PDQONAFAMZ', 'Mini Portable Bluetooth Speaker With Built-in Mic (Color & Print Varied)', 2, 'https://www.daraz.com.np/other-mini-portable-bluetooth-speaker-with-built-in-mic-color-print-varied-3336.html', 'https://np.daraz.io/t7i7r9EO3UkxBQU_gbsQC4P0iAg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/63/33/1.jpg?7585', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(58, 'SO445EL0YBIE8NAFAMZ', 'Soft Vision Bundle of 3 - VR Box Shinecon 4th Generation, Bluetooth Gaming Remote &  Earphone', 5, 'https://www.daraz.com.np/soft-vision-bundle-of-3-vr-box-shinecon-4th-generation-bluetooth-gaming-remote-earphone-44675.html', 'https://np.daraz.io/6-agZfvOsHD3vj4tIT2sxNwCAb4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/57/644/1.jpg?5213', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(59, 'OT776EL14S8K4NAFAMZ', 'Garmin Forerunner 235 2.5D Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-forerunner-235-2.5d-tempered-glass-screen-protector-120586.html', 'https://np.daraz.io/KFoXPSz8RmR0zx-v8FLlVSGCUq4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/68/5021/1.jpg?4755', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(60, 'OT776EL0UOGVONAFAMZ', 'Mini Bluetooth Speaker - White', 2, 'https://www.daraz.com.np/other-mini-bluetooth-speaker-white-103515.html', 'https://np.daraz.io/7RfeBuBuGz-yRhOSEcVIG9BMw6Q=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/5301/1.jpg?7938', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(61, 'AA370EL12WC1CNAFAMZ', 'EastVita 5Ft 1.5m HDMI To 3-RCA Video Audio AV Component Converter Adapter Cable For HDTV DVD', 1, 'https://www.daraz.com.np/other-eastvita-5ft-1.5m-hdmi-to-3-rca-video-audio-av-component-converter-adapter-cable-for-hdtv-dvd-43356.html', 'https://np.daraz.io/n0Iu4NJtlvlltMqRkxYpx938ceI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/65/334/1.jpg?6648', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(62, 'OT776EL0OM1DKNAFAMZ', 'VR Box Version 2.0 - Virtual Reality 3D Glasses', 5, 'https://www.daraz.com.np/other-vr-box-version-2.0-virtual-reality-3d-glasses-93314.html', 'https://np.daraz.io/56DuWXIckSop20HIKNqsCw9Xcsw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/41/339/1.jpg?3595', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(63, 'OT776EL0WXDM0NAFAMZ', 'Mini Hands Free Outdoor Bluetooth Speaker with Sound Quality', 2, 'https://www.daraz.com.np/other-mini-hands-free-outdoor-bluetooth-speaker-with-sound-quality-50355.html', 'https://np.daraz.io/AiGPhwrkjR_lIVF0pQqUii6oiPs=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/55/305/1.jpg?6485', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(64, 'OT776EL0TH02CNAFAMZ', 'Garmin Fenix Chronos Tempered Glass Screen Protector 2.5D High Definition 9H', 4, 'https://www.daraz.com.np/other-garmin-fenix-chronos-tempered-glass-screen-protector-2.5d-high-definition-9h-120594.html', 'https://np.daraz.io/lfTqZV0f94MEr_N5tEWzpXY6QyU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/5021/1.jpg?5315', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(65, 'OT776EL07ARYCNAFAMZ', 'Male To Female Jumper Wire 10cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-male-to-female-jumper-wire-10cm-20-pcs-106221.html', 'https://np.daraz.io/bYt1c2ztynT9VDln8nTrm6D55H4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/2601/1.jpg?2188', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(66, 'OT776EL13T64WNAFAMZ', 'VR Shinecon 3D Glasses + Wireless Remote Control Gamepad', 5, 'https://www.daraz.com.np/other-vr-shinecon-3d-glasses-wireless-remote-control-gamepad-66866.html', 'https://np.daraz.io/ftOpdeQC4Bu9eW2T7T-YHpo6BNo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/66/866/1.jpg?7206', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(67, 'OT776EL0XOWCONAFAMZ', 'X6 Curved Smart Watch', 4, 'https://www.daraz.com.np/other-x6-curved-smart-watch-98565.html', 'https://np.daraz.io/hLKRikyQOIqRm39KjtBNVYKwqk0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/56/589/1.jpg?6236', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(68, 'OT776EL0TBDWKNAFAMZ', 'USB Type C To HDMI Adapter', 1, 'https://www.daraz.com.np/other-usb-type-c-to-hdmi-adapter-104294.html', 'https://np.daraz.io/FWqESj4gxE2GrEOIfnl7zrxS7Gc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/49/2401/1.jpg?8338', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(69, 'OT776EL0USD8GNAFAMZ', 'VR Shinecon Combo Premium VR Glass + Remote', 5, 'https://www.daraz.com.np/other-vr-shinecon-combo-premium-vr-glass-remote-21715.html', 'https://np.daraz.io/dG1d6fYYibsnG8WLdpVYSEacNXc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/712/1.jpg?5984', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(70, 'OT776EL16Q2G4NAFAMZ', 'Metal Mini Portable Wireless Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-metal-mini-portable-wireless-bluetooth-speaker-106717.html', 'https://np.daraz.io/IMlw3ZpsmfMuW_Imt39QRKvhIE4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/71/7601/1.jpg?4105', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(71, 'OT776EL1JI138NAFAMZ', 'X2 Smart Watch Bluetooth Sport Fitness Tracker Heart Rate', 4, 'https://www.daraz.com.np/other-x2-smart-watch-bluetooth-sport-fitness-tracker-heart-rate-102239.html', 'https://np.daraz.io/7Cb-Vq1XdMAXmU0c_kgSI7DsAos=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/93/2201/1.jpg?3696', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(72, 'OT776EL07MZOWNAFAMZ', 'Portable Bluetooth Speaker With USB + TF Card + FM Radio (JY-25)', 2, 'https://www.daraz.com.np/other-portable-bluetooth-speaker-with-usb-tf-card-fm-radio-jy-25-3821.html', 'https://np.daraz.io/ywMDE6cqb4yoT8_ahIMtQ4YXJ-8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/12/83/1.jpg?1917', '2018-06-03 06:43:30', '2018-06-03 06:50:50'),
(73, 'OT776EL10H0LGNAFAMZ', 'Male To Male Jumper Wire 10cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-male-to-male-jumper-wire-10cm-20-pcs-106216.html', 'https://np.daraz.io/QyWBkUIJr3D914Cafktnfm7CVj0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/61/2601/1.jpg?2188', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(74, 'OT776EL0C9KOKNAFAMZ', 'Citizen Watch NY0040-09EE Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-citizen-watch-ny0040-09ee-tempered-glass-screen-protector-120602.html', 'https://np.daraz.io/p2AAc5SCTyr3gNQ5M4DXqogDW7E=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/20/6021/1.jpg?5516', '2018-06-03 06:43:30', '2018-06-03 06:50:51'),
(75, 'OT776EL0PO95CNAFAMZ', 'VR Shinecon with Gamepad - Pleasing Eye Effect', 5, 'https://www.daraz.com.np/other-vr-shinecon-with-gamepad-pleasing-eye-effect-22134.html', 'https://np.daraz.io/b5TG59H_DMo_hniad-0KowtOnGo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/43/122/1.jpg?6044', '2018-06-03 06:43:30', '2018-06-03 06:50:52'),
(76, 'AA370EL0A4SSKNAFAMZ', '2 in 1 Lightning Adapter Headphone For iPhone X 8/8/7/7 Plus', 1, 'https://www.daraz.com.np/other-2-in-1-lightning-adapter-headphone-for-iphone-x-8877-plus-102071.html', 'https://np.daraz.io/EMm7r6lt0A2u3iiaho8I2dVYAh0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/17/0201/1.jpg?1560', '2018-06-03 06:43:30', '2018-06-03 06:50:49'),
(77, 'WK851EL13BHN0NAFAMZ', 'W-KING S20 Portable Waterproof Bluetooth Super Bass Loudspeaker- Blue', 2, 'https://www.daraz.com.np/w-king-s20-portable-waterproof-bluetooth-super-bass-loudspeaker-blue-114066.html', 'https://np.daraz.io/aqSLcGfTfKqfv2GAuoi5ta0s41k=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/66/0411/1.jpg?5734', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(78, 'OT776EL13L5K0NAFAMZ', 'I7 Bluetooth Smartwatch', 4, 'https://www.daraz.com.np/other-i7-bluetooth-smartwatch-29466.html', 'https://np.daraz.io/ybxI-3UXx-Sc-meU5GQSkK5bugE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/66/492/1.jpg?6748', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(79, 'OT776EL02GY5SNAFAMZ', 'VR Box (VR02)- White', 5, 'https://www.daraz.com.np/other-vr-box-vr02-white-5140.html', 'https://np.daraz.io/8zKZE-UYTQGhfz7ZvEhlRK-hvwE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/04/15/1.jpg?1893', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(80, 'OT776EL0O8LKWNAFAMZ', 'Music Mini Box Bluetooth Speaker - Black', 2, 'https://www.daraz.com.np/ab-tech-music-mini-box-bluetooth-speaker-black-21704.html', 'https://np.daraz.io/FVZBRo41_yxyMlAO0v2UjIPVDj0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/40/712/1.jpg?6887', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(81, 'OT776EL1AKYG4NAFAMZ', 'USB C To Micro USB Adapter Convert Connector', 1, 'https://www.daraz.com.np/other-usb-c-to-micro-usb-adapter-convert-connector-104287.html', 'https://np.daraz.io/_PFYIRZHA5RufodCjmFUFHhMqZg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/78/2401/1.jpg?7618', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(82, 'OT776EL15DO5WNAFAMZ', 'Citizen Watch BM8475 Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-citizen-watch-bm8475-tempered-glass-screen-protector-120596.html', 'https://np.daraz.io/EuvwMA2hUn3NjmRULjjueVyjwRg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/69/5021/1.jpg?5396', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(83, 'OT776EL1LN8ESNAFAMZ', 'VR Shinecon 3D Glasses + Wireless Remote Control Gamepad-Black', 5, 'https://www.daraz.com.np/other-vr-shinecon-3d-glasses-wireless-remote-control-gamepad-black-122869.html', 'https://np.daraz.io/rW_YuRGuR4JbYUozaOxR1OERV6o=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/96/8221/1.jpg?4749', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(84, 'OT776EL0WXQ18NAFAMZ', '1080P HDMI Male To VGA Female Adapter Converter Cable For PC/HDTV/Laptop', 1, 'https://www.daraz.com.np/other-1080p-hdmi-male-to-vga-female-adapter-converter-cable-for-pchdtvlaptop-112355.html', 'https://np.daraz.io/S_NXvl6kCuw-mMB656dAfKNvJZE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/55/3211/1.jpg?2447', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(85, 'OT776EL16L4Z8NAFAMZ', 'Charge 2+ Waterproof Wireless Portable Speaker - Black', 2, 'https://www.daraz.com.np/other-charge-2-waterproof-wireless-portable-speaker-black-103517.html', 'https://np.daraz.io/qycz-AF_pe8ubhuS6iZbXOxLgRE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/71/5301/1.jpg?8739', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(86, 'OT776EL0BLZX0NAFAMZ', 'Moto 360 2nd Gen 42mm Smart Watch Tempered Glass Anti-Scratch', 4, 'https://www.daraz.com.np/other-moto-360-2nd-gen-42mm-smart-watch-tempered-glass-anti-scratch-120591.html', 'https://np.daraz.io/kxdTb62fyKZowfId_35p9aLPpjI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/19/5021/1.jpg?4955', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(87, 'OT776EL062JA8NAFAMZ', 'Combo of VR Box With Gaming Remote Controller and  Earphone', 5, 'https://www.daraz.com.np/other-combo-of-vr-box-with-gaming-remote-controller-and-earphone-69101.html', 'https://np.daraz.io/S2ldOvluhBl7Wrk9uEu57AoG3uA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/196/1.jpg?3447', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(88, 'OT776EL1AD5I8NAFAMZ', 'JC 176 Dual Driver Dual Diaphragm HiFi Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-jc-176-dual-driver-dual-diaphragm-hifi-bluetooth-speaker-67877.html', 'https://np.daraz.io/goi-nmExg6rjzDhhnuX8hsTAcxA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/77/876/1.jpg?9007', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(89, 'SO445EL0REK7CNAFAMZ', 'Soft Vision 10 Meter Long HDMI To HDMI Cable', 1, 'https://www.daraz.com.np/soft-vision-10-meter-long-hdmi-to-hdmi-cable-92064.html', 'https://np.daraz.io/8AtB-xDImJ3Tdncd2zpFV6lTmlg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/46/029/1.jpg?5704', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(90, 'OT776EL1B4E7SNAFAMZ', 'X6 Bluetooth Smart Watch With Camera SIM Memory Card - (White/Black)', 4, 'https://www.daraz.com.np/other-x6-bluetooth-smart-watch-with-camera-sim-memory-card-whiteblack-74197.html', 'https://np.daraz.io/Rbu6yCJV-EarDY3sSQOqzLuRyvQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/79/147/1.jpg?8287', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(91, 'OT776EL0ME5LSNAFAMZ', 'VR Shinecon With Gamepad - Pleasing Eye Effect', 5, 'https://www.daraz.com.np/other-vr-shinecon-with-gamepad-pleasing-eye-effect-21673.html', 'https://np.daraz.io/w3KKXOQ_JViG1Zz8LxyQEwk_mOk=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/37/612/1.jpg?5947', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(92, 'OT776EL0XD3YWNAFAMZ', 'New Design WS-Y66B Portable Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-new-design-ws-y66b-portable-bluetooth-speaker-93065.html', 'https://np.daraz.io/9ueIZm4QtbQfA_m1ubJ__soiM7Q=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/56/039/1.jpg?1887', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(93, 'OT776EL0P5S3ONAFAMZ', 'Female To Female Jumper Wire 20cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-female-to-female-jumper-wire-20cm-20-pcs-106224.html', 'https://np.daraz.io/bPWvrY9Cga3xWyCMhInpvLkQrV4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/42/2601/1.jpg?2188', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(94, 'OT776EL0MX8ESNAFAMZ', 'Garmin Forerunner 220 2.5D High Definition 9H Tempered Glass Screen Protector', 4, 'https://www.daraz.com.np/other-garmin-forerunner-220-2.5d-high-definition-9h-tempered-glass-screen-protector-120583.html', 'https://np.daraz.io/muh16zske-jI-gcYxDyc6UT6GgA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/38/5021/1.jpg?4638', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(95, 'OT776EL1EFO74NAFAMZ', 'VR Box with Bluetooth Control Game Pad', 5, 'https://www.daraz.com.np/bestdeals-vr-box-with-bluetooth-control-game-pad-21748.html', 'https://np.daraz.io/X-PrJfi_GpfieGqTyNb89ocB8Bg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/84/712/1.jpg?0444', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(96, 'OT776EL0M3DHKNAFAMZ', 'USB 2.0 A Female to A Female Coupler Adapter For USB Cable', 1, 'https://www.daraz.com.np/other-usb-2.0-a-female-to-a-female-coupler-adapter-for-usb-cable-90173.html', 'https://np.daraz.io/NmHWkDt2iOmkyv8Oe3EUSApAUlo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/37/109/1.jpg?8006', '2018-06-03 06:43:31', '2018-06-03 06:50:50'),
(97, 'OT776EL1ETWJKNAFAMZ', 'Music Mini Box Bluetooth Speaker', 2, 'https://www.daraz.com.np/other-music-mini-box-bluetooth-speaker-67358.html', 'https://np.daraz.io/5GYZbjFk1B8dAY2Ft4Tp_0s7k-w=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/85/376/1.jpg?6785', '2018-06-03 06:43:31', '2018-06-03 06:50:52'),
(98, 'OT776EL1IMZ18NAFAMZ', 'D3 Bluetooth Smartwatch - Black', 4, 'https://www.daraz.com.np/other-d3-bluetooth-smartwatch-black-117719.html', 'https://np.daraz.io/lXBH6B1MZYf8yVH4yxj9QOOTNfE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/91/7711/1.jpg?9705', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(99, 'OT776EL0AHHI8NAFAMZ', 'VR Box (VR02)', 5, 'https://www.daraz.com.np/other-vr-box-vr02-21671.html', 'https://np.daraz.io/oRokJHdnSBMvixwxrwQ3CYyo0eQ=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/17/612/1.jpg?5949', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(100, 'BE416EL0TX184NAFAMZ', 'Y1 Bluetooth Smartwatch With SIM Slot', 4, 'https://www.daraz.com.np/bestchoice-y1-bluetooth-smartwatch-with-sim-slot-105205.html', 'https://np.daraz.io/I2y9cxnjTiiAr5mEYIpz8n9HTx0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/50/2501/1.jpg?0057', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(101, 'OT776EL0J7G1WNAFAMZ', 'Male To Male Jumper Wire 20cm - 20 Pcs', 1, 'https://www.daraz.com.np/other-male-to-male-jumper-wire-20cm-20-pcs-106223.html', 'https://np.daraz.io/mMqvvHbHEfvy-D1znhCm-7FrxW8=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/32/2601/1.jpg?2188', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(102, 'OT776EL0WFWR4NAFAMZ', 'VR Box With Bluetooth Control Gamepad', 5, 'https://www.daraz.com.np/other-vr-box-with-bluetooth-control-gamepad-9445.html', 'https://np.daraz.io/PUYlGVIm2ll3UF-9xS1_Wonq_mg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/54/49/1.jpg?7450', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(103, 'AA370EL0YLI1GNAFAMZ', 'USB C To Micro USB Adapter Convert Connector', 1, 'https://www.daraz.com.np/other-usb-c-to-micro-usb-adapter-convert-connector-101185.html', 'https://np.daraz.io/nj1WC_NJ3OoDPGiYrSOXKRD1T9M=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/58/1101/1.jpg?0042', '2018-06-03 06:43:31', '2018-06-03 06:50:51'),
(104, 'ON440EL0Q2JT4NAFAMZ', 'Uwatch U11C Smart Watch Phone Bluetooth MTK2502 Remote Camera', 4, 'https://www.daraz.com.np/onlineshopgroup-uwatch-u11c-smart-watch-phone-bluetooth-mtk2502-remote-camera-98734.html', 'https://np.daraz.io/bYObczviBvNiRn5mApXm0NTIYT4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/43/789/1.jpg?2093', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(105, 'OT776EL12HI5WNAFAMZ', 'Z4 3D Glasses VR Box With Headphones-White', 5, 'https://www.daraz.com.np/other-z4-3d-glasses-vr-box-with-headphones-white-124646.html', 'https://np.daraz.io/4gQGwB9shHDV_tLl5P6DLtFbT94=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/64/6421/1.jpg?3445', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(106, 'OT776EL1MN8PGNAFAMZ', 'Moto 360 1st Gen 46mm Smart Watch Tempered Glass', 4, 'https://www.daraz.com.np/other-moto-360-1st-gen-46mm-smart-watch-tempered-glass-120589.html', 'https://np.daraz.io/uqaNMCFmlId7sZOSdzGQbcwvTVU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/98/5021/1.jpg?4876', '2018-06-03 06:43:31', '2018-06-03 06:50:53'),
(107, 'OT776EL1MZYYONAFAMZ', 'VR 2.0 Generation With 360 HD Video Play Along/Motion/Detection/Rotation', 5, 'https://www.daraz.com.np/other-vr-2.0-generation-with-360-hd-video-play-alongmotiondetectionrotation-69099.html', 'https://np.daraz.io/l2NCRZTK7QOseNNrSdIemMtDp7U=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/99/096/1.jpg?3447', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(108, 'OT776EL0ZDSK4NAFAMZ', 'Apple Macbook Pro Type-C Hub Adapter 7 in 1 With HDMI', 1, 'https://www.daraz.com.np/other-apple-macbook-pro-type-c-hub-adapter-7-in-1-with-hdmi-103495.html', 'https://np.daraz.io/NsGiPsWa7ygxlJB_ttcOHUkbwZA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/59/4301/1.jpg?5538', '2018-06-03 06:43:32', '2018-06-03 06:50:51'),
(109, 'ON440EL0VE0MSNAFAMZ', 'X6 Bluetooth Smartwatch With Camera Support SIM Card', 4, 'https://www.daraz.com.np/onlineshopgroup-x6-bluetooth-smartwatch-with-camera-support-sim-card-122725.html', 'https://np.daraz.io/rKLKH1-y9hOp5CdLuqhBDnrNstI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/52/7221/1.jpg?8429', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(110, 'OT776EL0I94MWNAFAMZ', 'USB 2.0 Type A Male to A Female Extension Cable 3 Meter - Black', 1, 'https://www.daraz.com.np/other-usb-2.0-type-a-male-to-a-female-extension-cable-3-meter-black-95603.html', 'https://np.daraz.io/a5uzgsRy6G7CAWuRcCFTC9AkFBM=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/30/659/1.jpg?1285', '2018-06-03 06:43:32', '2018-06-03 06:50:51'),
(111, 'OT776EL0HKBYSNAFAMZ', 'Samsung Gear S3 Tempered Glass Screen Protecto 2.5D High Definition 9H', 4, 'https://www.daraz.com.np/other-samsung-gear-s3-tempered-glass-screen-protecto-2.5d-high-definition-9h-120592.html', 'https://np.daraz.io/X266OtOLq2w8p5evYKzjBqWq5fE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/29/5021/1.jpg?5156', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(112, 'OT776EL0M7X58NAFAMZ', 'Gold Plated Mini DP To DVI VGA HDMI  3 In 1 Cable', 1, 'https://www.daraz.com.np/other-gold-plated-mini-dp-to-dvi-vga-hdmi-3-in-1-cable-112373.html', 'https://np.daraz.io/L2dMbzG-MyO0irpgXD8j_X7buEo=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/37/3211/1.jpg?6262', '2018-06-03 06:43:32', '2018-06-03 06:50:52'),
(113, 'OT776EL0RTTNWNAFAMZ', 'U8 Smartwatch', 4, 'https://www.daraz.com.np/other-u8-smartwatch-114764.html', 'https://np.daraz.io/yBWcFWMO5johtaWMeRoaNGg2CZE=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/46/7411/1.jpg?9253', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(114, 'KP432EL14VD4WNAFAMZ', 'Type-C Male to Micro USB Female Converter Syncing Charging', 1, 'https://www.daraz.com.np/kpitsolution-type-c-male-to-micro-usb-female-converter-syncing-charging-84686.html', 'https://np.daraz.io/2__dMvVpQqUX1XxnJwvenOOGjQ4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/68/648/1.jpg?9845', '2018-06-03 06:43:32', '2018-06-03 06:50:52'),
(115, 'OT776EL0USKY8NAFAMZ', 'Black Smartwatch - Gt08', 4, 'https://www.daraz.com.np/other-black-smartwatch-gt08-22715.html', 'https://np.daraz.io/bb4QHf2Qsr0H175YUUn42fT60qU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/51/722/1.jpg?2085', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(116, 'AA370EL1L6FE8NAFAMZ', '3.5mm Audio Cable Male to 2 Female Aux Cable Stereo Jack Splitter Cable Adapter', 1, 'https://www.daraz.com.np/other-3.5mm-audio-cable-male-to-2-female-aux-cable-stereo-jack-splitter-cable-adapter-83069.html', 'https://np.daraz.io/FWG2iD0HRcqyP9ncFAOaX2cVyM0=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/96/038/1.jpg?1026', '2018-06-03 06:43:32', '2018-06-03 06:50:52'),
(117, 'OT776EL065LMGNAFAMZ', 'M2 Intelligence Health Bracelet - (Black)', 4, 'https://www.daraz.com.np/other-m2-intelligence-health-bracelet-black-93301.html', 'https://np.daraz.io/fxz8gGBu_j3rxMizu7idW9FvjU4=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/339/1.jpg?7966', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(118, 'ON440EL04L2Z8NAFAMZ', 'Round Waterproof Blood Pressure/Heart Rate Monitor Smartwatch', 4, 'https://www.daraz.com.np/onlineshopgroup-round-waterproof-blood-pressureheart-rate-monitor-smartwatch-120770.html', 'https://np.daraz.io/xU0tOC14XnTIZFzoK8zcv40voaA=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/07/7021/1.jpg?8035', '2018-06-03 06:43:32', '2018-06-03 06:50:54'),
(119, 'OT776OT05YCTKNAFAMZ', 'HDMI Male to VGA + Audio Converter Cable For PC/Laptop', 1, 'https://www.daraz.com.np/other-hdmi-male-to-vga-audio-converter-cable-for-pclaptop-10001.html', 'https://np.daraz.io/2AH5oGzwgsdll8LfOMBB5siacHI=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/10/001/1.jpg?5553', '2018-06-03 06:43:32', '2018-06-03 06:50:52'),
(120, 'OT776EL0ZDT94NAFAMZ', '1080P HDTV HDMI Male To 3 RCA Audio Video AV Cable Cord Adapter', 1, 'https://www.daraz.com.np/other-1080p-hdtv-hdmi-male-to-3-rca-audio-video-av-cable-cord-adapter-13495.html', 'https://np.daraz.io/4DwA7OWc7ANltnWMPXh3L6OPXdg=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/59/431/1.jpg?5836', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(121, 'OT776OT1CEBRKNAFAMZ', '5 Meter Long HDMI To HDMI Cable', 1, 'https://www.daraz.com.np/other-5-meter-long-hdmi-to-hdmi-cable-9218.html', 'https://np.daraz.io/qATzcLa_TSTUQEoA8Fw2-3z2-98=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/81/29/1.jpg?2773', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(122, 'OT776OT0W5FFSNAFAMZ', 'HDMI-HDMI 10 Meter Cable', 1, 'https://www.daraz.com.np/other-hdmi-hdmi-10-meter-cable-10045.html', 'https://np.daraz.io/xiEiWQ2TIi49_9csF_2suZYWPqw=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/54/001/1.jpg?1087', '2018-06-03 06:43:32', '2018-06-03 06:50:53'),
(123, 'OT776EL0X8LXKNAFAMZ', '4ft USB 2.0 A Type Male to DC 5.5 x 2.1mm DC 5V Power Plug Connector Cable', 1, 'https://www.daraz.com.np/other-4ft-usb-2.0-a-type-male-to-dc-5.5-x-2.1mm-dc-5v-power-plug-connector-cable-92855.html', 'https://np.daraz.io/bYSlk30zlFZiaZqeqd6ME7-JOmU=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(80)/product/55/829/1.jpg?0885', '2018-06-03 06:43:32', '2018-06-03 06:50:53');

-- --------------------------------------------------------

--
-- Table structure for table `target_pages`
--

CREATE TABLE `target_pages` (
  `id` int(11) NOT NULL,
  `url` text NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `target_pages`
--

INSERT INTO `target_pages` (`id`, `url`, `description`) VALUES
(1, 'https://www.daraz.com.np/cables/', 'Cables'),
(3, 'https://www.daraz.com.np/mobiles-tablets-smartwatches', 'Mobile devices'),
(4, 'https://www.daraz.com.np/wireless-speakers/', 'Wireless Speakers'),
(5, 'https://www.daraz.com.np/vr-headsets/', 'VR Headsets');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `category_id` (`id`);

--
-- Indexes for table `prices`
--
ALTER TABLE `prices`
  ADD PRIMARY KEY (`id`),
  ADD KEY `price_link` (`prod_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sku` (`sku`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `target_pages`
--
ALTER TABLE `target_pages`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `prices`
--
ALTER TABLE `prices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=247;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=124;

--
-- AUTO_INCREMENT for table `target_pages`
--
ALTER TABLE `target_pages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `prices`
--
ALTER TABLE `prices`
  ADD CONSTRAINT `price_link` FOREIGN KEY (`prod_id`) REFERENCES `products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
>>>>>>> 8e27e40220dc8794da2e3e1fff5967c53eafa9d5
