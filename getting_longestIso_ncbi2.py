import pandas as pd

m_names=['protein', 'gene']
m_types={'protein':'string', 'gene':'string'}
df=pd.read_csv("/lustre/scratch116/vr/projects/vgp/user/mu2/mChoDid1-paper/orthofinder-Longest/GCF_000313985.2_ASM31398v2_translated_cds.faa.protgene", names=m_names, sep="\t", dtype=m_types)
df

m1_names=['protein', 'size']
m1_types={'protein':'string', 'size':'int'}
df_size=pd.read_csv("/lustre/scratch116/vr/projects/vgp/user/mu2/mChoDid1-paper/orthofinder-Longest/GCF_000313985.2_ASM31398v2_translated_cds.faa.length", names=m1_names, sep="\t")
df_size

df_and_size = pd.merge(df, df_size, on='protein')
df_and_size1 = df_and_size.sort_values(['gene', 'size'], ascending=False)
df_and_size1.to_csv("/lustre/scratch116/vr/projects/vgp/user/mu2/mChoDid1-paper/orthofinder-Longest/hedgehog_translated_cds.allISOS", index=False, sep="\t")
longest_isos = df_and_size1[['protein', 'gene', 'size']].drop_duplicates(subset='gene')
longest_isos1 = longest_isos.sort_values('gene')
longest_isos1
longest_isos1.to_csv("/lustre/scratch116/vr/projects/vgp/user/mu2/mChoDid1-paper/orthofinder-Longest/hedgehog_translated_cds.name_gene_size_longest1", index=False, sep="\t")
longest_isos1['protein'].to_csv("/lustre/scratch116/vr/projects/vgp/user/mu2/mChoDid1-paper/orthofinder-Longest/hedgehog_translated_cds.longestprot.ID", index=False, header=None)
