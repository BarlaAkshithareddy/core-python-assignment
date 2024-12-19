class Patients:
    def search(search_disease,patients):
        l=[]
        for i in patients:
            if i["Disease"]==search_disease:
                l.append(i['Name'])
        return l   
    patients=eval(input("paitents = "))
    search_disease=input("search_disease = ")
    res=search(search_disease,patients)
    print("Patients with Flu: ",res)