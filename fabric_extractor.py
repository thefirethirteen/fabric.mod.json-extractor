"""
MIT License

Copyright (c) 2022 thefirethirteen

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# fabric_extractor.py

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
