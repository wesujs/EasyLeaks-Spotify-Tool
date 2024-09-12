<!-- Improved compatibility of back to top link: See: https://github.com/wesujs/EasyLeaks-Spotify-Tool/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the EasyLeaks-Spotify-Tool. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/wesujs/EasyLeaks-Spotify-Tool">
    <img src="app_logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">EasyLeaks-Spotify-Tool</h3>

  <p align="center">
    An easy to add grails/leaks/removed songs back to spotify
    <br />
    <a href="https://github.com/wesujs/EasyLeaks-Spotify-Tool"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/wesujs/EasyLeaks-Spotify-Tool">View Demo</a>
    ·
    <a href="https://github.com/wesujs/EasyLeaks-Spotify-Tool/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/wesujs/EasyLeaks-Spotify-Tool/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python.org]][Python-url]
[![pyglet][pyglet-badge]][pyglet-url]
[![yt-dlp][yt-dlp-badge]][yt-dlp-url]
[![customtkinter][customtkinter-badge]][customtkinter-url]
[![Pillow][pillow-badge]][pillow-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

 - Python 3.12 or later [Python-url]
 - Spotify Desktop App
 - Windows Operating System's Only (For Now).


 ### Process
 
 1. The youtube video containing the song is downloaded using Google API
 
 2. Once downloaded the video title is parsed to find the artist name and song title

 3. The metadata of the mp3 is then changed to match

 4. The file is then moved to the target source folder and installed


### Installation

1. Download the zipped folder or Clone the repo:
   ```sh
   git clone https://github.com/wesujs/EasyLeaks-Spotify-Tool.git
   ```
3. Install Python Modules
    - Run the `run.bat` file

4. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Open Desktop Spotify and ensure local files are enabled and you have a source folder selected
    - You can check using these instructions [Spotify Local Files](https://community.spotify.com/t5/FAQs/Local-Files/ta-p/5186118)

2. Once you have that set up you can run the program with:
  ```bash
  python main.py
  ```
3. Select your source folder from before.

4. Input the youtube link to the song you would like to have on your spotify

5. Playlist links work as well, but will take more time depending on the size

### Mobile Device Local File Transfer

1. For those want to download these items on a mobile/other device follow these steps:

    - Follow the tutorial for mobile [Spotify Local Files](https://community.spotify.com/t5/FAQs/Local-Files/ta-p/5186118)

    - Add the local file song to your liked songs
    - Open your spotify app and it will automatically download.
    - If you remove the files from your computer they will still remain on the mobile device


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog
- [ ] Add NoSQL Database Support For Managing Local Music
- [ ] Algorithms to maximize audio quality
- [ ] Machine Learning to increase metadata inputs

See the [open issues](https://github.com/wesujs/EasyLeaks-Spotify-Tool/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/wesujs/EasyLeaks-Spotify-Tool/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=wesujs/EasyLeaks-Spotify-Tool" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Willie Spratt - [@wesujs](https://twitter.com/wesujs)

Project Link: [EasyLeaks](https://github.com/wesujs/EasyLeaks-Spotify-Tool)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/wesujs/EasyLeaks-Spotify-Tool.svg?style=for-the-badge
[contributors-url]: https://github.com/wesujs/EasyLeaks-Spotify-Tool/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/wesujs/EasyLeaks-Spotify-Tool.svg?style=for-the-badge
[forks-url]: https://github.com/wesujs/EasyLeaks-Spotify-Tool/network/members
[stars-shield]: https://img.shields.io/github/stars/wesujs/EasyLeaks-Spotify-Tool.svg?style=for-the-badge
[stars-url]: https://github.com/wesujs/EasyLeaks-Spotify-Tool/stargazers
[issues-shield]: https://img.shields.io/github/issues/wesujs/EasyLeaks-Spotify-Tool.svg?style=for-the-badge
[issues-url]: https://github.com/wesujs/EasyLeaks-Spotify-Tool/issues
[license-shield]: https://img.shields.io/github/license/wesujs/EasyLeaks-Spotify-Tool.svg?style=for-the-badge
[license-url]: https://github.com/wesujs/EasyLeaks-Spotify-Tool/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/williespratt
[product-screenshot]: app_ss.png
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[Python-url]: https://www.python.org/
[pyglet-badge]: https://img.shields.io/badge/pyglet-3E434A?style=for-the-badge&logo=python&logoColor=white

[pyglet-url]: http://pyglet.org/

[yt-dlp-badge]: https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white
[yt-dlp-url]: https://github.com/yt-dlp/yt-dlp

[customtkinter-badge]: https://img.shields.io/badge/customtkinter-3776AB?style=for-the-badge&logo=python&logoColor=white
[customtkinter-url]: https://github.com/TomSchimansky/CustomTkinter

[pillow-badge]: https://img.shields.io/badge/Pillow-11557C?style=for-the-badge&logo=python&logoColor=white
[pillow-url]: https://python-pillow.org/