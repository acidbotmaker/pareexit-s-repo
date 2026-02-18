import asyncio
import aiohttp
from pathlib import Path
import time
import aiofiles

DOWNLOAD_DIR = Path("Tasks for async-await/100-images-code/downloaded_images")

LIST_URL: str = "https://picsum.photos/v2/list?page=2&limit=100"


async def download_image(
    session: aiohttp.ClientSession, url: str, filename: str
) -> None:
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                filepath = DOWNLOAD_DIR / filename

                async with aiofiles.open(filepath, mode="wb") as f:
                    await f.write(content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download {filename} file.")

    except Exception as e:
        print(f"Error: {e}")


async def download_all() -> None:
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with session.get(LIST_URL) as response:
            image_data = await response.json()

        tasks = [
            download_image(
                session, img["download_url"], f"image_{idx+1}_{img['id']}.jpg"
            )
            for idx, img in enumerate(image_data)
        ]

        await asyncio.gather(*tasks)


def main() -> None:
    start_time = time.time()

    print("Starting downloads...")

    asyncio.run(download_all())

    elapsed_time = time.time() - start_time

    print(f"\n{'='*30}\nCompleted in {elapsed_time:.2f}s\n{'='*30}")


if __name__ == "__main__":
    main()
