#!/usr/bin/env python3

import sys, hashlib, time, os, random, binascii, zlib
import urllib.request, urllib.parse
from re import search

# Color
if sys.platform == "win32":
    # Windows için renksiz (ANSI desteklemeyen eski sürümler için)
    BB = YY = GG = WW = RR = CC = MM = B = Y = G = W = R = C = P = ''
else:
    # Linux, Termux (Android), macOS ve diğerleri için renkli
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
    print (P+"              python3 "+sys.argv[0]+" --info\n"+W)
 
def info():
    print (GG+"\n 0{======================"+WW+" INFO "+GG+"=======================}0")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Name     "+CC+":"+WW+" Hashgen"+GG+"                               |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Code     "+CC+":"+WW+" Python3"+GG+"                               |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Version  "+CC+":"+WW+" v1.2.7 (Alpha)"+GG+"                        |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Author   "+CC+":"+WW+" TheDarkRoot"+GG+"                           |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Email    "+CC+":"+WW+" 7H3D4RKR007@gmail.com"+GG+"                |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Github   "+CC+":"+WW+" https://github.com/TheDarkRoot"+GG+"       |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Telegram "+CC+":"+WW+" @TheDarkRoot (t.me/TheDarkRoot)"+GG+"      |")
    print (GG+" |"+BB+" ["+RR+"="+BB+"] "+WW+"Team     "+CC+":"+WW+" TurkHackTeam (www.turkhackteam.org)"+GG+"  |")
    print (GG+" 0{===================================================}0\n")
    print (BB+" ["+RR+"="+BB+"] "+WW+"python3 "+sys.argv[0]+" -u")
    print (BB+"\n ["+RR+"="+BB+"] "+WW+"To Update Hashgen.py")
    print (BB+"\n ["+RR+"="+BB+"] "+WW+"List of supported hashes:")
    print (YY+"\n ["+WW+"01"+YY+"] "+CC+"MySQL 3.2.3")
    print (YY+" ["+WW+"02"+YY+"] "+CC+"MySQL 4.1")
    print (YY+" ["+WW+"03"+YY+"] "+CC+"MSSQL 2000")
    print (YY+" ["+WW+"04"+YY+"] "+CC+"MSSQL 2005")
    print (YY+" ["+WW+"05"+YY+"] "+CC+"MD4")
    print (YY+" ["+WW+"06"+YY+"] "+CC+"MD5")
    print (YY+" ["+WW+"07"+YY+"] "+CC+"SHA1")
    print (YY+" ["+WW+"08"+YY+"] "+CC+"SHA224")
    print (YY+" ["+WW+"09"+YY+"] "+CC+"SHA256")
    print (YY+" ["+WW+"10"+YY+"] "+CC+"SHA384")
    print (YY+" ["+WW+"11"+YY+"] "+CC+"SHA512")
    print (YY+" ["+WW+"12"+YY+"] "+CC+"RIPEMD160")
    print (YY+" ["+WW+"13"+YY+"] "+CC+"WHIRLPOOL")
    print (YY+" ["+WW+"14"+YY+"] "+CC+"CRC32")
    print (YY+" ["+WW+"15"+YY+"] "+CC+"ADLER32")
    print (YY+" ["+WW+"16"+YY+"] "+CC+"DES Crypt")
    print (YY+" ["+WW+"17"+YY+"] "+CC+"BSDi Crypt")
    print (YY+" ["+WW+"18"+YY+"] "+CC+"BIGCrypt")
    print (YY+" ["+WW+"19"+YY+"] "+CC+"Crypt16")
    print (YY+" ["+WW+"20"+YY+"] "+CC+"MD5 Crypt")
    print (YY+" ["+WW+"21"+YY+"] "+CC+"SHA1 Crypt")
    print (YY+" ["+WW+"22"+YY+"] "+CC+"SHA256 Crypt")
    print (YY+" ["+WW+"23"+YY+"] "+CC+"SHA512 Crypt")
    print (YY+" ["+WW+"24"+YY+"] "+CC+"Sun MD5 Crypt")
    print (YY+" ["+WW+"25"+YY+"] "+CC+"Apr MD5 Crypt")
    print (YY+" ["+WW+"26"+YY+"] "+CC+"PHPASS")
    print (YY+" ["+WW+"27"+YY+"] "+CC+"CTA PBKDF2 SHA1")
    print (YY+" ["+WW+"28"+YY+"] "+CC+"Dlitz PBDKF2 SHA1")
    print (YY+" ["+WW+"29"+YY+"] "+CC+"Atlassian's PBKDF2")
    print (YY+" ["+WW+"30"+YY+"] "+CC+"Django PBKDF2 SHA1")
    print (YY+" ["+WW+"31"+YY+"] "+CC+"Django PBKDF2 SHA256")
    print (YY+" ["+WW+"32"+YY+"] "+CC+"Grub's PBKDF2")
    print (YY+" ["+WW+"33"+YY+"] "+CC+"SCRAM Hash")
    print (YY+" ["+WW+"34"+YY+"] "+CC+"BSD nthash")
    print (YY+" ["+WW+"35"+YY+"] "+CC+"Oracle11")
    print (YY+" ["+WW+"36"+YY+"] "+CC+"LanManager Hash")
    print (YY+" ["+WW+"37"+YY+"] "+CC+"Windows NT-Hash")
    print (YY+" ["+WW+"38"+YY+"] "+CC+"Cisco Type 7")
    print (YY+" ["+WW+"39"+YY+"] "+CC+"FHSP\n"+W)

