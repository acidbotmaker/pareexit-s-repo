# Task-3: Use async function to download images from array of urls at the same time
import asyncio
import aiohttp
import aiofiles
from pathlib import Path
from typing import List, Optional

DOWNLOAD_DIR = Path("Tasks for async-await/downloaded_images")

URLs: List[str] = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDCoZOlY05iDyrVnJGfFwE6aSL_YObRf8YTQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3au9dyNY7UPpOSeWc6YDwMQ1hN5cErKaOgA&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0vKSFN7EDNmm8-6SUofhSLaSk8nBBH9TiMw&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWHUm6Z0ORnosy36kbPNT-rkZnoFVnFLV6Uw&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiAwSp3ZiNlI5W1xkBLcaWVfQZ6ErLXL5BcQ&s",
]


async def download_image(
    session: aiohttp.ClientSession, url: str, filename: str
) -> Optional[Path]:
    try:
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
        print(f"Error downloading {filename}: {e}")
        return None


async def url_download() -> None:
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)  # create directory if not exists

    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [
            download_image(session, url, f"image-{i+1}.jpg")
            for i, url in enumerate(URLs)
        ]
        await asyncio.gather(*tasks)


async def main() -> None:
    print("Downloading started...")
    await url_download()
    print("Download completed!")


if __name__ == "__main__":
    asyncio.run(main())
