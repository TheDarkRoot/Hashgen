#! usr/bin/python2

import sys , hashlib , time , os , random , binascii , zlib

from urllib import urlopen, urlencode
from re import search

# Color
if sys.platform == "linux" or sys.platform == "linux2":

	BB = "\033[34;1m" # Blue Light
	YY = "\033[33;1m" # Yellow Light
	GG = "\033[32;1m" # Green Light
	WW = "\033[0;1m"  # White Light
	RR = "\033[31;1m" # Red Light
	CC = "\033[36;1m" # Cyan Light
	MM = "\033[35;1m" # Magenta Light
	B = "\033[34;1m"  # Blue
	Y = "\033[33;1m"  # Yellow
	G = "\033[32;1m"  # Green
	W = "\033[0;1m"   # White
	R = "\033[31;1m"  # Red
	C = "\033[36;1m"  # Cyan
	M = "\033[35;1m"  # Magenta

	# Random Color
	rand = (BB,YY,GG,RR,CC)
	P = random.choice(rand)

elif sys.platform == "win32":

	BB = '' # Blue Light
	YY = '' # Yellow Light
	GG = '' # Green Light
	WW = '' # White Light
	RR = '' # Red Light
	CC = '' # Cyan Light
	B = ''  # Blue
	Y = ''  # Yellow
	G = ''  # Green
	W = ''  # White
	R = ''  # Red
	C = ''  # Cyan
	P = ''  # Random Color

def banner():
    print (CC+'\n              Hash Generator'+GG+' v1.0.0')
    print (P+'  #      #'+WW+' #########################################')
    print (P+'  #      #   ##    ####  #    #  ####  ###### #    # ')
    print (P+'  #      #  #  #  #      #    # #    # #      ##   # ')
    print (P+'  ######## #    #  ####  ###### #      #####  # #  # ')
    print (P+'  #      # ######      # #    # #  ### #      #  # # ')
    print (P+'  #      # #    # #    # #    # #    # #      #   ## ')
    print (P+'  #      # #    #  ####  #    #  ####  ###### #    # ')
    print (WW+'  #################['+CC+' TheDarkRoot'+WW+' ]################## ')
    print (P+"              python2 "+sys.argv[0]+" --info\n"+W)
 
