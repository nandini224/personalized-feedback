-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 14, 2018 at 02:09 PM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `frustration`
--
CREATE DATABASE IF NOT EXISTS `frustration` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `frustration`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=31 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add registration model', 7, 'add_registrationmodel'),
(20, 'Can change registration model', 7, 'change_registrationmodel'),
(21, 'Can delete registration model', 7, 'delete_registrationmodel'),
(22, 'Can add answer model', 8, 'add_answermodel'),
(23, 'Can change answer model', 8, 'change_answermodel'),
(24, 'Can delete answer model', 8, 'delete_answermodel'),
(25, 'Can add feedback model', 9, 'add_feedbackmodel'),
(26, 'Can change feedback model', 9, 'change_feedbackmodel'),
(27, 'Can delete feedback model', 9, 'delete_feedbackmodel'),
(28, 'Can add notification model', 10, 'add_notificationmodel'),
(29, 'Can change notification model', 10, 'change_notificationmodel'),
(30, 'Can delete notification model', 10, 'delete_notificationmodel');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'mindsparkadmin', 'notificationmodel'),
(6, 'sessions', 'session'),
(8, 'user', 'answermodel'),
(9, 'user', 'feedbackmodel'),
(7, 'user', 'registrationmodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-07-30 09:20:55.927437'),
(2, 'auth', '0001_initial', '2018-07-30 09:21:05.998856'),
(3, 'admin', '0001_initial', '2018-07-30 09:21:08.171260'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-07-30 09:21:08.233660'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-07-30 09:21:09.865064'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-07-30 09:21:10.835266'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-07-30 09:21:11.537267'),
(8, 'auth', '0004_alter_user_username_opts', '2018-07-30 09:21:11.585067'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-07-30 09:21:12.146668'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-07-30 09:21:12.193468'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-07-30 09:21:12.240268'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-07-30 09:21:13.147070'),
(13, 'sessions', '0001_initial', '2018-07-30 09:21:13.836471'),
(14, 'user', '0001_initial', '2018-07-30 09:21:14.149873'),
(15, 'user', '0002_answermodel', '2018-08-10 10:47:26.215397'),
(16, 'user', '0003_auto_20180811_1041', '2018-08-11 05:11:53.132648'),
(17, 'user', '0004_feedbackmodel', '2018-08-12 08:06:57.671575'),
(18, 'user', '0005_auto_20180812_1514', '2018-08-12 09:44:31.407439'),
(19, 'mindsparkadmin', '0001_initial', '2018-08-12 09:45:48.658565'),
(20, 'mindsparkadmin', '0002_auto_20180812_1542', '2018-08-12 10:12:23.706294');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3bzs2lxlnu3f4ybkhejq4ifesdd3wngd', 'OTA1MDBhNjc2YzNkYzkyYzBjYWQ2MGViNWZmYjE1ZDI1NTg2MTg4Yzp7InVzZXJpZCI6MSwidG90YWwiOjB9', '2018-08-17 09:54:33.089871'),
('43vmfr8tp15dzssok8kta2pr46ibonjx', 'OTA1MDBhNjc2YzNkYzkyYzBjYWQ2MGViNWZmYjE1ZDI1NTg2MTg4Yzp7InVzZXJpZCI6MSwidG90YWwiOjB9', '2018-08-23 10:27:25.063881'),
('hj6ejpoqu2sb13z592tuojkeo4we1wju', 'YjVjNmRmNDBiNDAyMzBmMWNjMDg5NDM2YTA5MDU0ZGQyMWFmMmUwMjp7InVzZXJpZCI6MSwidG90YWwiOjAsIm5hbWUxIjo4LCJuYW1lMiI6OCwibmFtZTMiOjAsIm5hbWU0IjowfQ==', '2018-08-28 11:18:39.980033');

-- --------------------------------------------------------

--
-- Table structure for table `mindsparkadmin_notificationmodel`
--

