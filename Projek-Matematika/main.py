from matematika import persegi, lingkaran
from matematika.bangun_ruang import kubus as kbs
from matematika.bangun_ruang import bola

sisi = 5
r = 7

# Persegi
print("Luas Persegi:", persegi.luas_persegi(sisi))
print("Keliling Persegi:", persegi.keliling_persegi(sisi))

# Lingkaran
print("Luas Lingkaran:", round(lingkaran.luas_lingkaran(r), 2))
print("Keliling Lingkaran:", round(lingkaran.keliling_lingkaran(r), 2))

# Kubus
print("Volume Kubus:", kbs.volume_kubus(sisi))
print("Luas Permukaan Kubus:", kbs.luas_permukaan_kubus(sisi))

# Bola
print("Volume Bola:", round(bola.volume_bola(r), 2))
print("Luas Permukaan Bola:", round(bola.luas_permukaan_bola(r), 2))
