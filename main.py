from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(400, 300)
window.config(padx=30, pady=30)
window.config(padx=30, pady=30, bg="#fce4ec")

# Determines the BMI category based on the calculated value.
def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "Severely Underweight!"
        result_label.config(fg="blue")
    elif 16 < bmi <= 17:
        result_string += "Moderately Underweight!"
        result_label.config(fg="blue")
    elif 17 < bmi <= 18.5:
        result_string += "Mildly Underweight!"
        result_label.config(fg="green")
    elif 18.5 < bmi <= 25:
        result_string += "Healthy Weight"
        result_label.config(fg="green")
    elif 25 < bmi <= 30:
        result_string += "Pre-obese"
        result_label.config(fg="orange")
    elif 30 < bmi <= 35:
        result_string += "Obesity Class 1"
        result_label.config(fg="orange")
    elif 35 < bmi <= 40:
        result_string += "Obesity Class 2"
        result_label.config(fg="red")
    else:
        result_string += "Obesity Class 3"
        result_label.config(fg="red")
    return result_string

# Gets user input, calculates BMI, and handles possible errors.
def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except ValueError:
            result_label.config(text="Enter a valid number!")


weight_labels= Label(window, text="Enter Your Weight (kg) : ")
weight_labels.pack(pady=(50, 0))
weight_input= Entry(width=20)
weight_input.pack(pady=(10, 0))

height_labels= Label(window, text="Enter Your Height (cm) : ")
height_labels.pack(pady=(40, 0))
height_input= Entry(width=20)
height_input.pack(pady=(10, 0))

calculate_button = Button(window, text="Calculate", command=calculate_bmi)
calculate_button.pack(pady=(10, 10))

result_label = Label(window, text="")
result_label.pack(pady=20)




window.mainloop()