import os
import uvicorn


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_manager.settings")

if __name__ == "__main__":
    uvicorn.run("task_manager.asgi:application", host="0.0.0.0", port=8000, workers=1)
