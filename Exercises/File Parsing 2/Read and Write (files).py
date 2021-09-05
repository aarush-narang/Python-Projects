with open('read.txt', 'r') as f:
    text = f.read()

text = text.split('\n')
with open('write.txt', 'a') as f:
    for i in range(0, int((len(text))/2)):
        f.write(f'{text[(0+(2*i))]}\n')

with open('write.txt', 'r') as f:
    new_text = f.read()

print(new_text)
