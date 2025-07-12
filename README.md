# Sistem Pemesanan Lapangan Badminton Majujaya

Proyek ini adalah aplikasi konsol sederhana yang dibuat dengan Python untuk mengelola pemesanan lapangan badminton. Aplikasi ini memungkinkan pengguna untuk melihat jadwal yang tersedia, melakukan pemesanan, dan mencetak struk sebagai bukti transaksi.

## Fitur Utama

- **Pemesanan Interaktif**: Pengguna dapat memesan salah satu dari dua lapangan yang tersedia untuk hari dan jam tertentu.
- **Tampilan Jadwal**: Menampilkan jadwal yang sudah terisi untuk setiap lapangan, membantu pengguna memilih waktu yang kosong.
- **Validasi Otomatis**: Sistem secara otomatis memeriksa ketersediaan jadwal untuk mencegah tumpang tindih pemesanan.
- **Kalkulasi Biaya**: Biaya sewa dihitung secara otomatis berdasarkan durasi pemakaian (Rp 30.000 per jam).
- **Cetak Struk**: Setelah pembayaran berhasil, sistem akan mencetak struk digital yang berisi detail pemesanan.

## Cara Menjalankan Proyek

1.  Pastikan Anda memiliki Python 3 terinstal di komputer Anda.
2.  Simpan kode dari file [`Pemesanan lapangan badminton.py`]
3.  Buka terminal atau command prompt, navigasikan ke direktori tempat Anda menyimpan file tersebut.
4.  Jalankan skrip dengan perintah berikut:

    ````sh
    python "Pemesanan lapangan badminton.py"
    ````

5.  Ikuti instruksi yang ditampilkan di menu untuk memesan lapangan atau melihat jadwal.

## Struktur Kode

Kode ini terstruktur di dalam kelas `LapanganBadminton` yang mengelola semua logika untuk satu lapangan.

-   [`LapanganBadminton`](/c:/Users/fachri/Documents/Python/Pemesanan%20lapangan%20badminton.py#L2): Kelas utama yang merepresentasikan sebuah lapangan badminton.
-   [`pesan_jadwal()`](/c:/Users/fachri/Documents/Python/Pemesanan%20lapangan%20badminton.py#L8): Fungsi untuk memproses pemesanan baru, mulai dari validasi input, pengecekan jadwal, hingga proses pembayaran.
-   [`is_jadwal_available()`](/c:/Users/fachri/Documents/Python/Pemesanan%20lapangan%20badminton.py#L38): Memeriksa apakah slot waktu yang diminta masih tersedia.
-   [`tampilkan_jadwal()`](/c:/Users/fachri/Documents/Python/Pemesanan%20lapangan%20badminton.py#L63): Menampilkan semua jadwal yang telah dipesan untuk lapangan tersebut.
-   [`cetak_struk()`](/c:/Users/fachri/Documents/Python/Pemesanan%20lapangan%20badminton.py#L52): Mencetak struk pemesanan setelah transaksi berhasil.

Di luar kelas,
