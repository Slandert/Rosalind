"""
Rosalind problem spec: http://rosalind.info/problems/spec/

Author: Michael Ayars

Given: A list L of n (n≤100) positive real numbers.

Return: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.

"""



MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}


def mass_spec(s):
    """
    s = list of prefix weights for protein mass.

    Returns string of amino acids with prefix spectrum matching s.
    """

    
    result = ''
    spectrum = list(map(float, s.split()))

    mass_table_dict = {}
    for i, k in MONOISOTOPIC_MASS_TABLE.items():
        mass_table_dict[round(k,4)] = i

    for j in range(1, len(spectrum)):
        a = spectrum[j - 1]
        b = spectrum[j]
        result += mass_table_dict[round(b - a, 4)]

    return result

if __name__ == "__main__":
    small_dataset = """
                    3524.8542
                    3710.9335
                    3841.974
                    3970.0326
                    4057.0646
                    """
    large_dataset = open('inputData/rosalind_input_spec.txt').read().strip()

    print (mass_spec(large_dataset))