CREATE TABLE IF NOT EXISTS `mindsparkadmin_notificationmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `notifications` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `mindsparkadmin_notificationmodel`
--

INSERT INTO `mindsparkadmin_notificationmodel` (`id`, `date`, `notifications`) VALUES
(3, '2018-05-11', 'Next week start the session class'),
(4, '2018-05-14', 'Tomorrow will be start the session exam at 10 am'),
(5, '2018-05-16', 'Tomorrow will be start the session two class'),
(6, '2018-05-20', 'Session result for coming soon'),
(7, '2018-05-24', 'Two days will be holiyday'),
(8, '2018-08-17', 'Tomorrow will be start the session four class'),
(9, '2018-08-17', 'Tomorow will be start session one exams'),
(10, '2018-08-19', 'First session class is completed'),
(11, '2018-08-20', 'Tomorrow will be start the exams');

-- --------------------------------------------------------

--
-- Table structure for table `user_answermodel`
--

CREATE TABLE IF NOT EXISTS `user_answermodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sessionone` int(11) NOT NULL,
  `sessiontwo` int(11) NOT NULL,
  `sessionthree` int(11) NOT NULL,
  `sessionfour` int(11) NOT NULL,
  `sessionfive` int(11) NOT NULL,
  `catagory` varchar(100) NOT NULL,
  `userId_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_answermodel_userId_id_2a6a2292_fk_user_registrationmodel_id` (`userId_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=103 ;

--
-- Dumping data for table `user_answermodel`
--

