import numpy as np # for image arrays 
import PIL.Image as pil # into pil array
import gzip # open gzip file

def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)

        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels: ", nolab)

        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]

    return labels

def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)

        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("Number of images: ", noimg)

        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("Number of column: ", nocol)

        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("Number of labels: ", norow)

        #images = [f.read(1) for i in range(no_images)]
        #images = [int.from_bytes(image, 'big') for image in images]


#looping through to get pixel
        images = []

        for i in range(noimg):
            row = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                row.append(cols)
            images.append(row)

        return images

#function to print out image
def print_out_image(image_array):
    for row in image_array:
        for col in row:
            print("." if col <= 127 else "#", end="")
        print()



#train_labels = read_labels_from_file("data/train-labels-idx1-ubyte.gz")
#text_labels = read_labels_from_file("data/t10k-labels-idx1-ubyte.gz")

train_images = read_images_from_file("data/train-images-idx3-ubyte.gz")

print_out_image(train_images[4999])

img = train_images[4999]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')
img.show()
img.save('2.png')# get images to save with the label names