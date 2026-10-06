select*
from AVION
where CAPACITE>350;

select NUMAV,NOMAV
from AVION
where localisation='kara';

select NUMPIL,VILLE_DEP
from PILOTE,VOL
where PILOTE.NUMPIL=VOL.NUMPIL;

