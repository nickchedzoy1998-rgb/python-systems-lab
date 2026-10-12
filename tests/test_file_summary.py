from pathlib import Path
import pytest
from collections import Counter

from src.python_systems_lab.file_summary import count_files_by_extension

FOLDER_FILES_MAP = {
    "user_data": ["profiles.json", "export.csv", "notes.txt", "settings.json", "USER_LOGS"],
    "financials": ["q3_report.csv", "budgets.json", "audit_summary.txt", "invoices.csv", "TRANSACTIONS"],
    "system_logs": ["error.txt", "access.json", "server_metrics.csv", "debug.txt", "SYSLOG"],
    "app_config": ["settings.json", "routes.csv", "env_vars.json", "setup_instructions.txt", "CONFIG"],
    "media_metadata": ["catalog.csv", "tags.json", "description.txt", "index.csv", "MANIFEST"],
}

paths = (
    Path("sales.csv"),
    Path("customers.csv"),
    Path("settings.json"),
    Path("profiles.json"),
    Path("events.json"),
    Path("README"),
)

@pytest.fixture
def populated_folders(tmp_path: Path) -> list[Path]:
    folder_paths = []

    for folder_name, files in FOLDER_FILES_MAP.items():
        folder = tmp_path /folder_name
        folder.mkdir()
        folder_paths.append(folder)

        for file_name in files:
            (folder / file_name).touch()

    return folder_paths

def test_count_files_by_extension() -> None:
    extension_counts = count_files_by_extension(paths)

    expected_result = {
        ".csv": 2,
        ".json": 3,
    }

    assert extension_counts == expected_result