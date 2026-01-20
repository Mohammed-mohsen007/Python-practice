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


# string = "Mohammed Mohsin" \
# "age is 25 " \
# "he is a student " \
# "and also he is working as an intern " \
# "in sdhub where "
# print(string)

# st = """Hello my self mohammed Mohsin
# i did my graduation from Indian school of business management and administration 
# the university located in 
# and also """

# print(st)

# Quick Quiz 
# name = "Harry"
# print(name[-4:-2])


# string = "Mohsin"
# integer = 5
# flt = 5.7

# # print(int(string))
# # print(float(integer))
# print(str(flt))

# # string = "6"
# # integer = 8
# # float = 5.7

# # print(str(string))

# a = 10.8
# a = int(a)
# print(a)

# string = "Taj Mahal is located in Agra"
# num1 = int(8/2)
# num2 = int("1" + "7")
# print(num2)

# print(float(2))
# print(5*5+2*5*6+6*6)



# Frequency Vs Session Depth

# plt.figure(figsize=(7,5))
# sns.scatterplor(
#     data=base_iterl,
#     x="sessions_per_day",
#     y="avg_session_minutes",
#     hue="cluster",
#     plaette="tab10",
#     s=20,
# alpha=0.55
# )

# plt.title("Iteration 1 (Unscaled) - Frequency vs Session Depth")
# plt.Legend(box_to_anchor=(1.02, 1))
# plt.tight_Layout()
# plt.show()

# # Consistency vs Ad Friction
# plt.figure(figsize=(7, 5))
# sns.scatterplot(
#     data=base_iterl,
#     x="days_active_last_30",
#     y="ads_skipped_pct",
#     hue="Cluster",
#     palette="tab10",
#     s=20,
#     alpha=0.55
# )
# plt.title("Iteration 1 (Unscaled) - Consistency vs Ad Friction")
# plt.Legend(bbox_to_anchor=(1.02, 1))
# plt.tight_Layout()
# plt.show()

# # 18) Silhouette Plot (FULL MANUAL)

# sil_values_1 = silhouette_samples(X1, labels1)
# sil_avg_1 = silhouette_score(X1, labels1)
# plt.figure(figsize=(7, 5))
# y_lower = 0
# vals0 = sil_values_1[labels1 == 0]
# vals0.sort()
# size0 = vals0.shape[0]
# y_upper = y_lower + size0
# plt.fill_betweenx(
#     np.arange(y_lower, y_upper),
#     0,
#     vals0,
#     alpha=0.8
# )

# plt.text(
#     -0.05,
#     y_lower + 0.5 * size0,
#     "Cluster 0"
# )

# y_lower = y_upper

# # CLUSTER 1

# vals1 = sil_values_1[labels1 == 1]
# vals1.sort()
# size1 = vals1.shape[0]
# y_upper - y_lower + size1
# plt.fill_betweenx(np.arange(y_lower, y_upper), 0, vals1, alpha=0.8)
# plt.text(-0.05, y_lower + 0.5 * size1, "cluster 1")
# y_lower = y_upper

# vals2 = sil_values_1[labels1 == 2]
# vals2.sort()
# size2 = vals2.shape[0]
# y_upper = y_lower + size2
# plt.fill_betweenx(np.arange(y_lower, y_upper), 0, vals2, alpha=0.8)
# plt.text(-0.05, y_lower + 0.5 * size2, "Cluster 2")
# y_lower = y_upper

# vals3 = sil_values_1[labels1 == 3]
# vals3.sort()
# size3 = vals3.shape[0]
# y_uppper = y_lower + size3
# plt.fill_betweenx(np.arange(y_lower, y_upper), 0, vals3, alpha=0.8)
# plt.text(-0.05, y_lower + 0.5 * size3, "Cluster 3")

# y_lower = y_upperplt.axvline(
#     x=sil_avg_1,
#     color="red",
#     linestyle="--",
#     label=f"Avg Silhoutte = {sil_avg_1:.2f}"
# )
# plt.title("Silhouette Plot (k=4) - Iteration 1 (Unscaled)")
# plt.xLabeL("Silhouette Coefficient")
# plt.yLabeL("Sample index (grouped by cluster)")
# plt.Legend()
# plt.tight_Layout()
# plt.show()

