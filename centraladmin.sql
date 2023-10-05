-- MySQL dump 10.13  Distrib 5.7.39, for Linux (x86_64)
--
-- Host: localhost    Database: central_admin
-- ------------------------------------------------------
-- Server version	5.7.39-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_delete` int(11) DEFAULT '0' COMMENT '1 = deleted, 0 = not deleted',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Ghazi Taqiyya','60879ae741d0aef9814485c02177e13120d438f96003cd40d3ce1bcbb62e14f9:ae2e69576cea4e29aad013a3195c2ffa','taqiyyaghazi@gmail.com','2022-09-09 09:01:20',0),(2,'Salwa Ziada Salsabiila','3396e86951bd9523b6294387e52366715ec7cf2b4c21a2b7a6327aadfe7b89a2:386ac79f35a3493daff08282e7cd6c01','salwaziada27@gmail.com','2022-09-09 09:12:08',0);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('4fc0adf42faf');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kode` varchar(7) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `tanggal` date NOT NULL,
  `waktu_mulai` datetime NOT NULL,
  `waktu_berakhir` datetime NOT NULL,
  `nama_pemateri` varchar(255) NOT NULL,
  `nama_pemateri_2` varchar(255) DEFAULT NULL,
  `contact_whatsapp` varchar(50) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `poster` varchar(255) NOT NULL,
  `deskripsi` varchar(2000) NOT NULL,
  `link_conference` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `is_published` int(11) DEFAULT '1' COMMENT '1 = published, 0 = not published',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_delete` int(11) DEFAULT '0' COMMENT '1 = deleted, 0 = not deleted',
  PRIMARY KEY (`id`),
  UNIQUE KEY `kode` (`kode`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (3,'de6e80','Membantu Pihak UMKM dalam hal penyediaan stok barang','2022-09-09','2022-09-09 08:00:00','2022-09-09 10:00:00','Bungaran Martua Pakpahan',NULL,'wa.me/+628137068001','bungaranmart2001@gmail.com','2022-09-08_102515_46364_poster_event.jpg','Webinar akan menjelaskan','https://meet.google.com/uyt-uhmv',NULL,0,'2022-09-08 10:25:16',0),(5,'02a10d','Membantu pihak UMKM  dalam hal penyediaan stok barang','2022-09-09','2022-09-09 10:00:00','2022-09-09 12:00:00','Bungaran Martua Pakpahan',NULL,'wa.me/+6281370680001','bungaranmart2001@gmail.com','2022-09-08_103250_80875_poster_event.jpg','Webinar akan menjelaskan bagaimana pihak UMKM dalam Manajemen inventory penyediaan stok barang dengan metode Algoritma Clustering yang akan disampaikan.','https://meet.google.com/uyi-uhmw-wfj',NULL,0,'2022-09-08 10:32:50',0),(6,'9c3358','Manajemen inventory UMKM dalam hal penyediaan stok barang','2022-09-09','2022-09-09 10:00:00','2022-09-09 12:00:00','Bungaran Martua Pakpahan',NULL,'wa.me/+6281370680001','bungaranmart2001@gmail.com','2022-09-08_132735_08459_poster_event.jpg','Webinar akan menjelaskan bagaimana pihak UMKM dalam Manajemen inventory penyediaan stok barang dengan metode Algoritma Clustering yang akan disampaikan.','https://meet.google.com/uyi-uhmw-wfj',NULL,1,'2022-09-08 13:27:36',0),(7,'6ac68b','Problem Solving Dengan Machine Learning','2022-09-15','2022-09-15 12:30:00','2022-09-15 14:30:00','Teguh Dayanto, S.T.',NULL,'wa.me/+6281227515025','teguh@gmail.com','2022-09-09_090538_28355_poster_event.jpg','[Pembelajaran Tamu]\n\nProblem Solving Dengan Machine Learning\n\nMachine Learning merupakan sebuah teknologi dimana mesin bisa belajar layaknya manusia. Pada dasarnya Machine Learning dapat mempelajari sebuah data yang ada dengan tugas tertentu. Pada webinar ini akan dibahas mengenai Problem Solving Dengan Machine Learning, Dengan :\n\nNarasumber : \nTeguh Dayanto, S.T.\nMentor SIB BISA AI Academy\n\nWaktu : \nSenin,12 September 2022\n19.00 - 21.00 WIB\n\nLink Pendaftaran:\nhttps://tampil.id','https://tampil.id/event/detail/VFdwWk1VNW5QVDA9',NULL,0,'2022-09-09 09:05:38',0),(8,'886c07','Society ERA 5.0 : Peluang, Tantangan dan Masa Depan','2022-10-22','2022-10-22 08:30:00','2022-10-22 10:30:00','Anwar Sanusi',NULL,'wa.me/+6287863825615','anwarsanusisan@gmail.com','2022-09-10_104259_72617_poster_event.jpg','Mengenalkan society era 5.0 kepada masyarakat beserta latar belakang yang mendasari munculnya era tersebut dan bagaimana masyarakat menghadapi era tersebut dengan melihat peluang tantangan yang akan datang demi masa depan masyarakat kedepannya.','https://meet.google.com/qpf-jjbs-gwh',NULL,0,'2022-09-10 10:42:59',0);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kategori`
--