def Update():
    # Sistemde /proc dizininin veya linux'a özgü bir dizinin varlığını kontrol et
    # Bu yöntem Termux ve tüm Linux sistemlerinde çalışır
    is_linux = os.path.exists("/proc") or sys.platform.startswith("linux")
    
    if is_linux:
        print (BB+" 0={"+WW+" Updating Hashgen... "+BB+"}=0\n")
        
        print (BB+"["+WW+"="+BB+"] "+GG+"Downloading new version...")
        cmd = "curl -s -L https://raw.githubusercontent.com/TheDarkRoot/Hashgen/master/Hashgen.py -o Hashgen.new.py"
        status = os.system(cmd)
        
        if status == 0:
            print (BB+"["+WW+"="+BB+"] "+GG+"Download finished. Replacing files...")
            os.system("mv Hashgen.new.py Hashgen.py")
            print (RR+"\n["+WW+"*"+RR+"] "+GG+"Update successfully completed!\n"+W)
        else:
            print (RR+"\n["+WW+"!"+RR+"] "+GG+"Update failed! Could not download the new file.\n"+W)
            if os.path.exists("Hashgen.new.py"):
                os.remove("Hashgen.new.py")
        
        sys.exit()
    else:
        # Hata ayıklama için platformu yazdırıyoruz
        print (RR+"["+WW+"!"+RR+"] "+GG+"Update feature is only for Linux/Termux.")
        print (RR+"["+WW+"!"+RR+"] "+GG+f"Detected platform: {sys.platform}"+W)
        sys.exit()

try:
    import progressbar, passlib
except ImportError:
    banner()
    time.sleep(0.5)
    print (BB+"["+WW+"="+BB+"] "+GG+"Installing missing modules: "+RR+"progressbar, passlib.\n"+W)

    # Kurulum komutlarını çalıştır ve sonuçlarını (0 veya hata kodu) değişkene ata
    pip_update = os.system("pip3 install --upgrade pip")
    passlib_install = os.system("pip3 install passlib")
    prog_install = os.system("pip3 install progressbar2") # progressbar2 is the maintained python 3 version

    # Eğer tüm kurulumlar 0 (başarılı) döndürdüyse
    if passlib_install == 0 and prog_install == 0:
        print (BB+"\n["+WW+"="+BB+"] "+GG+"Install success, please run the program again.\n"+W)
    else:
        # Eğer kurulumlardan biri bile başarısız olduysa
        print (RR+"\n["+WW+"!"+RR+"] "+YY+"Installation failed! Please check your internet connection or pip permissions.\n"+W)
    
    sys.exit()

