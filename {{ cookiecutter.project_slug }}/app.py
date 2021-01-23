
import os

import uvicorn

from {{cookiecutter.project_slug}}.controller import create_app

app = create_app()


if __name__ == "__main__":
    # running with debugging purpose ** NOT for production **
    port = int(os.environ["FASTAPI_APP_PORT"]) if "FASTAPI_APP_PORT" in os.environ else 5000
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        debug=True
    )
