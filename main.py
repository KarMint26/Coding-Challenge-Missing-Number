# buat fungsi untuk menyelesaikan masalah missing number
def solution(n, list_n):
    # Inisialisasi variable untuk dikembalikan sebagai jawaban
    ans = 0;
    
    # Tentukan terlebih dahulu sum atau hasil jumlah seluruh element di list_n
    sum_list_n = 0;
    for i in list_n:
        sum_list_n += i
    
    # Mencari keseluruhan (sum) hasil jumlah elementnya jika seluruh number atau angka tidak hilang
    sum_list_all = n * (n+1) / 2 # ini merupakan rumus untuk mencarinya
    
    # Menentukan jawabannya dengan melakukan operasi pengurangan sum_list_all dengan sum_list_n
    # karena pasti selisih angka merupakan angka yang hilang atau missing number
    ans = sum_list_all - sum_list_n
    
    # Mengembalikan value dari variable ans
    return ans;
    
# Membuat input yang akan digunakan oleh pengguna untuk mencari angka yang hilang
# Inisialisasi variable N dan List dari N yang akan dimasukan ke dalam function

# Meminta input pertama untuk N
N = int(input("Masukkan nilai N: "))
print("Masukkan angka-angka (kecuali satu angka yang hilang) dipisahkan oleh spasi:")

# Meminta input dengan angka-angka yang dipisahkan oleh spasi
list_n = list(map(int, input().split()))

# Simpan hasil ke variable result
result = int(solution(N, list_n)) # ubah ke integer
print(f"Output Missing Number: {result}")
