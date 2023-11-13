def luasPersegipanjang(panjang,lebar):
    L = panjang * lebar
    return L

def kelilingpersegipanjang(panjang,lebar):
    k = (2*panjang)+(2*lebar)
    return k

def luas_bola(jari_jari):
    L = 4*3.14*jari_jari**2
    return L

def volume_bola(jari_jari):
    V = 4*3.14*jari_jari**2
    return V

def luas_kubus(rusuk):
    L = round (6 * rusuk **2)
    return L

def volume_kubus(rusuk):
    V = round (rusuk **3)
    return V

def luas_kerucut(jarijari,tinggi,sisi):
    luasselimut = 3.14*jarijari*sisi
    return luasselimut

def volume_kerucut(jarijari,tinggi,sisi):
    Volume =  1/3*3.14*jarijari**2*tinggi
    return Volume

def luas_tabung(jarijari,tinggi):
    Luasselimut = 2*3.14*jarijari*tinggi
    return Luasselimut

def volume_tabung(jarijari,tinggi):
    volume = 3.14*jarijari**2*tinggi
    return volume

def luas_balok(panjang,lebar,tinggi):
    L= (2*panjang*lebar)+(2*panjang*tinggi)+(2*lebar*tinggi)
    return L

def volume_balok(panjang,lebar,tinggi):
    V= panjang*lebar*tinggi
    return V

def luas_limas_segiempat(sisi,tinggilimas,tinggisegitiga):
    L= (sisi*sisi)+(4*sisi*tinggisegitiga/2)
    return L

def volume_limas_segiempat(sisi,tinggilimas,tinggisegitiga):
    V= 1/3*(sisi*sisi)*tinggilimas
    return V

def luas_limas_segitiga(alassegitiga,tinggilimas,tinggisegitiga):
    L= 4*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return L

def volume_limas_segitiga(alassegitiga,tinggilimas,tinggisegitiga):
    V =  1/3*(1/2*alassegitiga*tinggisegitiga)*tinggilimas
    return V

def luas_prisma_segitiga(alas,tinggi,luas,tinggiprisma,sisi1,sisi2,sisi3):
    L = ( sisi1 + sisi2 + sisi3 ) * tinggiprisma
    return L

def volume_prisma_segitiga(alas,tinggi,luas,tinggiprisma,sisi1,sisi2,sisi3):
    V= ( alas * tinggi ) / 2 * tinggiprisma
    return V