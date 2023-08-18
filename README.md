# SubdirectoryCompiler-
Works only with Windows (so far, as tested)
Takes all contents of all subdirectories in the same directory of the python file and compiles them into a single folder named "# Compiled". 
In the unlikely case any duplicates are found, they will be placed in a folder named "# Duplicates" and given a (1) and (2) tag for each duplicate file for the user to manually adjust.

Each file will be renamed to contain the folder name in the front of the file. For instance, the following files would be compiled as follows:

- Original file: "./Cats/Persian.jpg"
- Compiled file: "./# Compiled/Cats Persian.jpg"

- Original file: "./Fruits/Apple.jpg"
- Compiled file: "./# Compiled/Fruits Apple.jpg"

Any duplicates will be compiled as follows:

- Duplicate #1 file: "./Cats/Apple.jpg"
- Duplicate #2 file: "./Fruits/Apple.jpg"
- Compiled file #1: "./# Duplicates/Apple (1).jpg"
- Compiled file #2: "./# Duplicates/Apple (2).jpg"

No duplicate files will be placed in the "# Compiled" folder, unless done so by the user manually (after any disputes have been resolved).
