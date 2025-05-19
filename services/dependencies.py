import os
from shutil import which

x11 = [
    "feh",
    "mpv",
    "xwinwrap",
    "ffmpeg",
    "rofi",
    "magick",
]

wayland = [
    "swww",
    "wlr-randr",
    "mpv",
    "ffmpeg",
    "mpvpaper",
    "rofi",
    "magick",
]


def check_your_session_type() -> list | None:
    env = os.environ["XDG_SESSION_TYPE"]
    if env == "wayland":
        dependencies = wayland
    elif env == "x11":
        dependencies = x11
    else:
        return

    missing_dependencies = []
    for i in dependencies:
        if not which(i):
            missing_dependencies.append(i)
