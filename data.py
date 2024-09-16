
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from save_load import *
import numpy as np
import time
import heapq
import cv2
import os
from save_load import *
from NNAccelerator import *
from PIL import Image
from IPython.display import display
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

import os

def load_data(infilename):
    img = Image.open(infilename)
    img.load()
    img = img.convert('RGB')
    data = np.asarray(img,dtype=np.uint8)
    return  data

    acc = NNAccelerator.NNAccelerator(preConverted=True,preAlligned=True, verboseLevel=4, dmaSafe=True)

    acc.verboseLevel = 2

    layer = 'dense_3'
    outputs2 = acc.variableExtract(acc.outputs[layer][acc.layers[layer].finalOutIdx], 5)
    classes = heapq.nlargest(5, range(len(outputs2)), outputs2.__getitem__)

    for i in range(5):
        print('    ', classes[i] + 1, outputs2[classes[i]])

    print(acc.softmax(outputs2), np.sum(acc.softmax(outputs2)))


def fpga_program(num_flip_flops, num_luts):
    # Create a random LUT (Look-Up Table)
    lut = np.random.randint(0, 2, size=(num_luts, 2))

    # Create a random flip-flop input sequence
    flip_flop_input = np.random.randint(0, 2, size=num_flip_flops)

    # Simulate the flip-flops
    flip_flop_output = np.zeros(num_flip_flops, dtype=np.int32)
    for i in range(num_flip_flops):
        flip_flop_output[i] = lut[flip_flop_input[i], 0] ^ lut[flip_flop_output[i - 1], 1]

    return lut, flip_flop_input, flip_flop_output


def read_video(video_path):
    frames = []
    labels = []

    # Your code to read frames and labels from the video
    # For demonstration purposes, let's assume each frame has a label (0 or 1)
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop if there are no more frames
        frames.append(frame)
        labels.append(0)  # Replace with your logic to assign labels

    cap.release()
    return frames, labels


def read_videos_from_folder(folder_path):
    video_data = []
    video_labels = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            video_path = os.path.join(folder_path, filename)
            frames, labels = read_video(video_path)
            video_data.append(frames)
            video_labels.append(labels)

    return video_data, video_labels



folder_path = 'Dataset/nfl-impact-detection/data'
videos, labels = read_videos_from_folder(folder_path)

x_train, x_test, y_train, y_test = train_test_split(videos, labels)
save("x_train",x_train)
save("x_test",x_test)
save("y_train",y_train)
save("y_test",y_test)




