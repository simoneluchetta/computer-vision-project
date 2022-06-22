import os
import numpy as np
import re

def sorted_alphanumeric(data):
    def convert(text): return int(text) if text.isdigit() else text.lower()
    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)

def import_npz(npz_dir):

    joints = []
    poses = []

    files = sorted_alphanumeric(os.listdir(npz_dir))

    for file in files:
        if file.endswith('.npz'):
            nupiezz = np.load(os.path.join(npz_dir, file))
            joints.append(nupiezz['smpl_joints'])
            poses.append(nupiezz['pose'])

    return np.array(joints), np.array(poses)

def main():
    import_npz('NPZ_OUTS')

if __name__ == '__main__':
    main()
