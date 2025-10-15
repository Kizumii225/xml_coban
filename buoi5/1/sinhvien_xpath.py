from lxml import etree

# Đọc file XML
tree = etree.parse("sinhvien.xml")
root = tree.getroot()

# --- Thực thi các truy vấn XPath ---

print("1 Tất cả sinh viên:")
students = root.xpath("//student")
for s in students:
    print(etree.tostring(s, pretty_print=True, encoding='unicode'))

print("\n2 Tên tất cả sinh viên:")
print(root.xpath("//student/name/text()"))

print("\n3 Tất cả ID sinh viên:")
print(root.xpath("//student/id/text()"))

print("\n4 Ngày sinh của SV01:")
print(root.xpath("//student[id='SV01']/date/text()"))

print("\n5 Các khóa học:")
print(root.xpath("//enrollment/course/text()"))

print("\n6 Thông tin sinh viên đầu tiên:")
print(etree.tostring(root.xpath('//student[1]')[0], pretty_print=True, encoding='unicode'))

print("\n7 Mã sinh viên học Vatly203:")
print(root.xpath("//enrollment[course='Vatly203']/studentRef/text()"))

print("\n8 Tên sinh viên học Toan101:")
print(root.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name/text()"))

print("\n9 Tên sinh viên học Vatly203:")
print(root.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()"))

print("\n10 Sinh viên sinh năm 1997:")
print(root.xpath("//student[starts-with(date,'1997')]/name/text()"))

print("\n11 Sinh viên sinh trước năm 1998:")
print(root.xpath("//student[number(substring(date,1,4)) < 1998]/name/text()"))

print("\n12 Tổng số sinh viên:")
print(int(root.xpath("count(//student)")))

print("\n13 <date> ngay sau <name> của SV01:")
print(root.xpath("//student[id='SV01']/name/following-sibling::date/text()"))

print("\n14 <id> ngay trước <name> của SV02:")
print(root.xpath("//student[id='SV02']/name/preceding-sibling::id/text()"))

print("\n15 course cùng enrollment với SV03:")
print(root.xpath("//enrollment[studentRef='SV03']/course/text()"))

print("\n16 Sinh viên có họ 'Trần':")
print(root.xpath("//student[starts-with(name,'Trần')]/name/text()"))

print("\n17 Năm sinh SV01:")
print(root.xpath("substring(//student[id='SV01']/date,1,4)"))
