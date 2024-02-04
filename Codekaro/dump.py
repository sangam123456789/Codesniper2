import subprocess

commands = [
    "python manage.py dumpdata Home.dp --indent 4 > ./backup/dp.json",
    "python manage.py dumpdata Home.tree --indent 4 > ./backup/tree.json",
    "python manage.py dumpdata Home.beginner --indent 4 > ./backup/beginner.json",
    "python manage.py dumpdata Home.binary --indent 4 > ./backup/binary.json",
    "python manage.py dumpdata Home.bit --indent 4 > ./backup/bits.json",
    "python manage.py dumpdata Home.brain --indent 4 > ./backup/brain.json",
    "python manage.py dumpdata Home.brute --indent 4 > ./backup/brute.json",
    "python manage.py dumpdata Home.dpstand --indent 4 > ./backup/dpstand.json",
    "python manage.py dumpdata Home.dsu --indent 4 > ./backup/dsu.json",
    "python manage.py dumpdata Home.graph --indent 4 > ./backup/graph.json",
    "python manage.py dumpdata Home.greed --indent 4 > ./backup/greedy.json",
    "python manage.py dumpdata Home.hash --indent 4 > ./backup/hash.json",
    "python manage.py dumpdata Home.implement --indent 4 > ./backup/implement.json",
    "python manage.py dumpdata Home.mixed --indent 4 > ./backup/mixed.json",
    "python manage.py dumpdata Home.pair --indent 4 > ./backup/pair.json",
    "python manage.py dumpdata Home.pointer --indent 4 > ./backup/pointer.json",
    "python manage.py dumpdata Home.recursion --indent 4 > ./backup/recursion.json",
    "python manage.py dumpdata Home.segtree --indent 4 > ./backup/segtree.json",
    "python manage.py dumpdata Home.sort --indent 4 > ./backup/sort.json",
    "python manage.py dumpdata Home.sub --indent 4 > ./backup/sub.json",
    "python manage.py dumpdata --indent 4 > ./backup/all.json"
]

for command in commands:
    subprocess.run(command, shell=True)
