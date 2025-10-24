from pathlib import Path

import DAL


def test_database_connection(db_path: Path):
    # Point DAL at a temp database and initialize
    DAL.DB_PATH = db_path
    DAL.init_db()

    assert db_path.exists(), "Database file should be created"

    # Ensure baseline projects are inserted exactly once
    DAL.ensure_baseline_projects()
    projects = DAL.get_all_projects()
    titles = {p["title"] for p in projects}
    assert "Corporate Programs Management System" in titles
    assert "Global Market Entry Strategy" in titles


def test_insert_and_fetch_project(db_path: Path):
    DAL.DB_PATH = db_path
    DAL.init_db()
    DAL.ensure_baseline_projects()

    new_id = DAL.insert_project(
        title="Test Project",
        description="Testing insert and fetch",
        image_file_name="test.png",
    )
    assert isinstance(new_id, int) and new_id > 0

    projects = DAL.get_all_projects()
    assert any(p["title"] == "Test Project" for p in projects)
