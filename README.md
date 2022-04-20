# NLP Final Presentation Repository
This repository contains code from this [paper](https://arxiv.org/pdf/2010.06196.pdf "paper") from the 2021 EMNLP Conference in an attempt to reproduce the authors' experiment and validate their results.
## Requirements:
* CUDA 11.3
* Anacond3 Prompt
* Python 3.9 and up.
## Installing Dependencies by Creating a New Environment in Anaconda3 Prompt:
```
cd */NLP-Final-Presentation/Modified_MaKE_EMNLP2021 (or wherever you stored the repository)
conda env create -f environment.yml
```
## Running Modfied Running Scripts:
```
Training: 
python train_batch.py

Testing: 
cd test (from Modified_MaKE_EMNLP2021)
python test_batch.py
```
