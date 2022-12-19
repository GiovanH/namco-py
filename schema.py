import glob
import bs4
import collections
import tqdm

scenes_glob = ["scripts/namcohigh/scenes/*.xml",]

all_tag_fingerprints = {}
all_tag_contents = {}

ignoretypes = [str, None]
def typeset(contents):
    l = [(t.name if t.name else type(t)) for t in contents]
    return frozenset(l)

def classcase(title):
    if not title:
       return ''
    return title[0].upper() + title[1:]

def convertFile(scene_file):
    global xml
    with open(scene_file, "r", encoding="utf-8") as fp:
        xml = bs4.BeautifulSoup(fp.read(), features="lxml-xml")

    for tag in xml.findAll(recursive=True):
        all_tag_fingerprints[tag.name] = all_tag_fingerprints.get(tag.name, []) + [
            tag.attrs
        ]
        all_tag_contents[tag.name] = all_tag_contents.get(tag.name, []) + [typeset(tag.contents)]


if __name__ == "__main__":
    for g in scenes_glob:
        for scene_file in tqdm.tqdm(glob.glob(g)):
            try:
                convertFile(scene_file)
            except:
                print(scene_file)
                raise
    with open("schema.md", "w") as fp:
        for tagname in all_tag_fingerprints:
            fp.write(f"### {tagname}\n")

            shown_keys = set()
            i = 1
            for contentset in all_tag_contents[tagname]:
                if contentset not in shown_keys:
                    shown_keys.add(contentset)
                    fp.write(f"\nContent variant {i}:\n")
                    i += 1
                    if not contentset:
                        fp.write("- (Empty)\n")
                    for k in contentset:
                        fp.write(f"- `{k}`\n")

            shown_keys = set()         
            i = 1
            all_keysets = [frozenset(tag.keys()) for tag in all_tag_fingerprints[tagname]]
            for tag in all_tag_fingerprints[tagname]:
                keyset = frozenset(tag.keys())
                if keyset not in shown_keys:
                    shown_keys.add(keyset)
                    fp.write(f"\nAttribute variant {i}:\n")
                    i += 1
                    if not tag:
                        fp.write("- (Empty)\n")
                    for k, v in tag.items():
                        optional = " (optional)" if not all(k in s for s in all_keysets) else ""
                        fp.write(f"- `{k}` (`{v}`){optional}\n")
            fp.write("\n")

    with open("template.py", "w") as fp:
        names = sorted(list(all_tag_fingerprints.keys()))

        def isProp(tagname):
            ever_has_attrs = any(a for a in all_tag_fingerprints[tagname])
            always_has_content = all(a for a in all_tag_contents[tagname])
            return (always_has_content and not ever_has_attrs)

        for tagname in [n for n in names if not isProp(n)]:
            fp.write(f"class {classcase(tagname)}(Node):\n    pass\n\n")

        fp.write('NODE_TYPES = {\n')
        for tagname in [n for n in names if not isProp(n)]:
            fp.write(f'    "{tagname}": {classcase(tagname)},\n')
        fp.write('}\n')

        fp.write('PROPERTY_NODES = [\n')
        for tagname in [n for n in names if isProp(n)]:
            fp.write(f'    "{tagname}",\n')
        fp.write(']\n')