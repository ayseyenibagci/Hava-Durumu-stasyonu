#Neslihan AKBULUT 
#Tuba AY 
#Ayşe YENİBAĞCI 
#Ceyda ÇAĞ 

import random
import time
import sys
def dünya():
    def hava_durumu_sozlugu(sicaklik, hissedilen_sicaklik, nem, ruzgar_hizi, ruzgar_yonu, yagis_turu, alcak_basinc, yuksek_basinc, bulutluluk_orani):
        return {
            "sıcaklık": sicaklik, 
            "hissedilen sıcaklık": hissedilen_sicaklik,
            "nem": nem,
            "rüzgar hızı": ruzgar_hizi,
            "rüzgar yönü": ruzgar_yonu,
            "yağış türü": yagis_turu,
            "alçak basınç": alcak_basinc,
            "yüksek basınç": yuksek_basinc,
            "bulutluluk oranı": bulutluluk_orani,}
    hava_durumu = { 
            "Güneşli": {
            "uv_indeks": 0, 
            "hava_durumu_sozlugu":{}      },
        "Yağmurlu": {
            "yagis_tipi":"", 
            "hava_durumu_sozlugu":{}  },
        "Karlı": {
            "kar_miktari":0, 
            "kar_tipi":"", 
            "hava_durumu_sozlugu":{}},
        "Fırtınalı": {
            "ruzgar_hizi":0, 
            "firtina_siddeti":0, 
            "firtina_suresi":0, 
            "hortum buyukluğu":"", 
            "hava_durumu_sozlugu":{}},
        "Sisli": {
            "gorus_mesafesi":0, 
            "hava_durumu_sozlugu":{}},
        "Dolu": {
            "dolu_buyuklugu":0, 
            "hava_durumu_sozlugu":{}},
        "Parçalı Bulutlu": {
            "gunes_isigi_miktari":0, 
            "gölge_miktari":0, 
            "hava_durumu_sozlugu":{}},
        "Bulutlu": {
            "gunes_isigi_miktari":0, 
            "hava_durumu_sozlugu":{}},}
    hava_bilgisi = {
        "Güneşli": "Sıcak",
        "Yağmurlu": "Serin",
        "Karlı": "Soğuk",
        "Fırtınalı": "Sıcak",
        "Sisli": "Serin",
        "Dolu": "Soğuk",
        "Parçalı Bulutlu": "Ilık",
        "Bulutlu": "Ilık"}
    def haftalık_hava_durumu_goster(hava_durumu):
        gunler=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
        for gun in gunler:
            durum = hava_durumu[gun]["Durum"]
            sicaklik = hava_durumu[gun]["Sıcaklık"]
            print(f"📆  {gun}: {durum},  🌡️  Sıcaklık: {sicaklik}°C")  
    cografi_bolgeler = {
        "Tropik Bölgeler": {
            "iklim_tipi": "tropikal iklim veya ekvatoral iklim", 
            "hava_durumu_egilimi":"yüksek sıcaklık, yüksek nem ve düzenli yağışa sahip, mevsimler az değişkenlik gösterir"},
        "Subtropikal Bölgeler": {
            "iklim_tipi": "substropikal iklim", 
            "hava_durumu_egilimi":"sıcak veya ılıman, orta derecede nem, yağış miktarı az, 4 mevsim görülür"},
        "Ilıman Bölgeler": {
            "iklim_tipi": "ılıman", 
            "hava_durumu_egilimi":"ılıman, nem ilkbahar ve yaz aylarında yüksek, düzenli yağış, 4 mevsim yaşanır, hava durumu değişken, mikroiklimler etkilidir"},
        "Arid ve Yarı Arid Bölgeler": {
            "iklim_tipi": "kurak iklim", 
            "hava_durumu_egilimi":"az yağış, yüksek sıcaklığa sahiptir, nem oranı düşük, gündüz ve gece arasında sıcaklık farkı çoktur, kum fırtınaları sıktır, yarı aridde aride oranla daha fazla yağış alır"},
        "Sert Kışlı Bölgeler": {
            "iklim_tipi": "soğuk iklim veya kutup iklimi", 
            "hava_durumu_egilimi":"düşük sıcaklık, kar yağışı sıktır, kışlar uzun yazlar kısa, gündüz ile gece arasında sıcaklık farkı çoktur"},
        "Dağlık Bölgeler": {
            "iklim_tipi": "alp iklimi veya dağ iklimi", 
            "hava_durumu_egilimi":"yüksek rakımlı dağlarda kar yağışı yaygındır, yaz ayları genelde ılımandır, yağış miktarı yüksek, hava durumu genellikle hızla değişir, mikroiklimler etkilidir"},
        "Polar Bölgeler": {
            "iklim_tipi": "polar iklim", 
            "hava_durumu_egilimi":"çok düşük sıcaklığa sahiptir, kışlar uzun yazlar kısa, düşük nem, kalıcı kar ve buz örtüsü ile kaplıdır, rüzgarlar sık görünür"}}
    def random_hava_durumu_olustur(iklim_tipi):
        sicaklik_range = {
            "tropikal iklim veya ekvatoral iklim": (25, 35),
            "substropikal iklim": (20, 30),
            "ılıman": (10, 25),
            "kurak iklim": (30, 45),
            "soğuk iklim veya kutup iklimi": (-20, 0),
            "alp iklimi veya dağ iklimi": (-10, 15),
            "polar iklim": (-40, -10)}
        nem_range = {
            "tropikal iklim veya ekvatoral iklim": (70, 90),
            "substropikal iklim": (50, 70),
            "ılıman": (40, 60),
            "kurak iklim": (10, 30),
            "soğuk iklim veya kutup iklimi": (40, 70),
            "alp iklimi veya dağ iklimi": (50, 80),
            "polar iklim": (30, 50)}
        yagis_turu = {
            "tropikal iklim veya ekvatoral iklim": ["Yağmur", "Fırtına"],
            "substropikal iklim": ["Yağmur", "Fırtına", "Yağış yok"],
            "ılıman": ["Yağmur", "Kar", "yağış yok"],
            "kurak iklim": ["Güneşli", "Kum Fırtınası"],
            "soğuk iklim veya kutup iklimi": ["Kar", "Buz Fırtınası"],
            "alp iklimi veya dağ iklimi": ["Kar", "Yağmur", "Yağış yok"],
            "polar iklim": ["Kar", "Buz Fırtınası"] }
        hissedilen_sicaklik={
                "tropikal iklim veya ekvatoral iklim": (12, 37),
                "substropikal iklim": (10, 30),
                "ılıman": (5, 40),
                "kurak iklim": (40, 45),
                "soğuk iklim veya kutup iklimi": (-35, 0),
                "alp iklimi veya dağ iklimi": (-15, 20),
                "polar iklim": (-50, 0)    }
        ruzgar_hizi={
                "tropikal iklim veya ekvatoral iklim": (0, 4),
                "substropikal iklim": (0, 6),
                "ılıman": (0, 3),
                "kurak iklim": (0, 1),
                "soğuk iklim veya kutup iklimi": (2, 10),
                "alp iklimi veya dağ iklimi": (2, 8),
                "polar iklim": (3, 7)   }
        sicaklik = random.randint(*sicaklik_range[iklim_tipi])
        nem = random.randint(*nem_range[iklim_tipi])
        yagis_turu = random.choice(yagis_turu[iklim_tipi])
        hissedilen_sicaklik=random.randint(*hissedilen_sicaklik[iklim_tipi])
        ruzgar_hizi=random.randint(*ruzgar_hizi[iklim_tipi])
        ruzgar_yonu = random.choice(["Kuzey", "Güney", "Doğu", "Batı"])
        alcak_basinc = random.randint(950, 1000)
        yuksek_basinc = random.randint(1000, 1050)
        bulutluluk_orani = random.randint(0, 100)
        hava_durumu= hava_durumu_sozlugu(sicaklik, hissedilen_sicaklik, nem, ruzgar_hizi, ruzgar_yonu, yagis_turu, alcak_basinc, yuksek_basinc, bulutluluk_orani)
        hava_durumu_tipi = "Güneşli" if yagis_turu == "Güneşli" else "Yağmurlu" if yagis_turu in ["Yağmur", "Fırtına"] else "Karlı" if yagis_turu in ["Kar", "Buz Fırtınası"] else "Fırtınalı" if yagis_turu == "Kum Fırtınası" else "Sisli" if yagis_turu == "Sis" else "Dolu" if yagis_turu == "Dolu" else "Parçalı Bulutlu" if yagis_turu == "Parçalı Bulutlu" else "Bulutlu"
        hava_durumu["hava_durumu_tipi"] = hava_durumu_tipi
        if hava_durumu_tipi == "Güneşli":
            hava_durumu["uv_indeksi"] = random.randint(1, 10)
        if hava_durumu_tipi == "Yağmurlu":
            hava_durumu["yağış türü"] = yagis_turu
        elif hava_durumu_tipi == "Karlı":
            hava_durumu["kar miktarı"] = random.randint(1, 30)  
            hava_durumu["kar tipi"] = "Toz Kar" if random.random() < 0.5 else "Islak Kar"
        elif hava_durumu_tipi == "Fırtınalı":
            hava_durumu["rüzgar hızı"] = random.randint(50, 100)  
            hava_durumu["fırtına şiddeti"] = random.randint(1, 5)
            hava_durumu["fırtına süresi"] = random.randint(1, 24)
            hava_durumu["hortum büyüklüğü"] = "Küçük Hortum" if random.random() < 0.5 else "Büyük Hortum"
        elif hava_durumu_tipi == "Sisli":
            hava_durumu["görüş mesafesi"] = random.randint(50, 500)  
        elif hava_durumu_tipi == "Dolu":
            hava_durumu["dolu büyüklüğü"] = random.randint(1, 10)  
        elif hava_durumu_tipi == "Parçalı Bulutlu" or hava_durumu_tipi == "Bulutlu":
            hava_durumu["güneş ışığı miktarı"] = random.randint(0, 100)  
            hava_durumu["gölge miktarı"] = random.randint(0, 100)  
        return hava_durumu
    def bölge_bilgilerini_yazdir(bolge_adi, ozellikler):
        print(f"{bolge_adi} Bölgesinin Özellikleri:")
        for iklim_tipi, hava_durumu_egilimi in ozellikler.items():
            print(f"- {iklim_tipi.capitalize()}: {hava_durumu_egilimi}")
    def bölge_seçimi():
        print("Coğrafi Bölgeler:")
        for i, bolge in enumerate(cografi_bolgeler.keys(), 1):
            print(f"{i}- {bolge}")
        print("8- Tüm Bölgeler")
        print("-----------------------")
        return input("Hangi bölgenin özelliklerini istersiniz? (numara olarak girin): ").strip()
    def bölgeye_göre_özellik():
        while True:
            bolge_sec = bölge_seçimi()
            if bolge_sec.isdigit():
                bolge_sec = int(bolge_sec)
                try:
                    if 1 <= bolge_sec <= len(cografi_bolgeler):
                        bolge_adi = list(cografi_bolgeler.keys())[bolge_sec - 1]
                        ozellikler = cografi_bolgeler[bolge_adi]
                        bölge_bilgilerini_yazdir(bolge_adi, ozellikler)
                    elif bolge_sec == 8:
                        for bolge_adi, ozellikler in cografi_bolgeler.items():
                            bölge_bilgilerini_yazdir(bolge_adi, ozellikler)
                    else:
                        print("Geçersiz bölge seçimi yaptınız. Lütfen geçerli bir numara giriniz.")
                        bölgeye_göre_özellik()
                except ValueError:
                    print("Geçersiz bölge seçimi yaptınız. Lütfen geçerli bir numara giriniz.")
                    continue
            else:
                bolge_adi = bolge_sec.title()
                if bolge_adi in cografi_bolgeler:
                    ozellikler = cografi_bolgeler[bolge_adi]
                    bölge_bilgilerini_yazdir(bolge_adi, ozellikler)
                else:
                    print("Geçersiz bölge seçimi yaptınız. Lütfen geçerli bir isim veya numara giriniz.")
                    continue  
            secim = input("Ana menüye dönmek için 'Ana menü(1)' yazınız, devam etmek için 'Devam(2)' yazınız. ")
            if secim == "1" or secim=="ana menü":
                anamenü()
                break
            elif secim == "2" or secim=="devam":
                continue
            else:
                print("Geçersiz seçim yaptınız. Lütfen 'Ana menü' veya 'Devam' giriniz.")
                break
    def karar():
        while True:
            seçim = input("Ana menüye dönmek için 'Ana menü(1)' yazınız, devam etmek için 'Devam(2)' yazınız.")
            if seçim == "ana menü":
                anamenü()
                break
            elif seçim == "devam":
                bölgeye_göre_hava_durumu()
                break
            else:
                print("Geçersiz seçim yaptınız. Lütfen 'Ana menü' veya 'Devam' giriniz.")
    def haftalık_öneriler(haftalık_hava_durumu):
        haftalık_sıcaklık = [durum["sıcaklık"] for gün, durum in haftalık_hava_durumu.items()]
        haftalık_hava_durumu_tipi = [durum["yağış türü"] for gün, durum in haftalık_hava_durumu.items()]
        min_sıcaklık = min(haftalık_sıcaklık)
        max_sıcaklık = max(haftalık_sıcaklık)
        ortalama_sıcaklık = sum(haftalık_sıcaklık) / len(haftalık_sıcaklık)
        sıcaklık_yorum = ""
        if max_sıcaklık > 30:
            sıcaklık_yorum = "Sıcaklık çok yüksek! Dışarı çıkarken güneş kremi kullanmayı ve bol su içmeyi unutmayın."
        elif max_sıcaklık > 25:
            sıcaklık_yorum = "Sıcaklık normalin üstünde. Bol su tüketmeye dikkat edin."
        elif min_sıcaklık < 5:
            sıcaklık_yorum = "Sıcaklık çok düşük! Dışarı çıkarken kalın giysiler giyin ve sıcak içecekler tüketin."
        elif min_sıcaklık < 10:
            sıcaklık_yorum = "Soğuk bir hafta görünüyor. İçinizi ısıtacak sıcak içecekler tüketebilirsiniz."
        yağış_tipi_sayısı = len(set(haftalık_hava_durumu_tipi))
        yağış_yorum = ""
        if yağış_tipi_sayısı > 2:
            yağış_yorum = "Bu hafta hava oldukça değişken gözüküyor. Şemsiye ve yağmurluk hazır bulundurun."
        elif "Kar" in haftalık_hava_durumu_tipi:
            yağış_yorum = "Kar yağışı bekleniyor. Araç kullanırken dikkatli olun ve kış lastiği takılı olduğundan emin olun."
        elif "Yağmur" in haftalık_hava_durumu_tipi:
            yağış_yorum = "Yağmurlu bir hafta görünüyor. Şemsiyenizi yanınızdan ayırmayın."
        print("Haftalık Öneriler:")
        print(f"- Haftanın en düşük sıcaklığı: {min_sıcaklık}°C")
        print(f"- Haftanın en yüksek sıcaklığı: {max_sıcaklık}°C")
        print(f"- Haftanın ortalama sıcaklığı: {ortalama_sıcaklık}°C")
        print(sıcaklık_yorum)
        print(yağış_yorum)
    def bölgeye_göre_hava_durumu():
        while True:
            bolge_sec = bölge_seçimi()
            try:
                bolge_sec = int(bolge_sec)
                if 1 <= bolge_sec <= len(cografi_bolgeler):
                    bolge_adi = list(cografi_bolgeler.keys())[bolge_sec - 1]
                    ozellikler = cografi_bolgeler[bolge_adi]
                    iklim_tipi = ozellikler["iklim_tipi"]
                    hava_durumu = random_hava_durumu_olustur(iklim_tipi)
                    print(f"{bolge_adi} için oluşturulan hava durumu:")
                    max_isim = max(len(k) for k in hava_durumu.keys())
                    for ozellik, deger in hava_durumu.items():
                        bosluk = max_isim - len(ozellik)
                        print(f"{ozellik}: {' ' * bosluk}{deger}")
                    while True:
                        hava_durumu_secim = input(f"{bolge_adi} için 7 günlük hava durumu ister misiniz? ((e)vet/(h)ayır):").lower()
                        if hava_durumu_secim == "evet" or hava_durumu_secim == "e":
                            print(f"{bolge_adi} için 7 günlük hava durumu yazdırılıyor...")
                            time.sleep(1)
                            print(f"{bolge_adi} için 7 günlük hava durumu:")
                            haftalik_durumlar = haftalık_hava_durumu_olustur()
                            haftalık_hava_durumu_goster(haftalik_durumlar)
                            while True:
                                öneri_isteği = input("Bu hafta öneri ister misiniz? ((e)vet/(h)ayır): ").lower()
                                if öneri_isteği == "evet" or öneri_isteği == "e":
                                    print("Bu hafta için öneriler: ")
                                    haftalık_öneriler(haftalik_durumlar) 
                                    break
                                elif öneri_isteği == "hayır" or öneri_isteği=="h":
                                    print("Öneriler sunulmadı.")
                                    karar(bolge_adi)
                                    break
                                else:
                                    print("Geçersiz seçim yaptınız. Lütfen 'evet' veya 'hayır' yazınız.")
                            break
                        elif hava_durumu_secim == "hayır" or hava_durumu_secim == "h":
                            print("Öneri istenmedi.")
                            break
                        else:
                            print("Geçersiz seçim yaptınız. Lütfen 'evet' veya 'hayır' yazınız.")
                elif bolge_sec == 8:
                    hava_durumlari = {}
                    for bolge_adi, ozellikler in cografi_bolgeler.items():
                        iklim_tipi = ozellikler["iklim_tipi"]
                        hava_durumu = random_hava_durumu_olustur(iklim_tipi)
                        hava_durumlari[bolge_adi] = hava_durumu
                    for bolge_adi, hava_durumu in hava_durumlari.items():
                        print(f"{bolge_adi} için oluşturulan hava durumu:")
                        max_isim = max(len(k) for k in hava_durumu.keys())
                        for ozellik, deger in hava_durumu.items():
                            bosluk = max_isim - len(ozellik)
                            print(f"{ozellik}: {' ' * bosluk}{deger}")
                    while True:
                        hava_durumu_secim = input(f"{bolge_adi} için 7 günlük hava durumu ister misiniz? ((e)vet/(h)ayır):").lower()
                        if hava_durumu_secim == "evet" or hava_durumu_secim == "e":
                            print(f"{bolge_adi} için 7 günlük hava durumu yazdırılıyor")
                            time.sleep(1)
                            print(f"{bolge_adi} için 7 günlük hava durumu:")
                            haftalik_durumlar = haftalık_hava_durumu_olustur()
                            haftalık_hava_durumu_goster(haftalik_durumlar)
                            break
                        elif hava_durumu_secim == "hayır" or hava_durumu_secim == "h":
                            print("İstenilmedi.")
                            karar(bolge_adi)
                            break
                        else:
                            print("Geçersiz seçim. Lütfen 'evet' veya 'hayır' yazınız.") 
                else:
                    print("Geçersiz seçim yaptınız. Lütfen 1-8 arası bir seçim yapınız.")   
                    continue
            except ValueError:
                bolge_adi = bolge_sec.title()
                if bolge_adi in cografi_bolgeler:
                    ozellikler = cografi_bolgeler[bolge_adi]
                    iklim_tipi = ozellikler["iklim_tipi"]
                    hava_durumu = random_hava_durumu_olustur(iklim_tipi)
                    print(f"{bolge_adi} için oluşturulan hava durumu:")
                    max_isim = max(len(k) for k in hava_durumu.keys())
                    for ozellik, deger in hava_durumu.items():
                        bosluk = max_isim - len(ozellik)
                        print(f"{ozellik}: {' ' * bosluk}{deger}")   
                    continue 
                else:
                    print("Geçersiz seçim yaptınız. Lütfen 1-8 arası bir seçim yapınız.")
                    continue
            while True:
                        seçim = input("Ana menüye dönmek için 'Ana menü' yazın, çıkış yapmak için 'Çıkış' yazın: ").lower()
                        if seçim == "ana menü":
                            anamenü()
                            break
                        elif seçim == "çıkış":
                            print("Çıkış yapılıyor...")
                            time.sleep(1)
                            print("Çıkış yapıldı. Yine bekleriz...")
                            exit()
                        else:
                            print("Geçersiz seçim yaptınız! Lütfen 'Ana menü' veya 'Çıkış' yazınız.") 
    def haftalık_hava_durumu_olustur():
        haftalik_durumlar = {}
        gunler=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
        for gun in gunler:
            iklim_tipi = random.choice(list(cografi_bolgeler.values()))["iklim_tipi"]
            hava_durumu = random_hava_durumu_olustur(iklim_tipi)
            haftalik_durumlar[gun] = hava_durumu
        return haftalik_durumlar
    def günlük_hava_durumu_goster(hava_durumu):
        print("Günlük Hava Durumu:")
        for gün, durum in hava_durumu.items():
            print(f" 📆  {gün}: {durum}")
    def haftalık_hava_durumu_goster(hava_durumu):
        for gun, durum in hava_durumu.items():
            hava_durumu_tipi = durum["yağış türü"]
            sicaklik = durum["sıcaklık"]
            print(f"📆  {gun}: {hava_durumu_tipi}, 🌡️ Sıcaklık: {sicaklik}°C")
    def anamenü():
        print("Hava Durumu Uygulamasına Hoş Geldiniz!")
        print("1. Bölgeye Göre Özellikler")
        print("2. Bölgeye Göre Hava Durumu")
        print("3. Çıkış")
        seçim = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if seçim == "1":
            bölgeye_göre_özellik()
        elif seçim == "2":
            bölgeye_göre_hava_durumu()
        elif seçim == "3":
            print("Çıkış yapılıyor...")
            time.sleep(1)
            print("Çıkış yapıldı. Yine bekleriz...")
            exit()
        else:
            print("Geçersiz seçim yaptınız! Lütfen '1' , '2' veya '3' giriniz.")
            anamenü()
    anamenü()
    def secim():
        secim = anamenü()  
        while secim not in ("3", "q", "çıkış"):  
            try:
                if secim == "1":
                    bölgeye_göre_özellik() 
                    print("1-Ana menü\n2-Çıkış")             
                    cevap2 = input("Lütfen yapmak istediğiniz işlemi seçiniz: ").lower()
                    if cevap2 == "1":
                        secim = anamenü() 
                    else:
                        print("Programdan çıkış yapılıyor...")
                        time.sleep(1)
                        print("Çıkış yapıldı. Yine bekleriz...")
                        break
                elif secim == "2":
                    bölgeye_göre_hava_durumu()
                    secim = anamenü()  
                elif secim == "4":
                    print("Geçersiz seçim yaptınız!")
                    secim = anamenü()  
                else:
                    print("Geçersiz seçim yaptınız!")
                    secim = anamenü()  
            except Exception as e:
                print(f"Beklenmeyen bir hata oluştu: {e}")
        if secim == "3":
            print("Çıkış yapıldı. Yine bekleriz...")
        else:
            print("Geçersiz seçim yaptınız!")
    karar()
