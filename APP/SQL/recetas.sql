-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 26, 2023 at 04:19 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ame`
--

-- --------------------------------------------------------

--
-- Table structure for table `recetas`
--

CREATE TABLE `recetas` (
  `receta_id` int(11) NOT NULL,
  `fecha` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `edad` varchar(255) DEFAULT NULL,
  `temp` varchar(255) DEFAULT NULL,
  `ta` varchar(255) DEFAULT NULL,
  `peso` varchar(255) DEFAULT NULL,
  `fc` varchar(255) DEFAULT NULL,
  `talla` varchar(255) DEFAULT NULL,
  `fr` varchar(255) DEFAULT NULL,
  `circun_abdom` varchar(255) DEFAULT NULL,
  `id` varchar(255) DEFAULT NULL,
  `alergias` varchar(255) DEFAULT NULL,
  `tratamiento` varchar(255) DEFAULT NULL,
  `Instruccion1` varchar(255) DEFAULT NULL,
  `Tratamiento2` varchar(255) DEFAULT NULL,
  `Instruccion2` varchar(255) DEFAULT NULL,
  `Tratamiento3` varchar(255) DEFAULT NULL,
  `Instruccion3` varchar(255) DEFAULT NULL,
  `Tratamiento4` varchar(255) DEFAULT NULL,
  `Instruccion4` varchar(255) DEFAULT NULL,
  `indicaciones_generales` varchar(255) DEFAULT NULL,
  `proxima_cita` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `recetas`
--
ALTER TABLE `recetas`
  ADD PRIMARY KEY (`receta_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `recetas`
--
ALTER TABLE `recetas`
  MODIFY `receta_id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
