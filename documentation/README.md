# README for SatNOGs documentation

Welcome Traveller!

This README is meant to help you find your way around this folder structure,
which should be rather intuitive.

## Building documentation

Most of the documents are written in LaTeX, so to compile them into PDFs for
easier viewing one needs LaTeX installed. There is also a helper script in both
folders called `make`, which will run the required commands to generate PDF
files.

To compile them run the following:
```
./make pdf
```

To remove all generated files run:
```
./make clean
```

## Software Requirements Doc

This document contains the requirements of our software system. It should be
read along side the spec and serves to aid the implmeneter in what *exactly*
we want out of the software system and how it should be approached. It also
contains definitions.


## SPEC

This document contains a highlevel overview of the software system, along with
some implementation details and references to the current state of the software.


## Progress Reports

You can find all of the progress reports that we made throughout the semester
under `progress_reports/`. They are numbered and dated. They should be read
to see some of our ideas and how they progressed as time went on.
