import time
import asyncio
import shutil  # shell utilities
from pathlib import Path
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

SOURCE_DIR = Path("Tasks for async-await/100-images-code/downloaded_images")
OUTPUT_DIR = Path("Tasks for async-await/100-images-code/resized_images")
# check for 100 images in SOURCE_DIR and create a list of it
IMAGE_FILES = list(SOURCE_DIR.glob("*.jpg"))[:100]


# check for directory exists
def prepare_directory():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# give path to save resize_images
def resize_image(file_path):
    try:
        with Image.open(file_path) as img:
            img = img.resize((30, 30))
            save_path = OUTPUT_DIR / file_path.name
            img.save(save_path)
    except Exception as e:
        print(f"Error: {e}")


# threading process
def run_threading():
    prepare_directory()
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(executor.map(resize_image, IMAGE_FILES))
    return time.time() - start


# multiprocessing process
def run_multiprocessing():
    prepare_directory()
    start = time.time()
    with ProcessPoolExecutor() as executor:
        list(executor.map(resize_image, IMAGE_FILES))
    return time.time() - start


# asyncio process
async def run_asyncio():
    prepare_directory()
    start = time.time()
    loop = asyncio.get_running_loop()
    tasks = [loop.run_in_executor(None, resize_image, f) for f in IMAGE_FILES]
    await asyncio.gather(*tasks)
    return time.time() - start


def main():
    if not IMAGE_FILES:
        print(f"No images found in {SOURCE_DIR}!")
        return

    print(f"Checking time taken by different processes for image resizing...\n")

    a_time = asyncio.run(run_asyncio())
    print(f"Asyncio Time: {a_time:.4f} seconds")

    t_time = run_threading()
    print(f"Threading Time: {t_time:.4f} seconds")

    m_time = run_multiprocessing()
    print(f"Multiprocessing Time: {m_time:.4f} seconds")


if __name__ == "__main__":
    main()
