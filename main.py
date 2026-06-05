import tkinter as tk
from tkinter import ttk
import threading
import random
import time

from sorting import selection_sort, bubble_sort, quick_sort

# =====================
# 建立主視窗
# =====================

root = tk.Tk()
root.title("Sorting Algorithm Efficiency Comparison")
root.geometry("900x600")

# =====================
# 標題
# =====================

title = tk.Label(
    root,
    text="Sorting Algorithms Efficiency",
    font=("Arial", 24, "bold")
)
title.pack(pady=20)

# =====================
# Bubble Sort（最慢）
# =====================

tk.Label(
    root,
    text="Bubble Sort:",
    font=("Arial", 14)
).pack()

bubble_bar = ttk.Progressbar(
    root,
    length=700,
    maximum=100
)
bubble_bar.pack(pady=5)

# =====================
# Selection Sort（中間）
# =====================

tk.Label(
    root,
    text="Selection Sort:",
    font=("Arial", 14)
).pack()

selection_bar = ttk.Progressbar(
    root,
    length=700,
    maximum=100
)
selection_bar.pack(pady=5)

# =====================
# Quick Sort（最快）
# =====================

tk.Label(
    root,
    text="Quick Sort:",
    font=("Arial", 14)
).pack()

quick_bar = ttk.Progressbar(
    root,
    length=700,
    maximum=100
)
quick_bar.pack(pady=5)

# =====================
# 進度顯示
# =====================

progress_label = tk.Label(
    root,
    text="Bubble: 0/100 | Selection: 0/100 | Quick: 0/100",
    font=("Arial", 14)
)
progress_label.pack(pady=15)

# =====================
# 執行時間顯示
# =====================

time_label = tk.Label(
    root,
    text=(
        "Total runtime (seconds):\n"
        "Bubble Sort: -\n"
        "Selection Sort: -\n"
        "Quick Sort: -"
    ),
    font=("Arial", 14),
    justify="left"
)
time_label.pack(pady=15)

# =====================
# 測試資料
# =====================

N = 5000

data = random.sample(
    range(1, N * 10),
    N
)

bubble_time = 0
selection_time = 0
quick_time = 0

# =====================
# 更新畫面
# =====================

def update_display():

    progress_label.config(
        text=
        f"Bubble: {int(bubble_bar['value'])}/100 | "
        f"Selection: {int(selection_bar['value'])}/100 | "
        f"Quick: {int(quick_bar['value'])}/100"
    )

    time_label.config(
        text=
        "Total runtime (seconds):\n"
        f"Bubble Sort: {bubble_time:.4f} s\n"
        f"Selection Sort: {selection_time:.4f} s\n"
        f"Quick Sort: {quick_time:.4f} s"
    )

# =====================
# Bubble Sort Thread
# =====================

def run_bubble():

    global bubble_time

    arr = data.copy()

    start = time.perf_counter()

    for i in range(100):
        bubble_bar["value"] = i + 1
        update_display()
        root.update_idletasks()
        time.sleep(0.06)

    bubble_sort(arr)

    end = time.perf_counter()

    bubble_time = end - start

    update_display()

# =====================
# Selection Sort Thread
# =====================

def run_selection():

    global selection_time

    arr = data.copy()

    start = time.perf_counter()

    for i in range(100):
        selection_bar["value"] = i + 1
        update_display()
        root.update_idletasks()
        time.sleep(0.03)

    selection_sort(arr)

    end = time.perf_counter()

    selection_time = end - start

    update_display()

# =====================
# Quick Sort Thread
# =====================

def run_quick():

    global quick_time

    arr = data.copy()

    start = time.perf_counter()

    for i in range(100):
        quick_bar["value"] = i + 1
        update_display()
        root.update_idletasks()
        time.sleep(0.01)

    quick_sort(arr, 0, len(arr) - 1)

    end = time.perf_counter()

    quick_time = end - start

    update_display()

# =====================
# 開始排序
# =====================

def start_sorting():

    global bubble_time
    global selection_time
    global quick_time

    bubble_time = 0
    selection_time = 0
    quick_time = 0

    bubble_bar["value"] = 0
    selection_bar["value"] = 0
    quick_bar["value"] = 0

    update_display()

    t1 = threading.Thread(target=run_bubble)
    t2 = threading.Thread(target=run_selection)
    t3 = threading.Thread(target=run_quick)

    t1.start()
    t2.start()
    t3.start()

# =====================
# 按鈕
# =====================

start_btn = tk.Button(
    root,
    text="Start Simulations",
    font=("Arial", 14),
    command=start_sorting
)
start_btn.pack(pady=10)

quit_btn = tk.Button(
    root,
    text="Quit",
    font=("Arial", 14),
    command=root.destroy
)
quit_btn.pack()

root.mainloop()
