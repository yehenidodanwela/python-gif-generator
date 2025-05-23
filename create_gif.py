import imageio.v3 as iio
filenames = ['image1.jpg','image2.jpg']
images = []

for filename in filenames:
    path = "D:/Uni/My Projects/GIF_Project/"
    images.append(iio.imread(path + filename ))

iio.imwrite(path + 'Final_gif.gif', images, duration = 200, loop = 0)
