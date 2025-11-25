import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        
        if height > 3: 
            height = height / 100
        
        bmi = weight / (height ** 2)  
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter your height (in meters):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

tk.Label(root, text="Enter your weight (in kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
