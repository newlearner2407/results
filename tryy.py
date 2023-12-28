# ... (your existing code)

def calculate_result(marks):
    # Modify this function based on your passing criteria
    passing_marks = 40
    return "Pass" if marks >= passing_marks else "Fail"

def display_results():
    # ... (your existing code)

    # Create the main window
    root = tk.Tk()
    root.title("Student Records")

    # Create a Treeview widget
    tree = ttk.Treeview(root)
    tree["columns"] = ("Full Name", "Branch", "From Year", "To Year",
                       "Subject 01", "Subject 02", "Subject 03", "Subject 04", "Subject 05", "Result")

    # Define column headings
    tree.heading("#0", text="Student ID")
    tree.heading("Full Name", text="Full Name")
    tree.heading("Branch", text="Branch")
    tree.heading("From Year", text="From Year")
    tree.heading("To Year", text="To Year")
    tree.heading("Subject 01", text="Subject 01")
    tree.heading("Subject 02", text="Subject 02")
    tree.heading("Subject 03", text="Subject 03")
    tree.heading("Subject 04", text="Subject 04")
    tree.heading("Subject 05", text="Subject 05")
    tree.heading("Result", text="Result")

    # Populate the Treeview with data
    for student in students:
        # Calculate total marks
        total_marks = sum(int(student[i]) for i in range(7, 12))
        result = calculate_result(total_marks)

        tree.insert("", "end", text=student[2], values=(student[1], student[4], student[5],
                                                         student[6], student[7], student[8], student[9],
                                                         student[10], student[11], result))

    # Pack the Treeview widget
    tree.pack(expand=True, fill="both")

    # Run the Tkinter main loop
    root.mainloop()

# ... (your existing code)
