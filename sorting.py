# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Data
X = [1, 5, 6, 4, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Sorting
sorted_merge = merge_sort(X)
sorted_quick = quick_sort(X)

print("Hasil Merge Sort:", sorted_merge)
print("Hasil Quick Sort:", sorted_quick)


# ANALISIS UNTUK MERGE SORT

# Merge sort adalah algoritma pengurutan yang bekerja dengan cara membagi data menjadi dua bagian yang lebih kecil sampai hanya tersisa satu elemen, lalu menggabungkan kembali bagian-bagian kecil tersebut dalam urutan yang terurut.
# Untuk kode ini menggunakan pendekatan divide and conquer (pecah data menjadi bagian kecil, lalu gabungkan).
# Fungsi merge_sort membagi array menjadi dua bagian dengan indeks tengah (mid).
# Fungsi merge menggabungkan dua bagian kecil dengan membandingkan elemen dari kiri dan kanan, memastikan hasil penggabungan tetap terurut.
# - Worst case-nya, yang mana waktu dibutuhkan tetap O(n log n), karena algoritma ini selalu memecah dan menggabungkan data dengan cara yang sama, tanpa mempedulikan data yang teracak.TabError
# - Best case-nya, ini juga sama yaitu O(n log n), dikarenakan jumlah angkanya tidak berubah meskipun data tersebut sudah terurut.
# - Avarage case (rata-rata), tetap O(n log n), karena cara algoritma bekerja tidak bergantung pada pengurutan awal data.
# Jadi secara keseluruhan Merge Sort selalu konsisten dan cocok untuk kasus yang membutuhkan stabilitas tinggi (elemen dengan nilai sama tetap dalam urutan yang sama). 

# ANALASIS UNTUK QUICT SORT

# Quick Sort adalah algoritma pengurutan yang memilih satu elemen dari data (disebut pivot) dan memisahkan data lainnya menjadi dua kelompok
# Pada kode ini, memilih elemen pivot di tengah array, kemudian data yang ada dibagi menjadi tiga bagian yaitu left (lebih kecil), middle (sama dengan pivot), right (lebih besar dari pivot). 
# Untuk itu adapun analisa kompleksitas dari quick sort ini adalah:
# - Worst case, di mana jika pivotnya selalu dipilih secara tidak optimal, kompleksitasnya O(n2) karena setiap kali hanya satu elemen diproses di satu sisi.
# - Best case,  jika pivot membagi data menjadi dua bagian yang hampir sama besar di setiap langkah, sehingga kompleksitasnya adalah O(n log n)
# - Avarage case, jika secara statistik pivot akan membagi data cukup merata, sehingga kompleksitas rata-rata adalah O(nlogn).

# Setiap algoritma di atas pastinya memiliki karakteristik dan kompleksitas yang tepat sesua dengan cara kerja kode tersebut.