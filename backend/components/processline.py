from setup.structure import ProcessLine, session
from components.process import process1, process2, process3, process4

processline1 = ProcessLine(1, "E", process1.process_id)
processline2 = ProcessLine(2, "F", process3.process_id)
processline3 = ProcessLine(3, "G", process2.process_id)
processline4 = ProcessLine(4, "H", process4.process_id)
session.add(processline1)
session.add(processline2)
session.add(processline3)
session.add(processline4)