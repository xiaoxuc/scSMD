<div align="center">
<h1>scSMD </h1>
<h3>A Deep Learning Method for Accurateclustering of Single Cells based on Auto-Encoder</h3>
Xiaoxu Cui<sup>1</sup>, Renkai Wu<sup>1</sup>, Yinghao Liu, Peizhan Chen, Qing Chang, Pengchen Liang*, Changyu He*
</div>



https://github.com/user-attachments/assets/3f54b675-c864-447b-b6b5-051510b12dd2



### Abstract
Background: Single-cell RNA sequencing (scRNA-seq) has transformed biological research by offering new insights into cellular heterogeneity, developmental processes, and disease mechanisms. As scRNA-seq technology advances, its role in modern biology has become increasingly vital. This study explores the application of deep learning to single-cell data clustering, with a particular focus on managing sparse, high-dimensional data.

Results: We propose the SMD deep learning model, which integrates nonlinear dimensionality reduction techniques with a porous dilated attention gate component. Built upon a convolutional autoencoder and informed by the negative binomial distribution, the SMD model efficiently captures essential cell clustering features and dynamically adjusts feature weights. Comprehensive evaluation on both public datasets and proprietary osteosarcoma data highlights the SMD model’s efficacy in achieving precise classifications for single-cell data clustering, showcasing its potential for advanced transcriptomic analysis.

Conclusion: This study underscores the potential of deep learning—specifically the SMD model—in advancing single-cell RNA sequencing data analysis. By integrating innovative computational techniques, the SMD model provides a powerful framework for unraveling cellular complexities, enhancing our understanding of biological processes, and elucidating disease mechanisms. The code is available https://github.com/xiaoxuc/scSMD

We propose the scSMD deep learning model, which integrates nonlinear dimensionality reduction techniques with a porous dilated attention gate component. Built upon a convolutional autoencoder and informed by the negative binomial distribution, the scSMD model efficiently captures essential cell clustering features and dynamically adjusts feature weights. Comprehensive evaluation on both public datasets and proprietary osteosarcoma data highlights the scSMD model’s efficacy in achieving precise classifications for single-cell data clustering, showcasing its potential for advanced transcriptomic analysis.

**0. Datasets.** </br>

(1) Baron Dataset: The single-cell RNA-seq data from human pancreatic islets can be accessed from the Gene Expression Omnibus (GEO) repository under accession number GSE84133 (https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE84133).

(2) PBMC Datasets: The PBMC datasets used in this study are available from 10x Genomics' single-cell gene expression section, which can be accessed via the following link: https://support.10xgenomics.com/single-cell-gene-expression/datasets.

(3) Bhattacherjee Dataset: The PBMC dataset from Bhattacherjee et al. (2020) is available in the GEO database under accession number GSE124952 (https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124952).

(4) Zeisel Dataset: The human brain cell atlas data from Zeisel et al. (2015) can be accessed from GEO under accession number GSE60361 (https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE60361).


**1. Main Environments.** </br>

The code for scSMD runs with Python version 3.9 and Pytorch==1.7.1. You should also have CUDA installed for GPU acceleration.

To get started, please create a Python environment for Pytorch, and install required packages such as numpy, pandas, scikit-learn, scanpy, and cudatoolkit. You can refer to the requirements.txt and install.txt files for a detailed overview of the packages used to generate the results.

**2. Data Preprocessing.** </br>

Running the preprocessing script for UMI-count data:

python preprocess_data.py -p Data/ -i pbmc4340.txt -o pbmcsSMD.csv
or
python preprocess_data.py --filepath Data/ --filename pbmc4340.txt --resultfile pbmcSMD.csv
The program accepts input files in .txt, .csv, and 10x_mtx formats.

For read-count data, use the following command:

python preprocess_data.py -p FILE_PATH/ -i FILE_NAME -o OUTPUT_FILE.csv -r
For additional help, type python preprocess_data.py -h to see the full usage guide.

**3. Training and Clustering.** </br>
python run_scSMD.py
Before running scSMD, make sure to modify the file paths and filenames (for both the preprocessed scRNA-seq data and its cell-type annotations), rename your dataset (e.g., dataset_name = 'pbmc'), and set the number of clusters (e.g., number_cluster = 8). You can also adjust other parameters such as batch size and maximum iterations.

The latent low-dimensional space will be saved as "dataset_name"_uspace.csv (e.g., pbmc_uspace.csv), which can be used for further visualization.

The final clustering result will be saved as "dataset_name"_clusters.csv (e.g., pbmc_clusters.csv).

