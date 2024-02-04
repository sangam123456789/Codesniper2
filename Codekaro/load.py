import subprocess

commands = [
    "python manage.py loaddata ./backup/dp.json",
    "python manage.py loaddata ./backup/tree.json",
    "python manage.py loaddata ./backup/beginner.json",
    "python manage.py loaddata ./backup/binary.json",
    "python manage.py loaddata ./backup/bits.json",
    "python manage.py loaddata ./backup/brain.json",
    "python manage.py loaddata ./backup/brute.json",
    "python manage.py loaddata ./backup/dpstand.json",
    "python manage.py loaddata ./backup/dsu.json",
    "python manage.py loaddata ./backup/graph.json",
    "python manage.py loaddata ./backup/greedy.json",
    "python manage.py loaddata ./backup/hash.json",
    "python manage.py loaddata ./backup/implement.json",
    "python manage.py loaddata ./backup/mixed.json",
    "python manage.py loaddata ./backup/pair.json",
    "python manage.py loaddata ./backup/pointer.json",
    "python manage.py loaddata ./backup/recursion.json",
    "python manage.py loaddata ./backup/segtree.json",
    "python manage.py loaddata ./backup/sort.json",
    "python manage.py loaddata ./backup/sub.json"
]

for command in commands:
    subprocess.run(command, shell=True)
