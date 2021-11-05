from tkinter import *

root = Tk()

root.title("license card")
root.geometry("300x400")

root.configure(bg="white")
canvas=Canvas(root,width=300,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150,90, font=('Comic', '24', 'bold italic') ,text="Identity Card")
label_name_tag = canvas.create_text(40,165, font=('Comic', '16', 'bold') ,text="Name :")
label_grade_tag = canvas.create_text(40,205, font=('Comic', '16', 'bold') ,text="Grade :")
label_hobbies_tag = canvas.create_text(50,250, font=('Comic', '16', 'bold') ,text="Hobbies :")

label_name = Label(root)
label_grade = Label(root)
label_hobbies = Label(root)

def myCardDetails():
    name = "naruto"
    print(type(name))  
    grade = 12
    print(type(grade))
    hobbies = ["Ninja art","Driving learner"]
    print(type(hobbies))
   
    label_name['text'] = name
    label_grade['text'] = grade
    label_hobbies['text'] = hobbies
   
   
button1 = Button(root, text = "Show my Driver Licens", command=myCardDetails)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=label_grade)
label_hobbies_window = canvas.create_window(155, 252, anchor=CENTER, window=label_hobbies)
canvas.pack()

root.mainloop()
