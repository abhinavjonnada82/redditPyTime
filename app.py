
import praw
import collections
import dash
import dash_core_components as dcc
import dash_html_components as html
import smtplib


reddit = praw.Reddit(client_id="jGPKzTuBE-Z95w",
                     client_secret="ml-vWi1dPEGd8NUtO70J_9yYFdY",
                     user_agent= "bot /u/kingNAV82",
                     username="kingNAV82",
                     password="apple123")
file = open("data.txt", "w")
listScore = {}
commentScore = {}
xList = []
yList = []
x2List = []
y2List = []
x1List = []
y1List = []


def writeIntoFile(holderToWrite):
    lineDivider = ('------------------------')
    file.write(holderToWrite)
    file.write(lineDivider)

def startReddit():
    subRedditSearch = input ("What do you wanna search for ?")
    subreddit = reddit.subreddit(subRedditSearch)
    print(subreddit.display_name)
    print(subreddit.title)
    writeIntoFile(subreddit.title)
    print(subreddit.description)
    writeIntoFile(subreddit.description)
    for submission in subreddit.hot(limit=10):
        listScore[submission.score] = submission.title
        commentScore[submission.title] = submission.num_comments

def graphCreator(listScore):
    print("Before Sorting : ")
    writeIntoFile("Before Sorting : ")
    for k, v in listScore.items():
        print (k, v)
        x2List.append(k)
        y2List.append(v)
        contentHolder = ('\n{} : {}\n'.format(k, v))
        writeIntoFile(contentHolder)
    print("\n")
    od = collections.OrderedDict(sorted(listScore.items()))
    print("After Sorting : ")
    file.write("After Sorting : ")
    for k, v in od.items():
        contentHolder = ('\n{} : {}\n'.format(k, v))
        writeIntoFile(contentHolder)
        print (k, v)
        xList.append(k)
        yList.append(v)

    print(xList)
    print(yList)

def graphCreator1(commentScore):

    print("Comments Section: ")
    writeIntoFile("Comments Section: ")
    for k, v in commentScore.items():
        print (k, v)
        x1List.append(k)
        y1List.append(v)
        contentHolder = ('\n{} : {}\n'.format(k, v))
        writeIntoFile(contentHolder)

    print(x1List)
    print(y1List)

#
#

def callForEmail():
    f = open("data.txt", "r", encoding="utf-8")
    contents = f.read()
    MY_ADDRESS = "mail.expenseTracker@gmail.com"
    PASSWORD = "test123*"
    email = input("Please enter your email address!\n")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MY_ADDRESS, PASSWORD)

    msg = "Your reddit query...\n" + contents + "\nThank you!!\n"
    server.sendmail(MY_ADDRESS, email, msg)
    server.quit()
    print("Email sent!! Please check your email address!!")


#

#
#
startReddit()
graphCreator(listScore)
graphCreator1(commentScore)
# callForEmail()


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
#
#
#
#
#
#
#
# print ("Hello World")
#
#
# # trace0 = go.Bar(
# #     x=yList,
# #     y=xList,
# #     marker = dict(
# #           color = 'blue'
# #     ),
# # )
# #
# # trace1 = go.Scatter(
# #     x=x1List,
# #     y=y1List,
# # )
# #
# # data = [trace0, trace1]
# #
# # py.plot(data, filename = 'basic-line.html', auto_open=True)
#
#
# graphy = dash.Dash()
# graphy.layout = html.Div([
#     html.Div(
#         className="row",
#         children=[
#             html.Div(
#                 className="six columns",
#                 children=[
#                     html.Div(
#                         children=dcc.Graph(
#                             id='right-graph',
#                             figure={
#                                 'data': [{
#                                     'x': x1List,
#                                     'y': y1List,
#                                     'type': 'scatter',
#                                 }],
#                                 'layout': {
#                                     'height': 800,
#                                     'line':{'width': 1, 'color': 'red' },
#
#
#                                 }
#                             }
#                         )
#                     )
#                 ]
#             ),
#             html.Div(
#                 className="six columns",
#                 children=html.Div([
#                     dcc.Graph(
#                         id='right-top-graph',
#                         figure={
#                             'data': [{
#                                 'x': y2List,
#                                 'y': x2List,
#                                 'type': 'bar',
#                                 'name': 'Score v. Submissions'
#
#                             }],
#                             'layout': {
#                                 'height': 400,
#                                 'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10},
#                                 'legend':{'x': 0, 'y': 1},
#                                 'hovermode':'closest'
#
#
#                             }
#                         }
#                     ),
#                     dcc.Graph(
#                         id='right-bottom-graph',
#                         figure={
#                             'data': [{
#                                 'x': yList,
#                                 'y': xList,
#                                 'type': 'bar'
#                             }],
#                             'layout': {
#                                 'height': 400,
#                                 'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10},
#                                 'legend':{'x': 0, 'y': 1},
#                                 'hovermode':'closest'
#                             }
#                         }
#                     ),
#
#                 ])
#             )
#         ]
#     )
# ])
#
# graphy.css.append_css({
#     'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# })
#
# if __name__ == '__main__':
#     graphy.run_server(debug=True)