from math import dist, sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def approach1(applicants,treasure):
    def dist_treasure(x,y):
        tx, ty = treasure
        return dist(tx, ty, x, y)
    (x1,y1),(x2,y2),(x3,y3),(x4,y4) = applicants
    #3 diff pairings
    p = [
        (dist(x1,y1,(x1+x2)/2,(y1+y2)/2),dist(x3,y3,(x3+x4)/2,(y3+y4)/2)),
        (dist(x1,y1,(x1+x3)/2,(y1+y3)/2),dist(x2,y2,(x2+x4)/2,(y2+y4)/2)),
        (dist(x1,y1,(x1+x4)/2,(y1+y4)/2),dist(x3,y3,(x3+x2)/2,(y3+y2)/2))
    ]
    idx = min(range(3), key=lambda i:p[i][0] + p[i][1])
    cx1,cy1, cx2,cy2 = {
        0: ((x1+x2)/2,(y1+y2)/2,(x3+x4)/2,(y3+y4)/2),
        1: ((x1+x3)/2,(y1+y3)/2,(x2+x4)/2,(y2+y4)/2),
        2: ((x1+x4)/2,(y1+y4)/2,(x3+x2)/2,(y3+y2)/2)
    }[idx]
    dists = [dist_treasure(x,y) for x,y in applicants]

    #0: p1 & p2, p3 & p4
    #1: p1 & p3, p2 & p4
    #2: p1 & p4, p2 & p3
    data = {"applicants": applicants, 
            "midpoints": [(cx1, cy1), (cx2, cy2)],
            "idx": idx}
    data["time"] = min(p[idx][0] + dist_treasure(cx1,cy1),p[idx][1] + dist_treasure(cx2,cy2))/5
    return data

def approach2(applicants, treasure):
    def dist_treasure(x,y):
        tx, ty = treasure
        return dist(tx, ty, x, y)
    (x1,y1),(x2,y2),(x3,y3),(x4,y4) = applicants
    #3 diff pairings
    p = [
        (dist(x1,y1,(x1+x2)/2,(y1+y2)/2),dist(x3,y3,(x3+x4)/2,(y3+y4)/2)),
        (dist(x1,y1,(x1+x3)/2,(y1+y3)/2),dist(x2,y2,(x2+x4)/2,(y2+y4)/2)),
        (dist(x1,y1,(x1+x4)/2,(y1+y4)/2),dist(x3,y3,(x3+x2)/2,(y3+y2)/2))
    ]
    idx = min(range(3), key=lambda i:min(p[i][0],p[i][1]))
    #0: p1 & p2, p3 & p4
    #1: p1 & p3, p2 & p4
    #2: p1 & p4, p2 & p3
    cx1,cy1, cx2,cy2 = {
        0: ((x1+x2)/2,(y1+y2)/2,(x3+x4)/2,(y3+y4)/2),
        1: ((x1+x3)/2,(y1+y3)/2,(x2+x4)/2,(y2+y4)/2),
        2: ((x1+x4)/2,(y1+y4)/2,(x3+x2)/2,(y3+y2)/2)
    }[idx]
    data = {"applicants": applicants, 
            "midpoints": [(cx1, cy1), (cx2, cy2)],
            "idx": idx}
    data["time"] = min(p[idx][0] + dist_treasure(cx1,cy1),p[idx][1] + dist_treasure(cx2,cy2))/5
    return data