class StudentGradeList:
    def __init__(self):
        self.student_grades = []

    def tambah(self, name, grade):
        self.student_grades.append({"name": name, "grade": grade})
        print(f"Data {name} dengan nilai {grade} berhasil ditambahkan.")

    def tampilkan(self):
        if not self.student_grades:
            print("Tidak ada data mahasiswa.")
        else:
            print("Daftar Nilai Mahasiswa:")
            for student in self.student_grades:
                print(f"Nama: {student['name']}, Nilai: {student['grade']}")

    def hapus(self, name):
        for i, student in enumerate(self.student_grades):
            if student["name"] == name:
                removed_student = self.student_grades.pop(i)
                print(f"Data {removed_student['name']} dengan nilai {removed_student['grade']} berhasil dihapus.")
                return
        print(f"Tidak ditemukan data mahasiswa dengan nama {name}.")

    def ubah(self, name, new_grade):
        for student in self.student_grades:
            if student["name"] == name:
                old_grade = student["grade"]
                student["grade"] = new_grade
                print(f"Data {name} berhasil diubah. Nilai lama: {old_grade}, Nilai baru: {new_grade}.")
                return
        print(f"Tidak ditemukan data mahasiswa dengan nama {name}.")

# Contoh penggunaan
grade_list = StudentGradeList()
grade_list.tambah("Muhammad Aziz Tri Ramadhan", 85)
grade_list.tambah("Putra Abdullah", 92)
grade_list.tampilkan()
grade_list.ubah("Muhammad Aziz Tri Ramadhan", 90)
grade_list.hapus("Putra Abdullah")
grade_list.tampilkan()