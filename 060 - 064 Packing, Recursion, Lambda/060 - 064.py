# 01
def get_score(**score) :
    for key , value in score.items() :
        print(f"{key} => {value}")

get_score(math="90%",Science="80%",Language="70%")
print("=" * 50)
get_score(Logic="70", Problems="60")

# 02 


def get_people_scores(name="",**scores) : 
    if scores == {}:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        if name != "" :
            print(f"Hello {name} This Is Your Score Table:")
        for key , value in scores.items():
            print(f"{key} => {value}")

get_people_scores("Ahmed")
print("=" * 50)
get_people_scores(Logic="70", Problems="60")
print("=" * 50)
get_people_scores("Mahmoud", Logic="70", Problems="60")
print("=" * 50)
get_people_scores("Osama", Math="90", Science="80", Language="70")

name = "Ahmed"
print(bool(name))

# 03 
scores_list = {
    'Math': "80%",
    'lang': "70%",
    'science': "50%",
    'Python': "80%",
    "Go": "40%"
}



def get_the_scores(name="", **scores) :
    if len(scores) > 0:
        if bool(name) :
            print(f"Hello {name} This Is Your Score Table:")
            for e,r in scores.items():
                print(f"{e} => {r}")
        else:
            for e,r in scores.items():
                print(f"{e} => {r}")
    else:
        print(f"Hello {name} You Have No Scores To Show")

get_the_scores("Osama", **scores_list) 
print("=" * 50)
get_the_scores("Osama")
print("=" * 50)
get_the_scores(**scores_list)