try:
    if len(sys.argv) > 1:
        if sys.argv[1] == "-u":
            Update()
        elif sys.argv[1] == "-i" or sys.argv[1] == "--info":
            info()
            sys.exit()
        else:
            print (RR+"["+WW+"!"+RR+"] "+GG+"Command Error!!!"+W)
            sys.exit()
except IndexError:
    sys.exit()

try:
    banner()
    x = input(CC+"["+WW+"~"+CC+"] "+GG+"String"+CC+": "+W)
except KeyboardInterrupt:
    print (RR+"\n["+WW+"!"+RR+"] "+GG+"Exiting...\n")
    sys.exit()

print (YY+"["+WW+"!"+YY+"] "+GG+"Generate Hash        :"+YY+" Please Wait!!!"+W)
time.sleep(0.5)

# passlib's hash methods take strings natively in python3
# mysql1323
from passlib.hash import mysql323
mysql1323 = mysql323.hash(x)
print (YY+"\n["+WW+"01"+YY+"]>"+GG+"MySQL 3.2.3         : "+W+mysql1323)

# mysql141
from passlib.hash import mysql41
mysql141 = mysql41.hash(x)
print (YY+"["+WW+"02"+YY+"]>"+GG+"MySQL 4.1           : "+W+mysql141)

# mssql2000
from passlib.hash import mssql2000 as m20
mssql2000 = m20.hash(x)
print (YY+"["+WW+"03"+YY+"]>"+GG+"MSSQL 2000          : "+W+mssql2000)

# mssql2005
from passlib.hash import mssql2005 as m25
mssql2005 = m25.hash(x)
print (YY+"["+WW+"04"+YY+"]>"+GG+"MSSQL 2005          : "+W+mssql2005)

# md4 (Note: requires OpenSSL config that supports legacy hashes)
try:
    m = hashlib.new("md4")
    m.update(x.encode('utf-8'))
    md4 = m.hexdigest()
    print (YY+"["+WW+"05"+YY+"]>"+GG+"MD4                 : "+W+md4)
except ValueError:
    print (YY+"["+WW+"05"+YY+"]>"+GG+"MD4                 : "+RR+"Not Supported by System OpenSSL"+W)

# md5
m = hashlib.new("md5")
m.update(x.encode('utf-8'))
md5 = m.hexdigest()
print (YY+"["+WW+"06"+YY+"]>"+GG+"MD5                 : " +W+md5)

# sha1
m = hashlib.new("sha1")
m.update(x.encode('utf-8'))
sha1 = m.hexdigest()
print (YY+"["+WW+"07"+YY+"]>"+GG+"SHA1                : "+W+sha1)

# Sha224
m = hashlib.new("sha224")
m.update(x.encode('utf-8'))
sha224 = m.hexdigest()
print (YY+"["+WW+"09"+YY+"]>"+GG+"SHA224              : "+W+sha224)

# Sha256
m = hashlib.new("sha256")
m.update(x.encode('utf-8'))
sha256 = m.hexdigest()
print (YY+"["+WW+"10"+YY+"]>"+GG+"SHA256              : "+W+sha256)

# Sha384
m = hashlib.new("sha384")
m.update(x.encode('utf-8'))
sha384 = m.hexdigest()
print (YY+"["+WW+"11"+YY+"]>"+GG+"SHA384              : "+W+sha384)

# Sha512
m = hashlib.new("sha512")
m.update(x.encode('utf-8'))
sha512 = m.hexdigest()
print (YY+"["+WW+"12"+YY+"]>"+GG+"SHA512              : "+W+sha512)

# Ripemd160
try:
    m = hashlib.new("ripemd160")
    m.update(x.encode('utf-8'))
    ripemd160 = m.hexdigest()
    print (YY+"["+WW+"13"+YY+"]>"+GG+"RIPEMD160           : "+W+ripemd160)
except ValueError:
    print (YY+"["+WW+"13"+YY+"]>"+GG+"RIPEMD160           : "+RR+"Not Supported by System OpenSSL"+W)

# Whirlpool
try:
    m = hashlib.new("whirlpool")
    m.update(x.encode('utf-8'))
    whirlpool = m.hexdigest()
    print (YY+"["+WW+"14"+YY+"]>"+GG+"WHIRLPOOL           : "+W+whirlpool)
