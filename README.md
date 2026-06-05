# 作業三：排序演算法效能比較

## 一、實驗目的

本作業旨在實作三種常見排序演算法：選擇排序（Selection Sort）、泡泡排序（Bubble Sort）以及快速排序（Quick Sort），並透過圖形化介面（GUI）與多執行緒（Thread）技術，同步比較三種排序演算法的執行效率差異。藉由實際測試與觀察，了解不同演算法在處理大量資料時的效能表現。

---

## 二、實驗環境

### 開發環境

* 開發語言：Python 3.x
* GUI 框架：Tkinter

### 使用模組

* threading
* random
* time
* tkinter.ttk

---

## 三、演算法介紹

### （一）Selection Sort（選擇排序）

選擇排序的原理為每次從未排序區域中找出最小值，再與目前位置的元素交換，逐步完成排序。

#### 執行流程

1. 從未排序區域中尋找最小值。
2. 與目前位置的元素交換。
3. 再從剩餘未排序元素中尋找最小值。
4. 重複上述步驟直到排序完成。

#### 時間複雜度

* Best Case：O(n²)
* Average Case：O(n²)
* Worst Case：O(n²)

---

### （二）Bubble Sort（泡泡排序）

泡泡排序透過反覆比較相鄰元素，若順序錯誤則進行交換，使較大的數值逐漸移動至陣列尾端。

#### 執行流程

1. 比較相鄰兩個元素。
2. 若前者大於後者則進行交換。
3. 完成一輪後，最大值會移至最後方。
4. 重複執行直到排序完成。

#### 時間複雜度

* Best Case：O(n)
* Average Case：O(n²)
* Worst Case：O(n²)

---

### （三）Quick Sort（快速排序）

快速排序採用分治法（Divide and Conquer）的概念進行排序。

本作業依照課堂講義內容，以陣列第一個元素作為 Pivot（基準點），利用左右指標進行資料分割，最後再遞迴排序左右子陣列。

#### 執行流程

1. 選定 Pivot。
2. 左右指標向中間移動。
3. 找到不符合條件的元素後進行交換。
4. 將 Pivot 放回正確位置。
5. 遞迴處理左右子陣列。

#### 時間複雜度

* Best Case：O(n log n)
* Average Case：O(n log n)
* Worst Case：O(n²)

---

## 四、系統設計

本系統使用 Tkinter 建立圖形化介面，並利用三個 Thread 同時執行三種排序演算法，以視覺化方式比較其執行效率。

### 系統流程

1. 產生 N 個不重複亂數。
2. 複製相同資料給三種排序演算法。
3. 建立三個執行緒（Thread）。
4. 同步執行 Bubble Sort、Selection Sort 與 Quick Sort。
5. 即時更新進度條顯示排序進度。
6. 顯示各排序演算法的執行時間。
7. 比較不同排序演算法的效能差異。

---

## 五、實驗結果

本次測試使用 N 個隨機且不重複的整數進行排序。

### 實驗結果

* Quick Sort 完成速度最快。
* Selection Sort 執行速度次之。
* Bubble Sort 執行速度最慢。
* 當資料量增加時，Quick Sort 與另外兩種排序演算法的差距更加明顯。

### 結果分析

Quick Sort 的平均時間複雜度為 O(n log n)，因此在大量資料下仍能維持良好的執行效率；而 Selection Sort 與 Bubble Sort 皆屬於 O(n²) 的演算法，需要進行大量比較與交換，因此執行時間明顯較長。

由實驗結果可知，在處理大量資料時，Quick Sort 的效能遠優於 Selection Sort 與 Bubble Sort。

---

## 六、結論

本作業成功實作 Bubble Sort、Selection Sort 與 Quick Sort 三種排序演算法，並透過 Tkinter 圖形化介面與多執行緒技術進行效能比較。

實驗結果顯示，Quick Sort 在大量資料下具有最佳排序效率；Selection Sort 與 Bubble Sort 雖然實作較為簡單，但執行效率相對較低。透過本次作業，不僅了解各種排序演算法的運作原理，也學習到 Thread、多工執行及 GUI 設計等程式開發技巧，進一步提升對演算法分析與系統設計的理解。
