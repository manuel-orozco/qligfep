import os

# Root directory of the setup FEP modules
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

# The directories to the input FF and run related input files are given here
FF_DIR = os.path.join(ROOT_DIR, "FF")
INPUT_DIR = os.path.join(ROOT_DIR, "INPUTS")

# Dictionary of locations of Q executables
Q_DIR = {'CSB':'/home/manuel/Software/Q6/bin/',
         'LOCAL':'/home/manuel/Software/Q6/bin/'
        }
BIN = os.path.join(ROOT_DIR, "bin")

# Directory for Schrodinger software (e.g., Maestro)
SCHROD_DIR = '/opt/schrodinger/suites2017-3/'

# CLUSTER INPUTS. To add your own cluster, use the same input as below
CSB = {'NODES'        : '1',
       'NTASKS'       : '16',
       'TIME'         : '0-12:00:00',  # d-hh:mm:ss
       'MODULES'      : 'module load gcc/6.2.0\n module load openmpi/2.1.0',
       'QDYN'         : Q_DIR['CSB'] + 'Qdyn6',
       'QPREP'        : Q_DIR['CSB'] + 'Qprep6',
       'QFEP'         : Q_DIR['CSB'] + 'Qfep6',
       'QCALC'        : Q_DIR['CSB'] + 'Qcalc6',
      }


LOCAL = {'NODES'      : '',
         'NTASKS'     : '',
         'TIME'       : '',  # d-hh:mm:ss
         'MODULES'    : '\n', # Add a \n for every added module
         'QDYN'         : Q_DIR['LOCAL'] + 'Qdyn6',
         'QPREP'        : Q_DIR['LOCAL'] + 'Qprep6',
         'QFEP'         : Q_DIR['LOCAL'] + 'Qfep6',
         'QCALC'        : Q_DIR['LOCAL'] + 'Qcalc6',
         'ACCOUNT'    : ''
        }
