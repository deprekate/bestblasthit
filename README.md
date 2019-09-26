# bestblasthit
A small utility to parse blast output and return only the best hit

To install `bestblasthit`,
```sh
 git clone https://github.com/deprekate/bestblasthit.git
 cd bestblasthit; make
```

Optionally then copy the compiled binary to the bin folder or somewhere else that is on your PATH

## Example
--------------

The included sample blast output file has multiple query hits for two sequences. We want to drop all but the two top hits, in addition to skipping hits that are to themselves (i.e. seq1 to seq1)

### Running
To test the program, run blastn on the sample fasta file and then pipe the output to bestblasthit:
```sh
blastn -subject tests/example.fasta -query tests/example.fasta -outfmt 6 -word_size 5 | ./bestblasthit  
```
If you already have output from a blast run you can pipe it to the bestblasthit binary:
```sh
cat tests/example.blastn | ./bestblasthit
```

### Output
Output is only the single top hit for each subject sequence, and should look like
```sh
seq1	seq2	100.000	50	0	0	1	50	1	50	2.86e-25	93.5
seq2	seq1	100.000	50	0	0	1	50	1	50	2.86e-25	93.5
```

