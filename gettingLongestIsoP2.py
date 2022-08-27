import pandas as pd
import sys
input1=sys.argv[1]

#input1 is a tab separated file containing the full path to two files created with gettingLongestisP1.sh. 
#Column one if *translated_cds.faa.protgene and column two is *translated_cds.faa.length
with open(input1) as f:
    for i in f:
        in_files=i.split("\t")
        protgene=in_files[0]
        lenghtpgene=in_files[1].rstrip("\n")
        m_names=['protein', 'gene']
        m_types={'protein':'string', 'gene':'string'}
        df=pd.read_csv(protgene, names=m_names, sep="\t", dtype=m_types)
        
        m1_names=['protein', 'size']
        m1_types={'protein':'string', 'size':'int'}
        df_size=pd.read_csv(lenghtpgene, names=m1_names, sep="\t")
        df_and_size = pd.merge(df, df_size, on='protein')
        df_and_size1 = df_and_size.sort_values(['gene', 'size'], ascending=False)
        df_and_size1.to_csv(f"{protgene}.allISOS", index=False, sep="\t")
        longest_isos = df_and_size1[['protein', 'gene', 'size']].drop_duplicates(subset='gene')
        longest_isos1 = longest_isos.sort_values('gene')
        longest_isos1.to_csv(f"{protgene}.longestIso1", index=False, sep="\t")
        longest_isos1['protein'].to_csv(f"{protgene}.longestprot.ID", index=False, header=None)
print("all done")
