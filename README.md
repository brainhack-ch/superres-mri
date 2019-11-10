# SuperResMRI

Brainhack Global 2019 - Project 05:  SINAPP (Modular BIDS App) for Motion-robust Super-Resolution MRI by Sébastien Tourbier

![](resources/images/superres-mri.jpg)

The essence of this project is to develop the next generation of the open-source [Medical Image Analysis Laboratory Super-Resolution ToolKit (MIALSRTK)](https://github.com/sebastientourbier/mialsuperresolutiontoolkit), a set of C++ image processing tools necessary to perform motion-robust super-resolution fetal MRI reconstruction. The new version will integrate all new advances in the neuroimaging field over the past three years with the advent of:

- the Brain Imaging Data Structure (BIDS), a standard to organize and describe neuroimaging data,
- and the BIDS App framework, which promotes reproducibility and portability. 

**Project started at previous Brainhack Open Geneva 19 as:** 

OG 2019 - Project 03: Package a portable and reproducible software for motion-robust MRI super-resolution (See achievements in ![presentation](resources/slides/BrainHack2019.pdf))

## Contribution, bug and support

This project is conducted with transparency in mind. It uses GitHub Issues (https://github.com/brainhack-ch/superres-mri/issues) and GitHub pull-request (https://github.com/brainhack-ch/superres-mri/pulls) to manage and discuss bugs and new features. 

## Installation
* Clone this repository:
```
git clone https://github.com/brainhack-ch/superres-mri.git <Your/installation/dir>
```
* Install the `supermri-env` conda environment with all the packages and dependencies:
```
conda env create -f environment.yml
```
* Download the latest version of the mialsuperresolutiontoolkit Docker image:
```
docker pull sebastientourbier/mialsuperresolutiontoolkit:latest
```


## Running the SINAPP example:

We provide two scripts in `sinapps/nlmdenoise/`. The script `build_sinapp-core_and_sinapp-nlmdenoise.sh`shows you how we build the sinapp-nlmdenoise docker image. The script `run_sinapp-nlmdenoise.sh` shows you how to execute it. 

Instructions to make it work:
* Edit the path defined by `superes-mri_dir` in `build_sinapp-core_and_sinapp-nlmdenoise.sh` by your `<Your/installation/dir>`.
* Edit the path defined by `bids_dir` in the  `run_sinapp-nlmdenoise.sh` script to the location of your BIDS dataset location (`<Your/BIDS/dir>`)
* In a terminal go to your `<Your/installation/dir>`:
```
cd <Your/installation/dir>
```
* Build the SINAPP:
```
sh build_sinapp-core_and_sinapp-nlmdenoise.sh
```
* Run the SINAPP that performs NLMdenoising on all T2w scans of sub-01 in `<Your/BIDS/dir>`:
```
sh run_sinapp-nlmdenoise.sh
```
Results are generated in `<Your/BIDS/dir>/derivatives/superres-mri/sub-01/nipype/sinapp_nlmdenoise`.

## Want to help with the development of the entire collection of SINAPPs?
Please check the github issue https://github.com/brainhack-ch/superres-mri/issues/7 dedicated to the management, tracking, and discussions about the developement of the SINAPP collection for the MIALSRTK library.

## Running the notebooks:

* Go to the notebooks directory in the cloned repo:
```
cd <Your/installation/dir>/notebooks
```

* Activate the conda environment `supermri-env`:
```
conda activate supermri-env
```

* Launch the ipython notebook server:
```
jupyter notebook
```


## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details

## Authors

* **Sebastien Tourbier**
* **Priscille**
* **Hamza**
* **Manik**
* **Olivier**
* **Guillaume**
* **Seirios**
* **Brenda**
* **Snezana**
* **Niloufar**

See also the list of [contributors](https://github.com/brainhack-ch/superres-mri/contributors) who participated in this project.

