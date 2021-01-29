# Code Challenge: Implement PatternCount

# Test Case
text = "CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA"
pattern = "CTC"
expOutput = 9

# Implementation
def PatternCount(text, pattern):
    plen = len(pattern)
    count = 0
    for i in range(len(text)-plen):
        if text[i:i+plen] == pattern:
            count += 1
    return count

# Testing
if PatternCount(text, pattern) == expOutput:
    print("Correct!")
else:
    print("Wrong!")
	

# Code Challenge: Implement MostFrequentPatterns

# Test Case
text = "CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC"
k = 5
expOutput = ["AAAAT","GGGGT","TTTTA"]

# Implementation
def WordsInText(text, k):
    wordlist = set()
    for i in range(len(text)-k):
        wordlist.add(text[i:i+k])
    return wordlist   
    
def MostFrequentPatterns(text, k):
    words = WordsInText(text, k)
    words_count = {}
    for w in words:  
        cnt = PatternCount(text, w)
        if cnt in words_count:
            words_count[cnt] += [w]
        else:
            words_count[cnt] = [w]
        
    return (words_count[max(words_count)], max(words_count))

if sorted(expOutput) == sorted(MostFrequentPatterns(text, k)[0]):
    print("Correct!")
else:
    print("Wrong!")
	
	

# Frequent Words in Vibrio cholerae

vibrio_cholerae = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"
k_array = range(3,10)

# Collecting results
for k in k_array:
    res = MostFrequentPatterns(vibrio_cholerae, k)
    print("%s appears %d times" % (str(res[0]), res[1]))
    
'''
# Results:

['tga'] appears 25 times
['atga'] appears 12 times
['gatca', 'tgatc'] appears 8 times
['tgatca'] appears 8 times
['atgatca'] appears 5 times
['atgatcaa'] appears 4 times
['atgatcaag', 'tcttgatca', 'cttgatcat', 'ctcttgatc'] appears 3 times


# Interesting notes [From Stepik users]:

* In average a give 3-mer would be expected to appear once in every 64 bases (4**3), lenght of this text is 540 so if 
distribution of 3-mer were balanced each would appear around 8.4 times. But 'tga' appears 25 times.
* About the 9-mer 'atgatcaag' and 'cttgatcat' are complements
'''

print("Analysis completed!")