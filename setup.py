from cx_Freeze import Executable, setup
import sys




build_exe_options = {
    "include_files": ["racket.png", "tenis_ball.png"]
     
}

base = None
if sys.platform == "win32":
    base = "win32GUI"


setup(
    name = "Ping Pong Game",
    version = "1.0",
    decription = "PingPong_Game",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base = base)]

)