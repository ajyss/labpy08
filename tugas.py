class DaftarNilaiMahasiswa:
    def __init__(self):
        # Membuat list kosong untuk menyimpan data mahasiswa
        self.data_nilai_mahasiswa = []
    
    def tambah(self, nama, nilai):
        # Menambahkan data mahasiswa baru ke dalam list
        self.data_nilai_mahasiswa.append({"nama": nama, "nilai": nilai})
        print(f"Data {nama} dengan nilai {nilai} berhasil ditambahkan.")
    
    def tampilkan(self):
        # Menampilkan daftar mahasiswa
        if not self.data_nilai_mahasiswa:
            # Jika list kosong
            print("Tidak ada data mahasiswa.")
        else:
            # Jika terdapat data mahasiswa
            print("Daftar Nilai Mahasiswa:")
            for mahasiswa in self.data_nilai_mahasiswa:
                print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
    
    def hapus(self, nama):
        # Menghapus data mahasiswa berdasarkan nama
        for i, mahasiswa in enumerate(self.data_nilai_mahasiswa):
            if mahasiswa["nama"] == nama:
                # Jika nama ditemukan, hapus data
                mahasiswa_dihapus = self.data_nilai_mahasiswa.pop(i)
                print(f"Data {mahasiswa_dihapus['nama']} dengan nilai {mahasiswa_dihapus['nilai']} berhasil dihapus.")
                return
        # Jika nama tidak ditemukan
        print(f"Tidak ditemukan data mahasiswa dengan nama {nama}.")
    
    def ubah(self, nama, nilai_baru):
        # Mengubah nilai mahasiswa berdasarkan nama
        for mahasiswa in self.data_nilai_mahasiswa:
            if mahasiswa["nama"] == nama:
                # Jika nama ditemukan, ubah nilai
                nilai_lama = mahasiswa["nilai"]
                mahasiswa["nilai"] = nilai_baru
                print(f"Data {nama} berhasil diubah. Nilai lama: {nilai_lama}, Nilai baru: {nilai_baru}.")
                return
        # Jika nama tidak ditemukan
        print(f"Tidak ditemukan data mahasiswa dengan nama {nama}.")

# Contoh penggunaan
# Membuat objek daftar nilai
daftar_nilai = DaftarNilaiMahasiswa()

# Menambahkan data mahasiswa
daftar_nilai.tambah("Muhammad Aziz Tri Ramadhan", 85)
daftar_nilai.tambah("Putra Abdullah", 92)

# Menampilkan daftar mahasiswa
daftar_nilai.tampilkan()

# Mengubah nilai mahasiswa
daftar_nilai.ubah("Muhammad Aziz Tri Ramadhan", 90)

# Menghapus data mahasiswa
daftar_nilai.hapus("Putra Abdullah")

# Menampilkan daftar mahasiswa setelah perubahan
daftar_nilai.tampilkan()