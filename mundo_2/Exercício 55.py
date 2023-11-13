# Ask for 5 weights and pick up the major and the minor
major = 0
minor = 0
for c in range(1, 6):
    weight = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        major = weight
        minor = weight
    else:
        if weight > major:
            major = weight
        if weight < minor:
            minor = weight
print("The heavier is {}kg and the thinner is {}kg!".format(major, minor))