DROP TABLE IF EXISTS `kategori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kategori` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kategori` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_delete` int(11) DEFAULT '0' COMMENT '1 = deleted, 0 = not deleted',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kategori`
--

LOCK TABLES `kategori` WRITE;
/*!40000 ALTER TABLE `kategori` DISABLE KEYS */;
/*!40000 ALTER TABLE `kategori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kehadiran`
--

DROP TABLE IF EXISTS `kehadiran`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kehadiran` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_event` int(11) NOT NULL,
  `kode_kehadiran` varchar(7) NOT NULL,
  `nama_peserta` varchar(255) NOT NULL,
  `email_peserta` varchar(255) NOT NULL,
  `link_sertifikat` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_delete` int(11) DEFAULT '0' COMMENT '1 = deleted, 0 = not deleted',
  PRIMARY KEY (`id`),
  KEY `id_event` (`id_event`),
  CONSTRAINT `kehadiran_ibfk_1` FOREIGN KEY (`id_event`) REFERENCES `event` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kehadiran`
--

LOCK TABLES `kehadiran` WRITE;
/*!40000 ALTER TABLE `kehadiran` DISABLE KEYS */;
/*!40000 ALTER TABLE `kehadiran` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activity` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_delete` int(11) DEFAULT '0' COMMENT '1 = deleted, 0 = not deleted',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES (1,'Seseorang dengan email:tes@gmail.com melakukan pengajuan event baru dengan kode:944dbb','2022-09-06 22:24:30',0),(2,'Seseorang dengan email:siapaayo@gmail.com melakukan pengajuan event baru dengan kode:61f676','2022-09-06 22:41:45',0),(3,'Seseorang dengan email:bungaranmart2001@gmail.com melakukan pengajuan event baru dengan kode:de6e80','2022-09-08 10:25:16',0),(4,'Seseorang dengan email:testing@gmail.com melakukan pengajuan event baru dengan kode:e7aaf2','2022-09-08 10:29:06',0),(5,'Seseorang dengan email:bungaranmart2001@gmail.com melakukan pengajuan event baru dengan kode:02a10d','2022-09-08 10:32:50',0),(6,'Seseorang dengan email:bungaranmart2001@gmail.com melakukan pengajuan event baru dengan kode:9c3358','2022-09-08 13:27:36',0),(7,'ADMIN baru dengan email:taqiyyaghazi@gmail.com berhasil dibuat','2022-09-09 09:01:20',0),(8,'ADMIN dengan email:taqiyyaghazi@gmail.com login','2022-09-09 09:01:36',0),(9,'Seseorang dengan email:teguh@gmail.com melakukan pengajuan event baru dengan kode:6ac68b','2022-09-09 09:05:38',0),(10,'ADMIN dengan email:taqiyyaghazi@gmail.com berhasil publish event dengan kode:6ac68b','2022-09-09 09:06:02',0),(11,'ADMIN dengan email:taqiyyaghazi@gmail.com berhasil unpublish event dengan kode:6ac68b','2022-09-09 09:06:18',0),(12,'ADMIN dengan email:taqiyyaghazi@gmail.com berhasil publish event dengan kode:9c3358','2022-09-09 09:06:42',0),(13,'ADMIN baru dengan email:salwaziada27@gmail.com berhasil dibuat','2022-09-09 09:12:08',0),(14,'ADMIN dengan email:salwaziada27@gmail.com login','2022-09-09 09:13:15',0),(15,'ADMIN dengan email:taqiyyaghazi@gmail.com login','2022-09-09 09:13:24',0),(16,'ADMIN dengan email:taqiyyaghazi@gmail.com login','2022-09-09 09:39:59',0),(17,'ADMIN dengan email:taqiyyaghazi@gmail.com login','2022-09-09 16:52:10',0),(18,'Seseorang dengan email:anwarsanusisan@gmail.com melakukan pengajuan event baru dengan kode:886c07','2022-09-10 10:42:59',0);
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portofolio`
--

DROP TABLE IF EXISTS `portofolio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portofolio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_user` int(11) NOT NULL,
  `approved` int(11) DEFAULT '0' COMMENT '1 = approved, 0 = not approved',
  `judul` varchar(50) NOT NULL,
  `deskripsi_singkat` text NOT NULL,
  `deskripsi_lengkap` text NOT NULL,
  `id_kategori` int(11) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `foto_1` varchar(100) DEFAULT NULL,
  `foto_2` varchar(100) DEFAULT NULL,
  `foto_3` varchar(100) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_delete` int(11) DEFAULT '0' COMMENT '1 = deleted, 0 = not deleted',
  PRIMARY KEY (`id`),
  KEY `id_kategori` (`id_kategori`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `portofolio_ibfk_1` FOREIGN KEY (`id_kategori`) REFERENCES `kategori` (`id`) ON DELETE CASCADE,
  CONSTRAINT `portofolio_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portofolio`
--

LOCK TABLES `portofolio` WRITE;
/*!40000 ALTER TABLE `portofolio` DISABLE KEYS */;
/*!40000 ALTER TABLE `portofolio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `jenis_kelamin` varchar(10) DEFAULT NULL,
  `nomor_telepon` varchar(17) DEFAULT NULL,
  `linkedin` varchar(100) DEFAULT NULL,
  `instagram` varchar(100) DEFAULT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `riwayat_kerja` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_delete` int(11) DEFAULT '0' COMMENT '1 = deleted, 0 = not deleted',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-10 12:26:28
