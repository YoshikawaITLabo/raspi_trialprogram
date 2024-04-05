-- MariaDB dump 10.19  Distrib 10.5.23-MariaDB, for debian-linux-gnu (aarch64)
--
-- Host: localhost    Database: webbackup
-- ------------------------------------------------------
-- Server version	10.5.23-MariaDB-0+deb11u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `finishedlist`
--

DROP TABLE IF EXISTS `finishedlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `finishedlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FileName` varchar(128) DEFAULT NULL,
  `FileSize` int(11) DEFAULT NULL,
  `CreationDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `UpdatedDate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finishedlist`
--

LOCK TABLES `finishedlist` WRITE;
/*!40000 ALTER TABLE `finishedlist` DISABLE KEYS */;
INSERT INTO `finishedlist` VALUES (3,'wordpress_images_240402032001.tar.gz',1874328940,'2024-04-01 18:21:22','2024-04-05 11:52:43'),(4,'wpcli.log',1048,'2024-04-04 19:00:29','2024-04-05 12:39:09'),(5,'240405-ec.sql.gz',21750,'2024-04-04 18:10:01','2024-04-05 12:45:49'),(6,'wordpress_images_240404032001.tar.gz',1874533802,'2024-04-03 18:21:21','2024-04-05 13:06:52'),(7,'wordpress_images_240403032001.tar.gz',1874328963,'2024-04-02 18:21:21','2024-04-05 13:19:11'),(8,'240405-wp.sql.gz',4308110,'2024-04-04 18:00:01','2024-04-05 13:19:32'),(9,'eccube_images_240402034001.tar.gz',66354058,'2024-04-01 18:40:13','2024-04-05 13:20:00'),(10,'240404-wp.sql.gz',4307999,'2024-04-03 18:00:02','2024-04-05 13:20:32'),(11,'eccube_images_240404034001.tar.gz',66360159,'2024-04-03 18:40:13','2024-04-05 13:20:57'),(12,'wordpress_images_240405032001.tar.gz',1874615788,'2024-04-04 18:21:22','2024-04-05 13:32:26'),(13,'eccube_backup.log',3400476,'2024-04-04 18:40:12','2024-04-05 13:35:55'),(14,'eccube_images_240403034001.tar.gz',66360159,'2024-04-02 18:40:13','2024-04-05 13:36:26'),(15,'eccube_images_240405034001.tar.gz',66360159,'2024-04-04 18:40:12','2024-04-05 13:36:57'),(16,'wordpress_backup.log',3117976,'2024-04-04 18:21:22','2024-04-05 13:37:16'),(17,'240404-ec.sql.gz',21750,'2024-04-03 18:10:01','2024-04-05 13:37:19');
/*!40000 ALTER TABLE `finishedlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostlist`
--

DROP TABLE IF EXISTS `hostlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hostlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(32) DEFAULT NULL,
  `port` smallint(6) DEFAULT NULL,
  `user` varchar(32) DEFAULT NULL,
  `keysfolder` varchar(64) DEFAULT NULL,
  `keyfile` varchar(64) DEFAULT NULL,
  `passphrase` varchar(64) DEFAULT NULL,
  `copy_source` varchar(64) DEFAULT NULL,
  `Copy_to` varchar(64) DEFAULT NULL,
  `Storage` varchar(64) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostlist`
--

LOCK TABLES `hostlist` WRITE;
/*!40000 ALTER TABLE `hostlist` DISABLE KEYS */;
INSERT INTO `hostlist` VALUES (1,'yoshisyou.com',22,'ubuntu','/home/kazuhiro/Documents/Key/','id_ed25519','WIb_.7pxv1D08yhK','/home/backup/','/home/kazuhiro/Downloads/','/mnt/rsp_nas/ras_backup/','2024-04-05 01:33:03','2024-04-05 10:45:26');
/*!40000 ALTER TABLE `hostlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `templist`
--

DROP TABLE IF EXISTS `templist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `templist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FileName` varchar(128) DEFAULT NULL,
  `FileSize` int(11) DEFAULT NULL,
  `CreationDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `UpdatedDate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `templist`
--

LOCK TABLES `templist` WRITE;
/*!40000 ALTER TABLE `templist` DISABLE KEYS */;
INSERT INTO `templist` VALUES (139,'wordpress_images_240404032001.tar.gz',1874533802,'2024-04-03 18:21:21','2024-04-05 12:54:16'),(140,'wordpress_images_240403032001.tar.gz',1874328963,'2024-04-02 18:21:21','2024-04-05 12:54:16'),(141,'240405-wp.sql.gz',4308110,'2024-04-04 18:00:01','2024-04-05 12:54:16'),(142,'eccube_images_240402034001.tar.gz',66354058,'2024-04-01 18:40:13','2024-04-05 12:54:16'),(143,'240404-wp.sql.gz',4307999,'2024-04-03 18:00:02','2024-04-05 12:54:16'),(144,'eccube_images_240404034001.tar.gz',66360159,'2024-04-03 18:40:13','2024-04-05 12:54:16'),(145,'wordpress_images_240405032001.tar.gz',1874615788,'2024-04-04 18:21:22','2024-04-05 12:54:16'),(146,'eccube_backup.log',3400476,'2024-04-04 18:40:12','2024-04-05 12:54:16'),(147,'eccube_images_240403034001.tar.gz',66360159,'2024-04-02 18:40:13','2024-04-05 12:54:16'),(148,'eccube_images_240405034001.tar.gz',66360159,'2024-04-04 18:40:12','2024-04-05 12:54:16'),(149,'wordpress_backup.log',3117976,'2024-04-04 18:21:22','2024-04-05 12:54:16'),(150,'240404-ec.sql.gz',21750,'2024-04-03 18:10:01','2024-04-05 12:54:17');
/*!40000 ALTER TABLE `templist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-05 22:56:06
