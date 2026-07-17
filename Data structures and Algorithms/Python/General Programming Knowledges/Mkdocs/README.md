## MkDocs
MkDocs is a fast, open-source static site generator written in Python that is specifically designed for building project documentation. It converts plain text files written in Markdown into a fully functional, responsive website.

### Installation
```bash
    pip install mkdocs
```
- to seek help : 
```bash
    mkdocs --help
```

### Start a new project
- we position ourselve in the folder we want to add the docs in, the project base
```bash
    mkdocs new .
```
- to see what have been created we do 
```bash
    mkdocs serve
```
- it will expose the documentation as a webpage
- if we want to modify this page we go to **docs>index.md**
- it is an md file, you can open it and modify it
- anytime i make a change here , we will see documentation directly in the website no need to update it


### Making pages
- to make a new file you create a new md file
- for exemple for having both base page and faq page we create ( index.md and faq.md)
- name of the page is the title of the new md files in docs

### Effects and Folders
- when we create a folder it will create a new tab list accross index and faq with a drop down list
- the drop down list will contain all link to pages which corespond to the md files contains in the folders
- if we have two md file in subfolder , we will have two elements in the drop down list that rediret to a page

### Hosting image
- as far as mkdocs in concerned, the docs folder is considered to be the root folder.
- mkdocs assume evrything you use to build the documentation is in the folder **docs**
- we will store all images in a folder call **images**
- docs >> code and images
- we can then use markdown notation to specify the path to the image
- we add it to the page we want the image to appear in
- exemple : ![/images/img.png](/images/img.png)


### Style and Css
- to add some style we create a new css file (custom.css)
```css
.navbar{
  background-image: none;
  background-color: black;
}
```
- we ask mkdocs to take it into account
- if we dont , the changes will not be take into account
- we do it in the **mkdocs.yml**:
```yml
    site_name: My Docs
    extra_css: [custom.css]
```
- it cool be easier to install a theme that you like
- it's kind of standard
```yml
    site_name: My Docs
    theme:
        name: readTheDocs
```


### Materials Mkdocs
- to install a new theme youshould make sure mkdocs is not serving anymore, stop the serve terminal
- then install mkdocs-material
```bash
    pip install mkdocs-material
```
- then i turn mkdocs on again
- then i modify mkdocs.yml
```yml
    site_name: My Docs
    theme:
        name: material
```
- you sould use it 
- it give you a nice clean doc website
- we can customise that theme
```yml
    site_name: My Docs
    theme:
    name: material
    palette:
        primary: purple
        accent: cyan
    font:
        text: Ubuntu
    icon:
        logo: material/cloud

```
- palette primary define the base color
- accent define color when the mouse put accent on a text


### CodeHilite
- we can highlight code
- to do it we stop to serve mkdocks, and install pygments
```bash
    pip install pygments
```
- we reserve that again
- we then add in the mkd.yml file : **markdown_extensions**, which are extension that deals with how the markedown file  being rendered
-  one extension we want to add is **Codehilite**
- we can also specify in that extension that we want to have line number rendered
```bash
    site_name: My Docs
    theme:
    name: material
    palette:
        primary: purple
        accent: cyan
    font:
        text: Ubuntu
    logo:
        icon: cloud
    markdown_extensions:
    - codehilite:
        linennums: true

```

- we can also add footnotes 
- for that we add extention call **footnotes** in the mkdocs.yml file
-  we add then the square bracket anchor in the page [^1]
- we refer to this bellow in the page
- [^1]: From a pydata video, can be found here.
- mkdocs.yml :
```yml
    site_name: My Docs
    theme:
    name: material
    palette:
        primary: purple
        accent: cyan
    font:
        text: Ubuntu
    logo:
        icon: cloud
    markdown_extensions:
    - footnotes
    - codehilite:
        linennums: true

```
- backend.md :
```md
    # Backend

    Our backend is written in python and go. We have some coding habbits.

    ![](/images/img.png)

    This image[^1] demonstrates something interesting.

    ```python
    for i in range(10):
        print(i)

```



### Extras
```bash
    pip install pymdown-extensions
```
- emoji :
```yml
  - pymdownx.emoji:
      emoji_generator: !!python/name:pymdownx.emoji.to_svg
```
- task list :
```yml
      - pymdownx.tasklist:
      custom_checkbox: true
```
- mathemathique:
```yml
    extra_javascript:
    - 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML'
    markdown_extensions:
    - pymdownx.arithmatex
```

