import os
import numpy as np

# Lib to work with .tif
import imagery_helper

# Find the current working directory
path = os.getcwd()

# Grab path to data folder
if os.path.isdir(os.path.join(path, 'Data')) == False:
    raise Exception('Data directory does not exist, run retrieve script')
data_dir_path = os.path.join(path, 'Data')


# Path to our imagery
src_path = "/home/facu/Desktop/HackathonMcGill2020/afghanistan.tif"

# path to output image
out_path = '/home/facu/Desktop/HackathonMcGill2020/afghanistanProcessed.tif'

# load
satdat = imagery_helper.load(src_path)

# display info
imagery_helper.info(satdat)

# scale to uint8
imagery_helper.scale_pixels(src_path, out_path, min=0, max=10000)

# compress
imagery_helper.compress(out_path, out_path, compression_type='JPEG')

print(f'Compression done, file can be found {out_path}')