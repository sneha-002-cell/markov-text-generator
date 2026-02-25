import random

text = "AI is the future. AI improves automation. Automation improves efficiency."

words = text.split()
chain = {}

for i in range(len(words) - 1):
    chain.setdefault(words[i], []).append(words[i + 1])

word = random.choice(words)
result = [word]

for _ in range(20):
    next_words = chain.get(word)
    if not next_words:
        break
    word = random.choice(next_words)
    result.append(word)

print("Generated Text:")
print(" ".join(result))
