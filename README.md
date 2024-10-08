Hello, this is a script for Dr. Hanyu Wei's concept of finding a method to rank chips on previously trained data.
Currently, this is 5 months of work by one person (me) and we're still cleaning data.


Current progress:
-Re did file searching system, actually now grabs all files within all subfolders and current folders
(THE ABOVE WILL BE EVEN BETTER FOR MOTHERBOARDS WHEN THEY COME IN; this only works for ASIC chips but should be easily transferrable)
-made a slightly inefficient file search function, could refine it further
-currently working on putting all data into the hdf5 file

Issues:
- not all csvs contain purely numeric/string/both data, so need to parse through that

Ideas:
- Polars for larger csvs?