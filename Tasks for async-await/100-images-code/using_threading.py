import threading
import requests
from pathlib import Path
import time
from queue import Queue

DOWNLOAD_DIR = Path("Tasks for async-await/100-images-code/downloaded_images")

LIST_URL: str = "https://picsum.photos/v2/list?page=2&limit=100"

print_lock = threading.Lock()


def download_image(url: str, filename: str) -> None:
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            filepath = DOWNLOAD_DIR / filename

            with open(filepath, "wb") as f:
                f.write(response.content)

            with print_lock:
                print(f"Downloaded: {filename}")
        else:
            with print_lock:
                print(f"Failed to download {filename} file.")

    except Exception as e:
        with print_lock:
            print(f"Error: {e}")


def worker(queue: Queue) -> None:
    while True:
        task = queue.get()
        if task is None:
            break

        url, filename = task
        download_image(url, filename)
        queue.task_done()


def download_all() -> None:
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    response = requests.get(LIST_URL)
    image_data = response.json()

    queue = Queue()

    for idx, img in enumerate(image_data):
        url = img["download_url"]
        filename = f"image_{idx+1}_{img['id']}.jpg"
        queue.put((url, filename))

    num_threads = 10
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=worker, args=(queue,))
        thread.start()
        threads.append(thread)

    queue.join()

    for _ in range(num_threads):
        queue.put(None)

    for thread in threads:
        thread.join()


def main() -> None:
    start_time = time.time()

    print("Starting downloads...")

    download_all()

    elapsed_time = time.time() - start_time

    print(f"\n{'='*30}\nCompleted in {elapsed_time:.2f}s\n{'='*30}")


if __name__ == "__main__":
    main()
