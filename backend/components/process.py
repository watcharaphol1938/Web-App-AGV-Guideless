from setup.structure import Process, session
from components.plant import plant1, plant2, plant3, plant4

process1 = Process(1, "A", plant1.plant_id)
process2 = Process(2, "B", plant3.plant_id)
process3 = Process(3, "C", plant2.plant_id)
process4 = Process(4, "D", plant4.plant_id)
session.add(process1)
session.add(process2)
session.add(process3)
session.add(process4)