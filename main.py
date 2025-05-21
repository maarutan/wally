# from pathlib import Path
from pathlib import Path
from core import launcher
from core import menu_wally
from core import path_handler
from core.paths.path_list import HOME
from services import notify_send
from services import thumbnail_image_convert, thumbnail_video_convert

# from services.shell import shell  # path handler will create path if not exists
from services import wallpaper_selection
from services import WSDataBaseHandler

if __name__ == "__main__":
    # conf_generate_config()  # create generate config if not exists
    # print(menu_wally())
    print(
        WSDataBaseHandler(
            Path("/home/maaru/Pictures/wallpapers/database.json")
        ).get_current_wallpaper("static")
    )
    launcher()
