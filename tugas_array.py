import array as arr
print("NO 1")
# 1. Ilham memiliki sebuah list yang berisi angka-angka acak. Anda ingin menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0, dan akan mengurutkan dari nilai yang terbesar ke yang terkecil. Bantu Ilham untuk menyelesaikan persoalan tersebut menggunakan array method.
# Input: [8, 3, 12, 4, 7, 2]
# Output: [12, 8, 7, 4, 0, 0]
arr = [8, 3, 12, 4, 7, 2]
output_arr = []
# menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0
for i in arr:
    if i <= 5:
        output_arr.append(0)
    else:
        output_arr.append(i)
# mengurutkan dari nilai yang terbesar ke yang terkecil
output_arr.sort(reverse=True)
print(output_arr)  

print("NO 2")
# 2.Budi memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang merupakan bilangan ganjil dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Bantu budi untuk menyelesaikan persoalan tersebut menggunakan array method.
# Input: [7, 4, 9, 2, 5, 1]
# Output: [2, 4]

arr = [7, 4, 9, 2, 5, 1]
output_arr = []
# menghapus semua nilai yang merupakan bilangan ganjil dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar
for i in arr:
    if i % 2 == 0:
        output_arr.append(i)

output_arr.sort()
print(output_arr)

print("NO 3")
# 3.Rani memiliki sebuah list yang berisi buah-buahan. Dia ingin menghapus semua kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut secara alfabetis. Bantulah Rani untuk mencapai ini.
# Input: kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
# Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
output = []
# menghapus semua kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut secara alfabetis
for i in kata:
    if len(i) >= 5:
        output.append(i)

output.sort()
print(output)

print("NO 4")
# 4.Dewi memiliki dua list yang berisi nama-nama buah-buahan. Dia ingin menggabungkan kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama. Setelah itu, dia ingin mengurutkan sisa buah-buahan secara alfabetis. Bantu Dewi
# Input: ["apel", "jeruk", "mangga"], ["apel", "anggur", "nanas"]
# Output: ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']

list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "anggur", "nanas"]
# menggabungkan kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama, mengurutkan sisa buah-buahan secara alfabetis.
hasil = sorted(set(list1 + list2))
print(hasil)

print("NO 5")
# 5.Dina memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang kurang dari 10 dan lebih dari 100, dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Implementasikan ini dengan menggunakan metode-metode yang tepat dari list.
# Input: [105, 20, 8, 150, 30, 5, 200]
# Output: [20, 30]
input_arr = [105, 20, 8, 150, 30, 5, 200]
output_arr = []
# menghapus semua nilai yang kurang dari 10 dan lebih dari 100
for i in input_arr:
    if 10 <= i <= 100:
        output_arr.append(i)

# mengurutkan sisa nilai tersebut dari terkecil ke terbesar
output_arr.sort()
print(output_arr)

