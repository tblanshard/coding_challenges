def scoreRanker(scores, arr):
    ranking = {}
    lastSeen = 0
    lastRanking = 0
    for i, score in enumerate(scores):
        if lastSeen != score:
            ranking[score] = lastRanking + 1
            lastSeen = score
            lastRanking += 1
    for item in arr:
        if item in ranking:
            print(ranking[item])
        else:
            copy = item
            while copy not in ranking and copy > 0:
                copy -= 1
            if copy == 0:
                new_ranking = len(ranking) - 1
                ranking[item] = new_ranking
                print(new_ranking)

            else:
                new_ranking = ranking[copy]
                for item in ranking:
                    if ranking[item] >= new_ranking:
                        ranking[item] += 1
                ranking[item] = new_ranking
                print(new_ranking)





scoreRanker([100,90,90,80,75,60], [50,65,77,90,102])
