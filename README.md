# images2byte
Write images to byte strings and saved as .pkl. And also converts byte strings to .png

## Usage
1. Download the images_byte.py into your desired folder
2. Open the folder and open terminal or cmd in the folder. Type the command:

```python
> python -m images_byte -h

usage: Images to Byte Converter [-h] -i Input Directory -o Output Directory -f Filename [-n [Num Images]] [-pkl]
                                [-png]

Converts images into byte, saved as .pkl

options:
  -h, --help            show this help message and exit
  -i Input Directory, --input-dir Input Directory
                        Input image directory
  -o Output Directory, --output-dir Output Directory
                        Output save directory
  -f Filename, --filename Filename
                        Save filename
  -n [Num Images], --num-images [Num Images]
                        Number of images to load, default=-1 (loads all images)
  -pkl, --write-byte
  -png, --write-png

Image to Bytes Converter v.0.0.1
```

3. Run code with input folder, destination folder, filename and option "-pkl" to saved images as pkl or "png" to extract images.

For example

```python
#  To save images as pkl
> python -m images_byte -i path/to/input-images -o /destination-folder -f output-filename -pkl
```

```python
# To extract images from "pkl" file and save as .png
> python -m images_byte -i path/to/input-pkl-file -o /destination-folder -f output-filename -png
```

## Citation
Please send me reference if you use this code for your work. Thank you
