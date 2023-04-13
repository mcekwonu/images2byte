#!/usr/bin/env/python


__author__ = "Ekwonu Michael C."

__date__ = "12th April 2023"


import os
import pickle
from tqdm import tqdm
from PIL import Image
from io import BytesIO
from pathlib import Path

class ImageBytes:
    """Convert images to bytes and vice versa.

    Args:
        source_dir (str): Source directory of images
        target_dir (str): Output directory to save results
        num_images (int): Number of image to load. Default is -1,
                        which loads all images in the input directory
        filename (str): Save filename
                
    Returns:
        numpy array
    """

    def __init__(self, source_dir,
                 target_dir,
                 filename,
                 num_images=-1
                  ):

        self.source_dir = source_dir
        self.target_dir = target_dir
        self.fname = filename
        self.n = num_images
              
        # Check for existence of output_dir and create if non-existent
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir, exist_ok=True)
            
    @property
    def _load_image_paths(self):
        """Load images filepaths"""

        if self.n == -1:
            img_filepaths = sorted(
                os.path.join(self.source_dir, f)
                for f in os.listdir(self.source_dir)
                if f.endswith(("tif", "png"))
            )
        else:
            img_filepaths = sorted(
                os.path.join(self.source_dir, f)
                for f in os.listdir(self.source_dir)[:self.n]
                if f.endswith(("tif", "png"))
            )

        return img_filepaths
    
    @property 
    def _load_bytes_path(self):
        """Load bytes file"""
        
        try: 
            if not self.source_dir.endswith(".pkl"):
                bytes_path = f"{self.source_dir}.pkl"
            else:
               bytes_path = self.source_dir
        except:
            raise(f"{self.source_dir} must include .pkl")
                
        if self.n:
             return bytes_path
        
        # return self.bytes_path
    
    @property
    def _write_to_pkl(self):
      """Save image bytes to pkl"""
      
      data = []

      with tqdm(desc="Loading images", leave=False, total=len(self._load_image_paths)) as progress_bar:
          for i, fp in enumerate(self._load_image_paths):
              with open(fp, "rb") as image_file: 
                  data.append(image_file.read())
                  progress_bar.update(i+1)                  
      
      with tqdm(desc="\nSaving image to bytes", leave=False) as pbar:
          with open(f"{self.target_dir}/{self.fname}.pkl", "wb") as f: 
              pickle.dump(data, f)          
              pbar.update(10)
            
    @property
    def _write_to_png(self):
        """Write bytes to image and saved as png"""
        
        out_dir = os.path.join(self.target_dir, self.fname) 
        Path(out_dir).mkdir(exist_ok=True)
                  
        with open(self._load_bytes_path, "rb") as byte_file: 
            byte_imgs = pickle.load(byte_file)
        
        with tqdm(desc="\nSaving decoded images", leave=False) as pb:
            for i, byte_im in enumerate(byte_imgs):
                im = Image.open(BytesIO(byte_im))
                im.save(f"{out_dir}/{i}.png", "PNG")
                pb.update(i+1)
        
            
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="Image to Bytes Converter",
        description="Converts images into bytes, saved as .npy, .pkl, .h5",
        epilog="%(prog)s v.0.0.1",
    )

    parser.add_argument(
        "-i",
        "--input-dir",
        type=str,
        required=True,
        help="Input image directory",
        metavar="Input Directory",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        required=True,
        help="Output save directory",
        metavar="Output Directory",
    )
    parser.add_argument(
        "-f", 
        "--filename", 
        type=str, 
        required=True,
        help="Save filename", 
        metavar="Filename"
        )
    parser.add_argument(
        "-n",
        "--num-images",
        type=int,
        nargs="?",
        default=-1,
        help="Number of images to load, default=-1 (loads all images)",
        metavar="Num Images",
    )
    parser.add_argument(
        "-pkl",
        "--write-byte",
        action="store_true",
    )
    parser.add_argument(
        "-png",
        "--write-png",
        action="store_true",
    )
    
    args = parser.parse_args()
    
    # instantiate class and run 
    image_bytes = ImageBytes(
        source_dir=args.input_dir,
        target_dir=args.output_dir,
        filename=args.filename,
        num_images=args.num_images,
        )
    
    if args.write_byte:
        image_bytes._write_to_pkl
    elif args.write_png:
        image_bytes._write_to_png