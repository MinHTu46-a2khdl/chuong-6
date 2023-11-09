# Nhập dữ liệu
so_tien_gui = int(input("Nhập số tiền gửi: "))
lai_suat = float(input("Nhập lãi suất: "))
so_thang_gui = int(input("Nhập số tháng gửi: "))

# Tính tiền lãi
tien_lai = so_tien_gui * lai_suat * so_thang_gui / 12

# Tính tổng số tiền nhận được
tong_so_tien = so_tien_gui + tien_lai

# Xuất kết quả
print("Tiền lãi:", tien_lai)
print("Tổng số tiền nhận được:", tong_so_tien)