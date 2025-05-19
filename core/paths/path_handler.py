from pathlib import Path
from services import FileManager
from core import (
    conf_get_root_dir,
    conf_get_static_dir,
    conf_get_live_dir,
    DATABASE_WALLY,
)
from .path_list import (
    LOGFILE,
    JSONC_CONFIGURE,
    TMP,
    WALLY_THUMBNAIL,
    CACHE,
    CACHE_WALLY_DIR,
)


check_exist = [
    LOGFILE,
    JSONC_CONFIGURE,
    TMP,
    WALLY_THUMBNAIL,
    CACHE,
    CACHE_WALLY_DIR,
    Path(f"{conf_get_root_dir()}"),
    Path(f"{conf_get_static_dir()}"),
    Path(f"{conf_get_live_dir()}"),
    DATABASE_WALLY,
]


Fm = FileManager
for i in check_exist:
    Fm(i).if_not_exists_create()
