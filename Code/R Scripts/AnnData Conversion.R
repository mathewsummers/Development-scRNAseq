## Script to convert thalamus development scRNAseq data to feather formats for reading into python and AnnData conversion

library(feather)
library(Matrix)

setwd("C:/Users/mathew.summers/Transcriptomics/Development scRNAseq/Code/R Scripts")


## Convert cell by gene matrix to Python readable format

fnInput = "../../Data/R Formats/P11_14_RNA_norm_dat_for_thalamus_gene_panel"
fnOutputData = "../../Data/dev_data.mtx"
fnOutputNames = "../../Data/gene_names.feather"

normData = readRDS(fnInput)

writeMM(normData, fnOutputData)

## Save gene names

genes = as.data.frame(row.names(normData))

write_feather(genes,fnOutputNames)

## Best estimate on what's contained in each of these other files:

# Raw counts (non-log normalized)
# "../../Data/R Formats/P11_14_RNA_counts_matrix_for_thalamus_gene_panel"

# Differential expression analysis results
# "../../Data/R Formats/TH_p11_p14_initial_itercluster_result2022-07-01"

# Data set filtered for differentially expressed genes
# "../../Data/R Formats/TH_p11_p14_rd_dat_filtered2022-07-01"