except ValueError:
    print (YY+"["+WW+"14"+YY+"]>"+GG+"WHIRLPOOL           : "+RR+"Not Supported by System OpenSSL"+W)

# crc32
h = zlib.crc32(x.encode('utf-8'))
crc32 = '%08X' % (h & 0xffffffff,)
print (YY+"["+WW+"14"+YY+"]>"+GG+"CRC32               : "+W+crc32.lower())

# adler32
h = zlib.adler32(x.encode('utf-8'))
adler32 = '%08X' % (h & 0xffffffff,)
print (YY+"["+WW+"15"+YY+"]>"+GG+"ADLER32             : "+W+adler32.lower())

# des
from passlib.hash import des_crypt
des = des_crypt.hash(x)
print (YY+"["+WW+"16"+YY+"]>"+GG+"DES Crypt           : "+W+des)

# Bsdi Crypt
from passlib.hash import bsdi_crypt
bsdi = bsdi_crypt.hash(x)
print (YY+"["+WW+"17"+YY+"]>"+GG+"BSDi Crypt          : "+W+bsdi)

# Bigcrypt
from passlib.hash import bigcrypt
big = bigcrypt.hash(x)
print (YY+"["+WW+"18"+YY+"]>"+GG+"BIGCrypt            : "+W+big)

# Crypt16
from passlib.hash import crypt16
crypt16 = crypt16.hash(x)
print (YY+"["+WW+"19"+YY+"]>"+GG+"Crypt16             : "+W+crypt16)

# Md5 crypt
from passlib.hash import md5_crypt as mc
md5_crypt_hash = mc.hash(x)
print (YY+"["+WW+"20"+YY+"]>"+GG+"MD5 Crypt           : "+W+md5_crypt_hash)

# Sha1 Crypt
from passlib.hash import sha1_crypt as mc
sha1_crypt_hash = mc.hash(x)
print (YY+"["+WW+"21"+YY+"]>"+GG+"SHA1 Crypt          : "+W+sha1_crypt_hash)

# Sha256 Crypt
from passlib.hash import sha256_crypt as mc
sha256_crypt_hash = mc.hash(x)
print (YY+"["+WW+"22"+YY+"]>"+GG+"SHA256 Crypt        : "+W+sha256_crypt_hash)

# Sha512 crypt
from passlib.hash import sha512_crypt as mc
sha512_crypt_hash = mc.hash(x)
print (YY+"["+WW+"23"+YY+"]>"+GG+"SHA512 Crypt        : "+W+sha512_crypt_hash)

# Sun md5 crypt
from passlib.hash import sun_md5_crypt as mc
sun_md5_crypt_hash = mc.hash(x)
print (YY+"["+WW+"24"+YY+"]>"+GG+"Sun MD5 Crypt       : "+W+sun_md5_crypt_hash)

# apache's md5 crypt
from passlib.hash import apr_md5_crypt as mc
apr_md5_crypt_hash = mc.hash(x)
print (YY+"["+WW+"25"+YY+"]>"+GG+"Apr MD5 Crypt       : "+W+apr_md5_crypt_hash)

# phppass
from passlib.hash import phpass as mc
phpass_hash = mc.hash(x)
print (YY+"["+WW+"26"+YY+"]>"+GG+"PHPASS              : "+W+phpass_hash)

# Cryptacular's PBDF2
from passlib.hash import cta_pbkdf2_sha1 as mc
cta_pbkdf2_sha1_hash = mc.hash(x)
print (YY+"["+WW+"27"+YY+"]>"+GG+"CTA PBKDF2 SHA1     : "+W+cta_pbkdf2_sha1_hash)

# Dwine PBDF2
from passlib.hash import dlitz_pbkdf2_sha1 as mc
dlitz_pbkdf2_sha1_hash = mc.hash(x)
print (YY+"["+WW+"28"+YY+"]>"+GG+"Dlitz PBDKF2 SHA1   : "+W+dlitz_pbkdf2_sha1_hash)

