import sqlite3
from pathlib import Path
from typing import Iterable, List, Dict, Any, Optional, Tuple

# Database file path (root of project)
DB_PATH = Path(__file__).parent / "projects.db"


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create the projects table if it doesn't exist."""
    DB_PATH.touch(exist_ok=True)
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                image_file_name TEXT NOT NULL
            )
            """
        )
        # Table ensured; baseline records are handled separately


def get_all_projects() -> List[Dict[str, Any]]:
    """Return all projects as a list of dicts (newest first)."""
    with _connect() as conn:
        rows = conn.execute(
            "SELECT id, title, description, image_file_name FROM projects ORDER BY id DESC"
        ).fetchall()
        return [dict(r) for r in rows]


def insert_project(title: str, description: str, image_file_name: str) -> int:
    """Insert a new project and return the new row id."""
    with _connect() as conn:
        cur = conn.execute(
            "INSERT INTO projects (title, description, image_file_name) VALUES (?, ?, ?)",
            (title, description, image_file_name),
        )
        conn.commit()
        return int(cur.lastrowid)


def ensure_baseline_projects() -> None:
    """Ensure the two baseline projects always exist in the database.

    If a baseline title is missing, insert it. Existing rows are left as-is.
    """
    baseline = [
        (
            "Corporate Programs Management System",
            "Prototype to manage corporate training programs: create courses, upload student data, "
            "auto-assign students to sections, and generate dynamic enrollment reports.",
            "project1.png",
        ),
        (
            "Global Market Entry Strategy",
            "Consulting project to develop a market entry strategy: trends analysis, competitive benchmarking, "
            "consumer segmentation, and implementation roadmap.",
            "project2.png",
        ),
    ]
    with _connect() as conn:
        for title, description, image_file_name in baseline:
            exists = conn.execute(
                "SELECT 1 FROM projects WHERE title = ? LIMIT 1", (title,)
            ).fetchone()
            if not exists:
                conn.execute(
                    "INSERT INTO projects (title, description, image_file_name) VALUES (?, ?, ?)",
                    (title, description, image_file_name),
                )
        conn.commit()


def delete_latest_project(exclude_titles: Optional[Iterable[str]] = None) -> Optional[Dict[str, Any]]:
    """Delete the most recent project (highest id), optionally excluding titles.

    Returns the deleted row as a dict, or None if nothing deleted.
    """
    exclude_titles = set(exclude_titles or [])
    with _connect() as conn:
        if exclude_titles:
            row = conn.execute(
                """
                SELECT id, title, description, image_file_name
                FROM projects
                WHERE title NOT IN ({placeholders})
                ORDER BY id DESC
                LIMIT 1
                """.format(placeholders=",".join(["?"] * len(exclude_titles))),
                tuple(exclude_titles),
            ).fetchone()
        else:
            row = conn.execute(
                "SELECT id, title, description, image_file_name FROM projects ORDER BY id DESC LIMIT 1"
            ).fetchone()

        if not row:
            return None

        conn.execute("DELETE FROM projects WHERE id = ?", (row["id"],))
        conn.commit()
        return dict(row)


def count_image_references(image_file_name: str) -> int:
    """Return how many projects reference the given image filename."""
    with _connect() as conn:
        (cnt,) = conn.execute(
            "SELECT COUNT(*) FROM projects WHERE image_file_name = ?", (image_file_name,)
        ).fetchone()
        return int(cnt)


def list_image_filenames() -> List[str]:
    """Return distinct image file names referenced by projects."""
    with _connect() as conn:
        rows = conn.execute("SELECT DISTINCT image_file_name FROM projects").fetchall()
        return [r[0] for r in rows]
