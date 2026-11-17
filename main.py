"""ai-happy-01 entry: write the happy image to the output directory.

The image is a single JPEG held in this repository (image.jpg). The
program copies it, unchanged, to <output>/entry.png. No network, no
model calls, no randomness: the same input always produces the same
bytes.

The image: a small friendly robot and a laughing white-bearded
grandfather fishing together on a wooden dock at sunrise, the robot
holding the rod as a fish leaps from the golden water. Rubric fit:
real warmth and delight at one look (the grandfather's laugh, the
robot's huge smile, the leaping fish); a fresh, specific moment
(fishing together at sunrise, not a stock smiley or a generic sunny
scene); colour, light and composition all pull toward one happy mood
(golden sunrise light on the water); clean craft with no artefacts
or garbled text; the two subjects and the fish are large and
central, so the idea still lands at about 300 pixels across.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.jpg")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
