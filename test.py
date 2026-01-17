# num = 25
# num = str(num)
# print("My age is: " + num)

# print(6 - 6 / 2)
# print(6/2)
# print(6-3)

# print(12 / 3)
# print(16 / 4)

# asterisk = "*" * 3
# name = "Python"
# result = asterisk + " " + name + " " + asterisk
# print(result)

# username = input("Enter Your Name: ")
# print("Hello, " + username + "! Welcome to Python Programming.")

# import random
# print(random.randint(1, 10))

# json parsing
# tuple_example = (1, 2, 3, 4, 5)
# set_example = {1, 2, 3, 4, 5}
# print(tuple_example) 
# print(set_example) 


# import numpy as np
# # Display options (optional)
# np.set_printoptions(precision=3, suppress=True)

# print("NumPy version:", np.__version__)

# #---------------------------
# #1) WHAT IS NUMPY & WHY ARRAYS?
# #---------------------------
# # python lists are flexible but NumPy arrays are faster for math,
# # memory-efficient, and enable vectorized operations.

# Py_list = [1, 2, 3, 4]
# arr = np.array(Py_list)

# print("Python list:", Py_list)
# print("NumPy array:", arr)
# print("Type [Python list]:", type(Py_list))
# print("Type [NumPy array]:", type(arr))
# print("Array shape:", arr.shape)
# print("Array data type:", arr.dtype)    
# print("Array item size (bytes):", arr.itemsize)
# print("Array total size (bytes):", arr.nbytes)
# print("Array dimensions:", arr.ndim)
# print("Array length:", len(arr))
# print("Array first element:", arr[0])
# print("Array last element:", arr[-1])
# print("Array slice [1:3]:", arr[1:3])
# print("Array slice [::2]:", arr[::2])
# print("Array sum:", arr.sum())


# # 2) CREATING ARRAYS (zeros, ones, arange, linspace, eye, full )

# a0 = np.zeros((2, 3))
# a1 = np.ones((2, 3))
# a2 = np.full((2, 3), 7)
# a3 = np.arange(0, 10, 2)        # start, stop, step
# a4 = np.linspace(0, 1, 5)       # evenly spaced points
# a5 = np.eye(4)                  # identity matrix

# print("\nzeros:\n", a0)
# print("\nones:\n", a1)
# print("\nfull:\n", a2)
# print("\narange:\n", a3)
# print("\nlinspace:\n", a4)
# print("\neye:\n", a5)

# # TRY IT
# # Create an array of numbers from 5 to 25 (inclusive stepping by 5.)

# #---------------------------
# #3) SHAPE, DIMENSIONS SIZE, NDIM, RESHAPE
# #---------------------------

# x = np.arange(1, 13)  # 1D array with 12 elements # 1..12
# print("\n1D x:", x)
# print("shape:", x.shape, "| size:", x.size, "| ndim:", x.ndim)

# x2 = x.reshape(3, 4)
# print("\nReshaped to 3x4:\n", x2)
# print("shape:", x2.shape, "| size:", x2.size, "| ndim:", x2.ndim)

# # Fiatten
# x_flat = x2.ravel()
# print("\nFlattened array:\n", x_flat)

# # TRY IT
# # Take np.arange(1, 17) and reshape it into 4x4

# #---------------------------
# #4) DTYPES & TYPE CONVERSION (astype)
# #---------------------------
# y = np.array([1, 2, 3], dtype=np.int32)
# z = y.astype(np.float64)

# print("\ny dtype:", y.dtype, "=>", y)
# print("z dtype:", z.dtype, "=>", z)

# # TRY IT
# # Create an float array [2, 2, 2.5, 3.9] and convert it to int.

# #---------------------------
# #5) INDEXING & SLICING (ID & 2D)
# #---------------------------
# v = np.array([10, 20, 30, 40, 50])
# print("\nArray v:", v)
# print("v[0]   :", v[0])
# print("v[-1]   :", v[-1])
# print("v[1:4] :", v[1:4])
# print("v[:3]  :", v[:3])
# print("v[::2]   :", v[::2])

