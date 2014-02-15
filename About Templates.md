Walker's Templates
==================
Walker's templates is a directory to help rsync to find correct files and walker build right directories and create proper configs

*/templates/structure
- $distrname$
..*excludes
..*includes
..*config
- master
..*excludes
..*includes
..*config

excludes - a file to add exclusions to rsync -r 
includes - a file to add inclusions to rsync -r
master