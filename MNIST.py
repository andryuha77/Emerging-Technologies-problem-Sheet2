# MNIST Problem Sheet 

import numpy as np # for image arrays 
import PIL.Image as pil # into pil array
import gzip # open gzip file

# # Read Labels function.
def read_labels_from_file(filename):
    # r stands for read, b - byes 
    with gzip.open(filename, 'rb') as f:
        # Gets Magic number by reading in the first 4 bytes and converts into an int
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)
        
        # Reads the next 4 byts for labels
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels: ", nolab)

        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]

    return labels

# Read Images Function.
def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        #Read magic number
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic is: ", magic)

        # Next 4 bytes = number of items (images)
        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("Number of images: ", noimg)
        
        # number of columns
        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("Number of column: ", nocol)

        #number of rows
        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("Number of labels: ", norow)

#looping through to get pixel
        images = []

        for i in range(noimg):
            row = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    # add the current pixel to the column array
                    cols.append(int.from_bytes(f.read(1), 'big'))
                #add the column array    
                row.append(cols)
            images.append(row)
        # Return the image array
        return images

#function to print out image to the Console
def print_out_image(image_array):
    for row in image_array:
        for col in row:
            print("." if col <= 127 else "#", end="")
        print()

train_images = read_images_from_file("data/train-images-idx3-ubyte.gz")

print_out_image(train_images[4999])

#Output image files as PNGs.
img = train_images[4999]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')
img.show()
# get images to save with the label names
img.save('2.png')
