import werobot

robot = werobot.WeRoBot(token='tokenhere')

@robot.handler
def hello(message):
    return 'Hello World!'

# �÷����������� 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()