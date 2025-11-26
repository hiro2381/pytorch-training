from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):

    def __init__(self, dataset_dir):
        dir_path_resolved = Path(dataset_dir).resolve()
        self.img_list = list(dir_path_resolved.glob("**/*.png"))

    def __len__(self):
        return len(self.img_list)
    
    def __getitem__(self, idx):
        img_path = self.img_list[idx]
        img = Image.open(img_path)
        return img

if __name__ == "__main__":
    my_dataset = MyDataset("04/exercise/data")
    print("===== problem1 =====")
    print(len(my_dataset))
    print("===== problem2 =====")
    print(my_dataset[49].size)