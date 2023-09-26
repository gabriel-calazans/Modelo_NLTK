import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import reuters

# Baixe o corpus de exemplo (você pode escolher outro corpus, se desejar)
nltk.download("reuters")

# Tokenização de palavras
words = reuters.words()

# Converta todas as palavras para minúsculas e filtre apenas as vogais
vowels = [word.lower() for word in words if word.lower() in 'aeiou']

# Calcule a frequência das vogais
freq_dist = FreqDist(vowels)

# Crie um dicionário para mapear vogais para contagens
vowel_counts = {vowel: freq_dist[vowel] for vowel in 'aeiou'}

# Imprima o resultado
total_vowels = sum(vowel_counts.values())
print(f"Tem neste texto {total_vowels} vogais, sendo elas:")
for vowel in 'aeiou':
    print(f"{vowel}: {vowel_counts[vowel]}", end=", " if vowel != 'u' else ".")
print()
