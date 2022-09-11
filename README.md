# Nh*ntai-Client/Scrapping-Server

This repo is still in development so there are a fuckton of file.
But the most importain one is the `testingapi.py`. It uses Selenium and Undetectedd-Chromedriver to bypass Cloudflare protection from bot like me and scrapes the source page, injects my css and js script files and display them on a localhost website.

Although I forked this repo from Nhentai_net(`nhentai_net.py`), their code sadly didn't work so I have to rewrote most of the program and turned it into a Flask server. It was fucking pain to figure out all the problems I encountered and I still didn't understand how did I manage to bypass Cross-origin Block when parsing those images. But hey, it kinda works.

Also, now you can open this kind of site in public without getting on a sex offender list. Yippee...
(The images wasn't edited, they are blured by design and you can unblur them with the side button)
![image](https://user-images.githubusercontent.com/84757707/189525518-9cd48fd0-6f4a-489b-99fc-0d7dc4c844aa.png)

## Using this thing
### Prerequisites
- Python/pip, you get the gist
- A shit load of patience because these pip modules will screw you up and crash on their own

### Setting up

Clone this.

Install all the modules in `testingapi.py`.

`python testingapi.py` and hope for the best. The localhost website should be usable like the original website, albeit there are some weird icons misplacements, missing logo, slight slowness.

