team = [["dhoni","batsman",50],["kohli","batsman",90],["chahal","bowler",5],["ishant","bowler",4]]

heighestScorebatsman =team[0][2]
batsman = ""
for i in team:
    # print(i)
    if i[1] == "batsman":
        if i[2] > heighestScorebatsman:
            heighestScorebatsman = i[2]
            print(i[0])
            batsman = i[0]

print("Heighest Score Batsman is",batsman,"with score",heighestScorebatsman)            

totalRuns = 0
for i in team:
    if i[1] =="batsman":
        totalRuns = totalRuns + i[2]

print("Total Runs Scored by Batsman is",totalRuns)        
        

