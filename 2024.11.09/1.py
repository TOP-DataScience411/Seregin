import sys

email = sys.stdin.readline().strip()

if email.count("@") == 1 and email.count(".") == 1:
    if email.find("@") + 1 < email.find("."):
        sys.stdout.write("да\n")
    else:
        sys.stdout.write("нет\n")
else:
    sys.stdout.write("нет\n")