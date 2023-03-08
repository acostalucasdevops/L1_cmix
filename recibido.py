import tabula
import os
import pathlib as p




source = (r"\\192.168.192.3\cmix-artigas\ELECTROMECANICA\USUARIOS\13. Lucas Acosta\ConcretMix\12. 2023\01. Enero\12\recibidos")
for relPath,dirs,files in os.walk(source):
        for file in files:
            if "OT" in file and "NOTA" not in file and ".pdf" in file[-4:(len(file))]:
                old = os.path.join(source,relPath,file)  #p.Path(source + "/" + file)
                new = os.path.join(source,relPath,"NOTA LIC OT " + file[2:])
               #new = p.Path(source + "/" + "NOTA LIC OT " + file[2:])                
                os.rename(src= old, dst= new)


# source = (r"//192.168.192.3/cmix-artigas/ELECTROMECANICA/USUARIOS/13. Lucas Acosta/ConcretMix/12. 2023/01. Enero/12/recibidos/382 - Fundaciones equipos 220kV/NOTA LIC OT 1561-382-23-Fundaciones equipos 220kV.pdf")
# dest = (r"//192.168.192.3/cmix-artigas/ELECTROMECANICA/USUARIOS/13. Lucas Acosta/ConcretMix/12. 2023/01. Enero/12/recibidos/382 - Fundaciones equipos 220kV/OT561-382-23-Fundaciones equipos 220kV.pdf")
# os.rename(src= source, dst= dest)