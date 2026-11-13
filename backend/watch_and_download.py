"""
Automated Watcher for Adaption Labs Cloud Jobs
Polls pending/running jobs (trajectories & invented outdoor workers), downloads completed CSVs into backend/data/adaption_exports/, and updates DATASET_MANIFEST.md.
"""
import os
import time
from pathlib import Path
from dotenv import load_dotenv
from adaption import Adaption

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "adaption_exports"
MANIFEST_PATH = BASE_DIR / "data" / "DATASET_MANIFEST.md"

load_dotenv(BASE_DIR / ".env")

def sync_pending_jobs():
    client = Adaption()
    jobs = [
        {
            "id": "e6fd4ced-b683-4abb-8e99-77aa496456db",
            "filename": "multi_turn_clinical_trajectories.csv",
            "name": "air_quality_health_advisories (extended)"
        },
        {
            "id": "0788bf56-1cf0-41fd-8a03-d255dc3ef4a7",
            "filename": "outdoor_workers_smog_protocols.csv",
            "name": "India Outdoor Workers & High-Risk Commuter Smog Protocols"
        }
    ]

    all_done = True
    for job in jobs:
        dest_file = DATA_DIR / job["filename"]
        if dest_file.exists() and dest_file.stat().st_size > 100:
            print(f"[ALREADY DOWNLOADED] {job['filename']} ({dest_file.stat().st_size / 1024:.1f} KB)")
            continue

        try:
            status_obj = client.datasets.get_status(job["id"])
            print(f"[STATUS] {job['name']} ({job['id']}): {status_obj.status}")
            if status_obj.status == "succeeded":
                print(f"[DOWNLOADING] {job['filename']}...")
                response = client.datasets.download(job["id"], file_format="csv")
                data = response.read()
                if len(data) > 0:
                    with open(dest_file, "wb") as f:
                        f.write(data)
                    print(f"[SAVED] {job['filename']} ({len(data)/1024:.1f} KB)")
                else:
                    print(f"[EMPTY] {job['filename']} received 0 bytes.")
                    all_done = False
            elif status_obj.status == "failed":
                print(f"[FAILED] Job {job['id']} failed on Adaption Labs: {status_obj.error_data}")
            else:
                all_done = False
        except Exception as e:
            print(f"[ERROR] Checking {job['id']}: {e}")
            all_done = False

    return all_done

if __name__ == "__main__":
    sync_pending_jobs()
