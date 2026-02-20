import os
import subprocess
import shutil
import sys

print("==== MAKE ANY PYTHON FILE A .EXE ====")

# file where thiz file is is
folder = os.getcwd()

# name of py thingy
bestandsnaam = input("PUT HERE NAME WITHOUT .PY  :").strip()

# path
volledig_pad = os.path.join(folder, bestandsnaam + ".py")

# if its not a file 
if not os.path.exists(volledig_pad):
    print(f"❌ FILE '{volledig_pad}' DOES NOT EXIST")
    input("PRESS ENTER TO QUIT")
    sys.exit()

# is pyinstaller installed type of shit
try:
    subprocess.run([sys.executable, "-m", "PyInstaller", "--version"], check=True, stdout=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    print("PYINSTALLERS NOT INSTALLED.... INSTALLING PYINSTALLERS")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)

print(f"compiling file, {bestandsnaam}.py → EXE...")

try:
    # put file same location as py-exe file
    subprocess.run([
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        volledig_pad
    ], check=True)

    exe_bron = os.path.join(folder, "dist", bestandsnaam + ".exe")
    exe_doel = os.path.join(folder, bestandsnaam + ".exe")

    if os.path.exists(exe_bron):
        shutil.move(exe_bron, exe_doel)

    # more shit
    shutil.rmtree(os.path.join(folder, "dist"), ignore_errors=True)
    shutil.rmtree(os.path.join(folder, "build"), ignore_errors=True)
    try:
        os.remove(os.path.join(folder, bestandsnaam + ".spec"))
    except:
        pass

    print(f"✅ DONE{exe_doel}")

except subprocess.CalledProcessError as e:
    print(f"❌ UNKNOWN COMPILING ERROR {e}")

input("PRESS ENTER TO QUIT")
