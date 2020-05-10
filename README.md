This is the basic template from which I am starting most of scripts I make.
It has "embedded" logging
It is written in Python3. It also work with Python2, but on some platforms, logging does not work properly.


It can be run directly:
python3 pythonTemplate.py param1


Or called by another script:
import pythonTemplate
pythonTemplate.mainFunction(param1)
