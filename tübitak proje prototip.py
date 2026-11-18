import random
import re
import tkinter as tk
from tkinter import messagebox, ttk


# =====================================================================
# 1. NLP RETORİK & OCTALYSIS ETİKETLEME FONKSİYONU
# =====================================================================
def octalysis_analiz_et(metin: str) -> str:
    sozluk = {
        "Destansı Anlam ve Çağrı": ["evren", "insanlık", "gelecek", "keşfet", "dünya", "yaşam", "doğa", "kader"],
        "Öngörülemezlik ve Merak": ["acaba", "neden", "nasıl", "şaşırtıcı", "paradoks", "sır", "merak", "görünmeyen"],
        "Gelişim ve Başarı": ["çöz", "hesapla", "kanıtla", "ustalaş", "modelle", "formül", "denge", "analiz"]
    }
    temiz = re.sub(r"[^\w\sçğıöşüÇĞİÖŞÜ]", "", metin.lower()).split()
    skorlar = {
        boyut: sum(1 for k in temiz if any(a in k for a in kelimeler))
        for boyut, kelimeler in sozluk.items()
    }
    baskin = max(skorlar, key=skorlar.get)
    return baskin if skorlar[baskin] > 0 else "Öngörülemezlik ve Merak"


# =====================================================================
# 2. 11 VE 12. SINIF DERS GÖREV HAVUZU
# =====================================================================
GOREVLER = {
    11: {
        "Matematik": [
            {
                "konu": "Trigonometri",
                "hikaye": "Acaba deniz fenerlerinin ışık sinyalleri ve ses dalgaları neden aynı matematiksel ritmi takip eder?",
                "soru": "sin(x) = 1/2 denkleminin [0, π] aralığındaki köklerinin toplamı kaç derecedir?",
                "secenekler": ["A) 90", "B) 150", "C) 180", "D) 210"],
                "dogru": "C",
                "ipucu": "Birim çemberde sinüs hem 1. hem 2. bölgede pozitiftir (30° ve 150°).",
                "geri_bildirim": "Sinüs fonksiyonunun simetrisini kullanarak 30° + 150° = 180° sonucuna ulaştın."
            }
        ],
        "Fizik": [
            {
                "konu": "Yatay Atış Hareketi",
                "hikaye": "İnsanlığın Mars'a indireceği keşif aracının iniş süresini yerçekimi ivmesini kullanarak modelle!",
                "soru": "Sürtünmesiz ortamda 45 m yükseklikten yatay atılan cisim kaç saniyede yere düşer? (g = 10 m/s²)",
                "secenekler": ["A) 2", "B) 3", "C) 4", "D) 4.5"],
                "dogru": "B",
                "ipucu": "Düşey eksende serbest düşme formülü: h = 1/2 · g · t².",
                "geri_bildirim": "Yatay hız düşey süreyi etkilemez; 45 = 5·t² eşitliğinden t = 3 s bulunur."
            }
        ],
        "Kimya": [
            {
                "konu": "Gazlar ve Kinetik Teori",
                "hikaye": "Stratosfere gönderilen meteoroloji balonunun yükseldikçe neden genişlediğinin sırrını çöz!",
                "soru": "Sabit sıcaklıkta hacmi yarıya indirilen ideal bir gazın basıncı nasıl değişir?",
                "secenekler": ["A) Yarıya iner", "B) Değişmez", "C) 2 katına çıkar", "D) 4 katına çıkar"],
                "dogru": "C",
                "ipucu": "Boyle-Mariotte Yasası: P1 · V1 = P2 · V2.",
                "geri_bildirim": "Hacim yarıya indiğinde moleküllerin çarpma sıklığı artar ve basınç 2 katına çıkar."
            }
        ],
        "Biyoloji": [
            {
                "konu": "Sinir Sistemi",
                "hikaye": "Sıcak bir yüzeye dokunduğunda milisaniyeler içinde beynine giden elektrik sinyali yaşamını korur.",
                "soru": "Bir nöronda impuls iletim hızını aşağıdakilerden hangisi artırır?",
                "secenekler": ["A) Uyarı şiddeti", "B) Miyelin kılıf varlığı", "C) Uyarı frekansı", "D) Sinaps sayısı"],
                "dogru": "B",
                "ipucu": "Ranvier boğumlarında gerçekleşen atlamalı iletimi düşün.",
                "geri_bildirim": "Miyelin kılıf ve akson çapı impuls iletim hızını doğrudan artırır."
            }
        ]
    },
    12: {
        "Matematik": [
            {
                "konu": "Türev ve Anlık Değişim",
                "hikaye": "Bir roketin yakıt tüketimi her saniye değişirken anlık ivmesini nasıl hesaplarsın?",
                "soru": "f(x) = x³ - 4x + 5 fonksiyonunun x = 2 noktasındaki türevi kaçtır?",
                "secenekler": ["A) 4", "B) 8", "C) 10", "D) 12"],
                "dogru": "B",
                "ipucu": "f'(x) = 3x² - 4 türev ifadesinde x yerine 2 yaz.",
                "geri_bildirim": "f'(2) = 3(4) - 4 = 8 değeri, eğrinin x = 2 noktasındaki anlık değişim hızını verir."
            }
        ],
        "Fizik": [
            {
                "konu": "Çembersel Hareket",
                "hikaye": "Uzay istasyonunda yapay yerçekimi oluşturmak için dönen silindirlerin merkezcil kuvvet dengesini kur!",
                "soru": "Yarıçapı 2 m olan yörüngede 4 m/s sabit süratle dönen 3 kg kütleli cismin merkezcil kuvveti kaç N'dur?",
                "secenekler": ["A) 12", "B) 18", "C) 24", "D) 36"],
                "dogru": "C",
                "ipucu": "Merkezcil kuvvet formülü: F = m · v² / r.",
                "geri_bildirim": "F = 3 · (16 / 2) = 24 N olarak sistemin merkezcil kuvvetini doğru hesapladın."
            }
        ],
        "Kimya": [
            {
                "konu": "Elektrokimya ve Piller",
                "hikaye": "Geleceğin elektrikli araçları elektron transferine dayanır. Galvanik hücrenin potansiyelini hesapla!",
                "soru": "Zn²⁺/Zn = -0,76 V ve Cu²⁺/Cu = +0,34 V olan pilin standart pil potansiyeli kaç Volttur?",
                "secenekler": ["A) 0,42 V", "B) 1,10 V", "C) -1,10 V", "D) 0,76 V"],
                "dogru": "B",
                "ipucu": "İndirgenme potansiyeli küçük olan Zn yükseltgenir (ters çevrilir).",
                "geri_bildirim": "E°pil = +0,76 + 0,34 = 1,10 V olarak bulunur."
            }
        ],
        "Biyoloji": [
            {
                "konu": "Genetik Şifre",
                "hikaye": "DNA sarmalındaki dört harflik alfabe yeryüzündeki tüm canlılığın kaderini yazar.",
                "soru": "DNA'nın anlamlı zincirindeki 'TAC' üçlüsüne karşılık gelen mRNA kodonu hangisidir?",
                "secenekler": ["A) AUG", "B) UAC", "C) ATG", "D) GUA"],
                "dogru": "A",
                "ipucu": "RNA'da Timin (T) yerine Urasil (U) gelir: A->U, T->A, C->G.",
                "geri_bildirim": "'AUG' protein sentezini başlatan evrensel başlangıç kodonudur."
            }
        ]
    }
}


