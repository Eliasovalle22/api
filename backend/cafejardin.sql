-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: cafejardin
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `precio` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'coca - cola',3200,'2024-10-18 22:35:06','2024-10-18 22:35:06'),(2,'papa  de pollo',2800,'2024-10-18 22:35:30','2024-10-19 10:00:32'),(3,'Sprite',3500,'2024-10-18 22:43:13','2024-10-18 22:43:25'),(5,'Empanada de pollo',2800,'2024-10-19 09:58:35','2024-10-19 09:58:35'),(6,'Empanada de carne',2800,'2024-10-19 09:58:52','2024-10-19 09:58:52'),(7,'Empanada de queso',3000,'2024-10-19 09:59:11','2024-10-19 09:59:11'),(8,'Empanada de jamón',3500,'2024-10-19 09:59:33','2024-10-19 09:59:33'),(9,'Patacón de pollo',3800,'2024-10-19 10:00:02','2024-10-19 10:00:02'),(10,'Patacón de carne',3800,'2024-10-19 10:00:13','2024-10-19 10:00:13');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'ramon@ul.edu.co','ramon2805*','2024-10-18 22:33:48','2024-10-18 22:34:36'),(2,'dalgis2024@ul.edu.co','Dalgis2805*','2024-10-18 22:41:35','2024-10-19 09:52:18'),(4,'moises@ul.edu.co','Moises2347','2024-10-19 09:51:49','2024-10-19 09:51:49'),(5,'darwin@ul.edu.co','Darwin324*','2024-10-19 09:53:37','2024-10-19 09:53:37'),(6,'yolanda@ul.edu.co','Yoli239*','2024-10-19 09:54:05','2024-10-19 09:54:05'),(7,'Jair2099@ul.edu.co','2099Jair@','2024-10-19 09:55:07','2024-10-19 09:55:07'),(8,'saraymont7@ul.edu.co','Sara992*','2024-10-19 09:56:20','2024-10-19 09:56:20'),(9,'camilomercado@ul.edu.co','cam2024@','2024-10-19 09:56:52','2024-10-19 09:56:52'),(10,'cafejardin@ul.edu.co','Cafeja2024','2024-10-19 09:57:23','2024-10-19 09:57:23');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-19 10:56:49
