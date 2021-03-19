import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create dictionary in form of {"A":"Alfa","B":"Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code word from a word that user inputs
word = input("Enter a Word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)