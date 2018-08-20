from app.models import QuestionsModel

# The dictionaries are being accessed as objects.
qns_data = [
    QuestionsModel(
        qns={
            "qn_id": 1,
            "qn_title": "How do you un-stage all commits using the terminal?",
            "qn_details": """I accidentally added a lot of temporary files using git add -A.
            I managed to un-stage the files using the following commands and managed to remove the dirty index.""",
            "answers": ["git reset", "rm .git/index", "git rm -rf --cached", "git stash && git stash pop"]
        }
    ),
    QuestionsModel(
        qns={
            "qn_id": 2,
            "qn_title": "How do you move a file to another folder the terminal?",
            "qn_details": """I am using Ubuntu 18.0 LTS and git is tracking my changes 
            thus interested in the command line""",
            "answers": ["mv [file] [directory]", "sudo mv info.txt config/", "mv info.txt config/information.txt"]
        }
    )
]
