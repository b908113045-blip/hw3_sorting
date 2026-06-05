# 作業三：排序演算法效能比

## 一、實驗目的

本作業旨在實作三種常見排序演算法：選擇排序（Selection Sort）、泡泡排序（Bubble Sort）以及快速排序（Quick Sort），並透過圖形化介面與多執行緒（Thread）技術，同步比較三種排序演算法的執行效率差異。藉由實際測試與觀察，了解不同演算法在處理大量資料時的效能表現。

## 二、實驗環境

* 開發語言：Python 3.x
* GUI框架：Tkinter 
* 使用模組： 
  * threading 
  * random
  * time 
  * tkinter.ttk

# 三、演算法介紹

（一）Selection Sort（選擇排序） 

選擇排序的原理為每次從未排序區域中找出最小值，再與目前位置的元素交換。 

執行流程：
  1. 從陣列中尋找最小值。
  2. 與第一個元素交換。
  3. 再從剩餘未排序元素中尋找最小值。
  4. 重複直到排序完成。

時間複雜度： 
  * Best Case：O(n²) 
  * Average Case：O(n²) 
  * Worst Case：O(n²)
    
（二）Bubble Sort（泡泡排序） 泡泡排序透過反覆比較相鄰元素，若順序錯誤則進行交換，使較大的數值逐漸移動至陣列尾端。 

執行流程：
 1. 比較相鄰兩個元素。
 2. 若前者大於後者則交換。
 3. 完成一輪後最大值會移至最後方。
 4. 重複執行直到排序完成。 

時間複雜度： 
  * Best Case：O(n) 
  * Average Case：O(n²)
  * Worst Case：O(n²)
    
（三）Quick Sort（快速排序） 快速排序採用分治法（Divide and Conquer）概念。 本作業依照課堂講義內容，選擇陣列第一個元素作為 Pivot（基準點），利用左右指標進行資料分割，最後再遞迴排序左右子陣列。

執行流程：
 1. 選定 Pivot。
 2. 左右指標向中間移動。
 3. 找到不符合條件的元素後交換。
 4. Pivot 放回正確位置。
 5. 遞迴處理左右子陣列。
 
時間複雜度： 
  * Best Case：O(n log n)
  *  Average Case：O(n log n)
  *  Worst Case：O(n²)
    
# 四、系統設計

本系統使用 Tkinter 建立圖形化介面，並利用三個 Thread 同時執行三種排序演算法。 

系統流程如下：
 1. 產生 N 個不重複亂數。
 2. 複製相同資料給三種排序演算法。
 3. 建立三個執行緒（Thread）。
 4. 同步執行 Selection Sort、Bubble Sort 與 Quick Sort。
 5. 即時更新進度條。
 6. 顯示各排序完成時間。
 7. 比較排序效能差異。

# 五、實驗結果

本次測試使用 N 個隨機不重複整數進行排序。 

執行結果顯示： 
  * Quick Sort 完成速度最快。
  * Selection Sort 與 Bubble Sort 耗時較長。
  * 當資料量增加時，Quick Sort 與另外兩種演算法的差距更加明顯。

從實驗可觀察到： Quick Sort 的平均時間複雜度為 O(n log n)，因此在大量資料下仍具有良好的執行效率；而 Selection Sort 與 Bubble Sort 因為需要大量比較與交換，其時間複雜度為 O(n²)，故執行時間明顯較長。 