def türkiye():
    import random
    import sys
    import time
    from datetime import datetime,timedelta
    def hava_durumu_sozlugu(sicaklik, hissedilen_sicaklik, nem, ruzgar_hizi, ruzgar_yonu, yagis_turu, alcak_basinc, yuksek_basinc, bulutluluk_orani):
        return {
            "sıcaklık": sicaklik, 
            "hissedilen sıcaklık": hissedilen_sicaklik,
            "nem": nem,
            "rüzgar hızı": ruzgar_hizi,
            "rüzgar yönü": ruzgar_yonu,
            "yağış türü": yagis_turu,
            "alçak basınç": alcak_basinc,
            "yüksek basınç": yuksek_basinc,
            "bulutluluk oranı": bulutluluk_orani  }
    bolgeler = { 
        "Marmara": {
            "iklim_tipi": "Karadeniz iklimi",
            "hava_durumu_egilimi": "bol miktarda yağış, ılıman iklim" },
        "Ege": {
            "iklim_tipi": "Akdeniz iklimi",
            "hava_durumu_egilimi": "ılıman, az yağışlı" },
        "Akdeniz": {
            "iklim_tipi": "Akdeniz iklimi",
            "hava_durumu_egilimi": "ılıman, az yağışlı"  },
        "İç Anadolu": {
            "iklim_tipi": "Step iklimi",
            "hava_durumu_egilimi": "kıtasal iklim, karasal iklim özellikleri" },
        "Karadeniz": {
            "iklim_tipi": "Karadeniz iklimi",
            "hava_durumu_egilimi": "bol miktarda yağış, ılıman iklim"  },
        "Doğu Anadolu": {
            "iklim_tipi": "Karasal iklim",
            "hava_durumu_egilimi": "sert kışlar, kısa yazlar"  },
        "Güneydoğu Anadolu": {
            "iklim_tipi": "Karasal iklim",
            "hava_durumu_egilimi": "sert kışlar, kısa yazlar"  }}
    marmara_sehirleri = ["İstanbul", "Bursa", "Tekirdağ", "Edirne", "Çanakkale"]
    ege_sehirleri = ["İzmir", "Muğla", "Aydın", "Manisa", "Denizli"]
    akdeniz_sehirleri = ["Antalya", "Mersin", "Adana", "Hatay", "İçel"]
    iç_anadolu_sehirleri = ["Ankara", "Konya", "Eskişehir", "Kayseri", "Kırıkkale"]
    karadeniz_sehirleri = ["Trabzon", "Samsun", "Rize", "Ordu", "Zonguldak"]
    doğu_anadolu_sehirleri = ["Van", "Erzurum", "Diyarbakır", "Malatya", "Elazığ"]
    güneydoğu_anadolu_sehirleri = ["Şanlıurfa", "Gaziantep", "Mardin", "Adıyaman", "Batman"]
    türkiye_cografi_bolgeler = {
        "Marmara": {
            "iklim_tipi": "Karadeniz iklimi",
            "hava_durumu_egilimi": "bol miktarda yağış, ılıman iklim",
            "şehirler": marmara_sehirleri },
        "Ege": {
            "iklim_tipi": "Akdeniz iklimi",
            "hava_durumu_egilimi": "ılıman, az yağışlı",
            "şehirler": ege_sehirleri},
        "Akdeniz": {
            "iklim_tipi": "Akdeniz iklimi",
            "hava_durumu_egilimi": "ılıman, az yağışlı",
            "şehirler": akdeniz_sehirleri },
        "İç Anadolu": {
            "iklim_tipi": "Step iklimi",
            "hava_durumu_egilimi": "kıtasal iklim, karasal iklim özellikleri",
            "şehirler": iç_anadolu_sehirleri },
        "Karadeniz": {
            "iklim_tipi": "Karadeniz iklimi",
            "hava_durumu_egilimi": "bol miktarda yağış, ılıman iklim",
            "şehirler": karadeniz_sehirleri },
        "Doğu Anadolu": {
            "iklim_tipi": "Karasal iklim",
            "hava_durumu_egilimi": "sert kışlar, kısa yazlar",
            "şehirler": doğu_anadolu_sehirleri },
        "Güneydoğu Anadolu": {
            "iklim_tipi": "Karasal iklim",
            "hava_durumu_egilimi": "sert kışlar, kısa yazlar",
            "şehirler": güneydoğu_anadolu_sehirleri }}
    def random_hava_durumu_olustur(iklim_tipi):
        sicaklik_range = {
            "Karadeniz iklimi": (5, 25),
            "Akdeniz iklimi": (15, 35),
            "Step iklimi": (0, 30),
            "Karasal iklim": (-15, 25)}
        nem_range = {
            "Karadeniz iklimi": (50, 90),
            "Akdeniz iklimi": (40, 80),
            "Step iklimi": (30, 70),
            "Karasal iklim": (20, 60)  }
        yagis_turu = {
            "Karadeniz iklimi": ["Yağmur", "Kar", "Kar Fırtınası"],
            "Akdeniz iklimi": ["Yağmur", "Fırtına"],
            "Step iklimi": ["Rüzgar", "Toz Fırtınası"],
            "Karasal iklim": ["Kar", "Buz Fırtınası"] }
        sicaklik = random.randint(*sicaklik_range[iklim_tipi])
        nem = random.randint(*nem_range[iklim_tipi])
        yagis = random.choice(yagis_turu[iklim_tipi])
        hissedilen_sicaklik = random.randint(sicaklik - 5, sicaklik + 5)
        ruzgar_hizi = random.randint(0, 30)
        ruzgar_yonu = random.choice(["Kuzey", "Güney", "Doğu", "Batı"])
        alcak_basinc = random.randint(950, 1000)
        yuksek_basinc = random.randint(1000, 1050)
        bulutluluk_orani = random.randint(0, 100)
        return hava_durumu_sozlugu(sicaklik, hissedilen_sicaklik, nem, ruzgar_hizi, ruzgar_yonu, yagis, alcak_basinc, yuksek_basinc, bulutluluk_orani)
    türkiye_hava_durumu = {}
    for bolge, ozellikler in türkiye_cografi_bolgeler.items():
        iklim_tipi = ozellikler["iklim_tipi"]
        türkiye_hava_durumu[bolge] = {
            "hava_durumu_sozlugu": random_hava_durumu_olustur(iklim_tipi)  }
    def gün_sonu_öneri(hava_durumu):
        print("Gün sonu önerisi:")
        if hava_durumu["yağış türü"] == "Yağmur":
            print("Akşama doğru yağmur yağabilir, şemsiye almayı unutmayınız.")
        elif hava_durumu["yağış türü"] == "Kar":
            print("Akşama doğru kar yağabilir, kalın giysiler giymeyi unutmayın.")
        elif hava_durumu["yağış türü"] == "Fırtına":
            print("Akşama doğru fırtına çıkabilir, dikkatli olmakta fayda var!.")
        elif hava_durumu["yağış türü"] == "Yağış yok" and hava_durumu["sıcaklık"]>18:
            print("Hava akşama çok güzel,dışarıda keyifli vakit geçirebilirsiniz")
        elif hava_durumu["yağış türü"] == "Yağış yok" and hava_durumu["sıcaklık"]<=18:
            print("Akşama yağış gözükmüyor ama hava soğuk olabilir.Üstünüze kalın bir şeyler almayı tercih edebilirsiniz")
        elif hava_durumu["yağış türü"] == "Güneşli" and hava_durumu["sıcaklık"]>=18:
            print("Akşama hava ")
        elif hava_durumu["yağış türü"] == "Kum fırtınası":
            print("Akşama doğru kar yağabilir, kalın giysiler giymeyi unutmayın.")
        elif hava_durumu["yağış türü"] == "Buz fırtınası":
            print("Akşama doğru kar yağabilir, kalın giysiler giymeyi unutmayın.")
        elif hava_durumu["rüzgar hızı"] > 30:
            print("Akşama doğru şiddetli rüzgar olabilir, dışarı çıkarken dikkatli olun.")
        elif hava_durumu["sıcaklık"] < 10:
            print("Akşama doğru hava soğuyabilir, üstünüze kalın bir şeyler almayı düşünebilirsiniz.")
        else:
            print("Akşama doğru hava durumu bilgisi bulunamadı")
    def karar(bolge_adi):
        while True:
            seçim = input("\n1-Başka bir ilin hava durumu\n2-Ana menü\n3-Çıkış\nLütfen yapmak istediğiniz işlemi seçin: ").lower()
            if seçim == "1":
                il_secimi(bolge_adi)
                break  
            elif seçim == "2":
                yanmenü()
                break  
            elif seçim == "3":
                print("Çıkış yapılıyor...")
                time.sleep(1)
                print("Çıkış yapıldı.Yine beklerizz.")
                sys.exit()
            else:
                print("Geçersiz seçim!") 
    def bölge_bilgilerini_yazdir(bolge_adi, ozellikler):
        print(f"{bolge_adi} Bölgesinin Özellikleri:")
        for ozellik, deger in ozellikler.items():
            print(f"- {ozellik.capitalize()}: {deger}")
    def bölge_seçimi():
        while True:
            print("Coğrafi Bölgeler:")
            for i, bolge in enumerate(türkiye_cografi_bolgeler.keys(), 1):
                print(f"{i}- {bolge}")
            print("8- Tüm Bölgeler")
            print("-----------------------")
            secim = input("Hangi bölgeyi istersiniz? (numara veya isim olarak girin): ").strip()
            if secim.isdigit():  
                secim = int(secim)
                if 1 <= secim <= 8:  
                    return str(secim)
                else:
                    print("Geçersiz seçim. Lütfen 1-8 arasında bir numara girin.")
            else:
                print("Geçersiz giriş. Lütfen bir numara girin.")
    def bölgeye_göre_özellik():
        while True:
            bolge_sec = bölge_seçimi()
            try:
                bolge_sec = int(bolge_sec)
                if 1 <= bolge_sec <= len(türkiye_cografi_bolgeler):
                    bolge_adi = list(türkiye_cografi_bolgeler.keys())[bolge_sec - 1]
                    ozellikler = türkiye_cografi_bolgeler[bolge_adi]
                    bölge_bilgilerini_yazdir(bolge_adi, ozellikler)
                    break
                elif bolge_sec == 8:
                    for bolge_adi, ozellikler in türkiye_cografi_bolgeler.items():
                        bölge_bilgilerini_yazdir(bolge_adi, ozellikler)
                    break
                else:
                    print("Geçersiz bölge seçimi. Lütfen geçerli bir numara girin.")
            except ValueError:
                print("Geçersiz giriş. Lütfen bir numara girin.")      
    def haftalık_öneriler(haftalik_hava_durumu):
        haftalık_sıcaklık=[durum["sıcaklık"] for durum in haftalik_hava_durumu.values()]
        haftalık_hava_durumu_tipi=[durum["yağış türü"] for durum in haftalik_hava_durumu.values()]
        min_sıcaklık=min(haftalık_sıcaklık)
        max_sıcaklık=max(haftalık_sıcaklık)
        ortalama_sıcaklık=sum(haftalık_sıcaklık)/ len(haftalık_sıcaklık)
        sıcaklık_yorum = ""
        if max_sıcaklık > 30:
            sıcaklık_yorum = "Sıcaklık çok yüksek! Dışarı çıkarken güneş kremi kullanmayı ve bol su içmeyi unutmayın."
        elif max_sıcaklık > 25:
            sıcaklık_yorum = "Sıcaklık normalin üstünde. Bol su tüketmeye dikkat edin."
        elif min_sıcaklık < 5:
            sıcaklık_yorum = "Sıcaklık çok düşük! Dışarı çıkarken kalın giysiler giyin ve sıcak içecekler tüketin."
        elif min_sıcaklık < 10:
            sıcaklık_yorum = "Soğuk bir hafta görünüyor. İçinizi ısıtacak sıcak içecekler tüketebilirsiniz."
        yağış_tipi_sayısı = len(set(haftalık_hava_durumu_tipi))
        yağış_yorum = ""
        if yağış_tipi_sayısı > 2:
            yağış_yorum = "Bu hafta hava oldukça değişken gözüküyor. Şemsiye ve yağmurluk hazır bulundurun."
        elif "Kar" in haftalık_hava_durumu_tipi:
            yağış_yorum = "Kar yağışı bekleniyor. Araç kullanırken dikkatli olun ve kış lastiği takılı olduğundan emin olun."
        elif "Yağmur" in haftalık_hava_durumu_tipi:
            yağış_yorum = "Yağmurlu bir hafta görünüyor. Şemsiyenizi yanınızdan ayırmayın."
        print("Haftalık Öneriler:")
        print(f"- Haftanın en düşük sıcaklığı: {min_sıcaklık}°C")
        print(f"- Haftanın en yüksek sıcaklığı: {max_sıcaklık}°C")
        print(f"- Haftanın ortalama sıcaklığı: {ortalama_sıcaklık}°C")
        print(sıcaklık_yorum)
        print(yağış_yorum)
          
    def bölgeye_göre_hava_durumu():
        bolge_sec = bölge_seçimi()
        try:
            bolge_sec = int(bolge_sec)
            if 1 <= bolge_sec <= len(türkiye_cografi_bolgeler):
                bolge_adi = list(türkiye_cografi_bolgeler.keys())[bolge_sec - 1]
                iklim_tipi = ozellikler["iklim_tipi"]
                hava_durumu = random_hava_durumu_olustur(iklim_tipi)
                print(f"{bolge_adi} Bölgesinin Şehirleri ve Hava Durumu:")
                for sehir in türkiye_cografi_bolgeler[bolge_adi]["şehirler"]:
                    hava_durumu = türkiye_hava_durumu[bolge_adi]["hava_durumu_sozlugu"]
                    print(f"\n{sehir} için hava durumu:")
                    for ozellik, deger in hava_durumu.items():
                        print(f"{ozellik.capitalize()}: {deger}") 
                while True:
                    hava_durumu_secim = input(f"{bolge_adi} için 7 günlük hava durumu ister misiniz?((e)vet/(h)ayır): ").lower()
                    if hava_durumu_secim == "evet" or hava_durumu_secim == "e":
                        print(f"{bolge_adi} için 7 günlük hava durumu yazdırılıyor")
                        time.sleep(1)
                        print(f"{bolge_adi} için 7 günlük hava durumu:")
                        haftalik_durumlar = haftalık_hava_durumu_olustur()
                        haftalık_hava_durumu_goster(haftalik_durumlar)
                    elif hava_durumu_secim=="hayır" or "h":
                        print("İstenilmedi")
                
                        öneri_isteği = input("Bu hafta öneri ister misiniz? ((e)vet/(h)ayır): ").lower()
                        if öneri_isteği == "evet" or öneri_isteği == "e":
                            print("Bu hafta için öneriler: ")
                            haftalık_öneriler(haftalik_durumlar) 
                            break
                        elif öneri_isteği == "hayır" or öneri_isteği=="h":
                            print("Tamam, öneriler sunulmadı.")
                            karar(bolge_adi)
                            break
                while True:
                    hava_durumu_secim = input("Herhangi bir ilin hava durumunu saatlik veya haftalık detayını görmek ister misiniz? (evet/hayır): ").lower()
                    Detay_il_Seçimi(bolge_adi)
                    if hava_durumu_secim == "evet" or hava_durumu_secim == "e":
                        while True:
                            cevap = input("\nÖneri ister misiniz? (evet/hayır): ").lower()
                            if cevap == "evet":
                                haftalık_mı_saatlik_mi = input("Saatlik hava durumu önerisi için '1', haftalık hava durumu önerisi için '2' yazın: ")
                                if haftalık_mı_saatlik_mi == "1":
                                    haftalık_öneriler(haftalik_durumlar)
                                    break
                                elif haftalık_mı_saatlik_mi == "2":
                                    gün_sonu_öneri(hava_durumu)
                                    break
                                else:
                                    print("Öneri istenmedi.")
                                    secim()
                            else:
                                print("Geçersiz giriş. Öneri almak için 'evet', almamak için 'hayır' girin.")
                            break
                    elif hava_durumu_secim == "hayır" or hava_durumu_secim == "h":
                        print("Hava durumu detayı yazılmadı")
                        time.sleep(1)
                        secim()
                    if bolge_sec == 8:
                        for bolge_adi, hava_durumu in türkiye_hava_durumu.items():
                            print(f"\n{bolge_adi} Bölgesinin Şehirleri ve Hava Durumu:")
                            for sehir in hava_durumu["şehirler"]:
                                hava_durumu = hava_durumu["hava_durumu_sozlugu"]
                                print(f"\n{sehir} için hava durumu:")
                                for ozellik, deger in hava_durumu.items():
                                    print(f"{ozellik.capitalize()}: {deger}")
                            cevap = input("\nÖneri ister misiniz? (e/h): ").lower()
                            if cevap == "e":
                                il_secimi(bolge_adi)
                            elif cevap == "h":
                                print("Öneri istenmedi.")
                            else:
                                print("Geçersiz giriş. Öneri almak için 'e', almamak için 'h' girin.")
                        karar(bolge_adi)
            else:
                print("Tüm bölgeler seçimi hava durumu için geçerli değildir")
                print("Seçenekler")
                time.sleep(1)
        except ValueError:
            bolge_adi = bolge_sec.title()
            if bolge_adi in türkiye_cografi_bolgeler:
                print(f"\n{bolge_adi} Bölgesinin Şehirleri ve Hava Durumu:")
                for sehir in türkiye_cografi_bolgeler[bolge_adi]["şehirler"]:
                    hava_durumu = türkiye_hava_durumu[bolge_adi]["hava_durumu_sozlugu"]
                    print(f"\n{sehir} için hava durumu:")
                    for ozellik, deger in hava_durumu.items():
                        print(f"{ozellik.capitalize()}: {deger}")
                cevap = input("\nÖneri ister misiniz? (e/h): ").lower()
                if cevap == "e":
                    il_secimi(bolge_adi)
                elif cevap == "h":
                    print("Öneri istenmedi.")
                else:
                    print("Geçersiz giriş yaptınız! Öneri almak için 'e', almamak için 'h' giriniz.")
                karar(bolge_adi) 
            else:
                print("Geçersiz seçim yaptınız! Lütfen geçerli bir isim girin.")
    def haftalık_hava_durumu_olustur():
        haftalik_durumlar={}
        gunler=["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
        for gun in gunler:
            iklim_tipi=random.choice(list(türkiye_cografi_bolgeler.values()))["iklim_tipi"]
            hava_durumu=random_hava_durumu_olustur(iklim_tipi)
            haftalik_durumlar[gun]=hava_durumu
        return haftalik_durumlar
    def günlük_hava_durumu_goster(hava_durumu):
        print("Günlük hava durumu: ")
        for gün,durum in hava_durumu.items():
            print(f" 📆  {gün}: {durum}")
    def haftalık_hava_durumu_goster(hava_durumu):
        for gun,durum in hava_durumu.items():
            hava_durumu_tipi=durum["yağış türü"]
            sicaklik=durum["sıcaklık"]
            print(f"📆  {gun}: {hava_durumu_tipi}, 🌡️  Sıcaklık: {sicaklik} °C ")
    def saatlik_hava_durumu_goster():
        su_an=datetime.now()
        saat=su_an.hour
        for i in range(saat+1,24,4):
            print(f" ⏰  Saat {i}:00")
            iklim_tipi=random.choice(list(türkiye_cografi_bolgeler.values()))["iklim_tipi"]
            hava_durumu=random_hava_durumu_olustur(iklim_tipi)
            sicaklık=hava_durumu["sıcaklık"]
            hava_durumu_tipi=hava_durumu["yağış türü"]
            print(f"Sıcaklık: {sicaklık} °C , Hava Durumu: {hava_durumu_tipi}")
            print("-" * 30)
            gün_sonu_öneri(hava_durumu)
    def Detay_il_Seçimi(bolge_adi):
        sehirler = türkiye_cografi_bolgeler[bolge_adi]["şehirler"]
        print("Hangi il için detay istersiniz?")
        for i, sehir in enumerate(sehirler, 1):
            print(f"{i}. {sehir}")
        while True:
            try:
                secilen_il = int(input("Lütfen bir il seçiniz (numara olarak): "))
                if 1 <= secilen_il <= len(sehirler):
                    secilen_sehir = sehirler[secilen_il - 1]
                    hava_durumu = türkiye_hava_durumu[bolge_adi]["hava_durumu_sozlugu"]
                    haftalık_mı_saatlik_mi = input("Saatlik hava durumu için (1), haftalık hava durumu için (2) yazınız: ")
                    if haftalık_mı_saatlik_mi == "1":
                        saatlik_hava_durumu_goster()
                    elif haftalık_mı_saatlik_mi == "2":
                        haftalik_durumlar = haftalık_hava_durumu_olustur()
                        haftalık_hava_durumu_goster(haftalik_durumlar)
                        
                    karar(bolge_adi)
                    break
                else:
                    print("Geçersiz seçim yaptınız! Lütfen geçerli bir numara giriniz.")
            except ValueError:
                print("Geçersiz giriş yaptınız! Lütfen bir numara girin.")
    def il_secimi(bolge_adi):
        sehirler = türkiye_cografi_bolgeler[bolge_adi]["şehirler"]
        print("\nHangi il için hava durumu istersiniz?")
        for i, sehir in enumerate(sehirler, 1):
            print(f"{i}. {sehir}")
        while True:
            try:
                secilen_il = int(input("Lütfen bir il seçiniz (numara olarak): "))
                if 1 <= secilen_il <= len(sehirler):
                    secilen_sehir = sehirler[secilen_il - 1]
                    hava_durumu = türkiye_hava_durumu[bolge_adi]["hava_durumu_sozlugu"]
                    haftalık_mı_saatlik_mi = input("Saatlik hava durumu için (1), haftalık hava durumu için (2) yazınız: ")
                    if haftalık_mı_saatlik_mi == "1":
                        saatlik_hava_durumu_goster()
                    
                    elif haftalık_mı_saatlik_mi == "2":
                        haftalik_durumlar = haftalık_hava_durumu_olustur()
                        haftalık_hava_durumu_goster(haftalik_durumlar)
                        
                    karar(bolge_adi)
                    break
                else:
                    print("Geçersiz seçim yaptınız! Lütfen geçerli bir numara giriniz.")
            except ValueError:
                print("Geçersiz giriş yaptınız! Lütfen bir numara girin.")
    def anamenü():
        print("Hava Durumu Uygulamasına Hoş Geldiniz!")
        print("1. Bölgeye Göre Özellikler")
        print("2. Bölgeye Göre Hava Durumu")
        print("3. Çıkış")
        seçim = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        if seçim in ("1", "2", "3"):
            return seçim
        else:
            print("Geçersiz seçim yaptınız! Lütfen 1, 2 veya 3 seçeneklerinden birini seçiniz.")
    def yanmenü():
        print("1. Bölgeye Göre Özellikler")
        print("2. Bölgeye Göre Hava Durumu")
        print("3. Çıkış")
        while True:
            try:
                kararr = int(input("Kararınızı seçiniz: "))
                if kararr == 1:
                    bölgeye_göre_özellik()
                elif kararr == 2:
                    bölgeye_göre_hava_durumu()
                elif kararr == 3:
                    print("Programdan çıkış yapılıyor...")
                    time.sleep(1)
                    print("Çıkış yapıldı. Yine bekleriz...")
                    sys.exit()
                else:
                    print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")
            except ValueError:
                print("Geçersiz giriş. Lütfen bir sayı girin.")
    def secim():
        global declision
        declision = anamenü()  
        while declision not in ("3", "q", "çıkış"):  
            try:
                if declision == "1":
                    bölgeye_göre_özellik() 
                    while True:
                        print("1-Ana menü\n2-Çıkış\n3-Devam et")             
                        cevap2 = input("Lütfen yapmak istediğiniz işlemi seçiniz: ").lower()
                        if cevap2 == "1":
                            declision = anamenü() 
                            break
                        elif cevap2 == "2":
                            print("Programdan çıkış yapılıyor...")
                            time.sleep(1)
                            print("Çıkış yapıldı. Yine bekleriz...")
                            sys.exit()
                        elif cevap2 == "3":
                            break
                        else:
                            print("Geçersiz seçim yaptınız!")
                elif declision == "2":
                    bölgeye_göre_hava_durumu()
                    while True:
                        print("1-Ana menü\n2-Çıkış\n3-Devam et")           
                        cevap2 = input("Lütfen yapmak istediğiniz işlemi seçiniz: ").lower()
                        if cevap2 == "1":
                            declision = anamenü() 
                            break
                        elif cevap2 == "2":
                            print("Programdan çıkış yapılıyor...")
                            time.sleep(1)
                            print("Çıkış yapıldı. Yine bekleriz...")
                            sys.exit()
                        elif cevap2 == "3":
                            break
                        else:
                            print("Geçersiz seçim yaptınız! Ana menüye dönülüyor...")
                            declision = anamenü()
                elif declision == "3":
                    print("Programdan çıkış yapılıyor...")
                    time.sleep(1)
                    print("Çıkış yapıldı. Yine bekleriz...")
                    sys.exit()
                else:
                    print("Geçersiz seçim yaptınız! Ana menüye dönülüyor...")
                    declision = anamenü()  
            except Exception as e:
                print(f"Beklenmeyen bir hata oluştu: {e}") 
    secim()
    def bolge_ozellikleri(bolge_adi):
        print(bolge_adi, "Bölgesinin Şehirleri ve Hava Durumu:\n")
        for sehir, hava_durumu in bolgeler[bolge_adi].items():
            print(f"{sehir} için hava durumu:")
            for ozellik, deger in hava_durumu.items():
                print(f"{ozellik}: {deger}")
            print()
        declision = input("Öneri ister misiniz? (evet/hayır): ").lower()
        if declision == "evet":
            while True:
                sehir_secim = input("\nHangi il için hava durumu istersiniz?\n" + "\n".join(f"{i+1}. {sehir}" for i, sehir in enumerate(bolgeler[bolge_adi])) + "\nLütfen bir il seçin (numara olarak): ")
                if sehir_secim.isdigit() and int(sehir_secim) in range(1, len(bolgeler[bolge_adi]) + 1):
                    sehir_adi = list(bolgeler[bolge_adi].keys())[int(sehir_secim) - 1]
                    break
                else:
                    print("Geçersiz seçim yaptınız!")
        elif declision != "hayır":
            print("Geçersiz seçim yaptınız!")
print("Hava durumu otomasyonuna hoş geldiniz!")
while True:
    print("1. Dünya")
    print("2. Türkiye")
    print("3. Çıkış")
    seçimm = input("Lütfen bir seçim yapınız: ").lower()
    if seçimm == "1" or seçimm == "bir" or seçimm == "dünya":
        dünya()
        break
    elif seçimm == "2" or seçimm == "iki" or seçimm == "türkiye":
        türkiye()
        break
    elif seçimm == "3" or seçimm == "üç" or seçimm == "çıkış":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Çıkış yapıldı. Yine bekleriz...")
        sys.exit()
    else:
        print("Geçersiz seçim! Lütfen geçerli bir seçim yapınız.")