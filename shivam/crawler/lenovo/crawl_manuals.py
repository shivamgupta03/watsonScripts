import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

products = ["100-14IBD Laptop (ideapad)","100-14IBY Laptop (ideapad)","100-15IBD Laptop (ideapad)","100-15IBY Laptop (ideapad)","100e Chromebook (Lenovo)","100e Chromebook 2nd Gen (Lenovo)","100e Chromebook 2nd Gen MTK (Lenovo)","100e Winbook (Lenovo)","100e Windows 2nd Gen Notebook (Lenovo)","100S-11IBY Laptop (ideapad)","100S-14IBR Laptop (ideapad)","110 Touch-15ACL Laptop (ideapad)","110-14AST Laptop (ideapad)","110-14IBR Laptop (ideapad)","110-14ISK Laptop (ideapad)","110-15ACL Laptop (ideapad)","110-15AST Laptop (ideapad)","110-15IBR Laptop (ideapad)","110-15ISK Laptop (ideapad)","110-17ACL Laptop (ideapad)","110-17IKB Laptop (ideapad)","110-17ISK Laptop (ideapad)","110S-11IBR Laptop (ideapad)","120S-11IAP Winbook (ideapad)","120S-14IAP Winbook (ideapad)","130-14AST Laptop (ideapad)","130-14IKB Laptop (ideapad)","130-15AST Laptop (ideapad)","130-15IKB Laptop (ideapad)","130S-11IGM Laptop (ideapad)","130S-14IGM Laptop (ideapad)","100S Chromebook (Lenovo)","11e 4th Gen Chromebook (Type 20HX 20J0) Laptop (ThinkPad)","11e Chromebook (Type 20DB, 20DU) Laptop (ThinkPad)","11e Chromebook (Type 20GD, 20GF) Laptop (ThinkPad)","Yoga 11e 4th Gen Chromebook (Type 20HW 20HY) Laptop","(ThinkPad)","11e (Type 20D9, 20DA) Laptop (ThinkPad)","11e (Type 20E6, 20E8) Laptop (ThinkPad)","11e (Type 20ED, 20EE) Laptop (ThinkPad)","11e 3rd Gen (Type 20G9, 20GB) Laptop (ThinkPad)","11e 4th Gen (Type 20HT 20HV) Laptop (ThinkPad)","11e 5th Gen (Type 20LR 20LQ) Laptop (ThinkPad)","13 Chromebook (Type 20GL, 20GM) Laptop (Thinkpad)","13 (Type 20GJ, 20GK) Laptop (ThinkPad)","13 Gen 2 (Type 20J1, 20J2) Laptop (ThinkPad)","14W Laptop (Lenovo)","2in1-11 Laptop (ideapad)","2in1-14 Laptop (ideapad)","300-14IBR Laptop (ideapad)","300-14ISK Laptop (ideapad)","300-15IBR Laptop (ideapad)","300-15ISK Laptop (ideapad)","300-17ISK Laptop (ideapad)","300e Chromebook (Lenovo)","300e Chromebook 2nd Gen (Lenovo)","300e Chromebook 2nd Gen MTK (Lenovo)","300e Winbook (Lenovo)","300e Windows 2nd Gen Notebook (Lenovo)","300S-11IBR Laptop (ideapad)","300S-14ISK Laptop (ideapad)","305-14IBD Laptop (ideapad)","305-15ABM Laptop (ideapad)","305-15IBD Laptop (ideapad)","305-15IBY Laptop (ideapad)","305-15IHW Laptop (ideapad)","310 Touch-15IKB Laptop (ideapad)","310 Touch-15ISK Laptop (ideapad)","310-14IAP Laptop (ideapad)","310-14IKB Laptop (ideapad)","310-14ISK Laptop (ideapad)","310-15ABR Laptop (ideapad)","310-15IAP Laptop (ideapad)","310-15IKB Laptop (ideapad)","310-15ISK Laptop (ideapad)","310S-11IAP Laptop (ideapad)","310S-14AST Laptop (ideapad)","310S-14IKB Laptop (ideapad)","310S-14ISK Laptop (ideapad)","310S-15IKB Laptop (ideapad)","320 Touch-15ABR Laptop (ideapad)","320 Touch-15IKB (Type 80XN) Laptop (ideapad)","320 Touch-15IKB (Type 81BH) Laptop (ideapad)","320-14AST Laptop (ideapad)","320-14IAP Laptop (ideapad)","320-14IKB Laptop (ideapad)","320-14ISK Laptop (ideapad)","320-15ABR Laptop (ideapad)","320-15AST Laptop (ideapad)","320-15IAP Laptop (ideapad)","320-15IKB (Type 80XL, 80YE) Laptop (ideapad)","320-15IKB (Type 81BG, 81BT) Laptop (ideapad)","320-15ISK Laptop (ideapad)","320-17ABR Laptop (ideapad)","320-17AST Laptop (ideapad)","320-17IKB (Type 80XM) Laptop (ideapad)","320-17IKB (Type 81BJ) Laptop (ideapad)","320-17ISK Laptop (ideapad)","320C-15IKB Laptop (ideapad)","320S-13IKB Laptop (ideapad)","320S-14IKB (Type 80X4) Laptop (ideapad)","320S-14IKB (Type 81BN) Laptop (ideapad)","320S-15ABR Laptop (ideapad)","320S-15AST Laptop (ideapad)","320S-15IKB (Type 80X5) Laptop (ideapad)","320S-15IKB (Type 81BQ) Laptop (ideapad)","320S-15ISK Laptop (ideapad)","330 Touch-15ARR Laptop (ideapad)","330 Touch-15IKB (Type 81DH) Laptop (ideapad)","330 Touch-15IKB (Type 81DJ) Laptop (ideapad)","330-14AST Laptop (ideapad)","330-14IGM Laptop (ideapad)","330-14IKB (Type 81DA) Laoptop (ideapad)","330-14IKB (Type 81G2) Laptop (ideapad)","330-15ARR Laptop (ideapad)","330-15AST Laptop (ideapad)","330-15ICH Laptop (ideapad)","330-15ICN Laptop (ideapad)","330-15IGM Laptop (ideapad)","330-15IKB (Type 81DC) Laptop (ideapad)","330-15IKB (Type 81DE) Laptop (ideapad)","330-15IKB (Type 81FD) Laptop (ideapad)","330-17AST Laptop (ideapad)","330-17ICH Laptop (ideapad)","330-17IKB (Type 81DK) Laptop (ideapad)","330-17IKB (Type 81DM) Laptop (ideapad)","330S-14AST Laptop (ideapad)","330S-14IKB Laptop (ideapad)","330S-15ARR Laptop (ideapad)","330S-15AST Laptop (ideapad)","330S-15IKB GTX1050 Laptop (ideapad)","330S-15IKB Laptop (ideapad)","510S-14ISK Laptop (ideapad)","520-15IKB (Type 80YL) Laptop (ideapad)","520-15IKB (Type 81BF) Laptop (ideapad)","520S-14IKB (Type 80X2) Laptop (ideapad)","520S-14IKB (Type 81BL) Laptop (ideapad)","530S-14ARR Laptop (ideapad)","530S-14IKB Laptop (ideapad)","530S-15IKB Laptop (ideapad)","720S Touch-15IKB Laptop (ideapad)","720S-13ARR Laptop (ideapad)","720S-13IKB (Type 81A8) Laptop (ideapad)","720S-13IKB (Type 81BV) Laptop (ideapad)","720S-14IKB (Type 80XC) Laptop (ideapad)","720S-14IKB (Type 81BD) Laptop (ideapad)","720S-15IKB Laptop (ideapad)","730S-13IWL Laptop (ideapad)","A10 Laptop (Lenovo)","A275 (Type 20KC, 20KD) Laptop (ThinkPad)","A285 (Type 20MW, 20MX) Laptop (ThinkPad)","A475 (Type 20KL, 20KM) Laptop (ThinkPad)","A485 (Type 20MU, 20MV) Laptop (ThinkPad)","B110-14IBR Laptop (Lenovo)","B320-14IKB Laptop (Lenovo)","B40-30 Laptop (Lenovo)","B40-45 Laptop (Lenovo)","B40-70 Laptop (Lenovo)","B41-30 Laptop (Lenovo)","B41-35 Laptop (Lenovo)","B41-80 Laptop (Lenovo)","B430 Laptop (Lenovo)","B4400 Laptop (Lenovo)","B4400s Laptop (Lenovo)","B4450s Laptop (Lenovo)","B460e Laptop (Lenovo)","B470 Laptop (Lenovo)","B470e Laptop (Lenovo)","B475 Laptop (Lenovo)","B475e Laptop (Lenovo)","B480 Laptop (Lenovo)","B485 Laptop (Lenovo)","B490 Laptop (Lenovo)","B490s Laptop (Lenovo)","B50-10 Laptop (Lenovo)","B50-30 Laptop (Lenovo)","B50-30 Touch Laptop (Lenovo)","B50-45 Laptop (Lenovo)","B50-50 Laptop (Lenovo)","B50-70 Laptop (Lenovo)","B51-30 Laptop (Lenovo)","B51-35 Laptop (Lenovo)","B51-80 Laptop (Lenovo)","B5400 Laptop (Lenovo)","B570 Laptop (Lenovo)","B570e Laptop (Lenovo)","B570e2 Laptop (Lenovo)","B575 Laptop (Lenovo)","B575e Laptop (Lenovo)","B580 Laptop (Lenovo)","B590 Laptop (Lenovo)","B70-80 Laptop (Lenovo)","B71-80 Laptop (Lenovo)","Lenovo B40-80 Laptop","Lenovo B50-80 Laptop","C340-14API Laptop (ideapad)","C340-14IWL Laptop (ideapad)","C340-15IWL Laptop (ideapad)","D330-10IGM Laptop (ideapad)","E10-30 Laptop (Lenovo)","E31-70 Laptop (Lenovo)","E31-80 Laptop (Lenovo)","E40-30 Laptop (Lenovo)","E40-70 Laptop (Lenovo)","E40-80 Laptop (Lenovo)","E41-10 Laptops (Lenovo)","E41-15 Laptops (Lenovo)","E41-20 Laptop (Lenovo)","E41-25 Laptop (Lenovo)","E41-35 Laptop (Lenovo)","E41-80 Laptop (Lenovo)","E4325 Laptop (Lenovo)","E4430 Laptop (Lenovo)","E49 Laptop (Lenovo)","E50-70 Laptop (Lenovo)","E50-80 Laptop (Lenovo)","E51-80 Laptop (Lenovo)","Edge 15 Laptop (Lenovo)","Edge 2-1580 Laptop (Lenovo)","E450 (ThinkPad)","E450c (ThinkPad)","E455 (ThinkPad)","E460 (ThinkPad)","E465 (ThinkPad)","E470 Laptop (ThinkPad)","E475 Laptop (ThinkPad)","E480 (Type 20KN, 20KQ) Laptop (ThinkPad)","E485 (Type 20KU) Laptop (ThinkPad)","E490 (Type 20N8, 20N9) Laptop (ThinkPad)","E490s (Type 20NG) Laptop (ThinkPad)","E495 (Type 20NE) Laptop (ThinkPad)","E550 (ThinkPad)","E550c (ThinkPad)","E555 (ThinkPad)","E560 (ThinkPad)","E560p (ThinkPad)","E565 (ThinkPad)","E570 Laptop (ThinkPad)","E575 Laptop (ThinkPad)","E580 (Type 20KS 20KT) Laptop (ThinkPad)","E585 (Type 20KV) Laptop (ThinkPad)","E590 (Type 20NB, 20NC) Laptop (ThinkPad)","E595 (Type 20NF) Laptop (ThinkPad)","Edge E120 (ThinkPad)","Edge E125 (ThinkPad)","Edge E130 (ThinkPad)","Edge E135 (ThinkPad)","Edge E145 (ThinkPad)","Edge E220s (ThinkPad)","Edge E320 (ThinkPad)","Edge E325 (ThinkPad)","Edge E330 (ThinkPad)","Edge E335 (ThinkPad)","Edge E420 (ThinkPad)","Edge E420s (ThinkPad)","Edge E425 (ThinkPad)","Edge E430 (ThinkPad)","Edge E430c (ThinkPad)","Edge E431 (ThinkPad)","Edge E435 (ThinkPad)","Edge E440 (ThinkPad)","Edge E445 (ThinkPad)","Edge E520 (ThinkPad)","Edge E525 (ThinkPad)","Edge E530 (ThinkPad)","Edge E530c (ThinkPad)","Edge E531 (ThinkPad)","Edge E535 (ThinkPad)","Edge E540 (ThinkPad)","Edge E545 (ThinkPad)","Edge L330 (ThinkPad)","Edge S430 (ThinkPad)","G360 Laptop (Lenovo)","G40-30 Laptop (Lenovo)","G40-45 Laptop (Lenovo)","G40-70 Laptop (Lenovo)","G40-80 Laptop (Lenovo)","G400 Laptop (Lenovo)","G400s Laptop (Lenovo)","G400s Touch Laptop (Lenovo)","G405 Laptop (Lenovo)","G405s Laptop (Lenovo)","G41-35 Laptop (Lenovo)","G410 Laptop (Lenovo)","G410s Touch Laptop (Lenovo)","G460e Laptop (Lenovo)","G470 Laptop (Lenovo)","G475 Laptop (Lenovo)","G480 Laptop (Lenovo)","G485 Laptop (Lenovo)","G50-30 Laptop (Lenovo)","G50-45 Laptop (Lenovo)","G50-70 Laptop (Lenovo)","G50-80 Laptop (Lenovo)","G50-80 Touch Laptop (Lenovo)","G500 Laptop (Lenovo)","G500s Laptop (Lenovo)","G500s Touch Laptop (Lenovo)","G505 Laptop (Lenovo)","G505s Laptop (Lenovo)","G51-35 Laptop (Lenovo)","G510 Laptop (Lenovo)","G510s Laptop (Lenovo)","G560e Laptop (Lenovo)","G570 Laptop (Lenovo)","G575 Laptop (Lenovo)","G580 Laptop (Lenovo)","G585 Laptop (Lenovo)","G70-35 Laptop (Lenovo)","G70-70 Laptop (Lenovo)","G70-80 Laptop (Lenovo)","G700 Laptop (Lenovo)","G710 Laptop (Lenovo)","G770 Laptop (Lenovo)","G780 Laptop (Lenovo)","Helix (Type 20CG, 20CH) Laptop (ThinkPad)","Helix (Type 3xxx) Laptop (ThinkPad)","K2450 Laptop (Lenovo)","K29 Laptop (Lenovo)","K4350 Laptop (Lenovo)","K4450 Laptop (Lenovo)","K49 Laptop (Lenovo)","L340-15API Laptop (ideapad)","L340-15API Touch Laptop (ideapad)","L340-15IRH Gaming Laptop (ideapad)","L340-15IWL Laptop (ideapad)","L340-15IWL Touch Laptop (ideapad)","L340-17API Laptop (ideapad)","L340-17IRH Gaming Laptop (ideapad)","L340-17IWL Laptop (ideapad)","L380 (type 20M5, 20M6) Laptops (ThinkPad)","L380 Yoga (type 20M7, 20M8) Laptops (ThinkPad)","L390 (type 20NR, 20NS) Laptops (ThinkPad)","L390 Yoga (type 20NT, 20NU) Laptops (ThinkPad)","L420 Laptop (ThinkPad)","L421 Laptop (ThinkPad)","L430 Laptop (ThinkPad)","L440 Laptop (ThinkPad)","L450 Laptop (ThinkPad)","L460 Laptop (ThinkPad)","L470 (type 20J4, 20J5) Laptop (ThinkPad)","L470 (type 20JU, 20JV) Laptops (ThinkPad)","L480 (type 20LS, 20LT) Laptops (ThinkPad)","L490 (type 20Q5, 20Q6) Laptops (ThinkPad)","L520 Laptop (ThinkPad)","L530 Laptop (ThinkPad)","L540 Laptop (ThinkPad)","L560 Laptop (ThinkPad)","L570 (type 20J8, 20J9) Laptops (ThinkPad)","L570 (type 20JQ, 20JR) Laptops (ThinkPad)","L580 (type 20LW, 20LX) Laptops (ThinkPad)","L590 (type 20Q7, 20Q8) Laptops (ThinkPad)","LaVie Z Laptop (Lenovo)","Legion Y520-15IKBA Laptop (Lenovo)","Legion Y520-15IKBM Laptop (Lenovo)","Legion Y520-15IKBN Laptop (Lenovo)","Legion Y530-15ICH Laptop (Lenovo)","Legion Y530-15ICH-1060 Laptop (Lenovo)","Legion Y540-15IRH Laptop (Lenovo)","Legion Y540-15IRH-PG0 Laptop (Lenovo)","Legion Y540-17IRH Laptop (Lenovo)","Legion Y540-17IRH-PG0 Laptop (Lenovo)","Legion Y545 Laptop (Lenovo)","Legion Y545-PG0 Laptop (Lenovo)","Legion Y7000-2019 Laptop (Lenovo)","Legion Y7000-2019-PG0 Laptop (Lenovo)","Legion Y7000P Laptop (Lenovo)","Legion Y7000P-1060 Laptop (Lenovo)","Legion Y720-15IKB Laptop (Lenovo)","Legion Y730-15ICH Laptop","Legion Y730-17ICH Laptop","Legion Y740-15ICHg Laptop (Lenovo)","Legion Y740-15IRH Laptop (ideapad)","Legion Y740-15IRHg Laptop (ideapad)","Legion Y740-17ICHg Laptop (Lenovo)","Legion Y740-17IRH Laptop (Lenovo)","Legion Y740-17IRHg Laptop (Lenovo)","Legion Y920-17IKB Laptop (Lenovo)","N20p Chromebook (Lenovo)","N21 Chromebook (Lenovo)","N22 Chromebook (Lenovo)","N22-20 Touch Chromebook (Lenovo)","N23 Chromebook (Lenovo)","N23 Yoga Chomebook (Lenovo)","N42-20 Chromebook (Lenovo)","N42-20 Touch Chromebook (Lenovo)","Yoga Chromebook C630 (Lenovo)","Flex 10 Laptop (Lenovo)","Flex 11 Chromebook (Lenovo)","Flex 14 Laptop (ideapad)","Flex 14D Laptop (ideapad)","Flex 15 Laptop (ideapad)","Flex 15D Laptop (ideapad)","Flex 2 Pro-15 Laptop (Lenovo)","Flex 2-14 Laptop (Lenovo)","Flex 2-14D Laptop (Lenovo)","Flex 2-15 Laptop (Lenovo)","Flex 2-15D Laptop (Lenovo)","Flex 3 -1435 Laptop (Lenovo)","Flex 3-1120 Laptop (Lenovo)","Flex 3-1130 Laptop (Lenovo)","Flex 3-1470 Laptop (Lenovo)","Flex 3-1480 Laptop (Lenovo)","Flex 3-1570 Laptop (Lenovo)","Flex 3-1580 Laptop (Lenovo)","Flex 4-1130 Laptop (Lenovo)","Flex 4-1435 Laptop (Lenovo)","Flex 4-1470 Laptop (Lenovo)","Flex 4-1480 Laptop (Lenovo)","Flex 4-1570 Laptop (Lenovo)","Flex 4-1580 Laptop (Lenovo)","Flex 5-1470 (Type 81C9) Laptop (Lenovo)","Flex 5-1470(Type 80XA) Laptop (Lenovo)","Flex 5-1570 (Type 80XB) Laptop (Lenovo)","Flex 5-1570 (Type 81CA) Laptop (Lenovo)","Flex 6-11IGM Laptop (Lenovo)","Flex 6-14ARR Laptop (Lenovo)","Flex 6-14IKB Laptop (Lenovo)","Flex Pro-13IKB Laptop (ideapad)","FLEX-14API Laptop (Lenovo)","FLEX-14IWL Laptop (ideapad)","FLEX-15IWL Laptop (ideapad)","M41-80 Laptop (Lenovo)","M4400 Laptop (Lenovo)","M4400s Laptop (Lenovo)","M4450 Laptop (Lenovo)","M490 Laptop (Lenovo)","M490s Laptop (Lenovo)","M495 Laptop (Lenovo)","M50-70 Laptop (Lenovo)","M5400 Laptop (Lenovo)","M5400 Touch Laptop (Lenovo)","N580 Laptop (ideapad)","N581 Laptop (ideapad)","N585 Laptop (ideapad)","N586 Laptop (ideapad)","N22 Winbook (Lenovo)","N23 Winbook (Lenovo)","N24 Winbook (Lenovo)","P400 Touch Laptop (ideapad)","P500 Laptop (ideapad)","P500 Touch Laptop (ideapad)","P580 Laptop (ideapad)","P585 Laptop (ideapad)","P1 (Type 20MD, 20ME) Laptop (ThinkPad)","P1 Gen 2 (Type 20QT, 20QU) Laptop (ThinkPad)","P40 Yoga Laptop (ThinkPad)","P43s (Type 20RH, 20RJ) Laptop (ThinkPad)","P50 Laptop (ThinkPad)","P50s Laptop (ThinkPad)","P51 (Type 20HH, 20HJ) Laptop (ThinkPad)","P51 (Type 20MM, 20MN) Laptop (ThinkPad)","P51s (Type 20HB, 20HC) Laptop (ThinkPad)","P51s (Type 20JY, 20K0) Laptop (ThinkPad)","P52 (Type 20M9, 20MA) Laptop (ThinkPad)","P52s (Type 20LB, 20LC) Laptop (ThinkPad)","P53 (Type 20QN, 20QQ) Laptop (ThinkPad)","P53s (Type 20N6, 20N7) Laptop (ThinkPad)","P70 Laptop (ThinkPad)","P71 (type 20HK, 20HL) Laptop (Thinkpad)","P72 (type 20MB, 20MC) Laptop (Thinkpad)","S10 Laptop (ideapad)","S100 Laptop (ideapad)","S100c Laptop (ideapad)","S110 Laptop (ideapad)","S130-11IGM Laptop (ideapad)","S130-14IGM Laptop (ideapad)","S145-14AST Laptop (ideapad)","S145-14IGM Laptop (ideapad)","S145-14IWL Laptop (ideapad)","S145-15AST Laptop (ideapad)","S145-15IGM Laptop (ideapad)","S145-15IWL Laptop (ideapad)","S200 Laptop (ideapad)","S205 Laptop (ideapad)","S205s Laptop (ideapad)","S206 Laptop (ideapad)","S210 Laptop (ideapad)","S210 Touch Laptop (ideapad)","S215 Laptop (ideapad)","S300 Laptop (ideapad)","S310 Laptop (ideapad)","S340-14API Laptop (ideapad)","S340-14IWL Laptop (ideapad)","S340-15API Laptop (ideapad)","S340-15API Touch Laptop (ideapad)","S340-15IWL Laptop (ideapad)","S340-15IWL Touch Laptop (ideapad)","S400 Laptop (ideapad)","S400 Touch Laptop (ideapad)","S400u Laptop (ideapad)","S405 Laptop (ideapad)","S410 Laptop (ideapad)","S410p Laptop (ideapad)","S410p Touch Laptop (ideapad)","S415 Laptop (ideapad)","S415 Touch Laptop (ideapad)","S500 Laptop (ideapad)","S500 Touch Laptop (ideapad)","S510p Laptop (ideapad)","S510p Touch Laptop (ideapad)","S530-13IWL Laptop (ideapad)","S540-14API Laptop (ideapad)","S540-14IWL Laptop (ideapad)","S540-14IWL Touch Laptop (ideapad)","S540-15IWL GTX Laptop (ideapad)","S540-15IWL Laptop (ideapad)","S940-14IWL Laptop (ideapad)","S20-30 Laptop (Lenovo)","S20-30 Touch Laptop (Lenovo)","S21e-20 Laptop (Lenovo)","S40-70 Laptop (Lenovo)","S41-35 Laptop (Lenovo)","S41-70 Laptop (Lenovo)","S41-75 Laptop (Lenovo)","S435 Laptop (Lenovo)","S430 Laptop (ThinkPad)","S431 Laptop (ThinkPad)","S440 Laptop (ThinkPad)","S5 2nd Gen (Type 20JA) Laptop (ThinkPad)","S531 Laptop (ThinkPad)","S540 Laptop (ThinkPad)","25 (Type 20K7) Laptop (ThinkPad)","T420 Laptop (ThinkPad)","T420i Laptop (ThinkPad)","T420s Laptop (ThinkPad)","T420si Laptop (ThinkPad)","T430 Laptop (ThinkPad)","T430i Laptop (ThinkPad)","T430s Laptop (ThinkPad)","T430si Laptop (ThinkPad)","T430u Laptop (ThinkPad)","T431s Laptop (ThinkPad)","T440 Laptop (ThinkPad)","T440p Laptop (ThinkPad)","T440s Laptop (ThinkPad)","T450 Laptop (ThinkPad)","T450s Laptop (ThinkPad)","T460 Laptop (ThinkPad)","T460p Laptop (ThinkPad)","T460s Laptop (ThinkPad)","T470 (Type 20HD, 20HE) Laptop (ThinkPad)","T470 (Type 20JM, 20JN) Laptop (ThinkPad)","T470p Laptop (ThinkPad)","T470s (type 20HF, 20HG) Laptop (ThinkPad)","T470s (type 20JS, 20JT) Laptop (ThinkPad)","T480 (Type 20L5, 20L6) Laptop (ThinkPad)","T480s (type 20L7, 20L8) Laptop (ThinkPad)","T490 (Type 20N2, 20N3) Laptop (ThinkPad)","T490 Type 20Q9, 20QH Laptop (ThinkPad)","T490s (Type 20NX, 20NY) Laptop (ThinkPad)","T495 (Type 20NJ, 20NK) Laptop (ThinkPad)","T495s (Type 20QJ, 20QK) Laptop (ThinkPad)","T520 Laptop (ThinkPad)","T520i Laptop (ThinkPad)","T530 Laptop (ThinkPad)","T530i Laptop (ThinkPad)","T540p Laptop (ThinkPad)","T550 Laptop (ThinkPad)","T560 Laptop (ThinkPad)","T570 (Type 20H9,20HA) Laptop (ThinkPad)","T570 (Type 20JW, 20JX) Laptop (ThinkPad)","T580 (Type 20L9, 20LA) Laptop (ThinkPad)","T590 (Type 20N4, 20N5) Laptop (ThinkPad)","ThinkBook 13s-IWL Laptops","ThinkBook 14s-IWL Laptops","Twist S230u Laptop (ThinkPad)","U300e Laptop (ideapad)","U300s Laptop (ideapad)","U310 Laptop (ideapad)","U310 Touch Laptop (ideapad)","U330 Laptop (ideapad)","U330 Touch Laptop (ideapad)","U330p Laptop (ideapad)","U400 Laptop (ideapad)","U410 Laptop (ideapad)","U410 Touch Laptop (ideapad)","U430 Touch Laptop (ideapad)","U430p Laptop (ideapad)","U510 Laptop (ideapad)","U530 Touch Laptop (ideapad)","U31-70 Laptop (Lenovo)","U41-70 Laptop (Lenovo)","V110-14AST Laptop (Lenovo)","V110-14IAP Laptop (Lenovo)","V110-15AST Laptop (Lenovo)","V110-15IAP Laptop (Lenovo)","V110-15IKB Laptop (Lenovo)","V110-15ISK Laptop (Lenovo)","V110-17IKB Laptop (Lenovo)","V110-17ISK (Lenovo)","V130-14IGM Laptop (Lenovo)","V130-14IKB Laptop (Lenovo)","V130-15IGM Laptop (Lenovo)","V130-15IKB Laptop (Lenovo)","V145-14AST Laptop (Lenovo)","V145-15AST Laptop (Lenovo)","V155-15API Laptop (Lenovo)","V310-14IKB Laptop (Lenovo)","V310-14ISK Laptop (Lenovo)","V310-15IKB Laptop (Lenovo)","V310-15ISK Laptop (Lenovo)","V320-17IKB (Type 81AH) Laptop (Lenovo)","V320-17IKB (Type 81CN) Laptop (Lenovo)","V320-17ISK Laptop (Lenovo)","V330-14ARR Laptop (Lenovo)","V330-14IKB Laptop (Lenovo)","V330-14ISK Laptop (Lenovo)","V330-15IKB Laptop (Lenovo)","V330-15ISK Laptop (Lenovo)","V340-17IWL Laptop (Lenovo)","V370 Laptop (Lenovo)","V4400 Laptop (Lenovo)","V4400u Laptop (Lenovo)","V470c Laptop (Lenovo)","V480 Laptop (Lenovo)","V480c Laptop (Lenovo)","V480s Laptop (Lenovo)","V490u Laptop (Lenovo)","V510-14IKB Laptop (Lenovo)","V510-15IKB Laptop (Lenovo)","V570 Laptop (Lenovo)","V570c Laptop (Lenovo)","V580 Laptop (Lenovo)","V580c Laptop (Lenovo)","V720-14 Laptop (Lenovo)","V730-13 Laptop (Lenovo)","W520 Laptop (ThinkPad)","W530 Laptop (ThinkPad)","W540 Laptop (ThinkPad)","W541 Laptop (ThinkPad)","W550s Laptop (ThinkPad)","X131e Chromebook (ThinkPad)","X220 Tablet Laptop (ThinkPad)","X220i Tablet Laptop (ThinkPad)","X230 Tablet Laptop (ThinkPad)","X230i Tablet Laptop (ThinkPad)","Y400 Laptop (ideapad)","Y410P Laptop (ideapad)","Y470 Laptop (ideapad)","Y470P Laptop (ideapad)","Y471A Laptop (ideapad)","Y480 Laptop (ideapad)","Y500 Laptop (ideapad)","Y510 Laptop (ideapad)","Y510P Laptop (ideapad)","Y570 Laptop (ideapad)","Y580 Laptop (ideapad)","Y700 Touch-15ISK Laptop (ideapad)","Y700-14ISK Laptop (ideapad)","Y700-15ACZ Laptop (ideapad)","Y700-15ISK Laptop (ideapad)","Y700-17ISK Laptop (ideapad)","Y710 Laptop (ideapad)","Y900-17ISK Laptop (ideapad)","Y910-17ISK Laptop (ideapad)","Y40-70 Laptop (Lenovo)","Y40-80 Laptop (Lenovo)","Y50-70 Laptop (Lenovo)","Y50-70 Touch Laptop (Lenovo)","Y70-70 Touch Laptop (Lenovo)","Yoga 11e Chromebook (ThinkPad)","Yoga 11e Chromebook (Type 20GC, 20GE) Laptop (ThinkPad)","Yoga 11 Laptop (ideapad)","Yoga 11s Laptop (ideapad)","Yoga 13 Laptop (ideapad)","Yoga 2 11 Laptop (Lenovo)","Yoga 2 13 Laptop (Lenovo)","Yoga 2 Pro Laptop (Lenovo)","Yoga 3 Pro-1370 Laptop (Lenovo)","Yoga 3-1170 Laptop (Lenovo)","Yoga 3-1470 Laptop (Lenovo)","Yoga 300-11IBR Laptop (ideapad)","Yoga 300-11IBY Laptop (ideapad)","Yoga 310-11IAP Laptop (ideapad)","Yoga 330-11IGM Laptop (ideapad)","Yoga 500-14ACL Laptop (ideapad)","Yoga 500-14IBD Laptop (ideapad)","Yoga 500-14IHW Laptop (ideapad)","Yoga 500-14ISK Laptop (ideapad)","Yoga 500-15IBD Laptop (ideapad)","Yoga 500-15IHW Laptop (ideapad)","Yoga 500-15ISK Laptop (ideapad)","Yoga 510-14AST Laptop (ideapad)","Yoga 510-14IKB Laptop (ideapad)","Yoga 510-14ISK Laptop (ideapad)","Yoga 510-15IKB Laptop (ideapad)","Yoga 510-15ISK Laptop (ideapad)","Yoga 520-14IKB (Type 80X8, 80YM) Laptop (ideapad)","Yoga 520-14IKB (Type 81C8) Laptop (ideapad)","Yoga 530-14ARR Laptop (ideapad)","Yoga 530-14IKB Laptop (ideapad)","Yoga 700-11ISK Laptop (ideapad)","Yoga 700-14ISK Laptop (ideapad)","Yoga 710-11IKB Laptop (ideapad)","Yoga 710-11ISK Laptop (ideapad)","Yoga 710-14IKB Laptop (ideapad)","Yoga 710-14ISK Laptop (ideapad)","Yoga 710-15IKB Laptop (ideapad)","Yoga 710-15ISK Laptop (ideapad)","Yoga 720-12IKB Laptop (ideapad)","Yoga 720-13IKB (Type 80X6) Laptop (ideapad)","Yoga 720-13IKB (Type 81C3) Laptop (ideapad)","Yoga 720-15IKB Laptop (ideapad)","Yoga 730-13IKB Laptop (ideapad)","Yoga 730-13IWL Laptop (Lenovo)","Yoga 730-15IKB Laptop (ideapad)","Yoga 730-15IWL Laptop (Lenovo)","Yoga 900-13ISK for BIZ (ideapad)","Yoga 900-13ISK Laptop (ideapad)","Yoga 900-13ISK2 Laptop (ideapad)","Yoga 900S-12ISK Laptop (ideapad)","Yoga 910-13IKB Glass (ideapad)","Yoga 910-13IKB Laptop (ideapad)","Yoga 920-13IKB Glass Laptop (ideapad)","Yoga 920-13IKB Laptop (ideapad)","Yoga C630-13Q50 Laptop (Lenovo)","Yoga C930-13IKB Glass Laptop (Lenovo)","Yoga C930-13IKB Laptop (Lenovo)","Yoga S730-13IWL Laptop (Lenovo)","Yoga S940-14IWL Laptop (Lenovo)","Yoga 11e (Type 20D9, 20DA) Laptop (ThinkPad)","Yoga 11e (Type 20E5, 20E7) Laptop (ThinkPad)","Yoga 11e 3rd Gen (Type 20G8, 20GA) Laptop (ThinkPad)","Yoga 11e 4th Gen (Type 20HS 20HU) Laptop (ThinkPad)","Yoga 11e 5th Gen (Type 20LN 20LM) Laptop (ThinkPad)","Yoga 12 Laptop (ThinkPad)","Yoga 14 (Type 20DM, 20DN) Laptop (ThinkPad)","Yoga 14 (Type 20FY) Laptop (ThinkPad)","Yoga 15 Laptop (ThinkPad)","Yoga 260 Laptop (ThinkPad)","Yoga 370 Laptop (ThinkPad)","Yoga 460 Laptop (ThinkPad)","Yoga Laptop (ThinkPad)","Z370 Laptop (ideapad)","Z380 Laptop (ideapad)","Z400 Laptop (ideapad)","Z400 Touch Laptop (ideapad)","Z410 Laptop (ideapad)","Z470 Laptop (ideapad)","Z475 Laptop (ideapad)","Z480 Laptop (ideapad)","Z485 Laptop (ideapad)","Z500 Laptop (ideapad)","Z500 Touch Laptop (ideapad)","Z510 Laptop (ideapad)","Z570 Laptop (ideapad)","Z575 Laptop (ideapad)","Z580 Laptop (ideapad)","Z585 Laptop (ideapad)","Z710 Laptop (ideapad)","Z40-70 Laptop (Lenovo)","Z40-75 Laptop (Lenovo)","Z41-70 Laptop (Lenovo)","Z50-70 Laptop (Lenovo)","Z50-75 Laptop (Lenovo)","Z51-70 Laptop (Lenovo)","Z70-80 Laptop (Lenovo)"]

start_url = 'https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/100-series/100-14iby/documentation'

driver = webdriver.Chrome('/Users/shivam/myworkspace/watson/crawler/drivers/chromedriver')
driver.get(start_url)


for product in products:
    driver.find_element_by_css_selector("a[t='Product Info Change Product|change product']").click()
    time.sleep(4)
    driver.find_element_by_css_selector("input[placeholder='Search by product name, serial number, machine type']").send_keys(product)
    time.sleep(3)
    driver.find_element_by_css_selector("strong[class='tt-highlight']").click()
    print (product)
    try:
        checkbox_element = driver.find_element_by_css_selector("input[data-name='Hardware Maintenance Manuals']").click()
    except NoSuchElementException:
        print (None)
        print ('\n')
        continue
    possible_names = ['Maintenance Manual', 'Hardware Maintenance and Manual', 'Hardware Manentance Manual', 'Hardware Maintanence Manual', 'Hardware Maintainence Manual', 'Hardware Manintenance Manunal']
    element = None
    for name in possible_names:
        temp_str = "a[data-title*='{}']".format(name)
        try:
            element = driver.find_element_by_css_selector(temp_str)
            break
        except NoSuchElementException:
            continue
    print (element.get_property('href'))
    print ('\n')
