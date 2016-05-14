#!/usr/bin/env python
# -*- coding=utf-8 -*-

import os

def apache_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "apache2" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "apache2" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "apache2" + " " + "stop")

def ssh_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "ssh" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "ssh" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "ssh" + " " + "stop")

def mysql_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "mysql" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "mysql" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "mysql" + " " + "stop")

def phpmyadmin_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "phpmyadmin" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "phpmyadmin" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "phpmyadmin" + " " + "stop")

def webin_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "webmin" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "webmin" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "webmin" + " " + "stop")

def samba_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "samba" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "samba" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "samba" + " " + "stop")


def freeradius_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "freeradius" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "freeradius" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "freeradius" + " " + "stop")


def postgresql_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "postgresql" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "postgresql" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "postgresql" + " " + "stop")


def networking_service():
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "networking" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "networking" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "networking" + " " + "stop")

def openvpn_service():
	print islem_ico
	islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")
	if islem == 1:
		os.system("service" + " " + "openvpn" + " " + "start")
	if islem == 2:
		os.system("service" + " " + "openvpn" + " " + "restart")
	if islem == 3:
		os.system("service" + " " + "openvpn" + " " + "stop")

service_starter_ico = """
#########################################################
#        PYTHON - SERVICE STARTER - GH0ST S0FTWARE      #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

print service_starter_ico

islemler_ico = """
(1) Apache Server Service	(6) Webmin Server Service
(2) SSH Server Service		(7) Samba Server Service
(3) MySQL Server Service	(8) FreeRadius Server Service
(4) Postgresql Server Service	(9) Network Server Service
(5) PhpMyAdmin Server Service	(10) OpenVPN Server Service										
"""

print islemler_ico

islem = input("Yapmak istediğiniz işlem numarasını giriniz : ")

islem_ico = """
(1) START
(2) RESTART
(3) STOP
"""

if islem == 1:
	apache_service()
if islem == 2:
	ssh_service()
if islem == 3:
	mysql_service()
if islem == 4:
	postgresql_service()
if islem == 5:
	phpmyadmin_service()
if islem == 6:
	webin_service()
if islem == 7:
	samba_service()
if islem == 8:
	freeradius_service()
if islem == 9:
	networking_service()
if islem == 10:
	openvpn_service
