import math
import os
import random
import re
import sys

def matriks():
# Buka File Matrix
    with open('matriks.txt') as file:
        
# Baca File Matrix
# Split untuk Memisahkan teks dan menempatkannya kedalam sel terpisah pada baris.
        n, m = map (int, file.readline().split())

# Strip untuk menghilangkan spasi dan teks dari posisi awal dan akhir nilai data.
#ljust untuk rata kiri
        matriks = [list (file.readline().
                         strip().
                         ljust(m))

                         for i in range(n)]
        
# menggabungkan string dari setiap baris dalam matriks yang ditransposisi menjadi satu.
    
    decoded = ''.join([''.join(item) for item in zip(*matriks)])

#Mengganti karakter non-alfanumerik dengan spasi tunggal
#karakter \b untuk batasan antar kata dan [^a-zA-Z0-9] 
    print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', decoded))

matriks()