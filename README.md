# Models of SmartH2O project
----

This repository contains the SmartH2O agent-based models for the district of __Valencia__, Spain (top folder `emivasa`) and the district of __Terre di Pedemonte__, Switzerland (top folder `ses`).

Each top folder contains four subfolders:

- `baseline` : the ABM source (the .alp file) simulating the baseline water consumption of the concerned district
- `baseline java applet`: the java applet of the baseline model, it is useful to run the model if you don't have Anylogic installed. 
- `observation` : the ABM source (the .alp file) simulating the water consumption of the users after that they have adopted the SmartH2O portal.
- `observation java applet`: the java applet of the observation model, it is useful to run the model if you don't have Anylogic installed.

In particular, each folder contains `esempi.xlsx` and `histograms.xlsx` files, containing the consumption characteristics of the agents in the model.

In addition, each observation’s subfolder, contains a `transition.xlsx` file: this contains the transition matrices for updating consumption characteristics of agents during the simulation.

## Security
In order to certificate the autenticity of the files, each folder contains the file `sha256sum.txt`: it lists the sha256 hash of every file present in the folder. The file has also been signed with the SmartH2O [OpenPGP](http://openpgp.org/) key, and the signature has been saved to `sha256sum.txt.asc`.

Thus, if you want to verify the files you downloaded, you have to perform two steps:

1. Verify the sign of `sha256sum.txt` using `sha256sum.txt.asc`
2. Verify the hashes contained into `sha256sum.txt`

The SmartH2O key, [available here](https://pgp.mit.edu/pks/lookup?op=vindex&search=0x9739174C8B57ACA9), has this fingerprint: `7F14 4F03 BCB9 9A3C D99D 7483 9739 174C 8B57 ACA9`

## Contacts
For any type of further questions write to `smarth2o@idsia.ch`. 
The maintainer of this dataset is Corrado Valeri (`corrado.valeri@supsi.ch`).
