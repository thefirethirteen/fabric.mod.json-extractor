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

# fabric_extractor_all.py
# Extracts just the `fabric.mod.json` of the mod file provided

import sys
import zipfile
import os

file = sys.argv[1]
mod_jar = zipfile.ZipFile(file, 'r')

os.mkdir("extracted")

mod_jar.extract("fabric.mod.json")
os.rename("./fabric.mod.json", "./extracted/" + file + ".json")

mod_jar.close()
