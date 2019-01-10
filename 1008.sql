/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : 1008

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2018-10-29 22:01:06
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `class`
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` char(20) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES ('2', '网工1501');
INSERT INTO `class` VALUES ('8', '科技1601');
INSERT INTO `class` VALUES ('13', '物理1503');
INSERT INTO `class` VALUES ('20', '数本1802');
INSERT INTO `class` VALUES ('24', '111');

-- ----------------------------
-- Table structure for `student`
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) COLLATE utf8_bin DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `class_id` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('6', '王亮', '2');
INSERT INTO `student` VALUES ('14', '万三11', '8');
INSERT INTO `student` VALUES ('15', '李四', '20');
INSERT INTO `student` VALUES ('21', 'hahaha', '2');
INSERT INTO `student` VALUES ('22', '222', '2');
INSERT INTO `student` VALUES ('23', '555', '2');
INSERT INTO `student` VALUES ('24', '777', '2');
INSERT INTO `student` VALUES ('25', '999', '13');
INSERT INTO `student` VALUES ('26', '888', '20');
INSERT INTO `student` VALUES ('27', 'vdv', '8');

-- ----------------------------
-- Table structure for `teacher`
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('2', '沈老师');
INSERT INTO `teacher` VALUES ('3', '王老师');
INSERT INTO `teacher` VALUES ('6', '2老师000');
INSERT INTO `teacher` VALUES ('13', '888');
INSERT INTO `teacher` VALUES ('14', '777');
INSERT INTO `teacher` VALUES ('15', '777');
INSERT INTO `teacher` VALUES ('16', '666');
INSERT INTO `teacher` VALUES ('17', '555');

-- ----------------------------
-- Table structure for `teacher2class`
-- ----------------------------
DROP TABLE IF EXISTS `teacher2class`;
CREATE TABLE `teacher2class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_id` (`teacher_id`),
  KEY `class_id` (`class_id`),
  CONSTRAINT `teacher2class_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`),
  CONSTRAINT `teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of teacher2class
-- ----------------------------
INSERT INTO `teacher2class` VALUES ('1', '2', '8');
INSERT INTO `teacher2class` VALUES ('2', '2', '13');
INSERT INTO `teacher2class` VALUES ('3', '3', '2');
INSERT INTO `teacher2class` VALUES ('4', '3', '24');
INSERT INTO `teacher2class` VALUES ('5', '6', '20');
INSERT INTO `teacher2class` VALUES ('6', '6', '2');
INSERT INTO `teacher2class` VALUES ('7', '6', '13');
INSERT INTO `teacher2class` VALUES ('21', '13', '8');
INSERT INTO `teacher2class` VALUES ('22', '13', '24');
INSERT INTO `teacher2class` VALUES ('23', '14', '20');
INSERT INTO `teacher2class` VALUES ('24', '14', '24');
INSERT INTO `teacher2class` VALUES ('25', '15', '20');
INSERT INTO `teacher2class` VALUES ('26', '15', '24');
INSERT INTO `teacher2class` VALUES ('27', '16', '20');
INSERT INTO `teacher2class` VALUES ('28', '16', '24');
INSERT INTO `teacher2class` VALUES ('29', '17', '8');
INSERT INTO `teacher2class` VALUES ('30', '17', '13');
