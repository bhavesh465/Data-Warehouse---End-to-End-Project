import pandas as pd
import numpy as np
import os

# Fixed date ID
DATEID = '20240728'

# Output directory path
directory = r"C:\Users\vikas\Desktop\Personal\End to End Project\Landing Directory"

# ✅ Make sure the directory exists
os.makedirs(directory, exist_ok=True)

# Loop through 100 stores
for i in range(1, 101):
    num_rows = np.random.randint(100, 1000)

    # Generate random data
    data = {
        'DateID': [DATEID] * num_rows,
        'ProductID': np.random.randint(1, 1001, size=num_rows),
        'StoreID': [i] * num_rows,
        'CustomerID': np.random.randint(1, 1001, size=num_rows),
        'QuantityOrderded': np.random.randint(1, 21, size=num_rows),
        'OrderAmount': np.random.randint(100, 1001, size=num_rows)
    }

    df = pd.DataFrame(data)

    # Generate random discount % and shipping cost %
    discount_perc = np.random.uniform(0.02, 0.15, size=num_rows)
    shipping_cost = np.random.uniform(0.05, 0.15, size=num_rows)

    # Calculated columns
    df['DiscountAmount'] = df['OrderAmount'] * discount_perc
    df['Shipping Cost'] = df['OrderAmount'] * shipping_cost
    df['TotalAmount'] = df['OrderAmount'] - (df['DiscountAmount'] + df['Shipping Cost'])

    # Output file name and path
    file_name = f"Store_{i}_{DATEID}.csv"
    file_path = os.path.join(directory, file_name)

    # Remove file if it already exists
    if os.path.exists(file_path):
        os.remove(file_path)

    # Save the dataframe to CSV
    df.to_csv(file_path, index=False)

    # Optional: print confirmation for each file
    print(f"Saved: {file_path}")
