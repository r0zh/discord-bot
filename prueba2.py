import random

gifs = ["https://tenor.com/view/shitpost-meme-yellow-emoji-funny-meme-fuck-i-just-forgor-gif-24710392","https://tenor.com/view/baby-crib-fall-gif-7909339"]
random_gifs = []

def pick_random():
    random_gifs = []
    random.shuffle(gifs)
    length = 0
    for gif in gifs:
        if length + len(gif) <= 2000:
            random_gifs.append(gif)
            length = length + len(gif)
    return (" ").join(random_gifs)

print(pick_random())