from lxml import etree

# Đọc file XML
tree = etree.parse("quanliquanan.xml")
root = tree.getroot()

# ---- Các truy vấn XPath ----
print("1. Tất cả bàn:")
for ban in root.xpath("//BAN"):
    print(etree.tostring(ban, pretty_print=True, encoding='unicode'))

print("\n2. Tất cả nhân viên:")
for nv in root.xpath("//NHANVIEN"):
    print(etree.tostring(nv, pretty_print=True, encoding='unicode'))

print("\n3. Tất cả tên món:")
print(root.xpath("//TENMON/text()"))

print("\n4. Tên nhân viên có mã NV02:")
print(root.xpath("//NHANVIEN[MANV='NV02']/TENV/text()"))

print("\n5. Tên và SDT của NV03:")
print(root.xpath("//NHANVIEN[MANV='NV03']/TENV/text()"))
print(root.xpath("//NHANVIEN[MANV='NV03']/SDT/text()"))

print("\n6. Tên món có giá > 50000:")
print(root.xpath("//MON[GIA>50000]/TENMON/text()"))

print("\n7. Số bàn của hóa đơn HD03:")
print(root.xpath("//HOADON[SOHD='HD03']/SOBAN/text()"))

print("\n8. Tên món có mã M02:")
print(root.xpath("//MON[MAMON='M02']/TENMON/text()"))

print("\n9. Ngày lập của hóa đơn HD03:")
print(root.xpath("//HOADON[SOHD='HD03']/NGAYLAP/text()"))

print("\n10. Mã món trong hóa đơn HD01:")
print(root.xpath("//HOADON[SOHD='HD01']//CTHD/MAMON/text()"))

print("\n11. Tên món trong hóa đơn HD01:")
print(root.xpath("//MON[MAMON = //HOADON[SOHD='HD01']//CTHD/MAMON]/TENMON/text()"))

print("\n12. Tên nhân viên lập hóa đơn HD02:")
print(root.xpath("//NHANVIEN[MANV = //HOADON[SOHD='HD02']/MANV]/TENV/text()"))

print("\n13. Đếm số bàn:")
print(len(root.xpath("//BAN")))

print("\n14. Đếm số hóa đơn lập bởi NV01:")
print(len(root.xpath("//HOADON[MANV='NV01']")))

print("\n15. Tên món trong hóa đơn của bàn số 2:")
print(root.xpath("//MON[MAMON = //HOADON[SOBAN=2]//CTHD/MAMON]/TENMON/text()"))

print("\n16. Nhân viên từng lập hóa đơn cho bàn số 3:")
print(root.xpath("//NHANVIEN[MANV = //HOADON[SOBAN=3]/MANV]/TENV/text()"))

print("\n17. Hóa đơn nhân viên nữ lập:")
for hd in root.xpath("//HOADON[MANV = //NHANVIEN[GIOITINH='Nữ']/MANV]"):
    print(etree.tostring(hd, pretty_print=True, encoding='unicode'))

print("\n18. Nhân viên từng phục vụ bàn số 1:")
print(root.xpath("//NHANVIEN[MANV = //HOADON[SOBAN=1]/MANV]/TENV/text()"))

print("\n19. Món được gọi nhiều hơn 1 lần:")
print(root.xpath("//MON[MAMON = //CTHD[SOLUONG>1]/MAMON]/TENMON/text()"))

print("\n20. Tên bàn + ngày lập HD02:")
tenban = root.xpath("//BAN[SOBAN = //HOADON[SOHD='HD02']/SOBAN]/TENBAN/text()")[0]
ngaylap = root.xpath("//HOADON[SOHD='HD02']/NGAYLAP/text()")[0]
print(f"{tenban} - {ngaylap}")
