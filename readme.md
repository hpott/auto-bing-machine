# Auto Bing Machine
**DISCLOSURE: THIS IS DESIGNED FOR EDUCATIONAL PURPORSES ONLY. I'M NOT REPOSONSIBLE IF YOU GET INTO TROUBLE**
## Background
I created the auto bing machine because I don't like Microsoft. A few of my friends asked me about automating Microsoft Rewards so I made this script one night.
## Requirements
- Firefox or Google Chrome
- GeckoDriver or Chrome Driver
- Python 3
- Selenium
- A UNIX based operating system (Linux, Mac, BSD, etc)

## Installation
Step 1: Install requirements

```python
pip3 install -r requirements.txt
```
Step 2: Install GeckoDriver (Firefox) or Chrome Driver (Chrome)


[Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)

[Download Chrome Driver](https://chromedriver.chromium.org/downloads)

Extract the binary then copy it to somewhere on your PATH (/bin, /usr/bin, /usr/share/bin, etc)

Step 3: Run the script

**For Firefox**

```bash
python3 ./main.py --firefox
```

**For Chrome**

```bash
python3 ./main.py --chrome
```
