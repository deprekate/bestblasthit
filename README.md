# bestblasthit
A small utility to parse blast output and return only the best hit

To install `bestblasthit`,
```sh
 git clone https://github.com/deprekate/bestblasthit.git
 cd bestblasthit; make
```

Example
--------------

The included sample blast output file has multiple query hits for two sequences. We want to drop all but the two top hits, in addition to skipping hits that are to themselves (i.e. seq1 to seq1)

To run on the example data:
```sh
cat example.blastn | ./bestblasthit 
```
Output are only the single top hit for each subject sequence, and should look like
```sh
seq1	seq2	100.000	64	0	0	1	64	1	64	7.91e-33	119
seq2	seq1	100.000	64	0	0	1	64	1	64	7.91e-33	119
```

