import os
from tqdm import tqdm


def DataFilter(input_dir):
    count = 0
    empty = 0
    imgs_dir = os.path.join(input_dir,'images')
    labels_dir = os.path.join(input_dir,'labels')
    basenames = os.listdir(imgs_dir)
    for basename in tqdm(basenames):
        basename = os.path.splitext(basename)[0]
        with open(os.path.join(labels_dir,basename + '.txt')) as f:
            lines = f.readlines()
        if len(lines) == 0:
            os.remove(os.path.join(labels_dir,basename + '.txt'))
            os.remove(os.path.join(imgs_dir,basename + '.npy'))
            empty += 1
        else:
            count += 1
    print('For',count+empty,'totally\n','There are ',count,'figures with annotations, ',
            str(empty),'removed') 

if __name__ == '__main__':
    input_dir = '//data/datasets/DOTA/TZ/split'
    DataFilter(input_dir)