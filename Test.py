pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

track = []

answer = input()

if answer in pasta:
    track.append('pasta')
if answer in apple_pie:
    track.append('apple pie')
if answer in ratatouille:
    track.append('ratatouille')
if answer in chocolate_cake:
    track.append('chocolate cake')
if answer in omelette:
    track.append('omelette')

for value in track:
    print(value + ' time!')