INSERT INTO `user_answermodel` (`id`, `sessionone`, `sessiontwo`, `sessionthree`, `sessionfour`, `sessionfive`, `catagory`, `userId_id`) VALUES
(1, 2, 2, 1, 0, 1, 'notmotivationalmessage', 6),
(2, 7, 1, 1, 3, 2, 'notmotivationalmessage', 4),
(3, 9, 6, 8, 10, 9, 'motivationalmessage', 1),
(4, 7, 9, 8, 10, 7, 'motivationalmessage', 3),
(5, 6, 7, 8, 5, 7, 'notmotivationalmessage', 5),
(6, 8, 8, 8, 9, 9, 'motivationalmessage', 7),
(7, 6, 6, 7, 7, 7, 'notmotivationalmessage', 8),
(8, 7, 8, 5, 10, 9, 'motivationalmessage', 2),
(9, 9, 9, 8, 8, 8, 'motivationalmessage', 9),
(10, 7, 5, 7, 6, 7, 'notmotivationalmessage', 10),
(11, 9, 7, 8, 9, 9, 'motivationalmessage', 11),
(12, 6, 6, 9, 6, 6, 'notmotivationalmessage', 12),
(13, 9, 9, 9, 10, 10, 'motivationalmessage', 13),
(14, 5, 5, 9, 5, 5, 'notmotivationalmessage', 14),
(15, 10, 9, 9, 9, 10, 'motivationalmessage', 15),
(16, 7, 5, 9, 5, 5, 'notmotivationalmessage', 16),
(17, 9, 9, 9, 9, 10, 'motivationalmessage', 17),
(18, 4, 4, 9, 4, 4, 'notmotivationalmessage', 18),
(19, 8, 8, 9, 9, 9, 'motivationalmessage', 19),
(20, 7, 7, 9, 7, 7, 'notmotivationalmessage', 20),
(21, 9, 9, 9, 9, 9, 'motivationalmessage', 21),
(22, 3, 4, 9, 3, 6, 'notmotivationalmessage', 22),
(23, 8, 8, 9, 8, 8, 'motivationalmessage', 23),
(24, 5, 5, 9, 5, 5, 'notmotivationalmessage', 24),
(25, 7, 7, 9, 7, 7, 'motivationalmessage', 25),
(26, 3, 3, 9, 3, 4, 'notmotivationalmessage', 26),
(27, 9, 9, 9, 9, 10, 'motivationalmessage', 27),
(28, 6, 6, 9, 6, 6, 'notmotivationalmessage', 28),
(29, 9, 9, 9, 9, 9, 'motivationalmessage', 29),
(30, 7, 7, 9, 5, 5, 'notmotivationalmessage', 30),
(31, 9, 8, 9, 8, 9, 'motivationalmessage', 31),
(32, 5, 6, 9, 6, 7, 'notmotivationalmessage', 32),
(33, 10, 9, 9, 9, 10, 'motivationalmessage', 33),
(34, 5, 6, 5, 6, 3, 'notmotivationalmessage', 34),
(35, 6, 7, 6, 7, 6, 'motivationalmessage', 35),
(36, 3, 4, 4, 4, 6, 'notmotivationalmessage', 36),
(37, 8, 5, 7, 8, 9, 'motivationalmessage', 37),
(38, 7, 9, 8, 4, 6, 'notmotivationalmessage', 38),
(39, 5, 5, 7, 9, 9, 'motivationalmessage', 39),
(40, 4, 6, 4, 6, 4, 'notmotivationalmessage', 40),
(41, 5, 7, 9, 8, 8, 'motivationalmessage', 41),
(42, 7, 3, 5, 6, 6, 'notmotivationalmessage', 42),
(43, 9, 9, 4, 10, 9, 'motivationalmessage', 43),
(44, 8, 5, 6, 5, 6, 'notmotivationalmessage', 44),
(45, 8, 8, 9, 8, 9, 'motivationalmessage', 45),
(46, 5, 6, 6, 6, 5, 'notmotivationalmessage', 46),
(47, 9, 8, 9, 8, 8, 'motivationalmessage', 47),
(48, 5, 6, 4, 4, 4, 'notmotivationalmessage', 48),
(49, 9, 9, 9, 9, 9, 'motivationalmessage', 49),
(50, 8, 7, 7, 7, 7, 'notmotivationalmessage', 50),
(51, 10, 10, 10, 10, 10, 'motivationalmessage', 51),
(52, 7, 8, 9, 7, 7, 'notmotivationalmessage', 52),
(53, 8, 8, 8, 9, 9, 'motivationalmessage', 53),
(54, 4, 6, 4, 5, 5, 'notmotivationalmessage', 54),
(55, 10, 10, 10, 10, 10, 'motivationalmessage', 55),
(56, 3, 6, 3, 6, 6, 'notmotivationalmessage', 56),
(57, 9, 9, 9, 9, 9, 'motivationalmessage', 57),
(58, 7, 8, 5, 5, 7, 'notmotivationalmessage', 58),
(59, 9, 9, 9, 9, 9, 'motivationalmessage', 59),
(60, 10, 7, 9, 8, 10, 'notmotivationalmessage', 60),
(61, 9, 9, 9, 9, 9, 'motivationalmessage', 61),
(62, 6, 3, 3, 3, 3, 'notmotivationalmessage', 62),
(63, 8, 8, 8, 8, 8, 'motivationalmessage', 63),
(64, 4, 4, 4, 4, 4, 'notmotivationalmessage', 64),
(65, 5, 5, 5, 5, 5, 'motivationalmessage', 65),
(66, 6, 6, 6, 6, 6, 'notmotivationalmessage', 66),
(67, 9, 9, 9, 9, 9, 'motivationalmessage', 67),
(68, 8, 8, 8, 8, 8, 'notmotivationalmessage', 68),
(69, 7, 7, 7, 7, 7, 'motivationalmessage', 69),
(70, 3, 3, 3, 3, 3, 'notmotivationalmessage', 70),
(71, 7, 7, 7, 7, 7, 'motivationalmessage', 71),
(72, 8, 8, 8, 8, 8, 'notmotivationalmessage', 72),
(73, 9, 9, 9, 9, 9, 'motivationalmessage', 73),
(74, 6, 6, 6, 6, 6, 'notmotivationalmessage', 74),
(75, 10, 10, 10, 10, 10, 'motivationalmessage', 75),
(76, 6, 6, 6, 6, 6, 'notmotivationalmessage', 76),
(77, 7, 7, 7, 7, 7, 'motivationalmessage', 77),
(78, 2, 2, 2, 2, 2, 'notmotivationalmessage', 78),
(79, 9, 9, 9, 9, 9, 'motivationalmessage', 79),
(80, 6, 6, 6, 6, 9, 'notmotivationalmessage', 80),
(81, 8, 8, 8, 8, 8, 'motivationalmessage', 81),
(82, 5, 5, 5, 5, 5, 'notmotivationalmessage', 82),
(83, 9, 9, 9, 9, 9, 'motivationalmessage', 83),
(84, 5, 5, 5, 5, 5, 'notmotivationalmessage', 84),
(85, 8, 8, 8, 8, 8, 'motivationalmessage', 85),
(86, 6, 6, 6, 6, 6, 'notmotivationalmessage', 86),
(87, 9, 9, 9, 9, 9, 'motivationalmessage', 87),
(88, 5, 5, 5, 5, 5, 'notmotivationalmessage', 88),
(89, 7, 7, 7, 7, 7, 'motivationalmessage', 89),
(90, 5, 5, 5, 5, 5, 'notmotivationalmessage', 90),
(91, 7, 7, 7, 7, 7, 'motivationalmessage', 91),
(92, 8, 8, 8, 8, 8, 'notmotivationalmessage', 92),
(93, 9, 8, 8, 9, 9, 'motivationalmessage', 93),
(94, 5, 6, 7, 8, 3, 'notmotivationalmessage', 94),
(95, 9, 7, 10, 10, 9, 'motivationalmessage', 95),
(96, 4, 5, 5, 4, 7, 'notmotivationalmessage', 96),
(97, 6, 8, 10, 9, 10, 'motivationalmessage', 97),
(98, 7, 8, 9, 0, 8, 'notmotivationalmessage', 98),
(99, 8, 9, 9, 9, 9, 'motivationalmessage', 99),
(100, 5, 6, 5, 6, 6, 'notmotivationalmessage', 100),
(101, 10, 10, 10, 10, 10, 'motivationalmessage', 101),
(102, 9, 9, 9, 9, 9, 'motivationalmessage', 102);

