# Image Entropy Generator
This Python script generates random strings by leveraging the entropy in image data. The output can be customized to include numbers and letters, divided into blocks for better readability.

## Features

- Generates random strings from image data
- Supports customizable string length and block size
- Option to include letters (uppercase and lowercase)
- Saves the output to a file for reuse

## Requirements

- Python 3.x
- Required libraries:
  - `numpy`
  - `Pillow`

Install dependencies:
```bash
pip install numpy pillow

## Usage
python image_entropy_generator.py <image_path> <string_length> <block_size> [--include_letters] [--output_file <file_name>]

## Example
python image_entropy_generator.py sample_image.jpg 50 10 --include_letters --output_file output.txt