# m = np.arange(1, 13).reshape(3, 4)
# print("\nMatrix m:\n", m)
# print("m[0, 0]     :", m[0, 0])
# print("m[1, :]     :", m[1, :])
# print("m[:, 2]     :", m[:, 2])
# print("m[0:2, 1:3] :\n", m[0:2, 1:3])

# # TRY IT
# # From m, extract the last column and the top-left 2x2 block.

# #---------------
# #6) BOOLEAN MASKING (FILTERING)
# #--------------

# scores = np.array([45, 72, 88, 660, 91, 39, 77])
# mask_pass = scores >= 660
# print("\nScores:", scores)
# print("pass mask:", mask_pass)
# print("Passing scores:", scores[mask_pass])
# print("Scores between 70 and 90:", scores[(scores >= 70) & (scores<=90)])


# import matplotlib.pyplot as plt
# import pandas as pd

# # Configure Pandas display (NOT matplotlib)
# pd.set_option("display.max_columns", 200)
# pd.set_option("display.with", 160)

# # Ensures no hidden thems or styles are applied
# # Students see raw Matplotlib behavior
# plt.style.use("default")

# COL_LINE_ORDERS = "#1f77b4"
# COL_LINE_REV = "#2ca02c"
# COL_BAR = "#ff7f0e"
# COL_HIST = "#9467bd"
# COL_SCATTER = "#d62728"
# GRID_ALPHA = 0.4

# # LOad Swiggy Tables

# fact = spark.table("workspace.swiggy.fact_transactions").toPandas()
# dim_restaurant_product = spark.table("workspace.swiggy.dim_restaurant_product").toPandas()
# dim_campaign =  spark.table("workspace.swiggy.dim_campaign").toPandas()

# # Data Type Fixes (Important before plotting)

# # Converts string dates to datetime objects for time-series plots

# fact["transaction_date"] = pd.to-datetime(fact["transaction_date"], errors="coerce")

# #Ensures numeric fields are truly numeric 
# for c in ["net_amount", "gross_amount", "delivery_minutes"]:
#     if c in fact.columns:
#         fact[c ]= [pd.to_numeric(fact[c], errors="coerce")]

# #V1) LINE CHART -Daily Orders Trend

# daily_orders = (
#     fact.groupby("transaction_date", as_index=False)
#     .agg(orders=("transaction_id", "count"))
#     .sort_values("transaction_date")
# )

# plt.figure(figsize=(12, 4))

# plt.plot(
#     daily_orders["transaction_date"],
#     daily_orders["orders"],
#     color=COL_LINE_ORDERS,
#     linewidth=2
# )

# plt.title("Daily Orders Trend")

# plt.xLabel("Date")
# plt.yLabel("Orders")


# plt.grid(True, linestyle="--", alpha=GRID_ALPHA)
# plt.tight_Layout()

# plt.show()


# cuisine_orders = (
#     fact.mergr(
#         dim_restaurant_product[["restaurant_product_id", "cuisine_tag"]],
#         on="restaurant_product_id",
#         how="left"
#     )
#     .groupby("cuisine_tag", as_index=False)
#     .agg(orders=("transaction_id", "count"))
#     .sort_values("orders", ascending=False)
#     .head(9)
# )

# total_orders = cuisine_orders["orders"].sum()
# def autopct_cuisine(pct):
#     count = int(round(pct * total_orders / 100))
#     return f"{pct:.1f}%\n({count})"
# plt.figure(figsize=(6, 6))

# plt.pie(
#     cuisine_orders["orders"],
#     labels=cuisine_orders["cuisine_tag"],
#     autopct=autopct_cuisine,
#     startangle=90
# )

# plt.axis("equal")
# plt.title("Order Share by Cuisine (Top 9)")
# plt.show()


# plt.figure(figsize=(7, 4))

# plt.scatter(
#     fact["delivery_minutes"],
#     fact["net_amount"],
#     color=COL_SCATTER,
#     alpha=0.35,
#     s=18
# )

# plt.title("Delivery Time vs Net Amount")
# plt.xLabel("Delivery Minutes")
# plt.yLabel("Net Amount")
# plt.grid(True, linestyle="--", alpha=GRID_ALPHA)
# plt.tight_Layout()
# plt.show()


