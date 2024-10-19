import numpy as np
import matplotlib.pyplot as plt
import json
import transform_data

print(transform_data.unix_dh(1517443200))

print(transform_data.dh_unix(transform_data.unix_dh(1517443200)))
