import pandas as pd
import numpy as np
def window_increasese():
    df = pd.read_csv('input-simple.txt', delimiter="\n", names=["depths"])
    windows=np.convolve(df["depths"], np.ones(3, dtype=int), 'valid')
    diffs = np.ediff1d(windows, to_begin=0)
    return (0 < diffs).sum()

if __name__ == '__main__':
    print(window_increasese())
