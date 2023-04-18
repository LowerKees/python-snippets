import glob
import io
import pathlib
import zipfile
import os
import shutil

root_path = pathlib.Path("C:\\", "Users", "marti", "Downloads", "diag")

zip_dir = root_path.joinpath("loadDate=2023-01-12")
os.chdir(zip_dir)
zip_files = glob.glob("*diag*.xml.zip")

os.chdir(path=root_path.joinpath("unzipped"))

iterator = 0

for zip_file in zip_files:
    iterator += 1
    with open(zip_dir.joinpath(zip_file), "rb") as zip_bytes:
        buffer = io.BytesIO(zip_bytes.read())
        zipfile.ZipFile(buffer, mode="r").extractall(path=zip_file.replace(".xml.zip", ""))

xml_files = glob.glob("*/*.xml", recursive=True)

for xml_file in xml_files:
    shutil.move(xml_file, root_path.joinpath("all"))
