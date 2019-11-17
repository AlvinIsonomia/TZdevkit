import os
import tifffile
import numpy as np
from tqdm import tqdm
def tiff2npy(input_dir,output_dir,shape_file = False):
    '''
    shape_file will be a path of txt containing shape of each iamge with its basename
    '''
    tiffs = os.listdir(input_dir)
    if shape_file:
        f = open(shape_file,'w')
        for tiff in tqdm(tiffs):
            basename = os.path.splitext(tiff)[0]
            img = tifffile.imread(os.path.join(input_dir,tiff))
            img_shape = img.shape
            line = basename +' '+ ' '.join([str(i) for i in img_shape]) + '\n'
            f.write(line)
            np.save(os.path.join(output_dir,basename+'.npy'),img)
    else:
        for tiff in tqdm(tiffs):
            basename = os.path.splitext(tiff)[0]
            img = tifffile.imread(os.path.join(input_dir,tiff))
            img_shape = img.shape
            np.save(os.path.join(output_dir,basename+'.npy'),img)


def get_shape(shape_file):
    '''
    return a dict, {'basename of numpy' : [shape list]}
    '''
    shape_dict = {}
    with open(shape_file) as f:
        lines = f.readlines()
    for line in tqdm(lines):
        tmp_list = line.split()
        shape_dict[tmp_list[0]] = tuple([int(i) for i in tmp_list[1:]])
    # print(len(shape_dict))
    return shape_dict

def npread_plus(np_name,input_dict,input_type = 'uint8'):
    '''
    Want some shape_dict? RUN get_shape!
    '''
    shape_tuple = input_dict[os.path.splitext(np_name)[0].split('/')[-1]]
    mapmem = np.memmap(np_name,dtype=input_type,mode='r',shape=shape_tuple)
    # print(mapmem)
    return mapmem




if __name__ == '__main__':
    input_dir = '//data/datasets/DOTA/TZ/tiff'
    output_dir = '//data/datasets/DOTA/TZ/images'
    shape_file = '//data/datasets/DOTA/TZ/shape_file.txt'
    tiff2npy(input_dir,output_dir,shape_file)
    
    shape_dict = get_shape(shape_file)

    npys = os.listdir(output_dir)
    # for npy in npys:
    npread_plus(np_name = os.path.join(output_dir,npys[0]), input_dict = shape_dict)
