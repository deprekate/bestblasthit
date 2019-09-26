# bestblasthit
A small utility to parse blast output and return only the best hit

To install `bestblasthit`,
```sh
 git clone https://github.com/deprekate/bestblasthit.git
 cd bestblasthit; make
```

Example
--------------

Run on included sample data:
```sh
cat example.blastn | ./bestblasthit 
```
Output are only the single top hit for each subject sequence, and should look like
```sh
one	two	100.000	64	0	0	1	64	1	64	7.91e-33	119
two	one	100.000	64	0	0	1	64	1	64	7.91e-33	119
```

