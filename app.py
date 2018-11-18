
import praw
import collections
import dash
import dash_core_components as dcc
import dash_html_components as html
import smtplib
from abc import ABC, abstractmethod


reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent= "",
                     username="",
                     password="")

listScore = {}
commentScore = {}
xList = []
yList = []
x2List = []
y2List = []
x1List = []
y1List = []

class RedditBase():
    def __init__(self, para):
     self.para = para

     #helper function
    def writeIntoFile(self, holderToWrite):
        file = open("data.txt", "a")
        lineDivider = ('------------------------')
        file.write(holderToWrite)
        file.write(lineDivider)

    def startReddit(self):
        subRedditSearch = input ("What do you wanna search for ?")
        subreddit = reddit.subreddit(subRedditSearch)
        print(subreddit.display_name)
        print(subreddit.title)
        self.writeIntoFile(subreddit.title)
        print(subreddit.description)
        self.writeIntoFile(subreddit.description)
        self.redditFiller(subreddit)

    def redditFiller(self, subreddit):
        for submission in subreddit.hot(limit=10):
            listScore[submission.score] = submission.title
            commentScore[submission.title] = submission.num_comments

        self.graphCreator(listScore)
        self.graphCreator1(commentScore)

    def graphCreator(self, listScore):
        print("Before Sorting : ")
        self.writeIntoFile("Before Sorting : ")
        for k, v in listScore.items():
            print (k, v)
            x2List.append(k)
            y2List.append(v)
            contentHolder = ('\n{} : {}\n'.format(k, v))
            self.writeIntoFile(contentHolder)
        print("\n")
        od = collections.OrderedDict(sorted(listScore.items()))
        print("After Sorting : ")
        self.writeIntoFile("After Sorting : ")
        for k, v in od.items():
            contentHolder = ('\n{} : {}\n'.format(k, v))
            self.writeIntoFile(contentHolder)
            print (k, v)
            xList.append(k)
            yList.append(v)

        print(xList)
        print(yList)


    def graphCreator1(self, commentScore):
        print("Comments Section: ")
        self.writeIntoFile("Comments Section: ")
        for k, v in commentScore.items():
            print (k, v)
            x1List.append(k)
            y1List.append(v)
            contentHolder = ('\n{} : {}\n'.format(k, v))
            self.writeIntoFile(contentHolder)

        print(x1List)
        print(y1List)

class DashBase(ABC):
    def __init__(self, par):
        self.par = par

    @abstractmethod
    def chartsTime(self, param1, param2, param3, param4, param5, param6):
        raise NotImplementedError("Subclass must implement this abstract method")

class DashBoard(DashBase):
    def __init__(self, f):
        super().__init__(f)

    def chartsTime(self, x1List, y1List, xList, yList, x2List, y2List):
        graphy = dash.Dash()
        graphy.layout = html.Div([
            html.H1(
                children='Reddit Submissions (x-axis) v. Top Score & No. of Comments(y-axis)',
                style={
                    'textAlign': 'center',
                }
            ),
            html.Div(
                className="row",
                children=[
                    html.Div(
                        className="six columns",
                        children=[
                            html.Div(
                                dcc.Graph(
                                    id='right-graph',
                                    figure={
                                        'data': [{
                                            'x': x1List,
                                            'y': y1List,
                                            'type': 'scatter',
                                            'name': 'Submissions v. Number of Comments'
                                        }],
                                        'layout': {
                                            'height': 800,
                                        },
                                        'marker': {
                                             'size': 15,
                                             'line': {'width': 0.5, 'color': 'red'}
                                        },
                                    }
                                )
                            )
                        ]
                    ),
                    html.Div(
                        className="six columns",
                        children=html.Div([
                            dcc.Graph(
                                id='right-top-graph',
                                figure={
                                    'data': [{
                                        'x': y2List,
                                        'y': x2List,
                                        'type': 'bar',
                                        'name': 'Score v. Submissions'

                                    }],
                                    'layout': {
                                        'height': 400,
                                        'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10},
                                        'legend':{'x': 0, 'y': 1},
                                        'hovermode':'closest'


                                    }
                                }
                            ),
                            dcc.Graph(
                                id='right-bottom-graph',
                                figure={
                                    'data': [{
                                        'x': yList,
                                        'y': xList,
                                        'type': 'bar'
                                    }],
                                    'layout': {
                                        'height': 400,
                                        'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10},
                                        'legend':{'x': 0, 'y': 1},
                                        'hovermode':'closest'
                                    }
                                }
                            ),

                        ])
                    )
                ]
            )
        ])

        graphy.css.append_css({
            'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
        })

        graphy.run_server(debug=True)
    #

# class DashBAndEmail(ABC):
#     def __init__(self, par):
#         self.par = par
#
#     @abstractmethod
#     def callForEmail(self):
#         raise NotImplementedError("Subclass must implement this abstract method")
#
#
# class EmailTime(DashBAndEmail):
#     def __init__(self, f):
#         super().__init__(f)
#
#     def callForEmail(self):
#         # f = open("data.txt", "r", encoding="utf-8")
#         # contents = f.read()
#         MY_ADDRESS = "mail.expenseTracker@gmail.com"
#         PASSWORD = "test123*"
#         email = input("Please enter your email address!\n")
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(MY_ADDRESS, PASSWORD)
#         msg = "Your reddit query...\n"  + "\nThank you!!\n"
#         server.sendmail(MY_ADDRESS, email, msg)
#         server.quit()
#         print("Email sent!! Please check your email address!!")



if __name__ == "__main__":
    redditStart = RedditBase("redditStart")
    redditStart.startReddit()
    dashB = DashBoard("dashB")
    dashB.chartsTime(x1List, y1List, xList, yList, x2List, y2List)

    # responseEmail = input("Do you want an email? y or n")
    # if (responseEmail == "y" or "Y"):
    #     email = EmailTime("email")
    #     email.callForEmail()
    # else:
    #     print("Yes")





#
#
#
#


#
#
# #implement a queue
# # submission = reddit.submission(id='9xxsqd')
# # print(submission.url)
# # submission.comments.replace_more(limit=0)
# # for top_level_comment in submission.comments:
# #     print(top_level_comment.body)
#