-- --------------------------------------------------------

--
-- Table structure for table `user_feedbackmodel`
--

CREATE TABLE IF NOT EXISTS `user_feedbackmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(300) NOT NULL,
  `username_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_feedbackmodel_username_id_1c74a46b_fk_user_regi` (`username_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `user_feedbackmodel`
--

INSERT INTO `user_feedbackmodel` (`id`, `feedback`, `username_id`) VALUES
(3, ' It''s ok ,very usefull for me', 1),
(4, ' Thank you for your opportunity', 2),
(6, ' Very Exciting for performence', 2),
(7, 'Thanking you\r\n', 4),
(11, 'Thank you', 2),
(12, ' thanking you very use full for me', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user_registrationmodel`
--

CREATE TABLE IF NOT EXISTS `user_registrationmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(300) NOT NULL,
  `lastname` varchar(300) NOT NULL,
  `userid` varchar(200) NOT NULL,
  `password` varchar(100) NOT NULL,
  `mobilenumber` varchar(100) NOT NULL,
  `emailid` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=103 ;

--
-- Dumping data for table `user_registrationmodel`
--

INSERT INTO `user_registrationmodel` (`id`, `firstname`, `lastname`, `userid`, `password`, `mobilenumber`, `emailid`, `gender`) VALUES
(1, 'Santhosh', 'Kumar', 'Santhosh', '1234', '9789672179', 'santhosh1997@gmail.com', 'male'),
(2, 'Sanjai', 'Kumar', 'Sanjai', '6789', '8955217430', 'talktome@gmail.com', 'male'),
(3, 'Sabari', 'Nathan', 'Sabari', '1997', '8945216512', 'sabarinathan1350@gmail.com', 'male'),
(4, 'Suresh', 'Babu', 'Suresh', '1994', '9451208125', 'suresh76@gmail.com', 'male'),
(5, 'Saravana', 'Raj', 'Saravana', '3412', '7934717300', 'saravana51@gmail.com', 'male'),
(6, 'Siva', 'A', 'Siva', '1998', '9776565218', 'santhosh1997@gmail.com', 'male'),
(7, '?Hayden.', 'Nathan', 'Jashmin', '1992', '9789672179', 'santhosh1997@gmail.com', 'male'),
(8, 'Smith', 'Nathan', 'Rangini', '1993', '8955217430', 'talktome@gmail.com', 'male'),
(9, '?Hayden.', 'Kumar', 'Rogini', '1995', '8945216512', 'santhosh1997@gmail.com', 'male'),
(10, 'Saravana', 'Nathan', 'Padma', '1009', '8955217430', 'talktome@gmail.com', 'male'),
(11, '?Hayden.', 'Nathan', 'Padmavathi', '1654', '9789672179', 'sabarinathan1350@gmail.com', 'male'),
(12, 'Smith', 'Babu', 'Padmapriya', '1340', '9451208125', 'talktome@gmail.com', 'male'),
(13, 'Sabari', 'Kumar', 'Banu', '1993', '8945216512', 'santhosh1997@gmail.com', 'male'),
(14, 'Saravana', 'Babu', 'Banupriya', '1009', '8955217430', 'talktome@gmail.com', 'male'),
(15, '?Hayden.', 'Nathan', 'Banumathi', '1993', '9789672179', 'sabarinathan1350@gmail.com', 'male'),
(16, 'Sabari', 'Babu', 'Vikega', '1992', '9451208125', 'santhosh1997@gmail.com', 'male'),
(17, 'Smith', 'Kumar', 'Vishnu', '1654', '8945216512', 'sabarinathan1350@gmail.com', 'male'),
(18, 'Smith', 'Babu', 'Nithya', '1993', '8955217430', 'talktome@gmail.com', 'male'),
(19, 'Saravana', 'Nathan', 'Manohari', '1009', '9789672179', 'santhosh1997@gmail.com', 'male'),
(20, 'Sabari', 'Babu', 'Santhosni', '1992', '9451208125', 'sabarinathan1350@gmail.com', 'male'),
(21, '?Hayden.', 'Kumar', 'Mohanapriya', '1654', '8955217430', 'santhosh1997@gmail.com', 'male'),
(22, 'Smith', 'Babu', 'Thangapriya', '1009', '9789672179', 'talktome@gmail.com', 'male'),
(23, 'Saravana', 'Nathan', 'Manjula', '1993', '9451208125', 'santhosh1997@gmail.com', 'male'),
(24, 'Sabari', 'Babu', 'Geetha', '1340', '8945216512', 'suresh76@gmail.com', 'male'),
(25, '?Hayden.', 'Kumar', 'Prabu', '1992', '8955217430', 'sabarinathan1350@gmail.com', 'male'),
(26, 'Smith', 'Babu', 'Arthi', '1340', '9789672179', 'talktome@gmail.com', 'male'),
(27, 'Saravana', 'Nathan', 'Manochithra', '1009', '9451208125', 'santhosh1997@gmail.com', 'male'),
(28, 'Sabari', 'Babu', 'Manivannan', '1993', '8945216512', 'saravana51@gmail.com', 'male'),
(29, '?Hayden.', 'Babu', 'Manikkam', '1992', '9789672179', 'talktome@gmail.com', 'male'),
(30, 'Sabari', 'Kumar', 'Kailash', '1009', '9451208125', 'santhosh1997@gmail.com', 'male'),
(31, 'Smith', 'Nathan', 'Thomas', '1993', '8945216512', 'suresh76@gmail.com', 'male'),
(32, 'Saravana', 'Babu', 'James', '1654', '8955217430', 'sabarinathan1350@gmail.com', 'male'),
(33, 'Sabari', 'Kumar', 'Thilagavathy', '1992', '9789672179', 'santhosh1997@gmail.com', 'male'),
(34, 'Sabari', 'Nathan', 'Sanmugapriya', '1340', '9451208125', 'talktome@gmail.com', 'male'),
(35, 'Smith', 'Babu', 'Gayathiri', '1993', '8945216512', 'saravana51@gmail.com', 'male'),
(36, '?Hayden.', 'Kumar', 'Kanagadurga', '1009', '8955217430', 'santhosh1997@gmail.com', 'male'),
(37, 'Saravana', 'Raj', 'Krishma', '1992', '9789672179', 'suresh76@gmail.com', 'male'),
(38, 'Sabari', 'Nathan', 'santhipriya', '1654', '9451208125', 'talktome@gmail.com', 'male'),
(39, 'Smith', 'Raj', 'Geevetha', '1993', '8945216512', 'santhosh1997@gmail.com', 'male'),
(40, '?Hayden.', 'Kumar', 'Navaneethapriya', '1340', '8955217430', 'sabarinathan1350@gmail.com', 'male'),
(41, 'Saravana', 'Babu', 'Sathya', '1992', '9789672179', 'saravana51@gmail.com', 'male'),
(42, 'Sabari', 'Nathan', 'Saranyadevi', '1009', '9451208125', 'talktome@gmail.com', 'male'),
(43, 'Smith', 'Raj', 'Saranyakumari', '1993', '8945216512', 'santhosh1997@gmail.com', 'male'),
(44, 'Sabari', 'Babu', 'Sangeetha', '1340', '8955217430', 'suresh76@gmail.com', 'male'),
(45, '?Hayden.', 'Kumar', 'Saraswathi', '1009', '9789672179', 'sabarinathan1350@gmail.com', 'male'),
(46, 'Smith', 'Nathan', 'Saveetha', '1992', '9451208125', 'talktome@gmail.com', 'male'),
(47, 'Saravana', 'Raj', 'Senparuthi', '1654', '8945216512', 'santhosh1997@gmail.com', 'male'),
(48, '?Hayden.', 'Babu', 'Senba', '1993', '8955217430', 'suresh76@gmail.com', 'male'),
(49, 'Saravana', 'Nathan', 'Sivapriya', '1009', '9789672179', 'sabarinathan1350@gmail.com', 'male'),
(50, 'Smith', 'Babu', 'Sivani', '1993', '9451208125', 'talktome@gmail.com', 'male'),
(51, 'Saravana', 'Kumar', 'Sivanesh', '1654', '8945216512', 'santhosh1997@gmail.com', 'male'),
(52, '?Hayden.', 'Babu', 'Kokila', '1009', '9789672179', 'saravana51@gmail.com', 'male'),
(53, 'Smith', 'Nathan', 'Kokilavani', '1340', '8955217430', 'talktome@gmail.com', 'male'),
(54, 'Saravana', 'Babu', 'Jaiganesh', '1992', '9451208125', 'santhosh1997@gmail.com', 'male'),
(55, '?Hayden.', 'Kumar', 'Jayapriya', '1654', '8945216512', 'saravana51@gmail.com', 'male'),
(56, 'Saravana', 'Nathan', 'Jashmin', '1993', '9789672179', 'sabarinathan1350@gmail.com', 'male'),
(57, 'Smith', 'Babu', 'Banumathi', '1009', '8955217430', 'talktome@gmail.com', 'male'),
(58, 'Saravana', 'Kumar', 'Valarmathi', '1340', '8945216512', 'santhosh1997@gmail.com', 'male'),
(59, 'Saravana', 'Babu', 'Vekatan', '1992', '9789672179', 'saravana51@gmail.com', 'male'),
(60, '?Hayden.', 'Nathan', 'Vivega', '1009', '8955217430', 'suresh76@gmail.com', 'male'),
(61, 'Smith', 'Babu', 'Vishnuprakash', '1654', '9451208125', 'santhosh1997@gmail.com', 'male'),
(62, 'Saravana', 'Kumar', 'Nithyamenon', '1992', '8945216512', 'sabarinathan1350@gmail.com', 'male'),
(63, '?Hayden.', 'Nathan', 'Nithyasri', '1654', '9789672179', 'saravana51@gmail.com', 'male'),
(64, 'Smith', 'Raj', 'Nithyasri', '1009', '8955217430', 'santhosh1997@gmail.com', 'male'),
(65, 'Sabari', 'Kumar', 'Kiriza', '1340', '8945216512', 'talktome@gmail.com', 'male'),
(66, 'Sabari', 'Nathan', 'Ramsanthosh', '1992', '9789672179', 'santhosh1997@gmail.com', 'male'),
(67, 'Smith', 'Babu', 'Rogini', '1654', '8955217430', 'saravana51@gmail.com', 'male'),
(68, 'Sabari', 'Kumar', 'Padma', '1993', '9451208125', 'talktome@gmail.com', 'male'),
(69, 'Saravana', 'Raj', 'Padmavathi', '1009', '8945216512', 'santhosh1997@gmail.com', 'male'),
(70, 'Smith', 'Kumar', 'Padmapriya', '1992', '9789672179', 'sabarinathan1350@gmail.com', 'male'),
(71, 'Sabari', 'Nathan', 'Banu', '1654', '8955217430', 'talktome@gmail.com', 'male'),
(72, 'Saravana', 'Babu', 'Banupriya', '1993', '9451208125', 'santhosh1997@gmail.com', 'male'),
(73, 'Sabari', 'Kumar', 'Banumathi', '1340', '9789672179', 'suresh76@gmail.com', 'male'),
(74, 'Smith', 'Nathan', 'Vikega', '1992', '8945216512', 'talktome@gmail.com', 'male'),
(75, 'Sabari', 'Babu', 'Vishnu', '1009', '8955217430', 'santhosh1997@gmail.com', 'male'),
(76, 'Saravana', 'Kumar', 'Nithya', '1993', '9789672179', 'sabarinathan1350@gmail.com', 'male'),
(77, 'Sabari', 'Nathan', 'Santhosni', '1654', '8945216512', 'talktome@gmail.com', 'male'),
(78, 'Smith', 'Babu', 'Mohanapriya', '1992', '8955217430', 'suresh76@gmail.com', 'male'),
(79, 'Sabari', 'Kumar', 'Thangapriya', '1654', '9789672179', 'santhosh1997@gmail.com', 'male'),
(80, 'Saravana', 'Nathan', 'Manjula', '1993', '8945216512', 'sabarinathan1350@gmail.com', 'male'),
(81, 'Smith', 'Babu', 'Geetha', '1009', '8955217430', 'talktome@gmail.com', 'male'),
(82, 'Sabari', 'Kumar', 'Prabu', '1992', '8945216512', 'santhosh1997@gmail.com', 'male'),
(83, 'Saravana', 'Nathan', 'Arthi', '1654', '9789672179', 'suresh76@gmail.com', 'male'),
(84, 'Sabari', 'Babu', 'Manochithra', '1993', '8945216512', 'talktome@gmail.com', 'male'),
(85, 'Smith', 'Nathan', 'Manivannan', '1009', '8955217430', 'santhosh1997@gmail.com', 'male'),
(86, 'Sabari', 'Kumar', 'Manikkam', '1992', '9451208125', 'sabarinathan1350@gmail.com', 'male'),
(87, 'Saravana', 'Babu', 'Kailash', '1009', '8945216512', 'saravana51@gmail.com', 'male'),
(88, 'Smith', 'Raj', 'Thomas', '1993', '9789672179', 'santhosh1997@gmail.com', 'male'),
(89, 'Sabari', 'Kumar', 'James', '1340', '8955217430', 'talktome@gmail.com', 'male'),
(90, 'Saravana', 'Nathan', 'Thilagavathy', '1992', '8945216512', 'santhosh1997@gmail.com', 'male'),
(91, 'Smith', 'Babu', 'Sanmugapriya', '1009', '8945216512', 'saravana51@gmail.com', 'male'),
(92, 'Sabari', 'Kumar', 'Gayathiri', '1654', '9789672179', 'santhosh1997@gmail.com', 'male'),
(93, 'Sabari', 'Babu', 'Banumathi', '1992', '8945216512', 'talktome@gmail.com', 'male'),
(94, 'Smith', 'Nathan', 'Valarmathi', '1654', '8945216512', 'sabarinathan1350@gmail.com', 'male'),
(95, 'Sabari', 'Babu', 'Vekatan', '1993', '8955217430', 'santhosh1997@gmail.com', 'male'),
(96, 'Sabari', 'Kumar', 'Vivega', '1009', '8945216512', 'saravana51@gmail.com', 'male'),
(97, 'Smith', 'Babu', 'Vishnuprakash', '1992', '9789672179', 'talktome@gmail.com', 'male'),
(98, 'Sabari', 'Nathan', 'Nithyamenon', '1654', '8945216512', 'santhosh1997@gmail.com', 'male'),
(99, 'Sabari', 'Babu', 'Nithyasri', '1009', '9451208125', 'suresh76@gmail.com', 'male'),
(100, 'Smith', 'Kumar', 'Nithyasri', '1654', '8955217430', 'talktome@gmail.com', 'male'),
(101, 'Sabari', 'Babu', 'Kiriza', '1992', '8945216512', 'sabarinathan1350@gmail.com', 'male'),
(102, 'Smith', 'Nathan', 'Ramsanthosh', '1009', '9789672179', 'saravana51@gmail.com', 'male');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `user_answermodel`
--
ALTER TABLE `user_answermodel`
  ADD CONSTRAINT `user_answermodel_userId_id_2a6a2292_fk_user_registrationmodel_id` FOREIGN KEY (`userId_id`) REFERENCES `user_registrationmodel` (`id`);

--
-- Constraints for table `user_feedbackmodel`
--
ALTER TABLE `user_feedbackmodel`
  ADD CONSTRAINT `user_feedbackmodel_username_id_1c74a46b_fk_user_regi` FOREIGN KEY (`username_id`) REFERENCES `user_registrationmodel` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
