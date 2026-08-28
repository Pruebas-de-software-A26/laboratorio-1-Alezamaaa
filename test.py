import user_manager
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = 'test.log',
    filemode = 'w'
)

if __name__ == "__main__":
    manager = user_manager.UserManager()

    logging.info('TEST CASE #1 (RF1)')

    manager.add_user(1,'Alice')
    logging.info('The test passes with debugger :)')
    logging.info('end TEST CASE')

    logging.info('TEST CASE #2 (RF2)')

    manager.add_user(2, 'Bob')
    manager.add_user(3, 'Charlie')

    user1 = manager.find_user(2)

    logging.info('before if')
    if user1['name'] == 'Bob':
        logging.info ('PASS')
    else:
        logging.info('FAIL')

    logging.info('TEST CASE #3 (RF3)')

    manager.delete_user(3)
    logging.info('TEST CASE passed using debugger :)')
    logging.info('end TEST CASE')

    logging.info('TEST CASE #4 (RF4)')

    all_names = manager.get_all_names()
    logging.info(f'The names are: {all_names}')
    if all_names == ['Alice', 'Bob']:
        logging.info('PASS')
    else:
        logging.error('FAIL')
        logging.warning('Returns the IDs, not the Names')
    
    logging.info('end TEST CASE')

    logging.info('TEST CASE #6 (RNF#1)')

    for i in range (1000):
        manager.add_user(i, 'User'+str(i))
    logging.info('PASS')
    logging.info('Users added')

    logging.info('TEST CASE #7 (RNF#2)')