import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import DAL


BASELINE_FILES = {
    # Protect common/seed images from accidental removal
    "project1.png",
    "project2.png",
}


def main() -> int:
    # Ensure DB is ready to query
    DAL.init_db()
    DAL.ensure_baseline_projects()

    # Images in use (from DB)
    used = set(DAL.list_image_filenames())

    # Images on disk
    root = Path(__file__).resolve().parent.parent
    images_dir = root / "static" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    removed = []
    skipped = []
    for p in images_dir.iterdir():
        if not p.is_file():
            continue
        name = p.name
        # Keep if referenced in DB or is baseline
        if name in used or name in BASELINE_FILES:
            skipped.append(name)
            continue
        # Remove unreferenced file
        try:
            p.unlink()
            removed.append(name)
        except Exception as exc:
            print(f"Failed to remove {name}: {exc}")

    print(f"Removed: {removed}" if removed else "No orphan images removed.")
    if skipped:
        print(f"Kept (in-use or baseline): {sorted(skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

