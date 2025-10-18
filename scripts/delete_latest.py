import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import DAL

# Exclude baseline two projects so we don't remove them accidentally
baseline = {
    "Corporate Programs Management System",
    "Global Market Entry Strategy",
}

DAL.init_db()
DAL.ensure_baseline_projects()
deleted = DAL.delete_latest_project(exclude_titles=baseline)
if deleted:
    print(f"Deleted latest project: {deleted['title']} (id={deleted['id']})")
else:
    print("No non-baseline projects to delete.")
