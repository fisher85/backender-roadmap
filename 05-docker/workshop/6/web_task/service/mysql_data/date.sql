

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `test1` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `test1`;

--
-- Table structure for table `flag`
--

DROP TABLE IF EXISTS `flag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flag` (
  `flag_is` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flag`
--

LOCK TABLES `flag` WRITE;
/*!40000 ALTER TABLE `flag` DISABLE KEYS */;
INSERT INTO `flag` VALUES ('3686962a34ba2e4c0943547ec3bdb12a');
/*!40000 ALTER TABLE `flag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news` (
  `id` int(11) DEFAULT NULL,
  `title` varchar(20) DEFAULT NULL,
  `content` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (1,'To discus','MOSCOW, Dec 14 - RIA News. The Prime Ministers of Belarus and Russia Sergey Rumas and Dmitry Medvedev discussed over the telephone interaction on integration and trade, including a number of energy dialogue issues, the press service of the Cabinet reported on Saturday.'),(1,'Discussion on Kuril','MOSCOW, Dec 15 - RIA News. State Duma deputy Dmitry Novikov (\"Communist Party\") considers it pointless to return to the discussion between Russia and Japan on the Kuril Islands, as Japan violated the agreements necessary to ensure collective security by deploying US military bases on its territory.');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Admim','5UP3R53cr37P422w0Rd'),('Admin','5UP3R53cr37P422w0Rd');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

