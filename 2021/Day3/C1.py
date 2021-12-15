import pandas as pd
import numpy as np

def binary_diagnostic():
    df = pd.read_csv('input.txt', delimiter="\n",names=["binaryStr"],dtype = str)
    df=df['binaryStr'].str.split('',expand=True).mode()
    binary_string=df.to_string(index=False,header=False).replace(" ", "")
    gamma_rate=int(binary_string, 2)
    filped_bits = ''.join(['1' if i == '0' else '0' for i in binary_string])
    epsilon_rate=int(filped_bits, 2)
    return gamma_rate* epsilon_rate

if __name__ == '__main__':
    print(binary_diagnostic())
