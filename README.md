Ustensile
=========


Presentation
------------

This repo is a maker-repository. It stores the parameters and the STL-files of some *ustensile-s*.
This repo uses the javascript packages [desi82-cli](https://www.npmjs.com/package/desi82-cli) and [desi82-uis](https://www.npmjs.com/package/desi82-uis) of the design-library [desi82](https://charlyoleg2.github.io/parame82/).


Requirements
------------

- [node](https://nodejs.org) > 20.10.0
- [npm](https://docs.npmjs.com/cli) > 10.1.0


### Optional requirements

- [OpenSCAD](https://openscad.org/)

For Ubuntu users, *OpenSCAD* is available on [snapcraft](https://snapcraft.io/openscad) and can be installed with:

```bash
sudo snap install openscad
```

Upgrade
-------

For working with the latest *desi78* version:

```bash
npm outdated
npm update --save
git commit -am 'npm update --save'
```


Dev
---

```bash
git clone https://github.com/charlyoleg2/ustensile
cd ustensile
npm install
npm run
npm run desi78-uis
npx desi78-uis
npx desi78-cli --help
./make_ustensile.js
```

Vocabulary
----------

- Design: A parametrizable 3D parts. Desginix is a collection of designs.
- Reference: A particular parametrization of a design.
- Instance: The realization of a reference.


References for the ustensiles
-----------------------------

ID | Reference           | Design             | Nb of instances
---|---------------------|--------------------|----------------
1  | doorstop            | doorstop           | 1
2  | pencil\_holder      | pencil\_holder     | 1
3  | spiral              | spiral             | 1

Each reference has its own directory with its json-parametrization, scad-script and stl-file.


