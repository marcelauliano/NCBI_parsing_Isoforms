proteins="./*.fa"
for protein in $proteins
do
        grep ">"  $protein > $protein.1

        cat $protein.1 | awk '{print$1"\t"$2}' > $protein.12
        sed 's/>//g' $protein.12 > $protein.protgene
        rm $protein.1
        rm $protein.12
        python /software/team311/mu2/fastaLength_1.py $protein $protein.length
done
