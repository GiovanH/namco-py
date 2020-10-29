import glob
import bs4
import os
import re
import argparse
import namco
import textwrap
from pprint import pprint

scenes_glob = ["scripts/namcohigh/scenes/s_day0.xml",]

def fixname(char):
    fixes = {
        "valkyria": "valkyrie",
        "don": "donko",
        # "valkyria": "valkyrie"
    }
    return fixes.get(char, char)

def makeBackgrounds():
    os.makedirs("game/rpy", exist_ok=True)
    with open("game/rpy/backgrounds.rpy", "w") as rpy_file:
        for folder in ["bg", "event", "battlepose", "credits"]:
            for image_path in glob.glob(f"images/namcohigh/{folder}/*.*"):
                image_path = image_path.replace("\\", "/")
                __, image_name = os.path.split(image_path)
                image_name_plain, image_ext = os.path.splitext(image_name)

                image_identifier = f"i_{folder}_{image_name_plain}".replace("-", "_")
                rpy_line = f'image {image_identifier} = "{folder}/{image_name}"\n'
                rpy_file.write(rpy_line)
            rpy_file.write("\n")

def makeCharacters():
    os.makedirs("game/rpy/portrait", exist_ok=True)
    for folder in glob.glob(f"images/namcohigh/portrait/*"):
        char_name = os.path.split(folder)[1]
        fixed_name = fixname(char_name)
        with open(f"game/rpy/portrait/{char_name}.rpy", "w") as rpy_file:
            for image_path in glob.glob(f"{folder}/*.*"):
                image_path = image_path.replace("\\", "/")
                __, image_name = os.path.split(image_path)
                image_name_plain, image_ext = os.path.splitext(image_name)

                image_identifier = f"i_{fixed_name}_{image_name_plain}"
                rpy_line = f'image {image_identifier} = "portrait/{char_name}/{image_name}"\n'
                rpy_file.write(rpy_line)
            # rpy_file.write(makeSayer(fixed_name))

def makeSayer(char_name):
    return f'define {char_name} = Character("{char_name}")\n'

xml = None

def convertFile(scene_file):
    global xml
    with open(scene_file, "r", encoding="utf-8") as fp:
        xml = bs4.BeautifulSoup(fp.read(), features="lxml-xml")

    for tag in xml.findAll(recursive=False):
        # print(tag.name)
        if tag.name == "scene":
            scene = namco.Scene.fromTag(tag)
            # print(scene)
            with open(f"game/rpy/{scene.id}.rpy", "w", encoding="utf-8") as rpyfile:
                rpyfile.write(scene.toRpy())
        else:
            raise NotImplementedError(tag.name)

if __name__ == "__main__":
    makeCharacters()
    makeBackgrounds()
    for g in scenes_glob:
        for scene_file in glob.glob(g):
            try:
                convertFile(scene_file)
            except:
                print(scene_file)
                raise
