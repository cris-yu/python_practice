import os
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", "beautifulsoup4", "wheel", "networkx",
        "sympy", "django", "falsk", "werobot", "pyqt5", "pandas", "pyopengl", "docopt", "pygame"}
try:
    for lib in libs:
        os.system("pip install "+lib)
    print("sucessful")
except lib not in libs:
    print("failed somehow")
