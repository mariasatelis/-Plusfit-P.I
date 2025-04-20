-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28-Jul-2023 às 20:34
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `planusfit`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cadastro_1`
--

CREATE TABLE `cadastro_1` (
  `peso` int(10) NOT NULL,
  `altura` int(10) NOT NULL,
  `gordura` int(10) NOT NULL,
  `id` int(50) NOT NULL,
  `nome` varchar(120) NOT NULL,
  `sobrenome` varchar(120) NOT NULL,
  `email` varchar(120) NOT NULL,
  `senha` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `cadastro_1`
--

INSERT INTO `cadastro_1` (`peso`, `altura`, `gordura`, `id`, `nome`, `sobrenome`, `email`, `senha`) VALUES
(20, 41, 10, 1, 'a', 'a', 'a', 'a'),
(1, 1, 1, 2, 'a', 'a', 'a', 'a');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cadastro_1`
--
ALTER TABLE `cadastro_1`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cadastro_1`
--
ALTER TABLE `cadastro_1`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
