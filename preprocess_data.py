import numpy as np
import pandas as pd
import scanpy as sc
import os
import argparse


parser = argparse.ArgumentParser(description='Manual to this script')
parser.add_argument('-p', type=str, default='D:\\', help="input file path")
parser.add_argument('-i', type=str, default='.csv', help="input file name")
parser.add_argument('-o', type=str, default='.csv', help="save as .csv file")
parser.add_argument('-r', '--reads', action="store_true", help="if input file is read-counting, else UMI-counting")
args = parser.parse_args()

filename = args.p + args.i
print()

if filename[-3:] == "csv":
    adata = pd.read_csv(filename, header=0, index_col=0)
    print(adata.shape)
    #adata = adata.T
    data = sc.AnnData(adata, dtype=np.float32)
    print("The .csv file has been read!")
elif filename[-3:] == "txt":
    adata = pd.read_csv(filename, header=0, index_col=0, delim_whitespace=True)
    print(adata.shape)
    data = sc.AnnData(adata, dtype=np.float32)
    print("The .txt file has been read!")
elif filename[-3:] == "mtx":
    data = sc.read_10x_mtx(args.filepath, var_names='gene_symbols', cache=True)
    print("The 10x .mtx file has been read!")

sc.pp.filter_genes(data, min_cells=3)
sc.pp.normalize_total(data, target_sum=1e4)
sc.pp.log1p(data)
data.X[np.isnan(data.X) | np.isinf(data.X)] = 0

if args.reads:
    data = round(data.to_df())
    data = sc.AnnData(data, dtype=np.float32)
    sc.pp.highly_variable_genes(data, n_top_genes=784, flavor='seurat_v3', subset=True)
else:
    sc.pp.highly_variable_genes(data, n_top_genes=784, subset=True)

data = data[:, data.var.highly_variable]
data.to_df().to_csv(os.path.join(args.p, args.o))
print(data.shape)