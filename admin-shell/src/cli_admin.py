from __future__ import annotations
import requests

def add_user():
    username:str = input("Enter username:")
    email:str = input("Enter email:")
    password:str = input("Enter password:")
    resp = requests.post("http://auth-backend:8000/internal/register",json={
        "username":username,
        "email":email,
        "password":password,
    })
    print(resp.status_code,resp.json())

if __name__ == "__main__":

        std_input:int = int(input("""
- User Management
1. add user
Enter mode (number): """))

        match std_input:
            case 1:
                add_user()

        
