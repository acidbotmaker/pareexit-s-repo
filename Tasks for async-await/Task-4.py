# Task-4: Same as task 3, but only 3 downloads will run simultaneously
import asyncio
import aiohttp
import aiofiles
from pathlib import Path
from typing import List, Optional

DOWNLOAD_DIR = Path("Tasks for async-await/downloaded_images")
MAX_CONCURRENT_DOWNLOADS = 3

URLs: List[str] = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDCoZOlY05iDyrVnJGfFwE6aSL_YObRf8YTQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3au9dyNY7UPpOSeWc6YDwMQ1hN5cErKaOgA&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0vKSFN7EDNmm8-6SUofhSLaSk8nBBH9TiMw&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWHUm6Z0ORnosy36kbPNT-rkZnoFVnFLV6Uw&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiAwSp3ZiNlI5W1xkBLcaWVfQZ6ErLXL5BcQ&s",
]


async def download_image(
    session: aiohttp.ClientSession,
    url: str,
    filename: str,
    semaphore: asyncio.Semaphore,
) -> Optional[Path]:
    # semafore used for doing specific number of downloads at once
    async with semaphore:
        try:
            print(f"Downloading: {filename}")

            async with session.get(url) as response:
                response.raise_for_status()
                content = await response.read()

                # saving downloaded images
                output_path = DOWNLOAD_DIR / filename

                async with aiofiles.open(output_path, "wb") as f:
                    await f.write(content)

                print(f"Downloaded: {filename}")
                return output_path

        except Exception as e:
            print(f"Error: {e}")
            return None


async def main() -> None:
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)  # create directory if not exists

    print(f"Starting download with {MAX_CONCURRENT_DOWNLOADS} simultaneously downloads")

    # limit to 3 downloads at a time
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_DOWNLOADS)

    async with aiohttp.ClientSession() as session:
        tasks = [
            download_image(session, url, f"image-{i+1}.jpg", semaphore)
            for i, url in enumerate(URLs)
        ]
        results = await asyncio.gather(*tasks)

    print(
        f"Download completed! Successfully saved {len([r for r in results if r])} images."
    )


if __name__ == "__main__":
    asyncio.run(main())
