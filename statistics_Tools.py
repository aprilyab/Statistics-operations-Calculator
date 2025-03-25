import numpy as np

def mean(arr):
    return np.mean(arr)

def median(arr):
    return np.median(arr)

def standard_deviation(arr):
    return np.std(arr)

def variance(arr):
    return np.var(arr)

def minimum(arr):
    return np.min(arr)

def maximum(arr):
    return np.max(arr)

def index_of_min(arr):
    return np.argmin(arr)

def index_of_max(arr):
    return np.argmax(arr)

def percentile(arr, q):
    return np.percentile(arr, q)

# Menu
while True:
    print("\nChoose your desired statistical operation:")
    print("""
    ======= STATISTICAL OPERATIONS MENU =======
    1. Mean
    2. Median
    3. Standard Deviation
    4. Variance
    5. Minimum Value
    6. Maximum Value
    7. Index of Minimum Value
    8. Index of Maximum Value
    9. Percentile
    0. Exit
    ===========================================
    """)
    
    choice = input("Enter your choice (0-9): ")

    if choice == '0':
        print("Exiting the program. Goodbye!")
        break

    arr = np.array(list(map(float, input("Enter numbers separated by spaces: ").split())))

    if choice == '1':
        print("Mean:", mean(arr))
    elif choice == '2':
        print("Median:", median(arr))
    elif choice == '3':
        print("Standard Deviation:", standard_deviation(arr))
    elif choice == '4':
        print("Variance:", variance(arr))
    elif choice == '5':
        print("Minimum Value:", minimum(arr))
    elif choice == '6':
        print("Maximum Value:", maximum(arr))
    elif choice == '7':
        print("Index of Minimum Value:", index_of_min(arr))
    elif choice == '8':
        print("Index of Maximum Value:", index_of_max(arr))
    elif choice == '9':
        q = float(input("Enter the percentile (0-100): "))
        print(f"{q}th Percentile:", percentile(arr, q))
    else:
        print("Invalid choice! Please select a valid option.")
