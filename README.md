## Image Entropy Generator
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

## Install Dependencies
Install the required libraries using pip:
```bash
pip install numpy pillow
```

##  Usage
python image_entropy_generator.py <image_path> <string_length> <block_size> [--include_letters] [--output_file <file_name>]

### Arguments

-  <image_path>: Path to the image file (e.g., sample_image.jpg).
-  <string_length>: Length of the random string to generate (positive integer).
-  <block_size>: Size of each block in the output (positive integer).
-  --include_letters: Include uppercase and lowercase letters in the output (optional).
-  --output_file: Name of the file to save the output (default: generated_strings.txt).

## Example
```bash
python image_entropy_generator.py sample_image.jpg 50 10 --include_letters --output_file output.txt
```

OUTPUT:

The script generates a random string and saves it in a file that will look something like this:
```bash
123ab456cd
789ef012gh
...
```
## License
This project is licensed under the MIT License. See the [MIT License](License) file for details.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## Author
LODGE Shaquille
