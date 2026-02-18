import multiprocessing
import requests
from pathlib import Path
import time

DOWNLOAD_DIR = Path("Tasks for async-await/100-images-code/downloaded_images")

LIST_URL: str = "https://picsum.photos/v2/list?page=2&limit=100"


def download_image(args: tuple) -> None:
    url, filename = args
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            filepath = DOWNLOAD_DIR / filename

            with open(filepath, "wb") as f:
                f.write(response.content)
                print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download {filename} file.")

    except Exception as e:
        print(f"Error: {e}")


def download_all() -> None:
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    response = requests.get(LIST_URL)
    image_data = response.json()

    tasks = [
        (img["download_url"], f"image_{idx+1}_{img['id']}.jpg")
        for idx, img in enumerate(image_data)
    ]

    num_processes = 10

    with multiprocessing.Pool(processes=num_processes) as pool:
        pool.map(download_image, tasks)


def main() -> None:
    start_time = time.time()

    print("Starting downloads...")

    download_all()

    elapsed_time = time.time() - start_time

    print(f"\n{'='*30}\nCompleted in {elapsed_time:.2f}s\n{'='*30}")


if __name__ == "__main__":
    main()
