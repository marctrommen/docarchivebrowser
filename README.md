# Document Archive Browser as Static Website With Keyword Search

The following description is **PART TWO** of a two parts description for a whole
document archive system. **PART TWO** deals with the genaration of a static 
webpage as a simple, yet powerful document search and retrieval system to 
simply browse your documents as PDF within your web browser.

The *Document Archive Browser* as a static web page can either reside on any
file system (e.g. USB stick) or on a simple Web Server or Webpage hoster.


[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Linux](https://img.shields.io/badge/Linux-blue.svg)
![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)
![HTML 5](https://img.shields.io/badge/HTML-5-blue.svg)
![CSS 3](https://img.shields.io/badge/CSS-3-blue.svg)


**PART ONE** deals with the scanning of documents, 
collecting some meta information for further usage, 
enhancing the quality of the documents, reducing the file size of
them drastically, extract with the help of OCR tools (Tesseract) some plain 
text, putting the scanned images and extracted texts into one PDF with some
(previously collected) meta information and finally organizing all the files 
within a simple tree structure onto your file system. It is a totally decoupled
workflow and the *Communication Interface* between **PART ONE** and **PART TWO**
is just the file tree structure, existing of *Document_IDs*, Metadata as
*JSON files* and the *PDF files*.


## Content

*   [Feature List](#feature-list)
*   [SiteMap of Website](#sitemap-of-website)
*   [SiteMap of Build](#sitemap-of-build)
*   [Process of Build](#process-of-build)
*   [Links on CSS](#links-on-css)
*   [Links on Python](#links-on-python)


## Feature List

*   eigenes, simples Template System
*   responsive WebDesign (mobile first)
*   statische Web-Seiten
*   so wenige Abhängigkeiten wie möglich
*   Suche über Schlagwort-Katalog
*   Generierung entspricht einem Build-Prozess, inkl. Initialisierung, CleanUp, 
    usw.
*   Metainformationen zu den Dokumenten liegen als JSON-Dateien vor


## SiteMap of Website

Grobe SiteMap des Static-Document-Archive sieht wie folgt aus:

```
doc_archive_root
├── index.html (Liste aller Dokumente zum aktuellen Jahr <YYYY>)
├── pages.css
├── keyword_catalog.html (Liste aller Schlagworte)
├── keyword_<xxx>.html (Liste aller Dokumente zu einem Schlagwort <xxx>)
├── archive.html (Liste aller Jahresarchive)
├── archive_<YYYY>.html (Liste aller Dokumente zu einem Jahr <YYYY>)
└── archive
    ├── <yyyymmdd_xx>.* (verlinktes Dokument, z.B. PDF, PNG, JPG)
    └── ...
```	


## SiteMap of Build

Grobe SiteMap der Build-Umgebung des Generators sieht wie folgt aus:

```
project_root
├── source
|   ├── config_template.py
|   ├── build.py
|   ├── templatehandler.py
|   ├── oneyear.py
|   ├── onekeyword.py
|   ├── allkeywords.py
|   ├── allyears.py
|   ├── jsontreewalker.py
|   └── dirtreewalker.py
├── doc
|   ├── 
|   └── 
├── pages.css
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── templates
    ├── 
    ├── 
    └── 
```


## SiteMap of Scan Archive

```
scan_archive_root
├── YYYYMMDD_01
│   ├── YYYYMMDD_01.json
│   ├── YYYYMMDD_01.pdf
│   └── ...
├── YYYYMMDD_02
│   ├── YYYYMMDD_02.json
...
```



## Process of Build

Grober Ablauf des Build-Prozesses:

*   Initialisierung
*   CleanUp des letzten Builds (Verzeichnisbaum des Dokumenten-Archivs löschen)
*   Zielverzeichnisse erstellen
*   Scan-Archiv-Baum durchschreiten und in allen Unterverzeichnissen die
    JSON-Dateien einlesen und deren Metadaten in die globale Datenstruktur
    aufnehmen.
*   Datenstruktur für Jahresarchive erstellen (Jahr --> Dokument-ID)
*   Datenstruktur für Stichwortverzeichnisse erstellen 
    (Stichwort --> Dokument-ID)
*   index.html generieren
*   archive.html generieren
*   <yyyy>.html generieren (optional)
*   keyword_catalog.html generieren
*   verlinkte Dateien (Bilder, PDF, usw.) vom Scan-Archiv in das 
    Dokumenten-Archiv kopieren


## Links on CSS

*   [Google-Search](https://www.youtube.com/results?search_query=css3+responsive+web+design)
*   [Grid CSS Responsive Website Layout - "Mobile First" Design](https://www.youtube.com/watch?v=M3qBpPw77qo)
*   [Build a Responsive Grid CSS Website Layout From Scratch](https://www.youtube.com/watch?v=moBhzSC455o)
*   [HTML5 and CSS3 Responsive design with media queries](https://www.youtube.com/watch?v=fA1NW-T1QXc)
*   [Course: Build A Blog From Scratch with CSS3 - 1](https://medium.freecodecamp.org/how-to-design-and-develop-a-beautiful-blog-from-scratch-a0cd1af46845)
*   [Course: Build A Blog From Scratch with CSS3 - 2](https://scrimba.com/g/gbuildablog)
*   [Free Images](https://www.pexels.com/)
*   [Free Icons](https://fontawesome.com/)


## Links on Python

*   [Python 3 String.Template](https://docs.python.org/3/library/string.html#string.Template)
*   [Python 3 String Output-Formatting](https://docs.python.org/3/tutorial/inputoutput.html)
*   [Python 3 Abstract Base Classes (ABC)](https://docs.python.org/3/library/abc.html)