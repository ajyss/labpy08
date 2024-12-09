# TUGAS PRAKTIKUM 8
# Data Diri

Nama : Muhammad Aziz Tri Ramadhan

NIM : 312410380

Kelas : TI,24.A.3

# Flowchart 

<img src="flowchart.png">

# input dan outpu dari Praktikum 8

## 1. input tambah data 

<img src="input.png">

## outpu tambah data 

<img src="output.png">


1. Metode `__init__()`:
   - Inisialisasi kelas dengan membuat list kosong `student_grades` untuk menyimpan data mahasiswa

2. Metode `tambah(name, grade)`:
   - Menambahkan data mahasiswa baru ke dalam list
   - Menerima parameter nama dan nilai mahasiswa
   - Menambahkan data sebagai dictionary ke `student_grades`
   - Mencetak pesan konfirmasi penambahan data

3. Metode `tampilkan()`:
   - Menampilkan seluruh daftar mahasiswa
   - Jika list kosong, mencetak pesan "Tidak ada data mahasiswa"
   - Jika ada data, mencetak nama dan nilai setiap mahasiswa

4. Metode `hapus(name)`:
   - Menghapus data mahasiswa berdasarkan nama
   - Mencari mahasiswa dengan nama yang sesuai
   - Jika ditemukan, menghapus data dan mencetak konfirmasi
   - Jika tidak ditemukan, mencetak pesan bahwa data tidak ada

5. Metode `ubah(name, new_grade)`:
   - Mengubah nilai mahasiswa berdasarkan nama
   - Mencari mahasiswa dengan nama yang sesuai
   - Jika ditemukan, mengupdate nilai dan mencetak konfirmasi perubahan
   - Jika tidak ditemukan, mencetak pesan bahwa data tidak ada

Contoh penggunaan di akhir code menunjukkan:
- Membuat objek `grade_list`
- Menambahkan dua mahasiswa
- Menampilkan daftar
- Mengubah nilai Muhammad Aziz
- Menghapus data Putra Abdullah
- Menampilkan daftar terakhir

