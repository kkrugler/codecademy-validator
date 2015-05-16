num_cats = 15
num_birds = 0
def increase():
    global num_cats
    num_cats = num_cats + 2
    return num_cats
while (num_cats < 20):
    if (num_cats > 12) and (increase() > 17):
        num_birds = num_birds + 1
    num_cats = num_cats + 1
print '4. %s' % num_birds
