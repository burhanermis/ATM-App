                                        # BANKAMATİK UYGULAMA
                               
BurhanHesap={
        "ad": "Burhan Ermiş",
        "hesapNo": "123456",
        "bakiye": 3000,
        "ekHesap": 2000
        }                               

SaadetHesap={
        "ad": "Saadet Arslan",
        "hesapNo": "456789",
        "bakiye": 5000,
        "ekHesap": 2500
        } 

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap["bakiye"]>=miktar):
        print("Paranızı alabilirsiniz.")
        hesap["bakiye"]=hesap["bakiye"]-miktar
        bakiyeSorgula(hesap)
    else:
        toplam=hesap["bakiye"]+hesap["ekHesap"]
        if (toplam>=miktar):
            ekHesapKullanimi=input("Ek hesap kullanılsın mı? (e/h): ")
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"]=hesap["ekHesap"]- ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} no'lu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("Üzgünüz. Bakiyeniz yetersiz.")
            bakiyeSorgula(hesap)
    
def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} no lu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitinizde ise {hesap['ekHesap']} TL bulunmaktadır.")
    

paraCek(BurhanHesap, 2500)
print("********")
paraCek(BurhanHesap, 1500)    
paraCek(BurhanHesap, 2000)      












