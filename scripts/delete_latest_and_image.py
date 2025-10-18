import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
import DAL


BASELINE_TITLES = {
    "Corporate Programs Management System",
    "Global Market Entry Strategy",
}


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    images_dir = root / "static" / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    DAL.init_db()
    DAL.ensure_baseline_projects()

    deleted = DAL.delete_latest_project(exclude_titles=BASELINE_TITLES)
    if not deleted:
        print("No non-baseline projects to delete.")
        return 0

    title = deleted["title"]
    img = deleted.get("image_file_name")
    print(f"Deleted latest project: {title} (id={deleted['id']})")

    removed_image = False
    if img:
        remaining = DAL.count_image_references(img)
        if remaining == 0:
            path = images_dir / img
            if path.exists():
                try:
                    path.unlink()
                    removed_image = True
                except Exception as exc:
                    print(f"Warning: failed to remove image {img}: {exc}")

    if removed_image:
        print(f"Removed orphan image: {img}")
    else:
        if img:
            print(f"Image kept: {img} (still referenced or not found)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

