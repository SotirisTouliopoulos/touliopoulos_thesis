for file in ./dir_001/*.pdb ;

    #do python3 ./A_parser.py "$file" 4.0 > "$file".dist ;
    do python3 ./Z_parser.py "$file" 4.0 > "$file".dist ;

    #do python3 ./A_parser.py "$file" 5.0 > "$file".dist ;
    #do python3 ./Z_parser.py "$file" 5.0 > "$file".dist ;

    #do python3 ./A_parser.py "$file" 6.0 > "$file".dist ;
    #do python3 ./Z_parser.py "$file" 6.0 > "$file".dist ;

    #do python3 ./A_parser.py "$file" 7.0 > "$file".dist ;
    #do python3 ./Z_parser.py "$file" 7.0 > "$file".dist ;

    #do python3 ./A_parser.py "$file" 8.0 > "$file".dist ;
    #do python3 ./Z_parser.py "$file" 8.0 > "$file".dist ;
    
    #do python3 ./A_parser.py "$file" 9.0 > "$file".dist ;
    #do python3 ./Z_parser.py "$file" 9.0 > "$file".dist ;

    #do python3 ./A_parser.py "$file" 10.0 > "$file".dist ;
    #do python3 ./Z_parser.py "$file" 10.0 > "$file".dist ;

done