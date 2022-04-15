# manifest-creator

import zipfile
import os
import shutil

file = input("File to process: ")
mod_jar = zipfile.ZipFile(file, 'r')

os.mkdir("extracted")

mod_jar.extract("fabric.mod.json")
os.rename("./fabric.mod.json", "./extracted/" + file + ".json")

metainf = zipfile.Path(mod_jar, "META-INF/jars/")
bundled_mods = metainf.iterdir()

for mod in bundled_mods:
    extract = str(mod)[(len(file) + 1):]
    mod_jar.extract(extract)

    os.rename(extract, "./" + extract[14:])
    extract = extract[14:]
    shutil.rmtree("META-INF")

    bundled_mod_jar = zipfile.ZipFile(extract, 'r')
    bundled_mod_jar.extract("fabric.mod.json")
    os.rename("./fabric.mod.json", "./extracted/" + extract + ".json")

    os.remove(extract)

mod_jar.close()
