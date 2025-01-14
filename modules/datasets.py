import torch
import pdb
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
from PIL import Image
import os
from torchvision import transforms

class DemonstrationDataset(torch.utils.data.Dataset):
  'Characterizes a dataset for PyTorch'
  def __init__(self, data_path, split="train", transform=None):
        'Initialization'
        self.data_path = data_path
        self.split = split
        self.transform = transform

        self.front_images = []
        self.side_images = []
        self.front_gestures_1 = [] #start pose
        self.side_gestures_1 = []
        self.front_gestures_2 = [] #end pose
        self.side_gestures_2 = []
        self.actions = []
        if split == "train":
            start_idx, end_idx = 0, 600
        elif split == "test":
            start_idx, end_idx = 900, 1000
        else:
            raise AttributeError("unrecognized split")
        for i in range(start_idx, end_idx):
            # print("loading "+ f'{i:03d}'+" demo")
            pathname_demo_0 = os.path.join(self.data_path, f'{i:03d}', "demonstration/0/")
            pathname_demo_1 = os.path.join(self.data_path, f'{i:03d}', "demonstration/1/")
            pathname_gesture_0 = os.path.join(self.data_path, f'{i:03d}', "gesture/0/")
            pathname_gesture_1 = os.path.join(self.data_path, f'{i:03d}', "gesture/1/")
            self.actions.append(np.load(os.path.join(self.data_path, f'{i:03d}', "demonstration/actions.npy")))
            step = 0
            for path in os.listdir(pathname_demo_0):
                front_image =  Image.open(pathname_demo_0 + path).convert('RGB')
                self.front_images.append(front_image)
                step += 1
            for path in os.listdir(pathname_demo_1):
                side_image = Image.open(pathname_demo_1 + path).convert('RGB')
                self.side_images.append(side_image)
            for path in os.listdir(pathname_gesture_0):
                if path == '0000.jpg':
                    front_gesture_1 =  Image.open(pathname_gesture_0 + path).convert('RGB')
                    for i in range(step):
                        self.front_gestures_1.append(front_gesture_1)
                else:
                    front_gesture_2 =  Image.open(pathname_gesture_0 + path).convert('RGB')
                    for i in range(step):
                        self.front_gestures_2.append(front_gesture_2)
            for path in os.listdir(pathname_gesture_1):
                if path == '0000.jpg':
                    side_gesture_1 =  Image.open(pathname_gesture_1 + path).convert('RGB')
                    for i in range(step):
                        self.side_gestures_1.append(side_gesture_1)
                else:
                    side_gesture_2 =  Image.open(pathname_gesture_1 + path).convert('RGB')
                    for i in range(step):
                        self.side_gestures_2.append(side_gesture_2)
            # print(len(self.front_images), len(self.actions))
        
        self.actions = np.concatenate(self.actions, axis = 0)
        assert len(self.front_gestures_1) == len(self.front_gestures_2)
        assert len(self.side_gestures_1) == len(self.side_gestures_2)
        # pdb.set_trace()
                    
  def __len__(self):
        'Denotes the total number of samples'
        return len(self.front_images)

  def __getitem__(self, index):
        'Generates one sample of data'
        front_image = self.front_images[index]
        side_image = self.side_images[index]
        front_gesture_1 = self.front_gestures_1[index]
        side_gesture_1 = self.side_gestures_1[index]
        front_gesture_2 = self.front_gestures_2[index]
        side_gesture_2 = self.side_gestures_2[index]
        action = self.actions[index]
        if self.transform is not None:
            front_image = self.transform(front_image)
            side_image = self.transform(side_image)
            front_gesture_1 = self.transform(front_gesture_1)
            side_gesture_1 = self.transform(side_gesture_1)
            front_gesture_2 = self.transform(front_gesture_2)
            side_gesture_2 = self.transform(side_gesture_2)
        return front_image, side_image, front_gesture_1, side_gesture_1, front_gesture_2, side_gesture_2, torch.from_numpy(action)


class OversampledDataset(torch.utils.data.Dataset):
    def __init__(self, original_dataset, oversampled_action_idx):
        self.original_dataset = original_dataset
        self.actions = self.original_dataset.actions[:, oversampled_action_idx]

        num_classes = np.unique(self.actions).shape[0]
        max_num_samples = max([np.sum(self.actions == i) for i in range(num_classes)])
        self.oversampled_indices = []
        for i in range(num_classes):
            indices = np.arange(self.actions.shape[0])[self.actions == i].tolist()
            if len(indices) != max_num_samples:
                indices += np.random.choice(indices, max_num_samples - len(indices)).tolist()
            self.oversampled_indices += indices

    def __len__(self):
        return len(self.oversampled_indices)

    def __getitem__(self, index):
        original_index = self.oversampled_indices[index]
        front_image, side_image, front_gesture_1, side_gesture_1, front_gesture_2, side_gesture_2, _ = self.original_dataset[original_index]
        action = self.actions[original_index]
        return front_image, side_image, front_gesture_1, side_gesture_1, front_gesture_2, side_gesture_2, action 
