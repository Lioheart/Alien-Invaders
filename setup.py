import cx_Freeze

executables = [
    cx_Freeze.Executable("alien_invasion.py",
    base = "Win32GUI",
    icon = "ufo.ico")
    ]

cx_Freeze.setup(
    name="Alien Invasion",
    version = "1.0",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["images"]}},
    executables = executables
    )