# from pathlib import Path
from core import launcher
from core import menu_wally
from core import path_handler
from core.paths.path_list import HOME

# from services import rofi, check_your_session_type
# from services.shell import shell  # path handler will create path if not exists
from services import WSH


if __name__ == "__main__":
    # conf_generate_config()  # create generate config if not exists
    # print(menu_wally())
    launcher()
    # print(conf_get_root_dir())
