"""Script used to convert a video into each individual frame and saves them
"""

import argparse
from pathlib import Path
from cv2 import cv2


def main():
    """Converts a video into its individual frames and saves them
    """
    parser = argparse.ArgumentParser(description='Set arguments for converting video to images')
    parser.add_argument('video_in_dir', type=str, help='select directory for video')
    parser.add_argument('--save_dir', type=str, help='select directory for frames out')
    parser.add_argument('--video_skip', type=int, default=1, help='select how many frames to skip')

    # gets our arguments from the command line
    in_arg = parser.parse_args()

    # creates the dir where the photos will be stored if it does not exist
    Path(in_arg.save_dir).mkdir(parents=True, exist_ok=True)

    # gets the video
    vidcap = cv2.VideoCapture(in_arg.video_in_dir)
    success, image = vidcap.read()
    count = 0

    while success:
        if count % in_arg.video_skip == 0:
            cv2.imwrite("{}/frame_{}.jpg".format(in_arg.save_dir, count), image)     # save frame as JPEG file
            success, image = vidcap.read()
            print(f'Read a new frame {count}: ', success)

        success, image = vidcap.read()
        count += 1


# Call to main function to run the program
if __name__ == "__main__":
    main()
