# Creating a program to create a gif image

import imageio.v2 as iio

filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.mimsave('nyan-cat.gif', images, duration=0.2, loop=0)

