m_start ='Hello! \n You got into anonymous dating chat! \n' \
               'Press the button below to start chatting with the partner. '\
               'If you want to get to know a person better - press the like button and with mutual sympathy ' \
               'you can find out your partners nickname. If you do not like the partner, '\
               'then feel free to press the dislike button and start a new chat. \n' \
               'ATTENTION! For the bot to work successfully, you must have a nickname, '\
               'check your settings and make sure you have it listed! \n' \
               'To stop the bot, call the /stop command. '\
               'Please note that all your data will be deleted, otherwise you will remain in the database.'

m_is_not_free_users = 'Sorry, but there are currently no free users. '\
                   'As soon as another user logs in, we will connect you!'
m_is_connect = 'The connection has been established. Greet your partner! '

m_play_again = 'Want to chat with someone else?'

m_is_not_user_name = 'Sorry, but in our bot it is possible to communicate only if you have a username'

m_good_bye = 'Goodbye, we will be glad to see you again! Keep Supporting'

m_disconnect_user = 'Your caller has disconnected'

m_failed = 'Something went wrong!'

m_like = 'Great choice!'

m_dislike_user = 'Dialog Ended'

m_dislike_user_to = 'The caller ended the call'

m_send_some_messages = 'Can not forward own messages'

m_has_not_dialog = 'You are not in a dialogue'

dislike_str = 'End'

like_str = 'Like'


def m_all_like (x):
    return 'The Partner liked you \n' + 'His username:' + str (x) + \
           '\n Good luck with your communication! \n Thank you for being with us!'