# Atlassian's PBKDF2 Hash
from passlib.hash import cta_pbkdf2_sha1 as mc
atl_pbkdf2_sha1_hash = mc.hash(x)
print (YY+"["+WW+"29"+YY+"]>"+GG+"Atlassian's PBKDF2  : "+W+atl_pbkdf2_sha1_hash)

# Django sha1
from passlib.hash import django_pbkdf2_sha1 as m25
django_sha1_hash = m25.hash(x)
print (YY+"["+WW+"30"+YY+"]>"+GG+"Django PBKDF2 SHA1  : "+W+django_sha1_hash)

# django sha256
from passlib.hash import django_pbkdf2_sha256 as m25
django_sha256_hash = m25.hash(x)
print (YY+"["+WW+"31"+YY+"]>"+GG+"Django PBKDF2 SHA256: "+W+django_sha256_hash)

# grub pbkdf2
from passlib.hash import grub_pbkdf2_sha512 as m25
grup_pbkdf2_sha512_hash = m25.hash(x)
print (YY+"["+WW+"32"+YY+"]>"+GG+"Grub's PBKDF2       : "+W+grup_pbkdf2_sha512_hash)

# SCRAM
from passlib.hash import scram as mc
scram_hash = mc.hash(x)
print (YY+"["+WW+"33"+YY+"]>"+GG+"SCRAM Hash          : "+W+scram_hash)

# FreeBSD nthash
from passlib.hash import bsd_nthash as mc
bsd_nthash_hash = mc.hash(x)
print (YY+"["+WW+"34"+YY+"]>"+GG+"BSD nthash          : "+W+bsd_nthash_hash)

# oracle11
from passlib.hash import oracle11 as m25
oracle11_hash = m25.hash(x)
print (YY+"["+WW+"35"+YY+"]>"+GG+"Oracle11            : "+W+oracle11_hash)

# lanManager
from passlib.hash import lmhash as m25
lmhash_val = m25.hash(x)
print (YY+"["+WW+"36"+YY+"]>"+GG+"LanManager Hash     : "+W+lmhash_val)

# nthash
from passlib.hash import nthash as m25
nthash_val = m25.hash(x)
print (YY+"["+WW+"37"+YY+"]>"+GG+"Windows NT-Hash     : "+W+nthash_val)

# cisco type 7
from passlib.hash import cisco_type7 as m25
cisco_hash = m25.hash(x)
print (YY+"["+WW+"38"+YY+"]>"+GG+"Cisco Type 7        : "+W+cisco_hash)

# fhsp
from passlib.hash import fshp as m25
fhsp_hash = m25.hash(x)
print (YY+"["+WW+"39"+YY+"]>"+GG+"FHSP                : "+W+fhsp_hash+"\n")

print (YY+"["+GG+"*"+YY+"] "+GG+"Success generate all hash.\n")

print(YY + "[" + WW + "?" + YY + "] " + GG + "Save results to text file? (Y/n)")
save_choice = input(CC + "[" + WW + "~" + CC + "] " + GG + "Choice" + CC + ": " + W).lower()

