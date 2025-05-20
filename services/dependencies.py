import os
from shutil import which


class CheckDependencies:
    def __init__(self):
        self.x11 = [
            "feh",
            "mpv",
            "xwinwrap",
            "ffmpeg",
            "rofi",
            "magick",
        ]
        self.wayland = [
            "swww",
            "wlr-randr",
            "mpv",
            "ffmpeg",
            "mpvpaper",
            "rofi",
            "magick",
        ]

    def check_your_session_type(self) -> str:
        env = os.environ["XDG_SESSION_TYPE"]
        w = "wayland"
        x = "x11"
        if env == w:
            result = w
        elif env == x:
            result = x
        else:
            result = ""

        return result

    def check_dependencies(self) -> list:
        dependencies= []
        cyst = self.check_your_session_type()
        if cyst == "wayland":
            dependencies = self.wayland
        elif cyst == "x11":
            dependencies = self.x11

        missing_dependencies = []
        for i in dependencies
            if not which(i):
                missing_dependencies.append(i)

        return missing_dependencies
