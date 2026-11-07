import tkinter as tk
from library import bmi_calculator
window= tk.Tk()
# Kích thước cửa sổ và vị trí
width = 600
heigh = 400
x= (window.winfo_screenwidth() - width) // 2
y= (window.winfo_screenheight() - heigh) // 2
window.geometry(f"{width}x{heigh}+{x}+{y}")
# Tiêu đề cửa sỏ
window.title("BMI")
# Tiêu đề ứng dụng
tk.Label(master=window, text= " Tính chỉ số sức khỏe BMI ",font=("Mono",25)).pack(pady=10)
# Chiều cao
tk.Label(master= window,text= "Chiều cao (cm) ", font=("Mono",15), anchor="w").pack(fill='x',padx=10) # anchor phía( trái, phải)

# Frame 1
frm1= tk.Frame(master= window)
frm1.pack(fill="x",padx=15)

# entry1 - nhập chiều cao
entry1= tk.Entry(master=frm1,font=("Mono",15),width= 30)
entry1.grid(column=0,row=0)

# button
button = tk.Button(master= frm1, font=("Mono",15), text="tính BMI")
button.grid(column=1,row=0)

# Cân nặng
tk.Label(master=window,text= "Cân nặng (kg)",font=("Mono",15),anchor="w").pack(fill='x',padx=10)

#Frame 2
frm2= tk.Frame(master= window)
frm2.pack(fill="x",padx=15)

# entry2 - cân nặng
entry2= tk.Entry(master=frm2,font=("Mono",15),width= 30)
entry2.grid(column=0,row=0)

# Kết quả chỉ số BMI
result1= tk.Label(master=window,text= "Chỉ số BMI: xx.x ", foreground="red", font=("Mono",20))
result1.pack(pady=15) 
tk.Label(master=window,text="Lời khuyên sức khỏe",font=("Mono",15), anchor="w").pack(fill='x',padx=10)
frm12= tk.Frame(master=window, height=80, background="#76797E")
frm12.pack(fill='x',padx=10)
frm12.pack_propagate(False)

result2 = tk.Label(master=frm12,foreground="white",font=("Mono",15),background="#76797E")
result2.pack()
# Tính chỉ số BMI và đưa ra gợi ý sức khỏe
def handle_click():
    # Bước 1: lấy giữa liệu
    try:
        heigh= float(entry1.get())
        weigh= float(entry2.get())
        if ( heigh <= 0 or weigh <= 0):
            raise Exception()
        bmi = bmi_calculator(heigh/100,weigh)
        result1.config(text=f"Chỉ số BMI: {bmi}")
        # Lời khuyên sức khỏe   
        if( bmi < 18.5):
            text= " Hơi gầy, cần ăn uống đầy đủ và luyện taaoj thêm"
        result2.config(text= text)
    except:
        result2.config(text=f"Nhập sai kiểu dữ liệu!")
# Sự kiện khi click vào nút button
button.bind("<Button-1>",lambda e: handle_click())
window.mainloop()