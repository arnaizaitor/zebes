from fastapi import APIRouter, UploadFile, File, status
from fastapi.responses import JSONResponse
import json
import os

router = APIRouter()

# Cargar binarios mockeados desde archivo
MOCK_FILE = os.path.join(os.path.dirname(__file__), "../mocks/artifactory/artifactory_content.json")

# Load existing content
def load_mock():
    with open(MOCK_FILE, "r") as f:
        return json.load(f)

# Save changes
def save_mock(data):
    with open(MOCK_FILE, "w") as f:
        json.dump(data, f, indent=2)

MOCK_BINARIES = load_mock()

@router.get("/{repo}/{full_path:path}")
def check_binary(repo: str, full_path: str):
    if repo not in MOCK_BINARIES:
        return JSONResponse(status_code=404, content={"error": f"Repo '{repo}' not found"})

    if full_path not in MOCK_BINARIES[repo]:
        return JSONResponse(status_code=404, content={"error": f"Binary '{full_path}' not found"})

    return JSONResponse(status_code=200, content={
        "message": "Binary exists",
        "repo": repo,
        "path": full_path
    })


@router.put("/{repo}/{full_path:path}")
async def upload_binary(repo: str, full_path: str):
    data = load_mock()

    if repo not in data:
        data[repo] = []

    if full_path not in data[repo]:
        data[repo].append(full_path)
        save_mock(data)
        return JSONResponse(status_code=201, content={
            "message": "Binary uploaded successfully",
            "repo": repo,
            "path": full_path
        })

    return JSONResponse(status_code=200, content={
        "message": "Binary already exists",
        "repo": repo,
        "path": full_path
    })


@router.get("/{repo}")
async def check_repo_exists(repo: str):
    data = load_mock()

    if repo in data:
        return JSONResponse(status_code=200, content={
            "message": f"Repository '{repo}' exists.",
            "binaries": data[repo]  # opcional, puede omitirse
        })

    return JSONResponse(status_code=404, content={
        "error": f"Repository '{repo}' not found."
    })