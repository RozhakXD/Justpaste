# 🌐 JUSTPASTE.IT SCRAPER - GOOGLE

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build](https://img.shields.io/badge/Build-Passing-green.svg)](https://github.com/RozhakXD/Justpaste)

![Justpaste](https://github.com/user-attachments/assets/7ec54619-14da-4e40-8b32-d2a032c6052f)

Justpaste adalah alat untuk melakukan scraping link dari situs [Justpaste.it](https://justpaste.it/) menggunakan Google sebagai mesin pencarian. Tool ini dibuat untuk memudahkan Anda dalam mendapatkan tautan dari Justpaste.it secara otomatis.

## 🚀 Fitur Utama
- 🛠️ **Konfigurasi Mudah:** Sesuaikan pertanyaan pencarian sesuai kebutuhan Anda.
- 🔍 **Scraping Otomatis:** Dapatkan tautan dari Justpaste.it dengan cepat menggunakan query pencarian Google.
- 📂 **Penyimpanan Hasil:** Semua tautan yang ditemukan akan disimpan dalam file JSON untuk digunakan nanti.
- ⚡ **Kunjungan Otomatis:** Opsi untuk mengunjungi setiap tautan dan mendapatkan informasi terkait.

## 📦 Instalasi
Pastikan Anda memiliki Python versi 3.8 atau lebih baru. Instalasi paket yang diperlukan dapat dilakukan dengan perintah berikut:

```bash
pip install -r requirements.txt
```

Jika Anda belum menginstal `rich`, `httpx`, dan `beautifulsoup4`, tool ini akan secara otomatis menginstalnya untuk Anda.

## 📝 Cara Penggunaan
1. Clone repository ini ke dalam direktori lokal Anda:
    ```bash
    git clone https://github.com/RozhakXD/Justpaste.git
    cd Justpaste
    ```
2. Jalankan skrip:
    ```bash
    python Run.py
    ```
3. **Masukkan Pertanyaan**: Isi pertanyaan yang akan digunakan untuk pencarian. Misalnya, Anda bisa mengetik:
    ```yaml
    September 2024 site:justpaste.it
    ```
Anda juga bisa menekan Enter untuk menggunakan pertanyaan default.

4. **Pilih Opsi Kunjungan**: Pilih apakah Anda ingin mengunjungi setiap tautan yang ditemukan dan mengumpulkan lebih banyak informasi.
5. **Dapatkan Hasil**: Tautan yang berhasil ditemukan akan disimpan dalam direktori `Temporary` dengan nama file yang unik.

## 📂 Struktur Direktori
- `Temporary/`: Direktori untuk menyimpan hasil scraping dalam format JSON.
- `Run.py`: File utama untuk menjalankan scraper.

## ⚠️ Masalah
Beberapa masalah yang mungkin Anda temui saat menggunakan Justpaste:

- **Koneksi Internet Tidak Stabil**: Alat ini bergantung pada koneksi internet yang stabil untuk melakukan scraping. Jika koneksi tidak stabil, proses scraping dapat terhenti atau menghasilkan data yang tidak lengkap.
- **Pemblokiran oleh Google**: Google dapat mendeteksi aktivitas scraping dan memblokir permintaan Anda sementara waktu. Ini dapat diatasi dengan memperlambat kecepatan permintaan atau menggunakan proxy.
- **Hasil Pencarian Tidak Lengkap**: Kadang-kadang, tautan yang diinginkan mungkin tidak muncul dalam hasil pencarian karena perubahan algoritma Google atau karena penggunaan kata kunci yang tidak sesuai.
- **Kendala pada Parsing Konten**: Perubahan pada struktur HTML dari situs Justpaste.it dapat menyebabkan parsing konten gagal atau memberikan hasil yang tidak diinginkan.
- **Mode Pesawat dan Penggunaan CPU**: Disarankan menggunakan mode pesawat saat scraping untuk menghindari masalah dengan sistem deteksi spam. Selain itu, proses scraping bisa cukup intensif pada CPU.

## 📷 Tangkapan Layar
![FunPic_20240906](https://github.com/user-attachments/assets/e976ebcf-61a9-4ec9-94de-06e2ec6479fc)

## 💬 Dukungan
Jika Anda merasa proyek ini bermanfaat, pertimbangkan untuk mendukung pengembangan lebih lanjut:

- 💰 Trakteer: [Dukung saya di Trakteer](https://trakteer.id/rozhak_official/tip)
- ☕ PayPal: [Dukung saya di PayPal](https://paypal.me/rozhak9)

Setiap dukungan sangat berarti dan membantu untuk pengembangan alat ini ke depan. Terima kasih! 🙏

## 🙌 Kontribusi
Kontribusi sangat diterima! Silakan fork repository ini dan buat pull request atau buka issue untuk memberikan saran atau melaporkan masalah.

## 📜 Lisensi
Proyek ini dilisensikan di bawah [MIT License](https://github.com/RozhakXD/Justpaste?tab=MIT-1-ov-file) - lihat file `LICENSE` untuk lebih detail.
