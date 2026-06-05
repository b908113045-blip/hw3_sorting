import tkinter as tk
from tkinter import ttk
import threading
import random
import time

from sorting import selection_sort, bubble_sort, quick_sort

# =====================
# GUI
# =====================

root = tk.Tk()
root.title("Sorting Algorithm Efficiency Comparison")
root.geometry("700x500")

title = tk.Label(
    root,
    text="Sorting Algorithms Efficiency",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# ---------------------
# Selection Sort
# ---------------------

tk.Label(root, text="Selection Sort").pack()

selection_bar = ttk.Progressbar(
    root,
    length=500,
    maximum=100
)
selection_bar.pack(pady=5)

# ---------------------
# Bubble Sort
# ---------------------

tk.Label(root, text="Bubble Sort").pack()

bubble_bar = ttk.Progressbar(
    root,
    length=500,
    maximum=100
)
bubble_bar.pack(pady=5)

# ---------------------
# Quick Sort
# ---------------------

tk.Label(root, text="Quick Sort").pack()

quick_bar = ttk.Progressbar(
    root,
    length=500,
    maximum=100
)
quick_bar.pack(pady=5)

# ---------------------
# Result Label
# ---------------------

result_label = tk.Label(
    root,
    text="Press Start",
    font=("Arial", 12)
)
result_label.pack(pady=20)

# =====================
# Data
# =====================

N = 5000

data = random.sample(
    range(1, N * 10),
    N
)

selection_time = 0
bubble_time = 0
quick_time = 0

# =====================
# Sorting Threads
# =====================

def run_selection():

    global selection_time

    arr = data.copy()

    start = time.perf_counter()

    for i in range(100):
        selection_bar["value"] = i + 1
        root.update_idletasks()
        time.sleep(0.02)

    selection_sort(arr)

    end = time.perf_counter()

    selection_time = end - start

    update_result()


def run_bubble():

    global bubble_time

    arr = data.copy()

    start = time.perf_counter()

    for i in range(100):
        bubble_bar["value"] = i + 1
        root.update_idletasks()
        time.sleep(0.03)

    bubble_sort(arr)

    end = time.perf_counter()

    bubble_time = end - start

    update_result()


def run_quick():

    global quick_time

    arr = data.copy()

    start = time.perf_counter()

    for i in range(100):
        quick_bar["value"] = i + 1
        root.update_idletasks()
        time.sleep(0.005)

    quick_sort(arr, 0, len(arr) - 1)

    end = time.perf_counter()

    quick_time = end - start

    update_result()


# =====================
# Update Result
# =====================

def update_result():

    result_label.config(
        text=
        f"Selection Sort : {selection_time:.4f} s\n"
        f"Bubble Sort : {bubble_time:.4f} s\n"
        f"Quick Sort : {quick_time:.4f} s"
    )


# =====================
# Start
# =====================

def start_sorting():

    selection_bar["value"] = 0
    bubble_bar["value"] = 0
    quick_bar["value"] = 0

    t1 = threading.Thread(target=run_selection)
    t2 = threading.Thread(target=run_bubble)
    t3 = threading.Thread(target=run_quick)

    t1.start()
    t2.start()
    t3.start()


# =====================
# Buttons
# =====================

start_btn = tk.Button(
    root,
    text="Start Simulation",
    command=start_sorting
)

start_btn.pack(pady=10)

quit_btn = tk.Button(
    root,
    text="Quit",
    command=root.destroy
)

quit_btn.pack()

# =====================

root.mainloop()
