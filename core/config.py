from pathlib import Path
from services import FileManager, JsonManager
from utils import log_exceptions
from .paths.path_list import JSONC_CONFIGURE
import os


class ConfigHandler:
    def __init__(self):
        self.config_path = JSONC_CONFIGURE
        self.Fm = FileManager(self.config_path)
        self.Jm = JsonManager(self.config_path)
        self.default_config = """{
  "root_dir": "~/Pictures/wallpapers",
  "static_dir": "static",
  "live_dir": "live",
  "live_extensions": [ 
    "mp4",
    "gif"
  ],
  "static_extensions": [ 
    "jpg",
    "jpeg",
    "png",
    "webp"
  ]
}"""
        self.config_data = None

    @log_exceptions
    def generate_config(self) -> None:
        data = self.Fm.read()
        if not data:
            self.Fm.write(self.default_config)

    @log_exceptions
    def get_config(self) -> dict:
        if self.config_data is None:
            self.config_data = self.Jm.get_data() or {}
        return self.config_data

    @log_exceptions
    def get_config_option(self, item: str) -> str:
        data = self.get_config()
        return data.get(item, "")

    @log_exceptions
    def get_expanded_path(self, key: str) -> Path:
        raw_path = self.get_config_option(key)
        return Path(os.path.expanduser(raw_path))

    @log_exceptions
    def get_relative_path(self, key: str) -> Path:
        raw_path = self.get_config_option(key)
        abs_path = self.get_expanded_path("root_dir")
        return Path.joinpath(abs_path, raw_path)

    @log_exceptions
    def get_live_extensions(self):
        return self.get_config_option("live_extensions")

    @log_exceptions
    def get_static_extensions(self):
        return self.get_config_option("static_extensions")


config_handler = ConfigHandler()

conf_generate_config = config_handler.generate_config
conf_get_data = config_handler.get_config
conf_get_root_dir = lambda: config_handler.get_expanded_path("root_dir")
conf_get_static_dir = lambda: config_handler.get_relative_path("static_dir")
conf_get_live_dir = lambda: config_handler.get_relative_path("live_dir")


_root = conf_get_root_dir()
if not _root:
    try:
        conf_generate_config()
        _root = conf_get_root_dir()
    except Exception:
        _root = Path.home()

DATABASE_WALLY = (_root / "database.json") if _root else Path.home() / ".database.json"