def info():
    print (GG+"\n 0{======================"+WW+" INFO "+GG+"=======================}0")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Name     "+CC+":"+WW+" Hashgen"+GG+"                              |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Code     "+CC+":"+WW+" Python2"+GG+"                              |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Version  "+CC+":"+WW+" v1.0.0 (Alpha)"+GG+"                       |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Author   "+CC+":"+WW+" TheDarkRoot"+GG+"                          |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Email    "+CC+":"+WW+" 7H3D4RKR007@gmail.com"+GG+"                |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Github   "+CC+":"+WW+" https://github.com/TheDarkRoot"+GG+"       |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Telegram "+CC+":"+WW+" @TheDarkRoot (t.me/TheDarkRoot)"+GG+"      |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Team     "+CC+":"+WW+" TurkHackTeam (www.turkhackteam.org)"+GG+"  |")
    print (GG+" 0{===================================================}0\n")
    print (BB+" ["+RR+"="+BB+"] "+WW+"python2 "+sys.argv[0]+" -u")
    print (BB+"\n ["+RR+"="+BB+"] "+WW+"To Update Hashgen.py")
    print (BB+"\n ["+RR+"="+BB+"] "+WW+"List of supported hashes:")
    print (YY+"\n                          ["+WW+"01"+YY+"] "+CC+"MySQL 3.2.3")
    print (YY+"                          ["+WW+"02"+YY+"] "+CC+"MySQL 4.1")
    print (YY+"                          ["+WW+"03"+YY+"] "+CC+"MSSQL 2000")
    print (YY+"                          ["+WW+"04"+YY+"] "+CC+"MSSQL 2005")
    print (YY+"                          ["+WW+"05"+YY+"] "+CC+"MD4")
    print (YY+"                          ["+WW+"06"+YY+"] "+CC+"MD5")
    print (YY+"                          ["+WW+"07"+YY+"] "+CC+"SHA1")
    print (YY+"                          ["+WW+"08"+YY+"] "+CC+"SHA224")
    print (YY+"                          ["+WW+"09"+YY+"] "+CC+"SHA256")
    print (YY+"                          ["+WW+"10"+YY+"] "+CC+"SHA384")
    print (YY+"                          ["+WW+"11"+YY+"] "+CC+"SHA512")
    print (YY+"                          ["+WW+"12"+YY+"] "+CC+"RIPEMD160")
    print (YY+"                          ["+WW+"13"+YY+"] "+CC+"WHIRLPOOL")
    print (YY+"                          ["+WW+"14"+YY+"] "+CC+"CRC32")
    print (YY+"                          ["+WW+"15"+YY+"] "+CC+"ADLER32")
    print (YY+"                          ["+WW+"16"+YY+"] "+CC+"DES Crypt")
    print (YY+"                          ["+WW+"17"+YY+"] "+CC+"BSDi Crypt")
    print (YY+"                          ["+WW+"18"+YY+"] "+CC+"BIGCrypt")
    print (YY+"                          ["+WW+"19"+YY+"] "+CC+"Crypt16")
    print (YY+"                          ["+WW+"20"+YY+"] "+CC+"MD5 Crypt")
    print (YY+"                          ["+WW+"21"+YY+"] "+CC+"SHA1 Crypt")
    print (YY+"                          ["+WW+"22"+YY+"] "+CC+"SHA256 Crypt")
    print (YY+"                          ["+WW+"23"+YY+"] "+CC+"SHA512 Crypt")
    print (YY+"                          ["+WW+"24"+YY+"] "+CC+"Sun MD5 Crypt")
    print (YY+"                          ["+WW+"25"+YY+"] "+CC+"Apr MD5 Crypt")
    print (YY+"                          ["+WW+"26"+YY+"] "+CC+"PHPASS")
    print (YY+"                          ["+WW+"27"+YY+"] "+CC+"CTA PBKDF2 SHA1")
    print (YY+"                          ["+WW+"28"+YY+"] "+CC+"Dlitz PBDKF2 SHA1")
    print (YY+"                          ["+WW+"29"+YY+"] "+CC+"Atlassian's PBKDF2")
    print (YY+"                          ["+WW+"30"+YY+"] "+CC+"Django PBKDF2 SHA1")
    print (YY+"                          ["+WW+"31"+YY+"] "+CC+"Django PBKDF2 SHA256")
    print (YY+"                          ["+WW+"32"+YY+"] "+CC+"Grub's PBKDF2")
    print (YY+"                          ["+WW+"33"+YY+"] "+CC+"SCRAM Hash")
    print (YY+"                          ["+WW+"34"+YY+"] "+CC+"BSD nthash")
    print (YY+"                          ["+WW+"35"+YY+"] "+CC+"Oracle11")
    print (YY+"                          ["+WW+"36"+YY+"] "+CC+"LanManager Hash")
    print (YY+"                          ["+WW+"37"+YY+"] "+CC+"Windows NT-Hash")
    print (YY+"                          ["+WW+"38"+YY+"] "+CC+"Cisco Type 7")
    print (YY+"                          ["+WW+"39"+YY+"] "+CC+"FHSP\n"+W)

def Update():
	if sys.platform == "linux" or sys.platform == "linux2":
		print (BB+" 0={"+WW+" Update Hashgen. "+BB+"}=0\n")
		time.sleep(1)

		print (BB+"["+WW+"="+BB+"] "+GG+"Remove old Hashgen.")
		os.system("rm -rf Hashgen.py")
		time.sleep(1)

		print (BB+"["+WW+"="+BB+"] "+GG+"Downloading Hashgen.")
		time.sleep(1)

		print (RR+"["+WW+"*"+RR+"] "+RR+"Curl Started...\n"+W)

		os.system("curl https://raw.githubusercontent.com/TheDarkRoot/Hashgen/master/Hashgen.py -o Hashgen.py")

		print (RR+"\n["+WW+"*"+RR+"] "+GG+"Download finish.\n"+W)
		sys.exit()
	else:
		print ("Sorry, Hashgen update feature is only available on linux platform.\n")
		sys.exit()

try:
	import progressbar , passlib
    
except ImportError:
        banner()
	time.sleep(0.5)
        print (BB+"["+WW+"="+BB+"] "+GG+"installing module "+RR+"progressbar, passlib.\n"+W)

	os.system("pip2 install --upgrade pip")
	os.system("pip2 install passlib")
	os.system("pip2 install progressbar")

	print (BB+"\n["+WW+"="+BB+"] "+GG+"install success, run program again.\n"+W)
        sys.exit()

try:
    banner()
    x = raw_input(CC+"["+WW+"~"+CC+"] "+GG+"String"+CC+": "+W)

except NameError:
	print (RR+"\n["+Ww+"!"+RR+"] "+GG+"use "+WW+"python2.7\n")
	quit()

print (YY+"["+WW+"!"+YY+"] "+GG+"Generate Hash        :"+YY+" Please Wait!!!"+W)
time.sleep(0.5)

# mysql1323
from passlib.hash import mysql323
mysql1323 = mysql323.encrypt(x)
print (YY+"\n["+WW+"01"+YY+"]>"+GG+"MySQL 3.2.3         : "+W+mysql1323)

