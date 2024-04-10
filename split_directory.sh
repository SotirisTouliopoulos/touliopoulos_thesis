
i=0; 
for f in ./solvate_files/*; 
do 
    d=dir_$(printf %03d $((i/2700+1))); 
    mkdir -p $d; 
    mv "$f" $d; 
    let i++; 
done
