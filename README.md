# Nh*ntai-Client/Scrapping-Server
This project serves as a proof of concept for making a python server that can bypass Cloudflare Protection, a service used by millions of websites to protect them against bots, and extract data from it. The targeted website can be replaced with any website that also uses the same protection technology. The front end of this repo is not the main objective. The main object of this project is that data from protected websites can still be taken and convert into other form, such as HTML or json. This repo can be further expanded to be able to be hosted on a cloud computer, making an API.

This website is protected by Cloudflare, which means using normal libraries like request,... only return a blank page with no content on it. This repo tries to bypass the problem by making a virtual browser, simulating a real user interacting with the page. The page source will then modified, and served through flask.

This repo is still in development so there are a fuckton of file.
But the most importain one is `testingapi.py`. It uses Selenium and Undetected-Chromedriver to bypass Cloudflare protection from bot like me and scrapes the source page, injects my css and js script files and display them on a localhost website.

Although I forked this repo from Nhentai_net(`nhentai_net.py`), their code sadly didn't work so I have to rewrote most of the program and turned it into a Flask server. It was fucking pain to figure out all the problems I encountered and I still didn't understand how did I manage to bypass Cross-origin Block when parsing those images. But hey, it kinda works.

Also, now you can open this kind of site in public without getting on a sex offender list. Yippee...
## Using this thing
### Prerequisites
- Python/pip, you get the gist
- A shit load of patience because these pip modules will screw you up and crash on their own

### Setting up

Clone this.

Install all the modules in `testingapi.py`.

`python testingapi.py` and hope for the best. The localhost website should be usable like the original website, albeit there are some weird icons misplacements, missing logo, slight slowness.