# print("Iteration 1 Avg Silhouette:", round(sil_avg_1, 3))


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import silhouette_score, silhouette_samples
# sns.set(style="whitegrid")
# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", 180)
# spotify_user_behavior = spark.table("workspace.spotify.soptify_user_behavior").toPandas()
# CLUSTER_FEATURES_V1 = [
#     "daily_listening_minutes",    # usage intensity
#     "sessions_per_day",            # freuency
#     "days_active_last_30",          # consistency
#     "avg_session_minutes",          # depth
#     "skip_rate",                    # content friction
#     "liked_songs_pct",              # positive engagement
#     "ads_skipped_pct",              # monetization friction
# ]

# base = spotify_user_behavior[
#     ["user_id"] + CLUSTER_FEATURES_V1
# ].copy()
# k = 4
# x1 = base[CLUSTER_FEATURES_V1].copy()
# scaler = StandardScaler()
# x2_scaled = scaler.fit_transform(x1)
# x2 = pd.DateFrame(
#     x2_scaled,
#     columns=CLUSTER_FEATURES_V1,
#     index=base.index
# )
# KM2 = KMeans(
#     n_clusters=k,
#     random_state=42,
#     n_init=20,
#     max_iter=300
# )
# labels2 = km2.fit_predict(X2)
# inertia2 = km2.inertia_
# sil_avg_2 = silhouette_score(X2, labels2)
# base_iter2 = base.copy()
# base_iter2["cluster"] = labels2
# print(f"\nIteration 2 results | k={k}")
# print("Inertia  :", round(inertia2, 2))
# print("Silhouette:", roud(sil_avg_2, 3))
# sizes2 = base_iter2["cluster"].value_counts().sort_index()
# means2 = (
#     base_iter2.groupby("cluster")[CLUSTER_FEATURES_V1]
#     .mean()
#     .round(3)
# )
# profile2 = means2.copy()
# profile2.insert(0, "cluster_size", sizes2)
# print("\nCluster profile (means, original scale) - Iteration 2 (StandrdScaler labels):")
# display(profile2)
# plt.figure(figsize=(6, 4))
# base_iter2["cluster"].value_counts().sort_index().plot(kind="bar")
# plt.title("Cluster Size - Iteration 2 (StandardScaler)")
# plt.xLabeL("cluster")
# plt.yLabeL("Users")
# plt.show()
# plt.figure(figsize=(7, 5))
# sns.scatterplot(
#     data=base_iter2,
#     x="daily_listening_minutes",
#     y="skip_rate",
#     hue="cluster",
#     palette="tab10",
#     s=20,
#     alpha=0.55,
#     edgecolor=None
# )
# plt.title("Iteration 2 (StandardScaler) - Intensity vs Skip behavior")
# plt.Legend(title="cluster", bbox_to_anchor=(1.02, 1), loc="upper left")
# plt.tight_Layout()
# plt.show()
# plt.figure(figsize=(7, 5))
# sns.scatterplot(
#     data=base_iter2,
#     x="sessions_per_day",
#     y="avg_session_minutes",
#     hue="cluster",
#     palette="tab10",
#     s=20,
#     alpha=0.55,
#     edgecolor=None
# )
# plt.title("Iteration 2 (StandardScaler) - Frequency vs Session Depth")
# plt.Legend(title="Cluster", bbox_to_anchor=(1.02, 1), loc="upper left")
# plt.tight_Layout()
# plt.show()

# # Plot 3: Consistency vs Ad Friction
# plt.figure(figsize=(7, 5))
# sns.scatterplot(
#     data=base_iter2,
#     x="days_active_last_30",
#     y="ads_skipped_pct",
#     hue="cluster",
# )


# total_mark = 2160
# mark = 1889
# divided = (1889 / 2160) * 100
# print(divided)