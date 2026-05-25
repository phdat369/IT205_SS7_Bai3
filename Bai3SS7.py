# Phân tích 
# Đầu tiên chúng ta cần tạo 1 menu với gồm 4 chức năng như đề bài cho 
# Ở chức năng đầu tiên thì chúng ta chỉ cần in ra chuỗi gốc là print(raw_data) 
# Ở chức năng thứ 2 thì chúng ta cần tách từng nhân viên 
# Ở đây chúng ta thấy các nhân viên đang cách nhau bởi dấu "|" vì thế chúng ta cần dùng split để cắt ra 
# Và các trường thông tin đang cách nhau bởi dấu ";"
# Để id và phòng ban viết hoa toàn bộ thì dùng upper để nó in hoa hết tất cảư 
# Họ tên thì chúng ta dùng title 
# Ở số điện thoại có dấu trừ thì chúng ta phải cắt chuỗi sau đó mới nối lại thì nó sẽ mất dấu trừ 
# Nếu số điện thoại mà toàn chữ số thì chúng ta sẽ tạo ra 1 biến gồm 6 dấu "*" sau đó chúng ta dùng nối dựa trên vị trí 
# Còn mà có chữ cái thì chúng ta sẽ in ra lỗi 
# Còn chức năng 3 thì chúng ta tìm kiếm dựa trên id, trước khi tìm kiếm thì chúng ta cần xóa khoảng trắng, chuyển về chữ hoa 
# Và cuối cùng là kết thúc chương trình là break ra khỏi vòng lặp và kết thúc chương trình 

# Viết code
raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ;0988abc123 ; IT "
while True:
    choose = int(input("""=== HỆ THỐNG QUẢN LÝ NHÂN SỰ ===
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa dữ liệu và in báo cáo
3. Tìm kiếm nhân viên theo mã ID
4. Thoát chương trình
Nhập lựa chọn của bạn: """))
    match choose:
        case 1:
            print(raw_data)
        case 2:
            all_employee = raw_data.strip().split(" | ")
            print()
            print("                            === BẢNG BÁO CÁO ===")
            print("=" * 80)
            print(f"{'ID': <10} {'Họ và tên': <30} {'Phòng ban': <20} {'Số điện thoại': <10}")
            for employee in all_employee:
                info_employee = employee.strip().split(";")
                id_employee = info_employee[0].upper()
                name_employee = info_employee[1].title()
                department = info_employee[3].upper()
                phone_number = info_employee[2]
                if "-" in phone_number:
                    phone_number = phone_number.replace("-", "")
                elif phone_number.isdigit():
                    phone_number = '*'*6 + phone_number[6:]
                else:
                    phone_number = "Invalid Format"  
                print(f"{id_employee: <10} {name_employee: <30} {phone_number: <20} {department: <10}")
                print("=" * 80)
                print()
        case 3:
            search_id = input("Nhập id cần tìm kiếm: ")
            all_employee = raw_data.strip().split(" | ")
            count = 0
            for employee in all_employee:
                info_employee = employee.strip().split(";")
                id_employee = info_employee[0].lower()
                if id_employee == search_id.lower():
                    print()
                    print("                            === BẢNG BÁO CÁO ===")
                    print("=" * 80)
                    print(f"{'ID': <10} {'Họ và tên': <30} {'Phòng ban': <20} {'Số điện thoại': <10}")
                    id_employee = info_employee[0].upper()
                    name_employee = info_employee[1].title()
                    department = info_employee[3].upper()
                    phone_number = info_employee[2]
                    if "-" in phone_number:
                        phone_number = phone_number.replace("-", "")
                    elif phone_number.isdigit():
                        phone_number = '*'*6 + phone_number[6:]
                    else:
                        phone_number = "Invalid Format"  
                    print(f"{id_employee: <10} {name_employee: <30} {phone_number: <20} {department: <10}")
                    print("=" * 80)
                    print()
                    count += 1
            if count == 0: 
                print("Không tìm thấy nhân viên")
        case 4:
            break
        case _:
            print("Lựa chọn không hợp lệ")
print("=== CHƯƠNG TRÌNH KẾT THÚC ===")
