import tkinter as tk

# Function to calculate grade
def calculate_grade():
    try:
        m1 = int(entry1.get())
        m2 = int(entry2.get())
        m3 = int(entry3.get())

        total = m1 + m2 + m3
        avg = total / 3

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 50:
            grade = "C"
        else:
            grade = "Fail"

        result_label.config(
            text=f"Total: {total} | Avg: {avg:.2f} | Grade: {grade}"
        )

    except ValueError:
        result_label.config(text="Enter valid numbers!")

# Main window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("350x250")

# Title
tk.Label(root, text="Grade Calculator", font=("Arial", 16)).pack(pady=10)

# Input fields
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Subject 1").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

tk.Label(frame, text="Subject 2").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)

tk.Label(frame, text="Subject 3").grid(row=2, column=0, padx=5, pady=5)
entry3 = tk.Entry(frame)
entry3.grid(row=2, column=1)

# Button
tk.Button(root, text="Calculate", command=calculate_grade, bg="lightblue").pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()