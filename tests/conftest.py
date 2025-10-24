import importlib
import sys
from pathlib import Path

import pytest

import DAL


@pytest.fixture()
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "test_projects.db"


@pytest.fixture()
def app_module(db_path: Path, tmp_path: Path):
    # Ensure a clean import of the Flask app with a patched database location.
    if "app" in sys.modules:
        del sys.modules["app"]

    DAL.DB_PATH = db_path

    app_mod = importlib.import_module("app")
    app_mod.app.config["TESTING"] = True
    uploads = tmp_path / "uploads"
    uploads.mkdir(parents=True, exist_ok=True)
    app_mod.app.config["UPLOAD_FOLDER"] = str(uploads)
    return app_mod


@pytest.fixture()
def client(app_module):
    return app_module.app.test_client()

