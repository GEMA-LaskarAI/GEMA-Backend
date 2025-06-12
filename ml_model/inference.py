from main import recommend_majors

data = [
    {
        "question_id": "PS001",
        "score": 3
    },
    {
        "question_id": "PS002",
        "score": 4
    },
    {
        "question_id": "PS003",
        "score": 3
    },
    {
        "question_id": "PS004",
        "score": 1
    },
    {
        "question_id": "PS005",
        "score": 4
    },
    {
        "question_id": "PS006",
        "score": 2
    },
    {
        "question_id": "PS007",
        "score": 5
    },
    {
        "question_id": "PS008",
        "score": 1
    },
    {
        "question_id": "PS009",
        "score": 2
    },
    {
        "question_id": "PS010",
        "score": 4
    },
    {
        "question_id": "PS011",
        "score": 5
    },
    {
        "question_id": "PS012",
        "score": 2
    },
    {
        "question_id": "PS013",
        "score": 1
    },
    {
        "question_id": "PS014",
        "score": 1
    },
    {
        "question_id": "PS015",
        "score": 2
    },
    {
        "question_id": "PS016",
        "score": 4
    },
    {
        "question_id": "PS017",
        "score": 3
    },
    {
        "question_id": "PS018",
        "score": 1
    },
    {
        "question_id": "PS019",
        "score": 1
    },
    {
        "question_id": "PS020",
        "score": 1
    },
    {
        "question_id": "PS021",
        "score": 2
    },
    {
        "question_id": "PS022",
        "score": 5
    },
    {
        "question_id": "PS023",
        "score": 1
    },
    {
        "question_id": "PS024",
        "score": 4
    },
    {
        "question_id": "PS025",
        "score": 5
    },
    {
        "question_id": "PS026",
        "score": 1
    },
    {
        "question_id": "PS027",
        "score": 5
    },
    {
        "question_id": "PS028",
        "score": 1
    },
    {
        "question_id": "PS029",
        "score": 5
    },
    {
        "question_id": "PS030",
        "score": 3
    },
    {
        "question_id": "PS031",
        "score": 1
    },
    {
        "question_id": "PS032",
        "score": 2
    },
    {
        "question_id": "PS033",
        "score": 4
    },
    {
        "question_id": "PS034",
        "score": 1
    },
    {
        "question_id": "PS035",
        "score": 4
    },
    {
        "question_id": "PS036",
        "score": 2
    },
    {
        "question_id": "PS037",
        "score": 5
    },
    {
        "question_id": "PS038",
        "score": 3
    },
    {
        "question_id": "PS039",
        "score": 1
    },
    {
        "question_id": "PS040",
        "score": 4
    },
    {
        "question_id": "PS041",
        "score": 4
    },
    {
        "question_id": "PS042",
        "score": 1
    },
    {
        "question_id": "PS043",
        "score": 3
    },
    {
        "question_id": "PS044",
        "score": 5
    },
    {
        "question_id": "PS045",
        "score": 2
    },
    {
        "question_id": "PS046",
        "score": 2
    },
    {
        "question_id": "PS047",
        "score": 2
    },
    {
        "question_id": "PS048",
        "score": 3
    },
    {
        "question_id": "PS049",
        "score": 1
    },
    {
        "question_id": "AI001",
        "score": 4
    },
    {
        "question_id": "AI002",
        "score": 1
    },
    {
        "question_id": "AI003",
        "score": 2
    },
    {
        "question_id": "AI004",
        "score": 5
    },
    {
        "question_id": "AI005",
        "score": 2
    },
    {
        "question_id": "AI006",
        "score": 1
    },
    {
        "question_id": "AI007",
        "score": 2
    },
    {
        "question_id": "AI008",
        "score": 3
    },
    {
        "question_id": "AI009",
        "score": 5
    },
    {
        "question_id": "AI010",
        "score": 3
    },
    {
        "question_id": "AI011",
        "score": 3
    },
    {
        "question_id": "AI012",
        "score": 1
    },
    {
        "question_id": "AI013",
        "score": 5
    },
    {
        "question_id": "AI014",
        "score": 3
    },
    {
        "question_id": "AI015",
        "score": 2
    },
    {
        "question_id": "AI016",
        "score": 3
    },
    {
        "question_id": "AI017",
        "score": 4
    },
    {
        "question_id": "AI018",
        "score": 3
    },
    {
        "question_id": "AI019",
        "score": 3
    },
    {
        "question_id": "AI020",
        "score": 3
    },
    {
        "question_id": "AI021",
        "score": 3
    },
    {
        "question_id": "AI022",
        "score": 1
    },
    {
        "question_id": "AI023",
        "score": 3
    },
    {
        "question_id": "AI024",
        "score": 3
    },
    {
        "question_id": "AI025",
        "score": 2
    },
    {
        "question_id": "AI026",
        "score": 1
    },
    {
        "question_id": "AI027",
        "score": 2
    },
    {
        "question_id": "AI028",
        "score": 3
    },
    {
        "question_id": "AI029",
        "score": 5
    },
    {
        "question_id": "AI030",
        "score": 4
    },
    {
        "question_id": "AI031",
        "score": 5
    },
    {
        "question_id": "AI032",
        "score": 2
    },
    {
        "question_id": "AI033",
        "score": 3
    },
    {
        "question_id": "AI034",
        "score": 1
    },
    {
        "question_id": "AI035",
        "score": 3
    },
    {
        "question_id": "AI036",
        "score": 2
    },
    {
        "question_id": "AI037",
        "score": 2
    },
    {
        "question_id": "AI038",
        "score": 1
    },
    {
        "question_id": "AI039",
        "score": 4
    },
    {
        "question_id": "AI040",
        "score": 2
    },
    {
        "question_id": "AI041",
        "score": 2
    },
    {
        "question_id": "AI042",
        "score": 5
    },
    {
        "question_id": "AI043",
        "score": 3
    },
    {
        "question_id": "AI044",
        "score": 1
    },
    {
        "question_id": "AI045",
        "score": 3
    },
    {
        "question_id": "AI046",
        "score": 4
    },
    {
        "question_id": "AI047",
        "score": 5
    },
    {
        "question_id": "AI048",
        "score": 2
    },
    {
        "question_id": "AI049",
        "score": 3
    }
]

answer = [answer['score'] for answer in data]
majors = recommend_majors(answer)
print("Recommended Majors:", majors)