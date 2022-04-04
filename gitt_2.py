import os
import  requests

def repo_creator(name,private):
    api_key=os.environ.get("api_key")
    url="https://api.github.com/user/repos"
    head={
        "Authorization": f"Bearer  {api_key}"
    }
    repo_info={
        "name":name,
        "private":private
    }
    try:
        r=requests.post(url,headers=head,json=repo_info)
        return f"Repo has been created {r.status_code}"
    except Exception:
        return  f"Please check api key or data input {r.status_code}"

    
answer=None
name_of_repo = input("Please create a name for your repo? ")
while True:
    private_option= input("would you like to to make this private y/n: ").lower()
    answer_options=['y','n']
    
    if private_option not in answer_options:
        print("please check your input.please pick (y/n) ")
        continue

    if private_option == "y":
        answer = True
        break

    if private_option == "n":
        answer = False
        break


repo_builder=repo_creator(name_of_repo, answer)
print(repo_builder)
