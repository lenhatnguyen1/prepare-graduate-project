# Import Libraries
import math
import tkinter as tk
from tkinter import messagebox

# Declare the constant (the long of robot arm)
L1 = 150
L2 = 100


# Function to calculate the inverse kinematic
def inverse_kinematics(x, y, z):
    r = math.hypot(math.hypot(x, y), (z + 50))
    if r > L1 + L2:
        raise ValueError("Target position is out of reach")

    phi = math.atan2(math.hypot(x, y), (z + 50))
    theta1 = math.atan2(y, x)
    theta2 = math.acos((r * r + L1 * L1 - L2 * L2) / (2 * r * L1)) - phi
    theta3 = math.acos((L1 * L1 + L2 * L2 - r * r) / (2 * L1 * L2)) - math.pi
    return theta1, theta2, theta3


# Function to display the joint angles
def display_angles():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        z = float(entry_z.get())
        result = inverse_kinematics(x, y, z)
        theta1, theta2, theta3 = result
        # Display the result in degrees on the app
        label_result.config(
            text=f"Theta1: {round(math.degrees(theta1), 3)}°\nTheta2: {round(math.degrees(theta2), 3)}°\nTheta3: {round(math.degrees(theta3), 3)}°")
    except ValueError as e:
        messagebox.showerror("Error", e)
    except ZeroDivisionError as e:
        messagebox.showerror("Error", "Division by zero occurred")
    except Exception as e:
        messagebox.showerror("Error", "Something went wrong")


# Create a GUI window
window = tk.Tk()
window.title("Inverse Kinematics")
window.geometry("300x250")

# Create labels and entries for x, y, z coordinates
label_x = tk.Label(window, text="Enter x:")
label_x.grid(row=0, column=0, padx=10, pady=10)
entry_x = tk.Entry(window)
entry_x.grid(row=0, column=1, padx=10, pady=10)

label_y = tk.Label(window, text="Enter y:")
label_y.grid(row=1, column=0, padx=10, pady=10)
entry_y = tk.Entry(window)
entry_y.grid(row=1, column=1, padx=10, pady=10)

label_z = tk.Label(window, text="Enter z:")
label_z.grid(row=2, column=0, padx=10, pady=10)
entry_z = tk.Entry(window)
entry_z.grid(row=2, column=1, padx=10, pady=10)

# Create a button to calculate the joint angles
button_calc = tk.Button(window, text="Calculate", command=display_angles)
button_calc.grid(row=3, columnspan=2, padx=10, pady=10)

# Create a label to display the result
label_result = tk.Label(window)
label_result.grid(row=4, columnspan=2)

# Start the main loop of the window
window.mainloop()
