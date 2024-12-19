Rut Naomi Ester Sitompul
F55123057
TIB

Analisis untuk quis 2 (Naive & Qonquer)
NAIVE:
Pada program Naive bayes ini menggunakan Bubble sort untuk mensorting data yang ada. Dalam hal ini yaitu:

1. Best Case, yang dilakukan ketika data sudah terurut (ascending), di mana algoritma hanya perlu melakukan satu iterasi melalui array tanpa adanya pertukaran elemen. Pada kondisi ini kompleksitas waktunya menjadi O(n), karena hanya membutuhkan O(𝑛) n−1 perbandingan (melakukan 1 iterasi tanpa adanya swap).
2. Worst Case terjadi ketika data dalam urutan terbalik, kompleksitas menjadi 𝑂(𝑛2), ini dikarenakan algoritma tersebut membutuhkan hingga n(n-1)/2 operasi perbandingan dan pertukaran untuk dapat menyelesaikan sorting. Karena hal inilah bubble sort cenderung lambat untuk dataset yang besar yang mana sifatnya tidak efisien.

QONQUER:
Pada program qonquer.py menggunakan Quick sort untuk mensorting data yang ada. Dalam hal ini yakni:

1.  Best case untuk Quick Sort terjadi ketika pivot selalu membagi array menjadi dua bagian yang hampir sama besar, menghasilkan kompleksitas waktu O(nlogn). Pada bagian ini juga hjumlah pembagian atau elevel rekursinya adalah log n, dan setiap levelnya melakukan sorting sebanyak n.
2.  Worst case terjadi ketika pivot selalu menjadi elemen terkecil atau terbesar, kompleksitas menjadi O(n2) yang mana hal ini dapat terjadi karena algoritma yang bekerja serupa dengan iterasi linear dalam rekursi. Meski demikian, Quick sort ini biasanya lebih cepat dibandingkan dengan Bubble sort terlebih pada dataset yang besar.

Maka dalam hal ini dapat disimpulkan bahwa Quick sort memiliki kelebihan dalam kecepatan pada banyak skenario karena kompleksitas rata-rata yaitu O(n log n), sementara untuk Bubble sort ini terbatas untuk dataset kecil atau saat data sudah terurut. Bubble sort lebih baik untuk implementasi sederhana, sedangkan untuk dataset yang cukup besar atau acak Quick sort bisa menjadi pilihan yang baik.