# mysql141
from passlib.hash import mysql41
mysql141 = mysql41.encrypt(x)
print (YY+"["+WW+"02"+YY+"]>"+GG+"MySQL 4.1           : "+W+mysql141)

# mssql2000
from passlib.hash import mssql2000 as m20
mssql2000 = m20.encrypt(x)
print (YY+"["+WW+"03"+YY+"]>"+GG+"MSSQL 2000          : "+W+mssql2000)

# mssql2005
from passlib.hash import mssql2005 as m25
mssql2005 = m25.encrypt(x)
print (YY+"["+WW+"04"+YY+"]>"+GG+"MSSQL 2005          : "+W+mssql2005)

# md4
m = hashlib.new("md4")
m.update(x)
md4 = m.hexdigest()
print (YY+"["+WW+"05"+YY+"]>"+GG+"MD4                 : "+W+md4)

# md5
m = hashlib.new("md5")
m.update(x)
md5 = m.hexdigest()
print (YY+"["+WW+"06"+YY+"]>"+GG+"MD5                 : " +W+md5)

# sha1
m = hashlib.new("sha1")
m.update(x)
sha1 = m.hexdigest()
print (YY+"["+WW+"07"+YY+"]>"+GG+"SHA1                : "+W+sha1)

# Sha224
m = hashlib.new("sha224")
m.update(x)
sha224 = m.hexdigest()
print (YY+"["+WW+"09"+YY+"]>"+GG+"SHA224              : "+W+sha224)

# Sha256
m = hashlib.new("sha256")
m.update(x)
sha256 = m.hexdigest()
print (YY+"["+WW+"10"+YY+"]>"+GG+"SHA256              : "+W+sha256)

# Sha384
m = hashlib.new("sha384")
m.update(x)
sha384 = m.hexdigest()
print (YY+"["+WW+"11"+YY+"]>"+GG+"SHA384              : "+W+sha384)

# Sha512
m = hashlib.new("sha512")
m.update(x)
sha512 = m.hexdigest()
print (YY+"["+WW+"12"+YY+"]>"+GG+"SHA512              : "+W+sha512)

# Ripemd160
m = hashlib.new("ripemd160")
m.update(x)
ripemd160 = m.hexdigest()
print (YY+"["+WW+"13"+YY+"]>"+GG+"RIPEMD160           : "+W+ripemd160)

# Whirlpool
m = hashlib.new("whirlpool")
m.update(x)
whirlpool = m.hexdigest()
print (YY+"["+WW+"14"+YY+"]>"+GG+"WHIRLPOOL           : "+W+whirlpool)

# crc32
h = zlib.crc32(x)
crc32 = '%08X' % (h & 0xffffffff,)
print (YY+"["+WW+"14"+YY+"]>"+GG+"CRC32               : "+W+crc32.lower())

# adler32
h = zlib.adler32(x)
adler32 = '%08X' % (h & 0xffffffff,)
print (YY+"["+WW+"15"+YY+"]>"+GG+"ADLER32             : "+W+adler32.lower())

# des
from passlib.hash import des_crypt
des = des_crypt.encrypt(x)
print (YY+"["+WW+"16"+YY+"]>"+GG+"DES Crypt           : "+W+des)

# Bsdi Crypt
from passlib.hash import bsdi_crypt
bsdi = bsdi_crypt.encrypt(x)
print (YY+"["+WW+"17"+YY+"]>"+GG+"BSDi Crypt          : "+W+bsdi)

# Bigcrypt
from passlib.hash import bigcrypt
big = bigcrypt.encrypt(x)
print (YY+"["+WW+"18"+YY+"]>"+GG+"BIGCrypt            : "+W+big)

# Crypt16
from passlib.hash import crypt16
crypt16 = crypt16.encrypt(x)
print (YY+"["+WW+"19"+YY+"]>"+GG+"Crypt16             : "+W+crypt16)

# Md5 crypt
from passlib.hash import md5_crypt as mc
md5_crypt = mc.encrypt(x)
print (YY+"["+WW+"20"+YY+"]>"+GG+"MD5 Crypt           : "+W+md5_crypt)

# Sha1 Crypt
from passlib.hash import sha1_crypt as mc
sha1_crypt = mc.encrypt(x)
print (YY+"["+WW+"21"+YY+"]>"+GG+"SHA1 Crypt          : "+W+sha1_crypt)

# Sha256 Crypt
from passlib.hash import sha256_crypt as mc
sha256_crypt = mc.encrypt(x)
print (YY+"["+WW+"22"+YY+"]>"+GG+"SHA256 Crypt        : "+W+sha256_crypt)

