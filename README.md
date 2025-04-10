<h1>🛰️ ZEBES - Zone for Emulated Behavior of External Services</h1>

<p align="center">
  <img src="static/zebes_park.png" alt="Zebes Park Logo" width="450"/>
</p>

<p>
  <b>A mock server inspired by Metroid, built for developers stranded outside the corporate network.</b><br/>
  Simulate critical services like Artifactory, Bitbucket, Vault, Nubecica and more — without needing VPN access.<br/>
</p>

---

🪐 **ZEBES** is a lightweight mock server with a retro-futuristic flair, designed to help you run integration tests even when you're working completely offline.

> When you're trapped in the remote sector of your home — no VPN, no network, no backtracking —
> **ZEBES** is your only hope to survive development.

---

🔧 **Currently Mocked Services**:

- `/artifactory` — binary uploads, repository lookups
- `/bitbucket` — repository and branch endpoints
- `/vault` — secrets and token handling
- `/nubecica` — mystical internal cloud logic (coming soon)

---

📑 **Table of Contents**

- [🔧 Setup \& Deployment](#-setup--deployment)
  - [🛠️ Local Development](#️-local-development)
  - [🐳 Running with Docker](#-running-with-docker)
  - [📦 Virtual Environment Setup](#-virtual-environment-setup)
  - [📜 Managing Dependencies](#-managing-dependencies)
  - [💡 Developer Tips](#-developer-tips)
- [📘 API Documentation](#-api-documentation)
- [🧪 Adding New Mocks](#-adding-new-mocks)
- [🤝 Contributing](#-contributing)

---

## 🔧 Setup & Deployment
> _“Initializing local uplink to ZEBES... Scanning environment... VPN signal lost... Mock reactor engaged.”_

---

### 🛠️ Local Development

> For rapid iteration when developing or extending ZEBES modules.

```bash
uvicorn app.main:app --reload
```

- Accessible at: `http://localhost:8000`
- Auto-reloads on file changes
- Ideal for debugging and exploring new sectors 🛰️

---

### 🐳 Running with Docker

> Launch ZEBES from your command deck, fully isolated and containerized.

```bash
docker-compose up --build
```

- Accessible at: `http://localhost:8000`
- Recommended for team-wide use or sandboxing enemy APIs

---

### 📦 Virtual Environment Setup

> Before entering the system, suit up properly.

```bash
python -m venv venv
```

Activate the environment:

```bash
# Windows cmd
./venv/Scripts/activate.bat

# Windows powershell
./venv/Scripts/activate.ps1

# Linux / macOS
source venv/bin/activate
```

### 📜 Managing Dependencies

> Keeping your arsenal light and efficient.

First, install pip-tools package:

```bash
pip install pip-tools
```

Generate the requirements file with compatible versions:

```bash
pip-compile requirements.in
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 💡 Developer Tips

- 🧠 Use --reload in dev to auto-reboot when files change.
- 🔍 Inspect /openapi.json if docs fail to load.
- ⚠️ If you’re stuck in a “sector” without internet (aka home-office without VPN), remember:
ZEBES is self-contained. Just launch and survive.

## 📘 API Documentation

> "Scanning system schema... Weapon system: REST. Visual interface: ONLINE."

ZEBES automatically generates OpenAPI documentation for all mocked endpoints:

- 🛰️ **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
  Interactive interface to test and explore all mocked APIs.

- 🧬 **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
  Clean, readable API docs ideal for browsing or sharing with teams.

- 🧾 **OpenAPI JSON**: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)
  Machine-readable schema if you want to generate clients or validate contract tests.

## 🧪 Adding New Mocks

> "A new sector has been discovered. Integration required."

You can extend ZEBES with custom mocks per service:

1. **Add a new router** under `app/routes/`. For example: `gitlab.py`
2. Define your endpoints using FastAPI:
    ```python
    from fastapi import APIRouter

    router = APIRouter()

    @router.get("/projects")
    def list_projects():
        return [{"name": "Mocked Project"}]
    ```
3. Register your new router in `main.py`:
    ```python
    from app.routes import gitlab
    app.include_router(gitlab.router, prefix="/gitlab", tags=["GitLab"])
    ```
4. Restart the server — your new sector is live.

## 🤝 Contributing

> "Suit up, bounty hunter. We have work to do."

Whether you're fixing a bug, mocking a new service, or improving documentation — we welcome your help.

---

### ✅ Guidelines

- Use clear, consistent naming (`/vault`, `/bitbucket`, etc.)
- Keep mock data in `app/mocks/` per service
- Use `tags=["ServiceName"]` so endpoints are grouped in docs
- Favor realism in endpoints: mimic HTTP codes, delays, or edge cases

---

### 🧪 Useful commands

```bash
# Run server
uvicorn app.main:app --reload

# Format code
black .

# Check types
mypy app/