## Common utilities quick guide
------

The `python/utils` folder contains utilities which you may find useful.

#### Value

This implements a number with uncertainty. It is based on ufloat so many operations are supported.
Since the uncertainty package is not installed on lxplus you need to install it the first time

```
pip install uncertainties
```

Features available also in ufloat:

* many operations overloaded
* representation in exp notation
* display in latex format
* control on the precision of the numbers
* automatic detection of the significant digits

Added features wrt the normal ufloat:

* you can add a unit
* you can display the number with a speficic scale
* you can easily add to the code a custom representation

Here an example:
```
from utils.value import Value
a = Value(3000,10,'MeV')
b = Value(4000,40,'MeV')
c = a + b
7000.0 +/- 50.0 MeV
c.change_scale(-3)
(7000000.0 +/- 50000.0) x 10^-3 MeV
c.change_unit(3,'GeV')
(7000.0 +/- 50.0) GeV
d = a / b
0.750 +/- 0.008
```

#### latex_builder

You can use this object to automatically build latex from templates and compile it.

Here an example
```
from utils.formatter import PartialFormatter as Formatter
from utils.latex_builder import latex_doc

fmt = Formatter()
table = fmt.format(open(loc.TEPLATES+"table_template.txt").read(),**results)

latex = latex_doc(loc.TABLES+"/table.tex")
latex.set_title("My cool title")
latex.add_to_preamble(loc.LHCB+"/preamble.tex")
latex.add_to_preamble(loc.LHCB+"/lhcb-symbols-def.tex")
latex.insert_line("Inserts some explanation: main text of the latex")
latex.insert_figure(glob.glob(loc.PLOTS+"*.pdf"),ninrow=2)
latex.insert_tabular(table,"Some nice caption")
latex.close_and_compile()
```

#### Particles DB

The LHCb text file LHCb/ParticleTable.txt contains all the properties of particles
as defined by LHCB. This will be parsed and made available to you as a python object.

Here an example
```
from utils.particles_DB import db
db['e-']
--------------------------------
Name     : e-
PDG ID   : 11
Charge   : -1.0
Mass     : 0.000511
Lifetime : 1e+16
Width    : 0.0
-------------------------------
db['p+'].mass
0.93827205
db['pi+'].mass
0.13957018
db['K+'].tau
1.237939e-08
db['Z0'].width
10.0
db['W+'].pdgid
24

from utils.particles_DB import db, pdgid_db, mass_db
pdg_db['p+']
pdgid_db['p+']
2212
mass_db['p+']
0.93827205
```



