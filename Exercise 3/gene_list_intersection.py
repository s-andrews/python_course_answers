#!python

# Finding the intersection of two lists
list1 = ["Npepl1", "Rab13", "Reg4", "Asb17", "Clcnka", "Nup62", "Upf3a", "Kcnn1", "Ccdc151", "Arg1", "Tmem98", "Mtx3", "Isl1", "Fam53c"]
list2 = ["Kcnj2", "Rab13", "Reg4","Nol6", "Masp2", "Clcnka", "Upf3a", "Kcnn1", "Arg1", "Krt75", "Smpd3", "Mtx3", "Trim8", "Fam53c"]

intersection_list = []

for gene in list1:
    if gene in list2:
        intersection_list.append(gene)


print ("Genes in both lists were:\n")

intersection_list.sort()

for pos,gene in enumerate(intersection_list):
    print(pos+1,gene)