if save_choice == 'y':
    safe_x = "".join([c for c in x if c.isalnum() or c in (' ', '_', '-')])
    filename = f"{safe_x}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"String: {x}\n")
            f.write("-" * 28 + "\n")
            
            # Değişken tanımlı mı kontrol ederek dosyaya yaz
            f.write(f"[01] > MySQL 3.2.3         : {mysql1323 if 'mysql1323' in locals() else 'Not Supported'}\n")
            f.write(f"[02] > MySQL 4.1           : {mysql141 if 'mysql141' in locals() else 'Not Supported'}\n")
            f.write(f"[03] > MSSQL 2000          : {mssql2000 if 'mssql2000' in locals() else 'Not Supported'}\n")
            f.write(f"[04] > MSSQL 2005          : {mssql2005 if 'mssql2005' in locals() else 'Not Supported'}\n")
            f.write(f"[05] > MD4                 : {md4 if 'md4' in locals() else 'Not Supported'}\n")
            f.write(f"[06] > MD5                 : {md5 if 'md5' in locals() else 'Not Supported'}\n")
            f.write(f"[07] > SHA1                : {sha1 if 'sha1' in locals() else 'Not Supported'}\n")
            f.write(f"[08] > SHA224              : {sha224 if 'sha224' in locals() else 'Not Supported'}\n")
            f.write(f"[09] > SHA256              : {sha256 if 'sha256' in locals() else 'Not Supported'}\n")
            f.write(f"[10] > SHA384              : {sha384 if 'sha384' in locals() else 'Not Supported'}\n")
            f.write(f"[11] > SHA512              : {sha512 if 'sha512' in locals() else 'Not Supported'}\n")
            f.write(f"[12] > RIPEMD160           : {ripemd160 if 'ripemd160' in locals() else 'Not Supported'}\n")
            f.write(f"[13] > WHIRLPOOL           : {whirlpool if 'whirlpool' in locals() else 'Not Supported'}\n")
            f.write(f"[14] > CRC32               : {crc32 if 'crc32' in locals() else 'Not Supported'}\n")
            f.write(f"[15] > ADLER32             : {adler32 if 'adler32' in locals() else 'Not Supported'}\n")
            f.write(f"[16] > DES Crypt           : {des if 'des' in locals() else 'Not Supported'}\n")
            f.write(f"[17] > BSDi Crypt          : {bsdi if 'bsdi' in locals() else 'Not Supported'}\n")
            f.write(f"[18] > BIGCrypt            : {big if 'big' in locals() else 'Not Supported'}\n")
            f.write(f"[19] > Crypt16             : {crypt16 if 'crypt16' in locals() else 'Not Supported'}\n")
            f.write(f"[21] > SHA1 Crypt          : {md5_crypt_hash if 'md5_crypt_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[21] > SHA1 Crypt          : {sha1_crypt_hash if 'sha1_crypt_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[22] > SHA256 Crypt        : {sha256_crypt_hash if 'sha256_crypt_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[23] > SHA512 Crypt        : {sha512_crypt_hash if 'sha512_crypt_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[24] > Sun MD5 Crypt       : {sun_md5_crypt_hash if 'sun_md5_crypt_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[25] > Apr MD5 Crypt       : {apr_md5_crypt_hash if 'apr_md5_crypt_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[26] > PHPASS              : {phpass_hash if 'phpass_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[27] > CTA PBKDF2 SHA1     : {cta_pbkdf2_sha1_hash if 'cta_pbkdf2_sha1_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[28] > Dlitz PBDKF2 SHA1   : {dlitz_pbkdf2_sha1_hash if 'dlitz_pbkdf2_sha1_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[29] > Atlassian's PBKDF2  : {atl_pbkdf2_sha1_hash if 'atl_pbkdf2_sha1_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[30] > Django PBKDF2 SHA1  : {django_sha1_hash if 'django_sha1_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[31] > Django PBKDF2 SHA256: {django_sha256_hash if 'django_sha256_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[32] > Grub's PBKDF2       : {grup_pbkdf2_sha512_hash if 'grup_pbkdf2_sha512_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[33] > SCRAM Hash          : {scram_hash if 'scram_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[34] > BSD nthash          : {bsd_nthash_hash if 'bsd_nthash_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[35] > Oracle11            : {oracle11_hash if 'oracle11_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[36] > LanManager Hash     : {lmhash_val if 'lmhash_val' in locals() else 'Not Supported'}\n")
            f.write(f"[37] > Windows NT-Hash     : {nthash_val if 'nthash_val' in locals() else 'Not Supported'}\n")
            f.write(f"[38] > Cisco Type 7        : {cisco_hash if 'cisco_hash' in locals() else 'Not Supported'}\n")
            f.write(f"[39] > FHSP                : {fhsp_hash if 'fhsp_hash' in locals() else 'Not Supported'}\n")
            
        print(GG + "\n[" + WW + "+" + GG + "] Results saved as \""+ WW + "" + filename + ""+ GG + "\"" + W)
    except Exception as e:
        print(RR + "\n[" + WW + "!" + RR + "] Error saving file: " + str(e) + W)

print(YY + "[" + GG + "*" + YY + "] " + GG + "Success generate all hash.\n")