from pathlib import Path
import json


def return_all_skins_list(image_directory_name):
    images = []
    for image in Path(image_directory_name).glob("*entity.png"):
        images.append(image.stem.split(".")[0])
    return images


def return_all_skins_list_with_shapescape(image_directory_name):
    images = []
    for image in Path(image_directory_name).glob("*entity.png"):
        images.append("shapescape:" + image.stem.split(".")[0])
    return images


def return_all_skins_list_rc(image_directory_name):
    images = []
    for image in Path(image_directory_name).glob("*entity.png"):
        images.append("texture." + image.stem.split(".")[0])
    return images


def return_all_animation_names():
    file_path = Path("animation") / "poses.animation.json"
    # Read the JSON file
    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    # Extract animation names and remove the prefix
    animations = data.get("animations", {})
    animation_names = [
        name.replace("animation.shapescape.pose.", "") for name in animations.keys()
    ]

    return animation_names


def is_steve(image_name):
    is_steve = False
    if image_name.split("_")[1] == "s":
        is_steve = True
    return is_steve
