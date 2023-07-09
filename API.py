# Team members
# ( Lakshay Bansal 2021059 
#   Krishna Somani 2021058)
#We have made an api of a chess platform Lichess. It is a free website for playing chess.
#In this api code we have used api token instead of key which works similar to an api key.
# We have added 5 queries for user to execute and extract data from lichess database. 
import requests,json
import berserk
k=True
while k==True:
    api_url='https://lichess.org/api'
    token='lip_sp8L85QauQLZD7H9g6r7'
    session = berserk.TokenSession(token)
    client = berserk.Client(session=session)
    Puzzle=client.users.get_puzzle_activity()
    print('''
1. Get Top 10
2. Get user by ID
3. Get Leaderboard
4. User rating History
5. Get streamers ID
6. Exit''')
    a=int(input('Select any option: '))


    def lboard(x):
        lb=client.users.get_leaderboard(x)
        return(json.dumps(lb,indent=4))

    if a==1:
        Top_10=client.users.get_all_top_10()
        print(json.dumps(Top_10,indent=4))

    if a==2:
        print('Some of the IDs(examples): drnykterstein , rebeccaharris , wollongong2021 , abasovn')
        id=input('Enter Player"s ID: ')
        s=client.users.get_public_data(id)
        print(s)

    if a==3:
        print('Some of the games(examples): bullet ,blitz ,rapid , ultrabullet ')
        pref=input("Enter Game Type:")
        print(lboard(pref))

    if a==4:
        id=input('Enter Player"s ID: ')
        print('Some of the IDs(examples): drnykterstein , rebeccaharris , wollongong2021 , abasovn')
        History=client.users.get_rating_history(id)
        print(f'Rating histroy of {id}:')
        print(History)

    if a==5:
        live=client.users.get_live_streamers()
        print(json.dumps(live,indent=4))
    if a==6:
        k=False
        break