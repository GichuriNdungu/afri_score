from preprocessing import df 
import numpy as np
import tensorflow as tf 

non_numeric_cols = df.select_dtypes(include=['object']).columns
print(non_numeric_cols)