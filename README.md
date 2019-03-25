# SuperResMRI: 
> SINAPP (Modular BIDS App) for Motion-robust Super-Resolution MRI

OG 2019 - Project 03:  Package a portable and reproducible software for motion-robust MRI super-resolution  by Sébastien Tourbier

![](resources/images/superres-mri.jpg)

The essence of this project is to develop the next generation of the open-source [Medical Image Analysis Laboratory Super-Resolution ToolKit (MIALSRTK)](https://github.com/sebastientourbier/mialsuperresolutiontoolkit), a set of C++ image processing tools necessary to perform motion-robust super-resolution fetal MRI reconstruction. This new version will integrate all new advances in the neuroimaging field over the past three years with the advent of:

- the Brain Imaging Data Structure (BIDS), a standard to organize and describe neuroimaging data,
- and the BIDS App framework, which promotes reproducibility and portability. all state-of-the-art solutions for enhanced portability, reusability, reproducibility and replicability in neuroimaging.


## Install
* Clone this repository:
```
git clone https://github.com/brainhack-ch/superres-mri.git <Your/installation/dir>
```
* Install the packages and dependencies...
```
conda env create -f environment.yml
```

## Running:

* Go to the notebooks directory in the cloned repo
```
cd <Your/installation/dir>/notebooks
```

* Activate the conda environment supermri-env
```
conda activate supermri-env
```

* Runs the ipython notebook server:
```
python brainHack.ipynb
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Authors

* **Sebastien Tourbier**
* **Seirios**
* **Brenda**
* **Snezana**
* **Niloufar**

See also the list of [contributors](https://github.com/brainhack-ch/superres-mri/contributors) who participated in this project.

