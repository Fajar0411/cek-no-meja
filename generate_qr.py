import qrcode

# Fungsi untuk membuat QR Code berdasarkan nomor meja
def create_qr_code(meja_number):
    url = f"https://sistem-pemesanan.com/meja/{meja_number}"  # URL dengan nomor meja
    qr = qrcode.make(url)  # Membuat QR Code
    qr.save(f"meja_{meja_number}.png")  # Menyimpan QR Code sebagai gambar

# Buat QR Code untuk meja 21, 25, 30, dst.
create_qr_code(21)
create_qr_code(25)
create_qr_code(30)
