import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    "value_1": np.random.choice(['A', 'B', 'C', 'D'], size=1000),
    "value_2": np.random.choice(['X', 'Y', 'Z'], size=1000),
    "independent_var_1": np.random.rand(1000),
    "independent_var_2": np.random.rand(1000),
    "dependent_var": np.random.rand(1000)
}

df = pd.DataFrame(data)

# Save the DataFrame to a Parquet file
df.to_parquet("sample_data.parquet")