# Sha512 crypt
from passlib.hash import sha512_crypt as mc
sha512_crypt = mc.encrypt(x)
print (YY+"["+WW+"23"+YY+"]>"+GG+"SHA512 Crypt        : "+W+sha512_crypt)

# Sun md5 crypt
from passlib.hash import sun_md5_crypt as mc
sun_md5_crypt = mc.encrypt(x)
print (YY+"["+WW+"24"+YY+"]>"+GG+"Sun MD5 Crypt       : "+W+sun_md5_crypt)

# apache's md5 crypt
from passlib.hash import apr_md5_crypt as mc
apr_md5_crypt = mc.encrypt(x)
print (YY+"["+WW+"25"+YY+"]>"+GG+"Apr MD5 Crypt       : "+W+apr_md5_crypt)

# phppass
from passlib.hash import phpass as mc
phpass = mc.encrypt(x)
print (YY+"["+WW+"26"+YY+"]>"+GG+"PHPASS              : "+W+phpass)

# Cryptacular's PBDF2
from passlib.hash import cta_pbkdf2_sha1 as mc
cta_pbkdf2_sha1 = mc.encrypt(x)
print (YY+"["+WW+"27"+YY+"]>"+GG+"CTA PBKDF2 SHA1     : "+W+cta_pbkdf2_sha1)

# Dwine PBDF2
from passlib.hash import dlitz_pbkdf2_sha1 as mc
dlitz_pbkdf2_sha1 = mc.encrypt(x)
print (YY+"["+WW+"28"+YY+"]>"+GG+"Dlitz PBDKF2 SHA1   : "+W+dlitz_pbkdf2_sha1)

# Atlassian's PBKDF2 Hash
from passlib.hash import cta_pbkdf2_sha1 as mc
atl_pbkdf2_sha1 = mc.encrypt(x)
print (YY+"["+WW+"29"+YY+"]>"+GG+"Atlassian's PBKDF2  : "+W+atl_pbkdf2_sha1)

# Django sha1
from passlib.hash import django_pbkdf2_sha1 as m25
django_sha1 = m25.encrypt(x)
print (YY+"["+WW+"30"+YY+"]>"+GG+"Django PBKDF2 SHA1  : "+W+django_sha1)

# django sha256
from passlib.hash import django_pbkdf2_sha256 as m25
django_sha256 = m25.encrypt(x)
print (YY+"["+WW+"31"+YY+"]>"+GG+"Django PBKDF2 SHA256: "+W+django_sha256)

# grup pbkdf2
from passlib.hash import grub_pbkdf2_sha512 as m25
grup_pbkdf2_sha512 = m25.encrypt(x)
print (YY+"["+WW+"32"+YY+"]>"+GG+"Grub's PBKDF2       : "+W+grup_pbkdf2_sha512)

# SCRAM
from passlib.hash import scram as mc
scram = mc.encrypt(x)
print (YY+"["+WW+"33"+YY+"]>"+GG+"SCRAM Hash          : "+W+scram)

# FreeBSD nthash
from passlib.hash import bsd_nthash as mc
bsd_nthash = mc.encrypt(x)
print (YY+"["+WW+"34"+YY+"]>"+GG+"BSD nthash          : "+W+bsd_nthash)

# oracle11
from passlib.hash import oracle11 as m25
oracle11 = m25.encrypt(x)
print (YY+"["+WW+"35"+YY+"]>"+GG+"Oracle11            : "+W+oracle11)

# lanManager
from passlib.hash import lmhash as m25
lmhash = m25.encrypt(x)
print (YY+"["+WW+"36"+YY+"]>"+GG+"LanManager Hash     : "+W+lmhash)

# nthash
from passlib.hash import nthash as m25
nthash = m25.encrypt(x)
print (YY+"["+WW+"37"+YY+"]>"+GG+"Windows NT-Hash     : "+W+nthash)

# cisco type 7
from passlib.hash import cisco_type7 as m25
cisco = m25.encrypt(x)
print (YY+"["+WW+"38"+YY+"]>"+GG+"Cisco Type 7        : "+W+cisco)

# fhsp
from passlib.hash import fshp as m25
fhsp = m25.encrypt(x)
print (YY+"["+WW+"39"+YY+"]>"+GG+"FHSP                : "+W+fhsp+"\n")

print (YY+"["+GG+"*"+YY+"] "+GG+"Success generate all hash.\n")

try:
	if sys.argv[1] == "-u":
		Update()
	elif sys.argv[1] == "-i" or sys.argv[1] == "--info":
		info()
	else:
		print (RR+"["+WW+"!"+RR+"] "+GG+"Command Error!!!"+W)
		sys.exit()

except IndexError:
	sys.exit()

