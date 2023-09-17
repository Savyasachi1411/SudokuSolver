#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def is_valid(board, row, col, num):
    # Check if 'num' is already in the current row, column, or 3x3 grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def solve_sudoku():
    board = [[grid[i][j].get() for j in range(9)] for i in range(9)]
    
    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == "":
                    for num in map(str, range(1, 10)):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            grid[row][col].delete(0, 'end')
                            grid[row][col].insert(0, num)
                            if solve():
                                return True
                            board[row][col] = ""
                            grid[row][col].delete(0, 'end')
                    return False
        return True

    if solve():
        messagebox.showinfo("Solved!", "Sudoku puzzle has been solved.")
    else:
        messagebox.showinfo("No Solution", "The Sudoku puzzle has no valid solution.")

def clear_grid():
    for i in range(9):
        for j in range(9):
            grid[i][j].delete(0, 'end')

root = tk.Tk()
root.title("Free-Best Sudoku Solver")
root.geometry("400x400")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

style = ttk.Style()
style.configure("Custom.TButton", font=("Helvetica", 12, "bold"))

grid = []
for i in range(9):
    row = []
    for j in range(9):
        entry = ttk.Entry(frame, width=3, font=("Helvetica", 14), justify="center")
        entry.grid(row=i, column=j, sticky=(tk.W, tk.E, tk.N, tk.S))
        row.append(entry)
    grid.append(row)

solve_button = ttk.Button(root, text="Solve", command=solve_sudoku, style="Custom.TButton")
solve_button.grid(row=1, column=0, pady=10)

clear_button = ttk.Button(root, text="Clear", command=clear_grid, style="Custom.TButton")
clear_button.grid(row=2, column=0, pady=10)

colors = ["#FF5733", "#33FF57", "#5733FF", "#FF33F7", "#33C7FF", "#33FFEC", "#FFD333", "#FF3333", "#33FF98"]
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        for x in range(3):
            for y in range(3):
                cell_color = colors[(i//3)*3 + j//3]
                grid[i+x][j+y].configure(style="Custom.TButton", background=cell_color)

root.mainloop()






