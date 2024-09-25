import os
import logging

import uvicorn


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("The application will be served by Uvicorn via entrypoint module!!!")
    uvicorn.run("task_manager.asgi:application", host="0.0.0.0", port=8000, workers=1)
