# STARK: a tool for dependency-tree extraction and analysis
STARK is a highly-customizable tool that extracts different types of syntactic trees from parsed corpora (treebanks) and quantifies them with respect to frequency and other useful statistics, such as the strength of association between the nodes of a tree, and the tree's keyness in comparison to another treebank.

It is primarily aimed at processing treebanks based on the [Universal Dependencies](https://universaldependencies.org/) annotation scheme, but it also takes any other dependency treebank in the [CONLL-U](https://universaldependencies.org/format.html) format as input. 

## Installation and execution
Install Python 3 on your system (https://www.python.org/downloads/). 

### Linux users
Install pip and other libraries required by program, by running the following commands in terminal:
```bash
sudo apt install python3-pip
cd <PATH TO PROJECT DIRECTORY>
pip3 install -r requirements.txt
```

Execute extraction by first moving to project directory and executing the script with:
```bash
python3 stark.py 
```

### Windows users
Download pip installation file (https://bootstrap.pypa.io/get-pip.py) and install it by double clicking on it.

Install other libraries necessary for running by going into program directory and double clicking on `install.bat`. If windows defender is preventing execution of this file you might have to unblock that file by `right-clicking on .bat file -> Properties -> General -> Security -> Select Unblock -> Select Apply`.

Execute extraction by running `run.bat` (in case it is blocked repeat the same procedure as for `install.bat`).

### Default settings
By default, running the program as described above extracts trees from the `sample.conllu` file as defined by the settings in the `config.ini` file, i.e. all noun-headed trees occurring with part-of-speech tags as nodes. For more information on how to change the input file, the type of trees to be extracted and all other customizible parameters, see the [Settings](Settings) section below.

## Output

STARK produces a tab-separated (.tsv) file with a frequency-ranked list of all the trees matching the input criteria, as illustrated by the first few lines of the default output below. The description of the tree is given in the first column, while subsequent columns include additional information on individual nodes, the absolute and relative frequencies, the surface node order, and the root.

For adding other types of information to the output, such as additional statistics and links to visualised examples, see [Settings](Settings) below.

|Tree | Node A | Node B | Node C | A-Freq | R-Freq | Order | Nodes | Root |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DET <det NOUN | DET | NOUN |  | 1345 | 10773.01 | AB | 2 | NOUN| 
| ADP <case DET <det NOUN | ADP | DET | NOUN | 1163 | 9315.25 | ABC | 3 | NOUN| 
| ADP <case NOUN | ADP | NOUN |  | 1090 | 8730.54 | AB | 2 | NOUN| 
| PRON <nmod:poss NOUN | PRON | NOUN |  | 487 | 3900.71 | AB | 2 | NOUN| 
| CCONJ <cc NOUN | CCONJ | NOUN |  | 476 | 3812.61 | AB | 2 | NOUN| 


## Settings
The types of trees to be extracted and the associated output information can be defined through the parameters listed below and described in [more detail here](settings.md).

General settings:
-	`input`: location of the input file or directory (parsed corpus in .conllu)
-	`output`: location of the output file (frequency list in .tsv)

Tree specification:
-	`size`: number of nodes in the tree (integer or range)
- `node_type`: node characteristic under investigation (*form*, *lemma*, *upos* or *xpos*, *feats* or *deprel*)
-	`complete`: extraction of full subtrees only (i.e. heads with all dependents) rather than all possible subtrees (values *yes* or *no*)
-	`labeled`: extraction of labeled or unlabeled trees (values *yes* or *no*)
-	`fixed`: differentiating trees by surface word order (values *yes* or *no*)

Tree restrictions:
-	`root`: predefined characteristics of the root node (e.g. upos=NOUN)
-	`labels`: predefined list of dependency labels allowed in the extracted tree (values *yes* or *no*)
-	`query`: predefined tree structure based on the [DepSearch](https://orodja.cjvt.si/drevesnik/help/en/) query language(e.g. _ >obl NOUN).

Statistics: 
-	`association_measures`: calculates the strength of association between nodes by MI, MI3, t-test, logDice, Dice and simple-LL scores (values *yes* or *no*)
- `compare`: calculates the keyness of a tree in comparison to another treebank by LL, BIC, log ratio, odds ratio and %DIFF scores (reference treebank in .conllu)

Additional visualization:
- `grew_match`: describes the trees structure using the [grew](https://grew.fr/doc/request/) query language and links to UD treebank examples at https://universal.grew.fr/
- `dep_search`: describes the tree structure using the [DepSearch](https://orodja.cjvt.si/drevesnik/help/en/) query language

Output size:
-	`frequency_threshold`: minimum frequency of the tree in the treebank
-	`max_lines`: maximum number of trees in the output file

### Changing the settings


## Acknowledgment
This program was developed by Luka Krsnik in collaboration with Kaja Dobrovoljc and Marko Robnik Šikonja. Financial and infrastructural support was provided by [Slovenian Research and Innovation Agency](https://www.aris-rs.si/),  [CLARIN.SI](https://www.clarin.si/) and [CJVT UL](https://www.cjvt.si).

<p align="center">
<a href="http://www.clarin.si/info/about/"><img src="https://raw.githubusercontent.com/clarinsi/STARK/master/logos/CLARIN.png" alt="drawing" height="90"/></a>
<a href="https://www.arrs.si/"><img src="https://raw.githubusercontent.com/clarinsi/STARK/master/logos/ARRS.png" alt="drawing" height="110"/></a>
<a href="https://www.cjvt.si/en/"><img src="https://raw.githubusercontent.com/clarinsi/STARK/master/logos/CJVT.png" alt="drawing" height="70"/></a>
</p>

