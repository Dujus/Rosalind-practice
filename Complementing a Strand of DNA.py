DNA = "AAAACCCGGT"
tran_dict = {"A": "T", "T": "A", "C": "G", "G": 'C'}
with open('data/rosalind_revc.txt', 'r') as f:
    DNA = f.read().strip()
temp = list(DNA)

reverse = temp[::-1] # 记住这个反转，好像还可以用reverse

leng = len(reverse)

for base in range(0, leng):
    if reverse[base] in tran_dict:
        reverse[base] = tran_dict.get(reverse[base])

tran_DNA = "".join(reverse)
print(tran_DNA)
