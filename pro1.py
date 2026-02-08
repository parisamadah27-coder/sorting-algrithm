import time

def print_array(arr, label="arayeh"):
    print(f"{label}: {arr}")

def bubble_sort_with_steps(arr):
    print("\n" + "="*60)
    print("moratab sazi (Bubble Sort) - namayesh marahel")
    print("="*60)
    
    n = len(arr)
    arr_copy = arr.copy()
    print_array(arr_copy, "arayeh1")
    print(f"teedad marahel lazem dar badtarin halat: {n*(n-1)//2}")
    print("-"*40)
    
    step = 1
    for i in range(n):
        swapped = False
        print(f"\n--- pas shomareh {i+1} ---")
        for j in range(0, n-i-1):
            print(f"marhal {step}: moghayeseh {arr_copy[j]} va {arr_copy[j+1]}", end=" ")
            
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                swapped = True
                print(f"← jabeja shod [{arr_copy[j]} ↔ {arr_copy[j+1]}]")
            else:
                print("← jabeja nashod")
            
            print(f"   vazeeyat feely arayeh: {arr_copy}")
            step += 1
        
        if not swapped:
            print(f"\n✓ dar pas {i+1} .")
            break
    
    print("\n" + "="*40)
    print_array(arr_copy, "arayeh nahayi")
    print("="*40)
    
    return arr_copy

def merge_sort_with_steps(arr, depth=0, side=""):
    if len(arr) <= 1:
        indent = "  " * depth
        print(f"{indent}{side} bazgasht: {arr}")
        return arr
    
    indent = "  " * depth
    print(f"{indent}{side} taghsim: {arr}")
    
    mid = len(arr) // 2
    left = merge_sort_with_steps(arr[:mid], depth + 1, "chap")
    right = merge_sort_with_steps(arr[mid:], depth + 1, "rast")
    
    result = merge_with_steps(left, right, depth, side)
    
    print(f"{indent}{side} edgham shod: {result}")
    return result

def merge_with_steps(left, right, depth=0, side=""):
    indent = "  " * depth
    print(f"{indent}{side} edgham {left} و {right}")
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        print(f"{indent}  moghayeseh {left[i]} va (chap) {right[j]} (rast)", end=" ")
        if left[i] < right[j]:
            print(f"← {left[i]} ezafeh shod")
            result.append(left[i])
            i += 1
        else:
            print(f"← {right[j]} ezafeh shod")
            result.append(right[j])
            j += 1
    
    # اضافه کردن عناصر باقی‌مانده
    if i < len(left):
        print(f"{indent}ezafeh kardan baghi mandeh az chap: {left[i:]}")
        result.extend(left[i:])
    if j < len(right):
        print(f"{indent}  ezafeh kardan baghi mandeh az rast: {right[j:]}")
        result.extend(right[j:])
    
    print(f"{indent}  natijeh edgham: {result}")
    return result

def quick_sort_with_steps(arr, depth=0, side=""):
    if len(arr) <= 1:
        indent = "  " * depth
        print(f"{indent}{side} bazgasht: {arr}")
        return arr
    
    indent = "  " * depth
    print(f"{indent}{side} moratab sazi: {arr}")
    
    pivot = arr[len(arr) // 2]
    print(f"{indent}  entekhab pivot: {pivot}")
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    print(f"{indent}  chap : taghsim ={left}, miyaneh={middle}, rast={right}")
    
    left_sorted = quick_sort_with_steps(left, depth + 1, "chap")
    right_sorted = quick_sort_with_steps(right, depth + 1, "rast")
    
    result = left_sorted + middle + right_sorted
    print(f"{indent}{side} tarkib: {result}")
    
    return result

# توابع برای مقایسه زمان (بدون نمایش مراحل)
def bubble_sort_speed(arr):
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
                swapped = True
        if not swapped:
            break
    return arr_copy

def merge_sort_speed(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_speed(arr[:mid])
    right = merge_sort_speed(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort_speed(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_speed(left) + middle + quick_sort_speed(right)

def get_numbers_from_user():
    print("="*60)
    print("moratab sazi aedad")
    print("="*60)
    
    numbers = []
    print("Enter 10 number:")
    
    for i in range(10):
        while True:
            try:
                num = float(input(f"number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("enter number")
    
    print("\n" + "="*60)
    print(f"numbers entered: {numbers}")
    print("="*60)
    
    return numbers

def main():
    # دریافت اعداد از کاربر
    numbers = get_numbers_from_user()
    
    # ذخیره کپی از اعداد اصلی
    original_numbers = numbers.copy()
    
    # مرتب‌سازی حبابی با نمایش مراحل
    print("\n" + "="*60)
    print("shoroe morata sazi")
    print("="*60)
    
    # حبابی
    bubble_result = bubble_sort_with_steps(numbers)
    
    # ادغامی
    print("\n\n" + "="*60)
    print("moratab sazi edghami (Merge Sort) - namayesh marahel")
    print("="*60)
    print_array(original_numbers, "arayeh avaliyeh")
    print("-"*40)
    
    merge_result = merge_sort_with_steps(original_numbers.copy())
    
    print("\n" + "="*40)
    print_array(merge_result, "arayeh nahayi")
    print("="*40)
    
    # سریع
    print("\n\n" + "="*60)
    print("moratab sazi sarie (Quick Sort) - namayesh marahel")
    print("="*60)
    print_array(original_numbers, "arayeh avaliyeh")
    print("-"*40)
    
    quick_result = quick_sort_with_steps(original_numbers.copy())
    
    print("\n" + "="*40)
    print_array(quick_result, "arayeh nahayi")
    print("="*40)
    
    # مقایسه نتایج
    print("\n\n" + "="*60)
    print("moghayeseh natayej")
    print("="*60)
    print(f"original numbers {original_numbers}")
    print(f"bubble:      {bubble_result}")
    print(f"merge:     {merge_result}")
    print(f"quick:       {quick_result}")
    
    # بررسی صحت
    if bubble_result == merge_result == quick_result:
        print("\n✓ same result")
    else:
        print("\n different result")
    
      # مقایسه زمان اجرا 
    print("\n\n" + "="*60)
    print("Moghayeseh zaman ejra:")
    print("="*60)
    
    # اندازه‌گیری زمان bubble sort
    start_time = time.time()
    bubble_speed_result = bubble_sort_speed(original_numbers.copy())
    bubble_time = time.time() - start_time
    
    # اندازه‌گیری زمان merge sort
    start_time = time.time()
    merge_speed_result = merge_sort_speed(original_numbers.copy())
    merge_time = time.time() - start_time
    
    # اندازه‌گیری زمان quick sort
    start_time = time.time()
    quick_speed_result = quick_sort_speed(original_numbers.copy())
    quick_time = time.time() - start_time
    
    print(f"\nZaman ejra:")
    print(f"Bubble Sort: {bubble_time:.6f} saniye")
    print(f"Merge Sort:  {merge_time:.6f} saniye")
    print(f"Quick Sort:  {quick_time:.6f} saniye")
    
    print(f"\nMoghayeseh zamanha:")
    print(f"Bubble be Merge: {bubble_time/merge_time:.2f} barabar")
    print(f"Bubble be Quick: {bubble_time/quick_time:.2f} barabar")
    print(f"Merge be Quick:  {merge_time/quick_time:.2f} barabar")
    
    
    
   

if __name__ == "__main__":
    main()