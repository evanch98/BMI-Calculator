from tkinter import Tk, ttk, END

root = Tk()
root.geometry('300x150')
root.title('BMI Calculator')
root.resizable(0, 0)
root.wm_iconbitmap('BMI.ico')


# Grid Configuration
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=2)

# Weight Lable
weight_label = ttk.Label(root, text='Weight(kg)')
weight_label.grid(row=0, column=0, padx=5, pady=5)

# Weight Entry
weight_entry = ttk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

# Height Label
height_label = ttk.Label(root, text='Height(m)')
height_label.grid(row=1, column=0, padx=5, pady=5)

# Height Entry
height_entry = ttk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# BMI Label
bmi_label = ttk.Label(root, text='Your BMI')
bmi_label.grid(row=2, column=0, padx=5, pady=5)

# BMI Entry
bmi_entry = ttk.Entry(root)
bmi_entry.grid(row=2, column=1, padx=5, pady=5)

def calculate():
    """BMI = Weight / (Height ** 2)"""
    weight = weight_entry.get()
    height = height_entry.get()
    try:
        bmi = float(weight) / (float(height) ** 2)
        bmi_index = ['Underweight', 'Normal Weight', 'Overweight', 'Obese']
        if bmi < 18.5:
            text= f'{bmi:.2f} ({bmi_index[0]})'
            bmi_entry.delete(0, END)
            bmi_entry.insert(0, text)
        elif bmi > 24.9:
            text = f'{bmi:.2f} ({bmi_index[2]})'
            bmi_entry.delete(0, END)
            bmi_entry.insert(0, text)
        elif bmi > 30:
            text = f'{bmi:.2f} ({bmi_index[3]})'
            bmi_entry.delete(0, END)
            bmi_entry.insert(0, text)
        else:
            text = f'{bmi:.2f} ({bmi_index[1]})'
            bmi_entry.delete(0, END)
            bmi_entry.insert(0, text)
    except ValueError:
        bmi_entry.delete(0, END)
        bmi_entry.insert(0, "Invalid value.")
    except ZeroDivisionError:
        bmi_entry.delete(0, END)
        bmi_entry.insert(0, "Height cannot be zero.")

def clear():
    """Clears the text in the entry boxes."""
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    bmi_entry.delete(0, END)

# Calculate Button
cal_button = ttk.Button(root, text='Calculate', command=calculate)
cal_button.place(x=70, y=110)

# Clear Button
clear_button = ttk.Button(root, text='Clear', command=clear)
clear_button.place(x=160, y=110)

root.mainloop()
