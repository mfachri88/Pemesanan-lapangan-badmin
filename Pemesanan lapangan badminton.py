class LapanganBadminton:
    def __init__(self, nama_lapangan):
        # Inisialisasi objek LapanganBadminton dengan nama lapangan dan jadwal kosong
        self.nama_lapangan = nama_lapangan
        self.jadwal = {hari: {} for hari in ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']}

    def pesan_jadwal(self, hari, nama, jam_mulai, jam_selesai):
        # Fungsi untuk memesan jadwal lapangan
        # Memeriksa validitas input dan ketersediaan jadwal
        # Menghitung total biaya, menerima pembayaran, dan mencetak struk
        if hari not in self.jadwal or not (7 <= jam_mulai < jam_selesai <= 21):
            print("Input tidak valid.")
            return

        if not self.is_jadwal_available(hari, jam_mulai, jam_selesai):
            print("\nMaaf jadwal sudah terisi. Silakan pesan ulang.")
            return

        harga = self.hitung_harga(jam_mulai, jam_selesai)
        print(f"Total biaya: Rp {harga:,}")

        uang_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
        kembalian = uang_bayar - harga

        if kembalian < 0:
            print("\nMaaf uang yang dibayarkan kurang. Pemesanan dibatalkan.")
            return
        else:
            self.jadwal[hari][(jam_mulai, jam_selesai)] = {'nama': nama, 'harga': harga, 'lunas': True}
            print("Pemesanan berhasil. Terima kasih!")

            # Cetak struk
            self.cetak_struk(hari, jam_mulai, jam_selesai, harga, 'Lunas', uang_bayar, kembalian)

    def is_jadwal_available(self, hari, jam_mulai, jam_selesai):
        # Fungsi untuk memeriksa ketersediaan jadwal pada hari tertentu
        for jadwal in self.jadwal[hari]:
            if not (jam_mulai >= jadwal[1] or jam_selesai <= jadwal[0]):
                return False
        return True

    def hitung_harga(self, jam_mulai, jam_selesai):
        # Fungsi untuk menghitung total biaya berdasarkan lama bermain
        lama_bermain = jam_selesai - jam_mulai
        return lama_bermain * 30000

    def cetak_struk(self, hari, jam_mulai, jam_selesai, total_harga, status_pembayaran, uang_bayar, kembalian):
        # Fungsi untuk mencetak struk pemesanan
        print("\n========== Struk Pemesanan ==========")
        print(f"Lapangan: {self.nama_lapangan}")
        print(f"Hari: {hari}")
        print(f"Jam: {jam_mulai:02d}:00 - {jam_selesai:02d}:00")
        print(f"Total Harga: Rp {total_harga:,}")
        print(f"Status Pembayaran: {status_pembayaran}")
        print(f"Uang Bayar: Rp {uang_bayar:,}")
        print(f"Kembalian: Rp {kembalian:,}")
        print("=======================================")

    def tampilkan_jadwal(self):
        # Fungsi untuk menampilkan jadwal lapangan
        for hari in self.jadwal:
            if self.jadwal[hari]:
                print(f"\nJadwal lapangan {self.nama_lapangan} pada hari {hari}:")
                for jadwal, info in self.jadwal[hari].items():
                    jam_mulai, jam_selesai = jadwal
                    status_pembayaran = "Lunas" if info.get('lunas') else ""
                    print(f"{hari} | Nama: {info['nama']}   | Jam: {jam_mulai:02d}.00 - {jam_selesai:02d}.00   | Harga: Rp {info['harga']:,}   | Status: {status_pembayaran}")


# objek LapanganBadminton
lapangan1 = LapanganBadminton("Lapangan 1")
lapangan2 = LapanganBadminton("Lapangan 2")

# Input manual
while True:
    print(  ''' 
    =======================================================
    |                                                     |
    | SELF-SERVICE PEMESANAN LAPANGAN BADMINTON MAJUJAYA  |
    |                                                     |
    ======================================================= 
        ''')
    print("1. Tampilkan Jadwal")
    print("2. Pesan Lapangan 1")
    print("3. Pesan Lapangan 2")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")
    print("\n")
    if pilihan == '2' or pilihan == '3':
        hari = input("Masukkan hari (Senin-Minggu): ")
        nama = input("Masukkan nama: ")
        jam_mulai = int(input("Masukkan jam mulai (7-21): "))
        jam_selesai = int(input("Masukkan jam selesai (7-21): "))
        if pilihan == '2':
            lapangan1.pesan_jadwal(hari, nama, jam_mulai, jam_selesai)
        else:
            lapangan2.pesan_jadwal(hari, nama, jam_mulai, jam_selesai)
    elif pilihan == '1':
        lapangan1.tampilkan_jadwal()
        lapangan2.tampilkan_jadwal()
    elif pilihan == '4':
        print("Terima kasih. Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")