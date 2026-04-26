import json
import os
import time

MOUNT_PATH = "/mnt/ecs"


def main():
    timestamp = int(time.time())
    filename = f"demo-{timestamp}.txt"
    filepath = os.path.join(MOUNT_PATH, filename)
    content = f"Hello from ECS! Written at {timestamp}"

    with open(filepath, "w") as f:
        f.write(content)

    files = os.listdir(MOUNT_PATH)
    print(json.dumps({"files_in_mount": files[:20]}))


if __name__ == "__main__":
    main()
