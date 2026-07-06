files=['report.csv','data.xlsx','summary.docx','report.csv','data.csv']
count=1
for f in files:
    for g in files[count:]:
        if f==g:
            print(f"Duplicate found {g}")
    count+=1