 # Nhập dữ liệu
so_keo = int(input("Nhập số lượng kẹo: "))
so_nguoi = int(input("Nhập số người: "))

# Tính số kẹo mỗi người được chia
so_keo_moi_nguoi = so_keo // so_nguoi

# Tính số kẹo dư
so_keo_du = so_keo % so_nguoi

# Xuất kết quả
print("Số kẹo mỗi người được chia:", so_keo_moi_nguoi)
print("Số kẹo dư:", so_keo_du)