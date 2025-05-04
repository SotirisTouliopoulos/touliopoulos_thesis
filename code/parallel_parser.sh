for file in ./*.pdb ;

    #do python3 ./A_parser.py "$file" 5.0 > "$file".dist ;
    #do python3 ./Z_parser.py "$file" 5.0 > "$file".dist ;

    #do python3 ./A_parser.py "$file" 6.0 > "$file".dist ;
    do python3 ./Z_parser.py "$file" 6.0 > "$file".dist ;

    #do python3 ./A_parser.py "$file" 7.0 > "$file".dist ;
    #do python3 ./Z_parser.py "$file" 7.0 > "$file".dist ;

done
