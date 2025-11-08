import numpy as np

# ระบบสมการจากรูป
A = np.array([
    [2, -4, 1, -1],
    [0, 1, -3, 0],
    [1, 0, -4, 0],
    [0, 1, -1, 2]
])

b = np.array([6, 10, 0, 4])

print("เมทริกซ์ A:")
print(A)
print("\nเวกเตอร์ b:")
print(b)

# คำนวณ det(A)
det_A = np.linalg.det(A)
print(f"\ndet(A) = {det_A}")

if abs(det_A) < 1e-10:
    print("ระบบสมการไม่มีคำตอบเดียว (det(A) ≈ 0)")
else:
    print(f"det(A) = {det_A} ≠ 0, ระบบมีคำตอบเดียว")
    
    # ใช้ Cramer's Rule
    solutions = []
    for i in range(4):
        # สร้าง A_i โดยแทนคอลัมน์ที่ i ด้วย b
        A_i = A.copy()
        A_i[:, i] = b
        
        det_A_i = np.linalg.det(A_i)
        x_i = det_A_i / det_A
        solutions.append(x_i)
        
        print(f"\nA{i+1} (แทนคอลัมน์ที่ {i+1}):")
        print(A_i)
        print(f"det(A{i+1}) = {det_A_i}")
        print(f"x{i+1} = {det_A_i} / {det_A} = {x_i}")
    
    print("\n=== คำตอบสุดท้าย ===")
    for i, sol in enumerate(solutions):
        print(f"x{i+1} = {sol}")
    
    # ตรวจสอบคำตอบ
    print("\n=== ตรวจสอบคำตอบ ===")
    result = A @ np.array(solutions)
    print(f"A × [x1, x2, x3, x4] = {result}")
    print(f"ควรเท่ากับ b = {b}")
    print(f"ความแตกต่าง = {np.abs(result - b)}")