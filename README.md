# Chrome Extension Icon Generator

This script simplifies the process of creating icons for Chrome extension development. It automatically resizes a high-resolution base image into multiple standard icon sizes required by Chrome extensions.

## Features

- Resizes a single high-resolution image into multiple icon sizes.
- Supports standard Chrome extension icon sizes: 16x16, 19x19, 32x32, 38x38, 48x48, and 128x128 pixels.
- Automatically creates an output directory for the generated icons.

## Requirements

- Python 3.x
- Pillow library (for image processing)

## Installation

1. Clone the repository or download the script.
2. Install the required library using pip:

   ```bash
   pip install Pillow
   ```

## Usage

1. Place your high-resolution base image (e.g., `icon.png`) in the same directory as the script.
2. Run the script:

   ```bash
   python gen.py
   ```

3. The resized icons will be saved in a folder named `icons`.

## Example

Given a base image named `icon.png`, running the script will generate the following icons in the `icons` folder:

- icon16.png
- icon19.png
- icon32.png
- icon38.png
- icon48.png
- icon128.png
