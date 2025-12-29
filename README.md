# Envsafe

**Envsafe** is a lightweight Python utility for **safe, structured, and explicit environment variable management**.
It helps you load, validate, parse, and access environment variables without silently failing or scattering `os.getenv()` calls across your codebase.

> If an environment variable is missing, malformed, or unsafe — Envsafe makes it obvious.

---

## Why Envsafe?

Most Python projects handle environment variables like this:

```python
import os
DB_URL = os.getenv("DB_URL")
```

This has problems:

* Missing variables fail **silently**
* No type safety
* No validation
* No central place to manage env logic

**Envsafe fixes this** by giving you:

* Explicit loading
* Typed parsing
* Clear errors
* Centralized configuration logic

---

## Features

* ✅ Safe loading of environment variables
* ✅ Custom parsers for type conversion
* ✅ Explicit, readable access patterns
* ✅ Meaningful exceptions (no silent failures)
* ✅ Minimal, dependency-light design
* ✅ Works with `.env` files and system environment

---

## Project Structure

```text
envsafe/
├── src/envsafe/
│   ├── __init__.py
│   ├── core.py         # Core environment access logic
│   ├── exceptions.py   # Custom exception types
│   ├── loaders.py      # Environment loading utilities
│   └── parsers.py      # Type parsing and validation
│
├── tests/              # Unit tests
├── demo.py             # Minimal usage example
│
├── pyproject.toml      # Package configuration (Poetry)
├── poetry.lock
├── README.md
├── LICENSE
└── .python-version
```

---

## Installation

Once published:

```bash
pip install envsafe
```

For development (Poetry):

```bash
git clone https://github.com/your-username/envsafe.git
cd envsafe
poetry install
```

---

## Quick Start

### 1. Define your environment variables

```bash
export API_KEY="secret-key"
export TIMEOUT="30"
```

Or using a `.env` file:

```env
API_KEY=secret-key
TIMEOUT=30
```

---

### 2. Use Envsafe in your code

```python
from envsafe import env

api_key = env.get("API_KEY")
timeout = env.get_int("TIMEOUT")
```

If `API_KEY` is missing → **exception is raised immediately**.

---

## Core Concepts

### Safe Access (No Silent Failures)

```python
env.get("DATABASE_URL")
```

* Raises a clear exception if the variable does not exist
* Prevents misconfigured deployments from going unnoticed

---

### Typed Parsing

```python
env.get_int("PORT")
env.get_bool("DEBUG")
env.get_float("THRESHOLD")
```

Invalid values (e.g. `"abc"` for an int) raise descriptive errors.

---

### Defaults (Explicit Only)

```python
env.get("REGION", default="us-east-1")
```

Defaults are **opt-in**, never implicit.

---

## Error Handling

Envsafe defines **custom exception types** so you can handle failures cleanly:

```python
from envsafe.exceptions import EnvVarNotFoundError

try:
    secret = env.get("SECRET_KEY")
except EnvVarNotFoundError as e:
    print(e)
    exit(1)
```

This makes failures:

* Predictable
* Testable
* Easy to debug

---

## Demo

Run the included demo:

```bash
python demo.py
```

This demonstrates:

* Loading variables
* Parsing values
* Handling missing configuration

---

## Testing

```bash
poetry run pytest
```

Tests are isolated, deterministic, and do not rely on your system environment.

---

## Design Philosophy

* **Explicit > Implicit**
* **Fail fast > Fail silently**
* **Small surface area**
* **No magic**

Envsafe is intentionally simple.
It does one thing well: **environment safety**.

---

## Roadmap

Planned improvements:

* Schema-based env validation
* Grouped config objects
* Optional dotenv auto-loading
* Better IDE type hints

---

## License

This project is licensed under the **MIT License**.
See [`LICENSE`](LICENSE) for details.

---

## Contributing

Contributions are welcome.

1. Fork the repo
2. Create a feature branch
3. Add tests
4. Open a PR with a clear description

---

## Author

Built with care to solve a real problem faced in production Python systems.

---
