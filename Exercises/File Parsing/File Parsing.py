with open('file.txt', 'r') as f:
    text = f.read()

text = text.split(' ')

instances = {}
i = 0

word = input('What word would you like to look for? ')

for index in range(0, len(text)-1):
    if text[index] == word:
        i+=1
        if index != 0:
            if instances.get(i):
                instances[i]['wordleft'] = text[index - 1]
            else:
                instances[i] = {'wordleft': text[index - 1]}
        if index != len(text) - 1:
            if instances.get(i):
                instances[i]['wordright'] = text[index + 1]
            else:
                instances[i] = {'wordright': text[index + 1]}

if word not in text:
    print(f'Could not find any instances of the word "{word}"')
else:
    instances_string = ''
    for a in range(1, len(instances)+1):
        instances_string += f'Instance {a} of the word "{word}": Word to the Left: "{instances[a].get("wordleft") if instances[a].get("wordleft") else ""}", Word to the Right: "{instances[a].get("wordright") if instances[a].get("wordright") else ""}"\n'
    print(instances_string)
