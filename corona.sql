-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- 생성 시간: 20-07-02 07:35
-- 서버 버전: 10.4.11-MariaDB
-- PHP 버전: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 데이터베이스: `corona`
--

-- --------------------------------------------------------

--
-- 테이블 구조 `city`
--

CREATE TABLE `city` (
  `num` int(11) NOT NULL,
  `ill` int(11) NOT NULL,
  `clean` int(11) NOT NULL,
  `death` int(11) NOT NULL,
  `ing` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 테이블의 덤프 데이터 `city`
--

INSERT INTO `city` (`num`, `ill`, `clean`, `death`, `ing`) VALUES
(1, 74, 13, 0, 4739),
(2, 83, 0, 0, 2587),
(3, 2692, 4, 9, 5486),
(4, 5, 1, 0, 1323),
(5, 7, 2, 0, 718),
(6, 13, 0, 0, 1161),
(7, 20, 0, 0, 505),
(8, 1, 0, 0, 267),
(9, 80, 8, 1, 5392),
(10, 15, 0, 0, 836),
(11, 11, 0, 0, 644),
(12, 68, 0, 0, 2154),
(13, 5, 1, 0, 356),
(14, 2, 1, 0, 984),
(15, 547, 0, 8, 5087),
(16, 63, 0, 0, 1074),
(17, 2, 0, 0, 47);

-- --------------------------------------------------------

--
-- 테이블 구조 `people`
--

CREATE TABLE `people` (
  `ill` mediumtext DEFAULT NULL,
  `clean` mediumtext DEFAULT NULL,
  `death` mediumtext DEFAULT NULL,
  `ing` int(11) NOT NULL,
  `date` varchar(50) NOT NULL,
  `newill` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 테이블의 덤프 데이터 `people`
--

INSERT INTO `people` (`ill`, `clean`, `death`, `ing`, `date`, `newill`) VALUES
('6284', '108', '42', 21832, '03/07 -12 AM', 518);

-- --------------------------------------------------------

--
-- 테이블 구조 `world`
--

CREATE TABLE `world` (
  `num` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `ill` int(11) NOT NULL,
  `death` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 테이블의 덤프 데이터 `world`
--

INSERT INTO `world` (`num`, `name`, `ill`, `death`) VALUES
(1, '중국', 80552, 3042),
(2, '홍콩', 105, 2),
(3, '대만', 42, 1),
(4, '마카오', 10, 0),
(5, '일본', 349, 6),
(6, '싱가포르', 117, 0),
(7, '태국', 47, 1),
(8, '말레이시아', 50, 0),
(9, '베트남', 16, 0),
(10, '인도', 29, 0),
(11, '필리핀', 3, 1),
(12, '캄보디아', 1, 0),
(13, '네팔', 1, 0),
(14, '러시아', 3, 0),
(15, '스리랑카', 1, 0),
(16, '아프가니스탄', 1, 0),
(17, '파키스탄', 5, 0),
(18, '인도네시아', 2, 0),
(19, '이란', 3513, 107),
(20, '쿠웨이트', 58, 0),
(21, '바레인', 52, 0),
(22, '아랍에미리트', 28, 0),
(23, '이라크', 36, 2),
(24, '오만', 16, 0),
(25, '레바논', 16, 0),
(26, '이스라엘', 15, 0),
(27, '이집트', 3, 0),
(28, '알제리', 12, 0),
(29, '카타르', 8, 0),
(30, '요르단', 1, 0),
(31, '튀니지', 1, 0),
(32, '사우디', 5, 0),
(33, '모로코', 2, 0),
(34, '미국', 158, 11),
(35, '캐나다', 33, 0),
(36, '브라질', 3, 0),
(37, '멕시코', 5, 0),
(38, '에콰도르', 10, 0),
(39, '도미니카공화국', 1, 0),
(40, '아르헨티나', 1, 0),
(41, '칠레', 3, 0),
(42, '이탈리아', 3858, 148),
(43, '독일', 400, 0),
(44, '프랑스', 377, 6),
(45, '영국', 115, 0),
(46, '스페인', 200, 1),
(47, '오스트리아', 37, 0),
(48, '크로아티아', 9, 0),
(49, '핀란드', 7, 0),
(50, '스웨덴', 35, 0),
(51, '스위스', 57, 0),
(52, '벨기에', 23, 0),
(53, '덴마크', 10, 0),
(54, '에스토니아', 2, 0),
(55, '조지아', 3, 0),
(56, '그리스', 9, 0),
(57, '북마케도니아', 1, 0),
(58, '노르웨이', 56, 0),
(59, '루마니아', 4, 0),
(60, '네덜란드', 38, 0),
(61, '벨라루스', 6, 0),
(62, '리투아니아', 1, 0),
(63, '산마리노', 16, 1);

--
-- 덤프된 테이블의 인덱스
--

--
-- 테이블의 인덱스 `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`num`);

--
-- 테이블의 인덱스 `world`
--
ALTER TABLE `world`
  ADD PRIMARY KEY (`num`);

--
-- 덤프된 테이블의 AUTO_INCREMENT
--

--
-- 테이블의 AUTO_INCREMENT `city`
--
ALTER TABLE `city`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- 테이블의 AUTO_INCREMENT `world`
--
ALTER TABLE `world`
  MODIFY `num` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
