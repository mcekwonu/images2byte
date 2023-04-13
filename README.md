# images2bytes
Write images to byte strings and saved as .pkl. And also converts byte strings to .png

## Usage
1. Download the image_bytes.py into your desired folder
2. Open the folder and open terminal(if you are using Linux OS) or cmd(if you are using Windows OS) and type the command:

```python
> python -m image_bytes -h (To see the help and arguments to pass)
```

3. Run code with input folder, destination folder, filename and option "-pkl" to saved images as pkl or "png" to extract images.

For example
To save images as pkl
```python
> python -m images_byte -i path/to/input-images -o /destination-folder -f output-filename -pkl
```

To extract images from "pkl" file and save as .png
```python
> python -m images_byte -i path/to/input-pkl-file -o /destination-folder -f output-filename -png
```

## Citation
Please send me reference if you use this code for your work. Thank you
