from pathlib import Path
import sys
import os
from PIL import Image


class S:
    SEPARATOR = '\\' if sys.platform == 'win32' else '/'


def main():
    image_folder = str(Path(sys.argv[1]))
    if not image_folder.endswith(S.SEPARATOR):
        image_folder += S.SEPARATOR

    destination_folder = str(Path(sys.argv[2]))
    if not destination_folder.endswith(S.SEPARATOR):
        destination_folder += S.SEPARATOR

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(image_folder):
        clean_name = os.path.splitext(filename)[0]
        image = Image.open(f'{image_folder}{filename}')
        image.save(f'{destination_folder}{clean_name}.png', 'png')


if __name__ == '__main__':
    main()