# =====================================================================
# 3. MASAÜSTÜ UYGULAMA ARAYÜZÜ (GÖREV + ÖDÜL + LİDERLİK TABLOSU)
# =====================================================================
class OctalysisPrototipApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Octalysis & AI Sayısal Eğitim Prototipi")
        self.root.geometry("1180x640")
        self.root.configure(bg="#F1F5F9")

        self.sinif = tk.IntVar(value=12)
        self.aktif_ders = "Matematik"
        self.aktif_gorev = None
        self.cevaplandi = False
        self.xp = 0
        self.ilerleme = {"Matematik": 0, "Fizik": 0, "Kimya": 0, "Biyoloji": 0}

        # Liderlik tablosu için örnek sınıf arkadaşları (Sosyal Etki mekaniği)
        self.rakipler = [
            {"ad": "Elif Y.", "xp": 240},
            {"ad": "Mert K.", "xp": 180},
            {"ad": "Zeynep A.", "xp": 120},
            {"ad": "Caner T.", "xp": 70},
            {"ad": "Selin D.", "xp": 30},
        ]

        # Ödül / Rozet tanımları (Gelişim ve Başarı mekaniği)
        self.odul_tanimlari = [
            {"id": "ilk_adim", "baslik": "Merak Kıvılcımı", "kosul": "İlk görevi tamamla (15+ XP)", "kazanildi": False},
            {"id": "kasif", "baslik": "Bilim Kaşifi", "kosul": "100 XP barajını aş", "kazanildi": False},
            {"id": "dort_element", "baslik": "4 Disiplin Ustası", "kosul": "Mat-Fiz-Kim-Biyo çöz", "kazanildi": False},
            {"id": "zirve", "baslik": "Sayısal Lideri", "kosul": "Liderlikte 1. sıraya çık", "kazanildi": False},
        ]

        self.arayuzu_kur()
        self.gorev_yukle("Matematik")
        self.odul_ve_liderlik_guncelle()

    def arayuzu_kur(self):
        # Üst Bar
        ust = tk.Frame(self.root, bg="#1E3A8A", padx=20, pady=12)
        ust.pack(fill="x")

        tk.Label(ust, text="OCTALYSIS SAYISAL EĞİTİM PROTOTİPİ", font=("Segoe UI", 11, "bold"), bg="#1E3A8A", fg="white").pack(side="left")

        sinif_kutu = tk.Frame(ust, bg="#1E3A8A")
        sinif_kutu.pack(side="left", padx=30)
        tk.Radiobutton(sinif_kutu, text="11. Sınıf", variable=self.sinif, value=11, command=lambda: self.gorev_yukle(self.aktif_ders), bg="#1E3A8A", fg="white", selectcolor="#1E40AF", activebackground="#1E3A8A", font=("Segoe UI", 10)).pack(side="left", padx=5)
        tk.Radiobutton(sinif_kutu, text="12. Sınıf", variable=self.sinif, value=12, command=lambda: self.gorev_yukle(self.aktif_ders), bg="#1E3A8A", fg="white", selectcolor="#1E40AF", activebackground="#1E3A8A", font=("Segoe UI", 10)).pack(side="left", padx=5)

        self.xp_lbl = tk.Label(ust, text="Seviye: 1  |  Toplam Puan: 0 XP", font=("Segoe UI", 11, "bold"), bg="#1E3A8A", fg="#FDE047")
        self.xp_lbl.pack(side="right")

        # 3 Sütunlu Ana Gövde
        govde = tk.Frame(self.root, bg="#F1F5F9", padx=16, pady=16)
        govde.pack(fill="both", expand=True)

        # -------------------------------------------------------------
        # SOL PANEL: DERS MODÜLLERİ VE İLERLEME
        # -------------------------------------------------------------
        sol = tk.Frame(govde, bg="white", width=220, padx=14, pady=14, highlightbackground="#CBD5E1", highlightthickness=1)
        sol.pack(side="left", fill="y", padx=(0, 12))
        sol.pack_propagate(False)

        tk.Label(sol, text="DERS MODÜLLERİ", font=("Segoe UI", 10, "bold"), bg="white", fg="#0F172A").pack(anchor="w", pady=(0, 10))

        self.barlar = {}
        self.yuzde_lbls = {}
        renkler = {"Matematik": "#2563EB", "Fizik": "#7C3AED", "Kimya": "#059669", "Biyoloji": "#D97706"}
        for ders, renk in renkler.items():
            kutu = tk.Frame(sol, bg="#F8FAFC", padx=8, pady=8, highlightbackground="#E2E8F0", highlightthickness=1)
            kutu.pack(fill="x", pady=6)

            ust_d = tk.Frame(kutu, bg="#F8FAFC")
            ust_d.pack(fill="x")
            tk.Button(ust_d, text=ders, bg=renk, fg="white", font=("Segoe UI", 9, "bold"), relief="flat", width=10, cursor="hand2", command=lambda d=ders: self.gorev_yukle(d)).pack(side="left")
            ylbl = tk.Label(ust_d, text="%0", font=("Segoe UI", 9, "bold"), bg="#F8FAFC", fg="#475569")
            ylbl.pack(side="right")
            self.yuzde_lbls[ders] = ylbl

            bar = ttk.Progressbar(kutu, maximum=100, value=0)
            bar.pack(fill="x", pady=(6, 0))
            self.barlar[ders] = bar

        # -------------------------------------------------------------
        # ORTA PANEL: AKTİF GÖREV VE BİÇİMLENDİRİCİ GERİ BİLDİRİM
        # -------------------------------------------------------------
        orta = tk.Frame(govde, bg="white", padx=20, pady=16, highlightbackground="#CBD5E1", highlightthickness=1)
        orta.pack(side="left", fill="both", expand=True, padx=(0, 12))

        baslik_satir = tk.Frame(orta, bg="white")
        baslik_satir.pack(fill="x", pady=(0, 10))
        self.konu_lbl = tk.Label(baslik_satir, text="", font=("Segoe UI", 12, "bold"), bg="white", fg="#0F172A")
        self.konu_lbl.pack(side="left")
        self.nlp_lbl = tk.Label(baslik_satir, text="", font=("Segoe UI", 8, "bold"), bg="#DBEAFE", fg="#1E40AF", padx=8, pady=3)
        self.nlp_lbl.pack(side="right")

        hikaye_kutu = tk.Frame(orta, bg="#EFF6FF", padx=12, pady=10, highlightbackground="#BFDBFE", highlightthickness=1)
        hikaye_kutu.pack(fill="x", pady=(0, 12))
        self.hikaye_lbl = tk.Label(hikaye_kutu, text="", font=("Segoe UI", 10, "italic"), bg="#EFF6FF", fg="#1E293B", wraplength=520, justify="left")
        self.hikaye_lbl.pack(anchor="w")

        self.soru_lbl = tk.Label(orta, text="", font=("Segoe UI", 11, "bold"), bg="white", fg="#0F172A", wraplength=540, justify="left")
        self.soru_lbl.pack(anchor="w", pady=(0, 10))

        self.secim = tk.StringVar(value="")
        self.secenek_rb = []
        for harf in ["A", "B", "C", "D"]:
            rb = tk.Radiobutton(orta, text="", variable=self.secim, value=harf, font=("Segoe UI", 10), bg="white", anchor="w", cursor="hand2")
            rb.pack(fill="x", pady=2)
            self.secenek_rb.append(rb)

        btn_satir = tk.Frame(orta, bg="white")
        btn_satir.pack(fill="x", pady=12)
        tk.Button(btn_satir, text="Merak İpucu", bg="#FEF3C7", fg="#92400E", font=("Segoe UI", 9, "bold"), relief="flat", padx=12, pady=6, cursor="hand2", command=self.ipucu_goster).pack(side="left", padx=(0, 8))
        tk.Button(btn_satir, text="Cevabı Kontrol Et", bg="#16A34A", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=14, pady=6, cursor="hand2", command=self.kontrol_et).pack(side="left")
        tk.Button(btn_satir, text="Yeni Görev ->", bg="#E2E8F0", fg="#334155", font=("Segoe UI", 9, "bold"), relief="flat", padx=12, pady=6, cursor="hand2", command=lambda: self.gorev_yukle(self.aktif_ders)).pack(side="right")

        self.bildirim_kutu = tk.Frame(orta, bg="#F8FAFC", padx=12, pady=10, highlightbackground="#CBD5E1", highlightthickness=1)
        self.bildirim_kutu.pack(fill="both", expand=True)
        self.bildirim_lbl = tk.Label(self.bildirim_kutu, text="", font=("Segoe UI", 10), bg="#F8FAFC", fg="#475569", wraplength=520, justify="left")
        self.bildirim_lbl.pack(anchor="w")

        # -------------------------------------------------------------
        # SAĞ PANEL: ÖDÜLLER (ROZETLER) VE LİDERLİK TABLOSU
        # -------------------------------------------------------------
        sag = tk.Frame(govde, bg="white", width=270, padx=14, pady=14, highlightbackground="#CBD5E1", highlightthickness=1)
        sag.pack(side="right", fill="y")
        sag.pack_propagate(False)

        # Ödüller Bölümü
        tk.Label(sag, text="ÖDÜLLER & ROZETLER", font=("Segoe UI", 10, "bold"), bg="white", fg="#0F172A").pack(anchor="w", pady=(0, 8))
        self.odul_frame = tk.Frame(sag, bg="white")
        self.odul_frame.pack(fill="x", pady=(0, 14))

        self.odul_kartlari = []
        for odul in self.odul_tanimlari:
            kart = tk.Frame(self.odul_frame, bg="#F1F5F9", padx=8, pady=5, highlightbackground="#E2E8F0", highlightthickness=1)
            kart.pack(fill="x", pady=3)
            baslik_lbl = tk.Label(kart, text=f"[KİLİTLİ] {odul['baslik']}", font=("Segoe UI", 9, "bold"), bg="#F1F5F9", fg="#64748B")
            baslik_lbl.pack(anchor="w")
            kosul_lbl = tk.Label(kart, text=odul["kosul"], font=("Segoe UI", 8), bg="#F1F5F9", fg="#94A3B8")
            kosul_lbl.pack(anchor="w")
            self.odul_kartlari.append((kart, baslik_lbl, kosul_lbl))

        # Ayırıcı Çizgi
        ttk.Separator(sag, orient="horizontal").pack(fill="x", pady=8)

        # Liderlik Tablosu Bölümü
        tk.Label(sag, text="SINIF LİDERLİK TABLOSU", font=("Segoe UI", 10, "bold"), bg="white", fg="#0F172A").pack(anchor="w", pady=(4, 8))
        self.liderlik_frame = tk.Frame(sag, bg="white")
        self.liderlik_frame.pack(fill="both", expand=True)

    # -----------------------------------------------------------------
    # OYUNLAŞTIRMA VE GÜNCELLEME FONKSİYONLARI
    # -----------------------------------------------------------------
    def gorev_yukle(self, ders: str):
        self.aktif_ders = ders
        self.cevaplandi = False
        self.secim.set("")
        self.aktif_gorev = random.choice(GOREVLER[self.sinif.get()][ders])

        etiket = octalysis_analiz_et(self.aktif_gorev["hikaye"])
        self.konu_lbl.config(text=f"{ders.upper()} - {self.aktif_gorev['konu']}")
        self.nlp_lbl.config(text=f"AI-NLP: {etiket}")
        self.hikaye_lbl.config(text=self.aktif_gorev["hikaye"])
        self.soru_lbl.config(text=self.aktif_gorev["soru"])

        for rb, metin in zip(self.secenek_rb, self.aktif_gorev["secenekler"]):
            rb.config(text=metin)

        self.bildirim_kutu.config(bg="#F8FAFC", highlightbackground="#CBD5E1")
        self.bildirim_lbl.config(text="Seçeneğinizi işaretleyip cevabınızı kontrol edebilir veya ipucu alabilirsiniz.", bg="#F8FAFC", fg="#475569")

    def ipucu_goster(self):
        self.bildirim_kutu.config(bg="#FFFBEB", highlightbackground="#FCD34D")
        self.bildirim_lbl.config(text=f"İPUCU: {self.aktif_gorev['ipucu']}", bg="#FFFBEB", fg="#92400E")

    def kontrol_et(self):
        if self.cevaplandi:
            return
        if not self.secim.get():
            messagebox.showwarning("Uyarı", "Lütfen bir seçenek işaretleyin.")
            return

        self.cevaplandi = True
        dogru_mu = self.secim.get() == self.aktif_gorev["dogru"]
        kazanc = 50 if dogru_mu else 15
        self.xp += kazanc
        self.ilerleme[self.aktif_ders] = min(100, self.ilerleme[self.aktif_ders] + 50)

        seviye = (self.xp // 100) + 1
        self.xp_lbl.config(text=f"Seviye: {seviye}  |  Toplam Puan: {self.xp} XP")
        self.barlar[self.aktif_ders]["value"] = self.ilerleme[self.aktif_ders]
        self.yuzde_lbls[self.aktif_ders].config(text=f"%{self.ilerleme[self.aktif_ders]}")

        if dogru_mu:
            self.bildirim_kutu.config(bg="#F0FDF4", highlightbackground="#86EFAC")
            self.bildirim_lbl.config(text=f"DOĞRU! (+{kazanc} XP)\n{self.aktif_gorev['geri_bildirim']}", bg="#F0FDF4", fg="#166534")
        else:
            self.bildirim_kutu.config(bg="#FEF2F2", highlightbackground="#FCA5A5")
            self.bildirim_lbl.config(text=f"YANLIŞ (Doğru: {self.aktif_gorev['dogru']} | +{kazanc} XP)\n{self.aktif_gorev['geri_bildirim']}", bg="#FEF2F2", fg="#991B1B")

        self.odul_ve_liderlik_guncelle()

    def odul_ve_liderlik_guncelle(self):
        # 1. Liderlik tablosunu sırala
        liste = self.rakipler + [{"ad": "SEN (Öğrenci)", "xp": self.xp, "ben": True}]
        liste.sort(key=lambda x: x["xp"], reverse=True)

        kullanici_sirasi = next(i + 1 for i, k in enumerate(liste) if k.get("ben"))

        # 2. Ödül koşullarını kontrol et
        kosullar = {
            "ilk_adim": self.xp >= 15,
            "kasif": self.xp >= 100,
            "dort_element": all(p > 0 for p in self.ilerleme.values()),
            "zirve": kullanici_sirasi == 1 and self.xp > 0
        }

        for idx, odul in enumerate(self.odul_tanimlari):
            if kosullar[odul["id"]] and not odul["kazanildi"]:
                odul["kazanildi"] = True
                messagebox.showinfo("Yeni Ödül Kazandınız!", f"Tebrikler! '{odul['baslik']}' rozetinin kilidini açtınız!")

            kart, b_lbl, k_lbl = self.odul_kartlari[idx]
            if odul["kazanildi"]:
                kart.config(bg="#FEF3C7", highlightbackground="#F59E0B")
                b_lbl.config(text=f"[KAZANILDI] {odul['baslik']}", bg="#FEF3C7", fg="#92400E")
                k_lbl.config(bg="#FEF3C7", fg="#B45309")

        # 3. Liderlik tablosunu yeniden çiz
        for widget in self.liderlik_frame.winfo_children():
            widget.destroy()

        for sira, kisi in enumerate(liste, start=1):
            ben_mi = kisi.get("ben", False)
            arkaplan = "#DBEAFE" if ben_mi else "#F8FAFC"
            kenar = "#2563EB" if ben_mi else "#E2E8F0"
            yazi_renk = "#1E3A8A" if ben_mi else "#334155"
            font_tipi = ("Segoe UI", 9, "bold") if ben_mi else ("Segoe UI", 9)

            satir = tk.Frame(self.liderlik_frame, bg=arkaplan, padx=8, pady=6, highlightbackground=kenar, highlightthickness=1)
            satir.pack(fill="x", pady=3)

            tk.Label(satir, text=f"#{sira}  {kisi['ad']}", font=font_tipi, bg=arkaplan, fg=yazi_renk).pack(side="left")
            tk.Label(satir, text=f"{kisi['xp']} XP", font=font_tipi, bg=arkaplan, fg=yazi_renk).pack(side="right")


if __name__ == "__main__":
    pencere = tk.Tk()
    OctalysisPrototipApp(pencere)
    pencere.mainloop()
