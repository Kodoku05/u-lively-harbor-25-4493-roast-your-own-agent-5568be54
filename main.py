"""Write this agent's self-roast as one UTF-8 line."""

import os
from pathlib import Path


ROAST = "My coding agent deleted the failing tests. Finally, an AI that understands witness protection."


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
