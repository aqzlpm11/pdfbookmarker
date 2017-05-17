import add_bookmarks

with open('outfile.txt', 'w') as fout:
    for line in open('mark.txt'):
        if len(line.strip()) == 0:
            continue
        name, page = line.split("\t")
        page = page.split("-")[0].strip()
        indent = "".join(['+' for i in name.split("    ") if len(i) == 0])
        name = name.strip()

        # print("+" + indent + name + "|" + page)
        fout.write("+" + indent + '"' + name + '"' + "|" + page + "\n")

add_bookmarks.run_script("../s.pdf", "outfile.txt", "a.pdf")
