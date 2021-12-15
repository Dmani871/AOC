import pandas as pd
import numpy as np


def bit_criteria_filter(df, equally_common_value, most_common_bit=True):
    ranking_index = 0 if most_common_bit else -1
    binary_string = ""
    for col in df.columns:
        bit_frequency = df[col].value_counts()
        if len(bit_frequency) == 2 and bit_frequency[0] == bit_frequency[-1]:
            bit_criteria = equally_common_value
        else:
            bit_criteria = bit_frequency.index[ranking_index]
        binary_string += bit_criteria
        df = df[df[col] == bit_criteria]
    return binary_string


def binary_diagnostic():
    df = pd.read_csv('input.txt', delimiter="\n", names=["binaryStr"], dtype=str)
    df = df['binaryStr'].str.split('', expand=True)
    nan_value = float("NaN")
    df.replace("", nan_value, inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    oxygen_generator_rating_bits=bit_criteria_filter(df, "1")
    co2_scrubber_rating_bits=bit_criteria_filter(df, "0", False)
    oxygen_generator_rating=int(oxygen_generator_rating_bits, 2)
    c02_scrubber_rating = int(co2_scrubber_rating_bits, 2)
    return c02_scrubber_rating * oxygen_generator_rating


if __name__ == '__main__':
    print(binary_diagnostic())
