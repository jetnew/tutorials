# Jupyter Book Tutorial

## Setting up
1. `pip install jupyter-book`
2. `git clone <repo>`
3. `jb create newbook`
4. `cp -r newbook/* <repo>`
5. `jb build <repo>`
6. `cd <repo>`
7. `git add .`
8. `git commit -m "new book"`
9. `git push`

## Publish book
1. Push to a new branch called `gh-pages`:
    1. `pip install ghp-import`
    2. `ghp-import -n -p -f _build/html`

2. Under Settings > Pages, use `gh-pages` branch to host, and choose root directory `/`.
3. View website under `https://<user>.github.io/<myonlinebook>/`.

## Update book
1. `jb build <book>`
2. `ghp-import -n -p -f book/_build/html`