# Spidy
A web crawler modify from [rivermont/spidy](https://github.com/rivermont/spidy)

# How to run
There are 2 options to run this crawler, you can run it with Docker or directly run in your environment

## Python Base
Install require packages with`pip`:

    pip install -r requirements.txt

Then run:
```
 python spidy/crawler.py --config_name <your_config_name>
```
The result will be saved to `./data/<your_config_name>/*.zip`

### Config
On running, you can directly pass config file name through argument, the config file should be put under `./spidy/config`
Available Parameters:
- `OVERWRITE=False` tell crawler to continue on todo.txt
- `SAVE_PAGES=False` tell crawler not to save html, only save url in `done.txt`.
- `RESTRICT=True` tell crawler to stay within specific DOMAIN
- `DOMAIN="www.twreporter.org/"` tell crawler the Domain to stay within
- `REGEX_PATTERN="^https://www.twreporter.org/((?!\/image|.jpg|.png|.js|.svg|.mp3|.mp4|.ico|.woff2|.css|.JPG).)*$\/*"`
  - A customized regular expression string to filter out unwanted url format, crawler will only crawl if url match the pattern

---

## Using with Docker (still need to fix ssl issue on some machine)
Spidy can be easily run in a Docker container.<br>

- First, build the [`Dockerfile`](dockerfile): `docker build -t spidy .`
- Then, run it: `docker run --rm -it -v $PWD:/src/app spidy`
  - `--rm` tells Docker to clean up after itself by removing stopped containers.
  - `-it` tells Docker to run the container interactively and allocate a pseudo-TTY.
  - `-v $PWD:/src/app` tells Docker to mount the current working directory as `/src/app` directory inside the container. This is needed if you want Spidy's files (e.g. `crawler_done.txt`, `crawler_words.txt`, `crawler_todo.txt`) written back to your host filesystem.
