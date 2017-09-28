# Use iPython to run through some options on hexdata, nothing of interest but - check if any options on int. int.from_bytes takes two arguments, try inputting hexdata and 'big' - big/little depends on which way binary is read by your machine (left to right or right to left)

# Read gzip file adapted from https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip

def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4) 
        magic = int.from_bytes(magic,'big')
        print ("Magic is:", magic)

        nolab = f.read(4)
        nolab = int.from_bytes(nolab,'big')
        print ("Number of labels:", nolab)

        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big')for label in labels]
    return labels

train_labels  = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels  = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')